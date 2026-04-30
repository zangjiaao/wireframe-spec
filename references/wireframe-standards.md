# Wireframe Standards Reference (V2)

## 1) Core Layout Shell (Four Rows)
1. Row 1: `.preview-head` 标题 + 说明
2. Row 2: `.page-tabs` + `.tab` 页面切换
3. Row 3: `.page-canvas` + `.tab-panel` 页面展示区（静态 Tab 切换）
4. Row 4: `.annotation-row` + `#annotation-list` 当前页注释

默认不使用横向滚动联动作为主模式；如需对比多个状态，在同一 `tab-panel` 内放多卡片。

## 2) Required Component Dictionary
- 容器：`.wrap`, `.phone`, `.screen`
- 分区：`.block`, `.layout`, `.row-2`, `.row-4`, `.side`, `.side-item`
- 按钮：`.btn.primary`(主), `.btn`(次), `.btn-row`
- 表格：`.table`, `.tr`, `.td`
- 文本占位：`.line.s`, `.line.m`, `.line.l`
- 图片占位：`.img`
- 图标占位：`.icon`
- 图表占位：`.chart-area`
- 注释：`.annotation-row`, `.panel-notes`, `.note`, `.caption`
- 关键动作标识：`.note-badge`

## 3) Semantic Strategy (Comment-First)
1. 画面只表达布局结构，不表达最终业务文案。
2. 业务语义统一写在第4行注释，包括：
- 字段语义
- 规则口径
- 鉴权触发条件
- 风控/计数约束
3. 若出现 `tag`，必须声明“仅占位”。V2 不把 `tag` 作为默认语义组件。

## 4) Naming Consistency
- `tab_label` 与 `panel_title` 必须同义同词根。
- 允许“短标题/全标题”差异，但不得改变业务对象。
- 推荐格式：
  - `tab_label`: `抽奖页`
  - `panel_title`: `抽奖页（中奖弹窗状态）`

## 5) Mobile and Desktop Baseline
### 移动端
- 基线宽度：`390`（可选 `375`）
- 基线最小高度：`844`（可选 `812`）
- 高度策略：`min-height + 内容自增长`
- 标题栏：整条标题栏 + 底部分割线（与桌面端风格一致）

### 桌面端
- 统一侧边栏 + 内容区二级 Tab
- 禁止每页自定义侧边栏（除非用户明确要求）
- 图表模块使用 `.chart-area`，避免“文字行伪装图表”

## 6) CSS Snippets
```css
:root {
  --bg: #f5f5f5;
  --line: #222;
  --muted: #666;
  --panel: #fff;
  --phone-w: 390px;
  --phone-min-h: 844px;
}

.wrap {
  max-width: 1100px;
  margin: 0 auto;
  padding: 16px;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.tab-panel { display: none; }
.tab-panel.active { display: block; }

.phone-head, .screen-head {
  border-bottom: 2px solid var(--line);
  padding: 10px 12px;
  font-size: 14px;
  font-weight: 700;
  background: #fafafa;
}

.icon {
  width: 16px;
  height: 16px;
  border: 1px solid #333;
  border-radius: 4px;
  display: inline-grid;
  place-items: center;
  font-size: 10px;
}

.chart-area {
  height: 112px;
  border: 1px solid #333;
  border-radius: 6px;
  background: #f7f7f7;
  display: grid;
  place-items: center;
  font-size: 11px;
  color: #555;
}
```

## 7) Static Tab Switch Snippet
```html
<nav class="page-tabs" id="tabs">
  <button class="tab active" data-tab="home">首页</button>
  <button class="tab" data-tab="lottery">抽奖页</button>
</nav>

<main class="page-canvas">
  <section class="tab-panel active" data-panel="home">...</section>
  <section class="tab-panel" data-panel="lottery">...</section>
</main>

<section class="annotation-row">
  <h3>注释（当前页面）</h3>
  <ol id="annotation-list"></ol>
</section>
```

```js
const tabs = Array.from(document.querySelectorAll('.tab'));
const panels = Array.from(document.querySelectorAll('.tab-panel'));
const annotationList = document.getElementById('annotation-list');

function setNotes(panel) {
  const notes = panel.querySelector('.panel-notes');
  annotationList.innerHTML = notes ? notes.innerHTML : '<li>当前页面暂无注释。</li>';
}

function activate(tabName) {
  tabs.forEach((tab) => tab.classList.toggle('active', tab.dataset.tab === tabName));
  panels.forEach((panel) => {
    const isActive = panel.dataset.panel === tabName;
    panel.classList.toggle('active', isActive);
    if (isActive) setNotes(panel);
  });
}

tabs.forEach((tab) => tab.addEventListener('click', () => activate(tab.dataset.tab)));
```

## 8) Output Path and Naming
- 固定输出目录：`wireframes/`
- 默认文件：
  - `wireframes/layout-preview.html`
  - `wireframes/admin-layout-preview.html`
- 可选扩展文件：
  - `layout-preview--{topic}.html`
  - `admin-layout-preview--{topic}.html`

## 9) Delivery Message Template
交付回复固定三段：
1. 文件路径
2. 本轮结构变更摘要（结构层）
3. 结构审阅反馈请求

## 10) Templates
- `references/templates/mobile-layout-template.html`
- `references/templates/desktop-layout-template.html`
