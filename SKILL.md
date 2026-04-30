---
name: wireframe-spec
description: Use when users ask for 线框图、wireframe、页面布局草图、信息架构预览或HTML布局预览，并需要统一的低保真规范输出（移动端与桌面端）。
---

# Wireframe Spec

## Overview
输出可运行的低保真 HTML 线框，用于验证信息架构、页面分区和关键入口，不用于表达最终视觉。

## Default Contract (V2)
1. 默认交互模式：`静态 Tab 切换`。
2. 默认语义策略：`注释优先`（画面表达布局，语义写在第4行注释）。
3. 默认语言：中文（用户明确要求其他语言时再切换）。
4. 默认产物：移动端与桌面端各 1 个预览文件。
5. 默认启用：`WF Inspector`（元素抓取器）说明文案与快捷键约定。

## Output Contract
1. 只输出可编辑 HTML/CSS/少量原生 JS（不输出图片）。
2. 固定目录：`wireframes/`。
3. 固定主文件：
- `wireframes/layout-preview.html`
- `wireframes/admin-layout-preview.html`
4. 可选扩展命名（用户明确要求分主题/分版本时）：
- `layout-preview--{topic}.html`
- `admin-layout-preview--{topic}.html`
- `{topic}` 使用小写 kebab-case。
5. 同一 Tab 可并排展示多个状态卡（如默认态/弹窗态/空态/禁用态）。
6. 预览页面需内置元素抓取器（或保持与既有抓取器兼容），用于让用户无截图定位元素。

## Four-Row Layout
1. 第1行：标题与说明（`preview-head`）。
2. 第2行：页面 Tab（`page-tabs` + `tab`）。
3. 第3行：页面展示区（`page-canvas`，按 Tab 切换显示 `tab-panel`）。
4. 第4行：当前页面注释（`annotation-row` + `panel-notes`）。
5. 第1行与第3行默认不加额外外框容器。

## Semantic Rule (Comment-First)
1. 画面层仅表达结构占位，不承载最终业务文案。
2. 规则、字段、约束写入第4行注释：
- 规则口径（如“好友点击并参与才加次数”）
- 字段语义（如“倒计时、项目名称、领奖凭证”）
- 触发条件（如“未登录点击参与触发微信授权”）
3. `tag` 非默认语义组件；如使用，必须在说明中声明“仅字段占位，不代表最终徽章”。

## Component Dictionary (Required)
- 容器：`.wrap`（四行壳）、`.phone`（移动端卡片）、`.screen`（桌面端卡片）
- 分区：`.block`、`.layout`、`.row-2`、`.row-4`、`.side`、`.side-item`
- 按钮：`.btn.primary`（主要按钮）、`.btn`（次要按钮）、`.btn-row`
- 表格：`.table`、`.tr`、`.td`
- 文本占位：`.line.s`、`.line.m`、`.line.l`
- 图片占位：`.img`
- 图标占位：`.icon`（方/圆图标占位 + 简短标识）
- 图表占位：`.chart-area`（禁止用文字行伪装图表）
- 注释：`.annotation-row`、`.panel-notes`、`.note`、`.caption`
- 关键动作标注：`.note-badge`（圈号）
- 抓取器层：`.wf-highlight`、`.wf-inspector-tip`、`.wf-panel`

## Inspector Rule (Required)
1. 页面头部必须有抓取器使用说明文案（`Shift+I / 点击 / Alt+点击 / Esc`）。
2. 快捷键约定：
- `Shift + I`：开启/关闭选择模式
- 点击：选择当前最近元素并复制定位信息
- `Alt + 点击`：选择上一级可选容器并复制定位信息
- `Esc`：退出选择模式
3. 复制内容格式需为标准块：
```txt
[WF_TARGET]
file=wireframes/layout-preview.html
tab=抽奖页
panel=抽奖页（中奖弹窗状态）
section=活动规则
wf_id=
selector=.tab-panel[data-panel="lottery"] .block:nth-of-type(2)
text=活动规则
```
4. 抓取器自身 UI 必须加 `data-inspector-ignore`，避免被反选中。
5. 建议关键区块补充 `data-wf-id`，提升跨版本定位稳定性。

## Naming Consistency Rule
1. `tab_label`（短标题）与 `panel_title`（完整标题）必须同义同词根。
2. 禁止同页命名漂移（Tab 与卡片标题表达不同业务对象）。
3. 建议命名层次：
- 页面：`tab_label` / `panel_title`
- 区块：`block_title`
- 字段：写入第4行注释

## Mobile / Desktop Rules
1. 移动端：
- 手机基线默认 `390/844`，可选 `375/812`
- 高度为 `min-height` + 内容自增长（不设固定 max-height）
- 卡片标题使用整条标题栏样式（与桌面端同风格：浅灰底 + 底部分割线）
2. 桌面端：
- 统一侧边栏（全局一级导航）
- 页面差异在内容区二级 Tab 表达
- 禁止每页自定义侧边栏（除非用户明确要求）

## Workflow
1. 从需求提取页面清单、关键状态、关键规则。
2. 先搭四行壳，再填每个 Tab 的卡片结构。
3. 使用组件字典完成占位，不写高保真视觉。
4. 把业务语义和约束补到第4行注释。
5. 对齐命名一致性（Tab/标题同义）。
6. 注入或保留元素抓取器（含 `Alt+点击` 上级容器能力）与顶部说明文案。
7. 生成并保存到 `wireframes/`。

## Delivery Message Format (Required)
交付时固定三段：
1. 交付文件路径（绝对路径或相对路径）。
2. 本轮结构变更摘要（仅结构，不讲视觉润色）。
3. 请求“结构审阅反馈”（不请求视觉细节反馈）。

## Acceptance Checklist
1. 使用静态 Tab 切换，且同 Tab 可展示多状态卡。
2. 业务规则不在画面组件里硬编码，写在第4行注释。
3. 图表区使用 `.chart-area`，不使用文字行伪装。
4. 主次按钮、表格、图标等类名符合组件字典。
5. Tab 与卡片标题同义同词根。
6. 输出路径与命名符合 `wireframes/` 规范。
7. 桌面端保持统一侧边栏。
8. 元素抓取器可用：`Shift+I` 开关、点击复制、`Alt+点击` 选上级、`Esc` 退出。
9. 文档无互相矛盾条款。

## Reference
- `references/wireframe-standards.md`
- `references/templates/mobile-layout-template.html`
- `references/templates/desktop-layout-template.html`
