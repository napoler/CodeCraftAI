# 任务列表：实现异步获取用户个人资料的 API

本任务列表是 `spec.md` (SpecKit 规约) 的直接产物，用于指导编码实现。

## Phase 1: 模型与服务层 (TDD)

- [ ] **1.1 [Test]** 在 `tests/services/test_profile_service.py` 中，编写一个测试用例，断言当用户存在时，`get_user_profile` 函数返回正确的 `UserProfile` 模型。此测试最初会因为缺少实现而失败。
- [ ] **1.2 [Code]** 在 `src/app/models/profile.py` 中，创建 `UserProfile` Pydantic 模型，包含 `id`, `username`, `display_name`, `bio` 字段。
- [ ] **1.3 [Code]** 在 `src/app/services/profile_service.py` 中，创建 `get_user_profile` 异步函数。使其能够调用（模拟的）数据库层，获取用户信息并返回 `UserProfile` 模型，让测试 `1.1` 通过。
- [ ] **1.4 [Test]** 在 `tests/services/test_profile_service.py` 中，编写第二个测试用例，断言当用户不存在时，`get_user_profile` 函数会抛出一个特定的 `UserNotFound` 异常。
- [ ] **1.5 [Code]** 修改 `get_user_profile` 函数的实现，使其在用户不存在时能够抛出 `UserNotFound` 异常，让测试 `1.4` 通过。
- [ ] **1.6 [Refactor]** 回顾模型和服务层的代码，进行必要的重构以提高清晰度和性能。

## Phase 2: API 层 (TDD)

- [ ] **2.1 [Test]** 在 `tests/api/test_profile_api.py` 中，编写一个集成测试，模拟对 `/api/users/{userId}/profile` 的 `GET` 请求（针对一个存在的用户），并断言响应状态码为 `200`，且响应体符合 `UserProfile` 模型的结构。
- [ ] **2.2 [Code]** 在 `src/app/api/main.py` 中，添加新的 `GET /api/users/{userId}/profile` 端点。该端点应调用 `profile_service.get_user_profile` 函数，并将结果返回，让测试 `2.1` 通过。
- [ ] **2.3 [Test]** 在 `tests/api/test_profile_api.py` 中，编写第二个集成测试，模拟对一个不存在的用户 ID 的请求，并断言响应状态码为 `404`。
- [ ] **2.4 [Code]** 在 API 端点中添加错误处理逻辑，捕获 `UserNotFound` 异常并将其转换为 `HTTPException(status_code=404)`，让测试 `2.3` 通过。
- [ ] **2.5 [Refactor]** 回顾 API 层的代码，进行必要的重构。

## Phase 3: 最终验证

- [ ] **3.1 [Verify]** 运行整个项目的测试套件 (`pytest`)，确保所有测试都通过。
- [ ] **3.2 [Verify]** 运行代码格式化和静态分析工具，确保代码质量达标。
- [ ] **3.3 [Verify]** 确认最终实现与 `spec.md` 中的“完成的定义”完全一致。
