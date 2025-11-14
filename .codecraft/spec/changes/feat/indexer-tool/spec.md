<规约 UID="spec-002">

  <details>
    <summary>元数据 (点击展开)</summary>
    <元数据>
      <标题>规约：自动化索引工具</标题>
      <摘要>开发一个自动化脚本，用于扫描所有已归档的规约，并自动生成全局的 `INDEX.md` 文件。</摘要>
      <状态>草稿</状态>
      <负责人>@jules-ai</负责人>
      <流程级别>Tier-1</流程级别>
    </元数据>
  </details>

  <details>
    <summary>上下文 (点击展开)</summary>
    <上下文>
      <项目 名称="CodeCraftAI">
        <技术栈>Python</技术栈>
        <架构>CodeCraft Spec 驱动</架构>
      </项目>
      <关联>
        <原则>../../PRINCIPLES.md#5-唯一标识-everything-is-addressable</原则>
        <文档>../../INDEX.md</文档>
      </关联>
    </上下文>
  </details>

  <指令分析>
    <details>
      <summary>核心请求 (点击展开)</summary>
      <核心请求>
        <目标>将“索引更新”这一手动流程，转变为一个可靠的、可重复的自动化流程。</目标>
      </核心请求>
    </details>
  </指令分析>

  <实施计划>
    <details>
      <summary>解决方案 (点击展开)</summary>
      <解决方案>
        <顶层策略>
          创建一个独立的 Python 脚本 (`tools/indexer.py`)。
          该脚本将：
          1. 遍历 `.codecraft/spec/archive/` 目录下的所有 `spec.md` 文件。
          2. 使用正则表达式或一个简单的 XML 解析器，提取每个文件中的 UID（规约、功能等）。
          3. 根据提取到的信息，重新生成 `.code.craft/spec/INDEX.md` 的内容。
        </顶层策略>
        <文件变更>
          <创建>tools/indexer.py</创建>
          <修改>.codecraft/spec/INDEX.md</修改>
        </文件变更>
      </解决方案>
    </details>
  </实施计划>

</规约>
