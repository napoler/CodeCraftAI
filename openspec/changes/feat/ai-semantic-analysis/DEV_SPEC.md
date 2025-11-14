# 开发文档：Semantic Engine 模块

本文档是 `semantic_engine` 模块的官方开发与设计规范。所有实现代码都必须严格遵循本文档中定义的架构、接口和行为。

## 1. 模块总览

`semantic_engine` 的核心职责是将用户的自然语言指令（模糊指令）转化为 AI 代理可以执行的、精确的工具调用。它弥合了人类意图与机器操作之间的鸿沟。

### 1.1 设计原则
- **高内聚, 低耦合:** 引擎内部的组件（预处理器、解析器、映射器）职责单一，相互之间通过定义的接口通信。
- **可扩展性:** 添加新的意图或支持新的工具应尽可能简单，理想情况下只需修改配置文件或添加新的映射，而无需改动核心逻辑。
- **透明度:** 引擎的决策过程应易于理解和调试。

### 1.2 架构

本引擎采用三层流水线（Pipeline）架构：

`[自然语言输入]` -> `Preprocessor` -> `Parser` -> `Mapper` -> `[精确的工具调用]`

1.  **Preprocessor:** 负责清理和标准化输入文本。
2.  **Parser:** 负责从干净的文本中识别核心**意图 (Intent)** 和**实体 (Entities)**。
3.  **Mapper:** 负责将解析出的“意图-实体”对映射到一个或多个具体的工具函数调用上。

---

## 2. 组件规范

### 2.1 `preprocessor.py`

#### 函数: `clean_text(text: str) -> str`
- **职责:** 对输入的原始文本进行净化，为解析层做准备。
- **行为规范:**
  1. 将所有英文字符转换为小写。
  2. 移除文本两端的任何空白字符。
  3. 将文本中连续的多个空白字符替换为单个空格。
  4. 移除所有常见的标点符号（例如 `,`, `.`, `!`, `?`），但必须保留在文件名或路径中可能出现的特殊字符（例如 `.`）。
- **输入:** `str` - 原始用户指令。
- **输出:** `str` - 标准化后的文本。
- **示例:** `"  PLEASE, create a file called report.txt!! "` -> `"please create a file called report.txt"`

### 2.2 `intents.py`

- **职责:** 定义系统中所有支持的意图和实体的数据结构。这是引擎的“词汇表”。
- **`Intents` (Enum):**
  - `CREATE_FILE`: 创建一个文件。
  - `DELETE_ENTITY`: 删除一个文件或目录。
  - `LIST_FILES`: 列出当前目录下的文件。
  - `RENAME_ENTITY`: 重命名一个文件或目录。
  - `UNCLEAR_INTENT`: 无法识别意图。
- **实体结构 (TypedDict 或 Pydantic BaseModel):**
  - 为每个意图定义其需要的实体。例如，`CREATE_FILE` 需要 `{'filename': str}`。`RENAME_ENTITY` 需要 `{'source': str, 'destination': str}`。

### 2.3 `parser.py`

#### 类: `IntentParser`
- **职责:** 封装了核心的 NLP (自然语言处理) 逻辑，是引擎的大脑。
- **方法: `parse(text: str) -> dict`**
  - **行为规范:**
    1. 接收由 `preprocessor` 清理过的文本。
    2. 使用 NLP 模型（例如，基于规则的匹配、关键词提取，或未来更复杂的模型）来识别文本中最可能的 `Intents` 枚举成员。
    3. 根据识别出的意图，从文本中提取相应的实体。
    4. 如果无法自信地识别出任何一个已定义的意图，则必须返回 `UNCLEAR_INTENT`。
  - **输出:** 一个字典，包含 `intent` 和 `entities` 两个键。例如: `{ 'intent': Intents.CREATE_FILE, 'entities': {'filename': 'report.txt'} }`

### 2.4 `mapper.py`

#### 类: `ActionMapper`
- **职责:** 将 `IntentParser` 的解析结果转化为一个可执行的函数调用。
- **方法: `map(parse_result: dict) -> callable`**
  - **行为规范:**
    1. 接收 `IntentParser` 的输出。
    2. 内部维护一个从 `Intents` 到 AI 代理工具函数的映射关系。
    3. 根据输入的 `intent`，查找对应的工具函数，并使用 `entities` 来填充该函数的参数。
  - **输出:** 一个准备就绪的、可以被直接调用的函数（例如，一个配置好的 `functools.partial` 对象或一个包含函数名和参数的字典）。

## 3. 顶级接口 (`engine.py`)

#### 类: `SemanticEngine`
- **职责:** 作为引擎的统一入口点，整合所有内部组件。
- **方法: `process(raw_text: str) -> callable`**
  - **行为规范:**
    1. 实例化所有必要的组件 (`Preprocessor`, `Parser`, `Mapper`)。
    2. 按顺序调用 `clean_text`, `parser.parse`, `mapper.map`。
    3. 返回最终的可执行动作。
    4. 如果在任何步骤中出现无法处理的情况（例如 `UNCLEAR_INTENT`），应向上抛出一个特定的、需要用户澄清的异常（例如 `ClarificationNeededError`）。
