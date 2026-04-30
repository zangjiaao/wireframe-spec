# wireframe-spec

标准化低保真线框技能（移动端 / 桌面端）。用于在视觉设计前快速产出可运行 HTML 线框，统一结构表达、命名和交付格式，减少 Agent 实现歧义。

## 适用场景
- 线框图、wireframe、页面布局草图、信息架构预览
- 需要先验证页面结构、关键入口、状态分支
- 需要统一输出到 `wireframes/` 并进行结构评审

## 核心约定（V2）
- 默认交互：静态 Tab 切换
- 默认语义策略：注释优先（规则与字段语义写在第4行注释）
- 默认产物：移动端与桌面端各 1 份 HTML

## 目录结构
- `SKILL.md`：技能主规范
- `references/wireframe-standards.md`：规则参考与代码片段
- `references/templates/mobile-layout-template.html`：移动端模板
- `references/templates/desktop-layout-template.html`：桌面端模板
- `agents/openai.yaml`：技能展示配置

## 输出规范
- 固定目录：`wireframes/`
- 固定主文件：
  - `wireframes/layout-preview.html`
  - `wireframes/admin-layout-preview.html`
- 可选扩展命名：
  - `layout-preview--{topic}.html`
  - `admin-layout-preview--{topic}.html`

## 交付消息模板（固定三段）
1. 交付文件路径
2. 本轮结构变更摘要（仅结构）
3. 请求结构审阅反馈

## 校验
可使用 quick validate 脚本校验 skill frontmatter 与基本结构：

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py ~/.codex/skills/wireframe-spec
```
