# 标准 04：容错性与日志记录标准

- **状态**: 已采纳
- **版本**: 1.1.0
- **日期**: 2024-08-17

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
（*定义与英文版一致*）

### 规则二：有意义的错误日志记录
在 `except` 块中捕获到异常后，**必须**遵循以下两条准则：
1.  **严禁静默忽略**: **严禁**使用空的 `except` 块或 `except: pass`。
2.  **必须记录日志**: **必须**使用 Python 内置的 `logging` 模块记录有意义的错误信息。
    （*日志内容要求与英文版一致*）

## 3. 高级技巧：构建更具弹性的代码

仅仅捕获错误是不够的，一个卓越的工程师会构建能够优雅地处理甚至从中恢复的系统。我们鼓励 AI 开发者应用以下技巧。

### 技巧一：使用 `finally` 确保清理
对于那些获取了资源（如文件、网络连接）的操作，使用 `finally` 块来保证资源无论成功或失败都会被释放。

```python
import logging

def process_data_file(path):
    f = None
    try:
        f = open(path, 'r')
        # ... 处理文件 ...
    except Exception:
        logging.exception(f"处理文件失败: {path}")
        raise
    finally:
        if f:
            f.close()
            logging.info(f"文件 {path} 已关闭。")
```

### 技巧二：创建自定义异常
为你的应用领域定义专属的异常类。这能让上层调用者更精确地处理你组件的错误。

```python
import requests
import logging

class ApiDataError(Exception):
    """当API返回非预期或无效数据时抛出。"""
    pass

def fetch_user_data(user_id):
    try:
        response = requests.get(f"https://api.example.com/users/{user_id}")
        response.raise_for_status() # 对 4xx/5xx 错误抛出 HTTPError
        data = response.json()
        if "user" not in data:
            raise ApiDataError("API 响应中缺少 'user' 键。")
        return data["user"]
    except requests.exceptions.RequestException as e:
        logging.error(f"获取用户 {user_id} 时发生网络错误: {e}")
        raise
    except ApiDataError: # 可以被调用者专门捕获
        logging.error(f"收到无效的用户数据 {user_id}。")
        raise
```

### 技巧三：为瞬时错误实现重试机制
对于可能是暂时性的网络相关错误，实现一个简单的重试机制可以让你的应用更有弹性。

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
            logging.warning(f"第 {i+1}/{retries} 次尝试失败 {url}。{delay}秒后重试... 错误: {e}")
            time.sleep(delay)
    logging.error(f"所有 {retries} 次尝试均失败 {url}。")
    raise # 重试全部失败后，重新抛出最后的异常
```

## 4. 结论

遵循此标准将极大地提升我们项目的健壮性和可维护性。
