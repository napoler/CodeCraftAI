"""
This script automates the creation of API reference documentation for specified Python libraries.

It performs two main functions:
1.  **Generates Markdown Files**: For each library provided as a command-line argument,
    it creates a corresponding Markdown file in the `docs/api_reference/` directory.
    Each file is populated with the necessary `mkdocstrings` syntax to render the
    library's API documentation.
2.  **Updates MkDocs Navigation**: It dynamically and intelligently updates the `mkdocs.yml`
    configuration file to include links to the newly generated documentation pages
    under the "API Reference" section.

This tool is designed to be run manually whenever the team decides to add a new library
to the project's documented dependencies.

Usage:
    python scripts/generate_api_docs.py <library1> <library2> ...

Example:
    python scripts/generate_api_docs.py pytest ruff requests
"""

import argparse
from pathlib import Path
import sys
import yaml
import importlib.util

def is_library_installable(library_name: str) -> bool:
    """Check if a library is installed and can be imported."""
    spec = importlib.util.find_spec(library_name)
    return spec is not None

def create_api_doc_file(library_name: str, docs_dir: Path):
    """
    Creates a Markdown file for a given library with mkdocstrings syntax.

    Args:
        library_name: The name of the library.
        docs_dir: The path to the 'docs' directory.
    """
    api_ref_dir = docs_dir / "api_reference"
    api_ref_dir.mkdir(exist_ok=True)

    output_path = api_ref_dir / f"{library_name}.md"
    content = f"# API Reference for `{library_name}`\\n\\n::: {library_name}"

    try:
        output_path.write_text(content)
        print(f"✅ Successfully created Markdown file: {output_path.relative_to(Path.cwd())}")
    except IOError as e:
        print(f"❌ Error writing to file {output_path}: {e}", file=sys.stderr)
        sys.exit(1)

def update_mkdocs_config(library_name: str, project_root: Path):
    """
    Updates the mkdocs.yml navigation to include the new API reference.

    This function reads the mkdocs.yml file, finds the 'API Reference' section in the
    navigation, and appends a link to the new library's documentation page. It avoids
    adding duplicate entries.

    Args:
        library_name: The name of the library to add.
        project_root: The root directory of the project.
    """
    mkdocs_config_path = project_root / "mkdocs.yml"

    try:
        with open(mkdocs_config_path, 'r') as f:
            config = yaml.safe_load(f)
    except (IOError, yaml.YAMLError) as e:
        print(f"❌ Error reading or parsing {mkdocs_config_path}: {e}", file=sys.stderr)
        sys.exit(1)

    nav = config.get("nav", [])
    api_ref_section = None

    # Find or create the 'API Reference' section
    for item in nav:
        if isinstance(item, dict) and "API Reference" in item:
            api_ref_section_list = item["API Reference"]
            break
    else:
        api_ref_section_list = []
        nav.append({"API Reference": api_ref_section_list})

    new_entry_path = f"api_reference/{library_name}.md"

    # Check for duplicates based on the file path
    path_exists = any(
        (isinstance(entry, dict) and list(entry.values())[0] == new_entry_path) or
        (isinstance(entry, str) and entry == new_entry_path)
        for entry in api_ref_section_list
    )

    if not path_exists:
        # Use a simple string entry for cleaner YAML
        api_ref_section_list.append(new_entry_path)
        print(f"✅ Adding '{new_entry_path}' to 'API Reference' navigation.")
    else:
        print(f"ℹ️  '{new_entry_path}' already exists in the navigation. Skipping update.")
        return

    try:
        with open(mkdocs_config_path, 'w') as f:
            yaml.dump(config, f, allow_unicode=True, sort_keys=False, indent=2)
        print(f"✅ Successfully updated {mkdocs_config_path.relative_to(Path.cwd())}")
    except (IOError, yaml.YAMLError) as e:
        print(f"❌ Error writing to {mkdocs_config_path}: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    """Main function to parse arguments and orchestrate file creation and config updates."""
    parser = argparse.ArgumentParser(
        description="Generate API reference docs for Python libraries.",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument("libraries", nargs='+', help="A list of library names to document.")
    args = parser.parse_args()

    project_root = Path(__file__).resolve().parent.parent
    docs_dir = project_root / "docs"

    if not docs_dir.is_dir():
        print(f"❌ FATAL: Docs directory not found at {docs_dir}", file=sys.stderr)
        sys.exit(1)

    successful_libs = []
    failed_libs = []

    for library in args.libraries:
        print(f"\nProcessing library: {library}...")
        if not is_library_installable(library):
            print(f"⚠️ Warning: Library '{library}' is not installed or cannot be found.")
            print("  Please install it via 'pip install' before generating docs.")
            failed_libs.append(library)
            continue

        try:
            create_api_doc_file(library, docs_dir)
            update_mkdocs_config(library, project_root)
            successful_libs.append(library)
        except Exception as e:
            print(f"❌ An unexpected error occurred while processing '{library}': {e}", file=sys.stderr)
            failed_libs.append(library)

    print("\n---")
    print("🎉 API documentation generation process completed. 🎉")
    if successful_libs:
        print(f"Successfully processed: {', '.join(successful_libs)}")
    if failed_libs:
        print(f"Failed or skipped: {', '.join(failed_libs)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
