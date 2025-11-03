# Standard 04: Error Handling and Logging Standard

- **Status**: Adopted
- **Version**: 1.1.0
- **Date**: 2024-08-17

---

## 1. Core Principles

To build production-grade, robust, and reliable software, this project enforces error handling and logging as a **mandatory** coding standard. The core principles are:

1.  **Anticipate Failure**: We must assume that any external interaction can fail.
2.  **Fail Loudly and Clearly**: Errors must never be silently ignored.
3.  **Log for Diagnosis**: Every exception must be logged to provide clues for troubleshooting.

All developers, especially AI developers, **must** strictly adhere to this standard when writing code.

## 2. Mandatory Rules

### Rule 1: Mandatory Exception Handling (`try...except`)

All **Untrusted Operations** **must** be wrapped in a `try...except` block.

**"Untrusted Operations"** are explicitly defined as, but not limited to:
- **File I/O**: `open()`, `read()`, `write()`, etc.
- **Network Requests**: Any API calls made using libraries like `requests`, `httpx`, `aiohttp`.
- **Database Interactions**: Any database query, insert, update, or delete operation.
- **External Process Calls**: Any external commands executed using the `subprocess` module.
- **Data Parsing**: Parsing data from untrusted sources, e.g., `json.load`, `yaml.safe_load`.
- **Critical Algorithms**: Calculations that could produce mathematical errors (like division by zero) from unexpected inputs.

### Rule 2: Meaningful Error Logging

When an exception is caught in an `except` block, the following two guidelines **must** be followed:

1.  **No Silent Failures**: Using empty `except` blocks or `except: pass` to ignore errors is **strictly forbidden**. This is one of the highest-priority coding red lines.

2.  **Meaningful Logging is Required**: You **must** use Python's built-in `logging` module, at the `logging.error()` or `logging.exception()` level, to record meaningful error information.

    **Log content must include at a minimum**:
    - **What happened**: The type and message of the exception.
    - **Where it happened**: The module and function name.
    - **Relevant context**: The key variables or parameters that led to the error.

## 3. Advanced Techniques: Building Resilient Code

Beyond simply catching errors, a superior engineer builds systems that can gracefully handle or even recover from them. AI developers are encouraged to apply the following techniques.

### Technique 1: Ensure Cleanup with `finally`
For operations that acquire a resource (like a file or a network connection), use a `finally` block to guarantee the resource is released, whether the operation succeeded or failed.

```python
import logging

def process_data_file(path):
    f = None
    try:
        f = open(path, 'r')
        # ... process the file ...
    except Exception:
        logging.exception(f"Failed to process file: {path}")
        raise
    finally:
        if f:
            f.close()
            logging.info(f"File {path} closed.")
```

### Technique 2: Create Custom Exceptions
For domain-specific errors, define your own exception classes. This allows upstream callers to handle your component's errors with more precision.

```python
import requests
import logging

class ApiDataError(Exception):
    """Raised when the API returns unexpected or invalid data."""
    pass

def fetch_user_data(user_id):
    try:
        response = requests.get(f"https://api.example.com/users/{user_id}")
        response.raise_for_status() # Raises HTTPError for 4xx/5xx
        data = response.json()
        if "user" not in data:
            raise ApiDataError("'user' key missing from API response.")
        return data["user"]
    except requests.exceptions.RequestException as e:
        logging.error(f"Network error fetching user {user_id}: {e}")
        raise
    except ApiDataError: # Can be specifically caught by the caller
        logging.error(f"Invalid data received for user {user_id}.")
        raise
```

### Technique 3: Implement Retries for Transient Errors
For network-related errors that might be temporary ("transient"), implementing a simple retry mechanism can make your application much more resilient.

```python
import time
import requests
import logging

def get_with_retries(url, retries=3, delay=5):
    for i in range(retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            logging.warning(f"Attempt {i+1}/{retries} failed for {url}. Retrying in {delay}s... Error: {e}")
            time.sleep(delay)
    logging.error(f"All {retries} attempts failed for {url}.")
    raise # Re-raise the last exception after all retries fail
```

## 4. Code Examples

(The examples from the original Chinese version would be translated and placed here, following the "Good Practice" model.)

## 5. Conclusion

Adhering to this standard will dramatically improve the robustness and maintainability of our project. Any code that does not comply with this standard will be rejected during Code Review.
