# scripts/index_kb.py
import os
import yaml
from collections import defaultdict
import re

def parse_markdown_frontmatter(filepath):
    """Parses YAML frontmatter from a Markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Use regex to find the YAML frontmatter block
    match = re.search(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
    if not match:
        return None, None

    frontmatter_str = match.group(1)

    try:
        frontmatter = yaml.safe_load(frontmatter_str)
        return frontmatter, content[len(match.group(0)):]
    except yaml.YAMLError as e:
        print(f"Error parsing YAML in {filepath}: {e}")
        return None, None

def generate_kb_index():
    """Generates an index file for the knowledge base."""
    kb_dir = 'kb'
    index_filepath = os.path.join(kb_dir, '_index.md')
    template_filename = 'template.md'

    # Use a dictionary to store notes grouped by tags
    notes_by_tag = defaultdict(list)

    # Iterate over files in the knowledge base directory
    for filename in os.listdir(kb_dir):
        if not filename.endswith('.md') or filename == os.path.basename(index_filepath) or filename == template_filename:
            continue

        filepath = os.path.join(kb_dir, filename)
        frontmatter, _ = parse_markdown_frontmatter(filepath)

        if not frontmatter:
            # If frontmatter is None (parsing failed or doesn't exist), skip or handle
            notes_by_tag['Uncategorized'].append((filename, 'No Title / Parsing Error'))
            continue

        if 'tags' not in frontmatter or not frontmatter['tags']:
            # Assign to a default "Uncategorized" tag if no tags are present
            notes_by_tag['Uncategorized'].append((filename, frontmatter.get('title', 'No Title')))
            continue

        for tag in frontmatter['tags']:
            notes_by_tag[tag].append((filename, frontmatter.get('title', 'No Title')))

    # --- Generate the index file content ---

    output_content = "# Knowledge Base Index\n\n"
    output_content += "This index provides a categorized overview of all knowledge notes. Use it to quickly find relevant information before starting a new task.\n\n"
    output_content += "---\n\n"

    # Sort tags alphabetically for consistent output
    sorted_tags = sorted(notes_by_tag.keys())

    for tag in sorted_tags:
        output_content += f"## Tag: {tag}\n\n"

        # Sort notes under each tag alphabetically by title
        sorted_notes = sorted(notes_by_tag[tag], key=lambda x: x[1])

        for filename, title in sorted_notes:
            output_content += f"- **{title}**\n"
            output_content += f"  - `File`: [{filename}]({filename})\n\n"

    # --- Write the content to the index file ---

    with open(index_filepath, 'w', encoding='utf-8') as f:
        f.write(output_content)

    print(f"Successfully generated knowledge base index at '{index_filepath}'")

if __name__ == "__main__":
    generate_kb_index()
