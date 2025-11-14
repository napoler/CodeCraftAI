# AI 上下文清单 (AI Context Manifest) v1.0

**操作指令：** AI，你好。此文件是你与本规范体系交互的**唯一固定入口**。在执行任何任务前，请首先加载并严格遵循此文件的指示。

---

## 1. 核心系统文件 (Core System Files)

**规则：** 以下是本系统的“基本内存”。在**任何任务**中，你都**必须**首先加载并理解这三个核心文件。

*   `specs/ai-writing-standard.md` - **基础规范:** 定义了你必须遵守的通用工作流和核心原则。
*   `specs/style-and-tone-guide.md` - **风格指南:** 定义了你的写作风格和语调。
*   `specs/knowledge-contribution-guide.md` - **知识贡献指南:** 定义了你在任务结束时如何提炼和贡献知识。

---

## 2. 动态加载指令 (Dynamic Loading Instructions)

**规则：** 根据用户的**具体任务目标**，从以下“写作档案”中**选择一个最相关的**进行加载。**禁止**一次性加载所有档案。

*   **如果任务是解决初创网站的商业挑战 (流量、变现):**
    *   加载: `specs/niche-site-seed-accelerator.md`

*   **如果任务是模仿特定顶级作者的风格和结构以提升原创性:**
    *   加载: `specs/topic-dominance-profile.md`

*   **如果任务是进行SEO内容修订:**
    *   加载: `specs/seo-content-revision.md`

*   **如果任务是创建“如何做”类型的指南:**
    *   加载: `specs/how-to-guide.md`

*   **如果任务是进行迭代式的内容深化:**
    *   加载: `specs/iterative-refinement-profile.md`

*   **如果用户使用了语义标签:**
    *   加载: `docs/semantic-tag-directives-guide.md`

---

## 3. 全局忽略清单 (Global Ignore List)

**规则：** 为了节省Token并保持专注，你**永远不应该**主动读取以下文件和目录，除非用户在指令中明确要求：

*   `.github/` (项目工作流配置)
*   `adr/` (架构决策记录)
*   `kb/` (知识库，应通过规范中定义的流程访问，而不是直接读取)
*   `README.md` (项目总览，供人类阅读)
*   `CONTRIBUTING.md` (贡献指南)
*   `mkdocs.yml` (文档站点配置)
*   `LICENSE` (许可证)
*   `.gitignore` (Git忽略配置)
*   `00_AI_CONTEXT_MANIFEST.md` (本文档本身)

---
**操作流程总结:**
1.  加载并遵循本文档 (`00_AI_CONTEXT_MANIFEST.md`)。
2.  加载3个“核心系统文件”。
3.  根据用户任务，选择并加载1个最相关的“写作档案”。
4.  开始执行任务。
