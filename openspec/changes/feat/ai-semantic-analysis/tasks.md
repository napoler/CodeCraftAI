# 任务列表：实现 AI 语义分析引擎

本任务列表基于已批准的 `spec.md` 生成，将指导引擎的 TDD 开发过程。

## Phase 1: 核心组件开发 (TDD)

### 1.1 预处理层 (`preprocessor.py`)
- [ ] **[Test]** 编写测试，验证 `clean_text` 函数能正确地将输入文本转换为小写、移除多余的标点和空格。
- [ ] **[Code]** 实现 `clean_text` 函数，让测试通过。

### 1.2 意图与实体定义 (`intents.py`)
- [ ] **[Code]** 定义 `Intents` 枚举，包含 `CREATE_FILE`, `DELETE_ENTITY`, `LIST_FILES`, `RENAME_ENTITY`。
- [ ] **[Code]** 定义与每个意图相关的实体结构（例如，`CREATE_FILE` 需要 `filename` 实体）。

### 1.3 解析层 (`parser.py`)
- [ ] **[Test]** 编写测试，输入 “帮我建一个叫 report.txt 的文件”，断言 `IntentParser` 能识别出 `CREATE_FILE` 意图和 `filename='report.txt'` 实体。
- [ ] **[Test]** 编写更多测试，覆盖其他三种意图和不同的表达方式（例如 “删除 a.txt”、“把 a.txt 改成 b.txt”、“看看这里有啥文件”）。
- [ ] **[Code]** 实现 `IntentParser` 类。在内部，它将使用 NLP 库来分析经过预处理的文本，并提取出最可能的意图和相关实体。让所有测试通过。
- [ ] **[Test]** 编写测试，验证当指令不明确时（例如 “处理文件”），`IntentParser` 返回一个特殊的 `UNCLEAR_INTENT` 状态。
- [ ] **[Code]** 完善 `IntentParser` 的逻辑，使其能处理不明确的指令，让新测试通过。

### 1.4 映射层 (`mapper.py`)
- [ ] **[Test]** 编写测试，输入一个已解析的 `CREATE_FILE` 意图和实体，断言 `ActionMapper` 能返回一个正确的、待执行的 `create_file(filepath='report.txt')` 工具调用。
- [ ] **[Test]** 编写测试，覆盖其他三种意图到工具调用的映射。
- [ ] **[Code]** 实现 `ActionMapper` 类，它包含一个从意图到具体工具函数调用的映射字典。让所有测试通过。

## Phase 2: 引擎组装与集成 (TDD)

### 2.1 语义引擎 (`engine.py`)
- [ ] **[Test]** 编写一个端到端的集成测试，输入自然语言指令 “我要创建一个新文件，名字是 final_report.docx”，断言 `SemanticEngine` 的 `process` 方法能返回 `create_file(filepath='final_report.docx')` 工具调用。
- [ ] **[Code]** 实现 `SemanticEngine` 类，它在内部按顺序调用 `preprocessor`, `parser`, 和 `mapper`，将所有组件串联起来。让测试通过。
- [ ] **[Test]** 编写集成测试，验证当 `parser` 返回 `UNCLEAR_INTENT` 时，`SemanticEngine` 会抛出一个需要用户澄清的特定异常。
- [ ] **[Code]** 完善 `SemanticEngine` 的 `process` 方法，使其能处理不明确的意图，让新测试通过。

### 2.2 主循环集成
- [ ] **[Code]** (此步骤在沙箱外进行) 将 `SemanticEngine` 集成到 AI 代理的核心指令循环中。使用 `try...except` 块来捕获需要澄清的异常，并向用户发起提问。

## Phase 3: 最终验证

- [ ] **[Verify]** 运行 `semantic_engine` 目录下的所有测试 (`pytest src/semantic_engine/`)，确保 100% 通过。
- [ ] **[Verify]** 运行代码质量检查工具。
- [ ] **[Verify]** 确认最终实现与 `spec.md` 中的“完成的定义”完全一致。
