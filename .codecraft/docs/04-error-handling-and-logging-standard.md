# 标准 04：容错性与日志记录标准

- **状态**: 已采纳
- **版本**: 1.0.0
- **日期**: 2024-08-16

---

## 1. 核心原则

为了构建生产级的、健壮可靠的软件，本项目将容错性与日志记录作为**强制性**的编码规范。其核心原则是：

1.  **预见失败 (Anticipate Failure)**: 我们必须假设任何外部交互都可能失败。
2.  **明确失败 (Fail Loudly and Clearly)**: 绝不能让错误被“静默”地忽略。
3.  **记录以供诊断 (Log for Diagnosis)**: 每一个异常都必须被记录下来，为问题的排查提供线索。

所有开发者，特别是 AI 开发者，在编写代码时**必须**严格遵守本标准。

## 2. 强制性规则

### 规则一：强制性的异常捕获 (`try...except`)

所有**不可信赖的操作 (Untrusted Operations)** 都**必须**被包裹在一个 `try...except` 块中。

**“不可信赖的操作”** 被明确定义为包括但不限于以下几类：
- **文件 I/O**: `open()`, `read()`, `write()` 等。
- **网络请求**: 使用 `requests`, `httpx`, `aiohttp` 等库进行的任何 API 调用。
- **数据库交互**: 任何数据库的查询、插入、更新、删除操作。
- **外部进程调用**: 使用 `subprocess` 模块执行的任何外部命令。
- **数据解析**: 解析不可信来源的数据，如 `json.load`, `yaml.safe_load` 等。
- **关键算法**: 可能会因为非预期输入而产生数学错误（如除以零）的计算。

### 规则二：有意义的错误日志记录

在 `except` 块中捕获到异常后，**必须**遵循以下两条准则：

1.  **严禁静默忽略**: **严禁**使用空的 `except` 块或 `except: pass` 来忽略错误。这是最高优先级的编码红线之一。

2.  **必须记录日志**: **必须**使用 Python 内置的 `logging` 模块，以 `logging.error()` 或 `logging.exception()` 级别，记录下有意义的错误信息。

    **日志内容至少应包含**:
    - 发生了什么 (What happened): 异常的类型和消息。
    - 在哪里发生 (Where it happened): 模块名和函数名。
    - 相关的上下文 (What was the context): 导致错误的关键变量或参数。

## 3. 代码范例

为了确保 AI 能够精确理解本标准，以下提供了清晰的“错误做法”与“正确做法”的对比。

### 场景：读取一个配置文件

#### ❌ 错误的做法 (将被禁止)

```python
import json

# 错误 1: 没有捕获可能的 FileNotFoundError 或 json.JSONDecodeError
def get_config_value_bad_1(path, key):
    with open(path, 'r') as f:
        config = json.load(f)
    return config.get(key)

# 错误 2: "静默忽略"了异常，返回一个模棱两可的 None
def get_config_value_bad_2(path, key):
    try:
        with open(path, 'r') as f:
            config = json.load(f)
        return config.get(key)
    except (FileNotFoundError, json.JSONDecodeError):
        pass # 这是最危险的行为！调用者无法区分是“文件不存在”还是“key不存在”
```

#### ✅ 正确的做法 (强制要求)

```python
import json
import logging

# 配置日志记录器 (通常在应用启动时配置一次)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_config_value_good(path, key):
    """
    Safely reads a value from a JSON config file.
    """
    try:
        with open(path, 'r') as f:
            config = json.load(f)
        return config.get(key)

    # 捕获具体的、预期的异常
    except FileNotFoundError:
        logging.error(f"[CONFIG_LOAD] Failed to find config file at path: {path}")
        # 将异常向上层抛出，让调用者决定如何处理这个严重错误
        raise

    except json.JSONDecodeError as e:
        logging.exception(f"[CONFIG_LOAD] Failed to parse JSON from {path}. Error: {e}")
        # 使用 logging.exception 会自动包含堆栈跟踪信息
        raise

    except Exception as e:
        # 有一个通用的 Exception 作为最后的“安全网”，但应优先捕获具体异常
        logging.exception(f"[CONFIG_LOAD] An unexpected error occurred while reading config {path}: {e}")
        raise
```

## 4. 结论

遵循此标准，将极大地提升我们项目的健壮性和可维护性。任何不符合此标准的代码，都将在 Code Review 阶段被拒绝。
