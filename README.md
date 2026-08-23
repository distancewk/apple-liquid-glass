# LumaFlow

LumaFlow 是一个面向 Web 界面的设计与实现 Skill：

> 先用 Apple 风格的设计思想规划页面，再用固定的四层 SVG 液态玻璃方案实现材质。

它不是普通的 glassmorphism，也不是一套可以随意替换的玻璃滤镜。LumaFlow 的目标是让页面同时具备清晰的产品目的、自然的交互行为和稳定一致的液态玻璃视觉语言。

## 核心理念

LumaFlow 将界面设计拆成两层：

```text
设计层：目的、层级、视觉方向、交互、动效、排版、无障碍
        ↓
材质层：SVG 位移 + 四层液态玻璃结构
```

### 设计层

设计阶段借鉴 Apple Design 和 frontend-design 的有效部分：

- 明确页面的一个核心目的
- 建立清晰的内容层级和常用路径
- 选择统一的视觉方向与记忆点
- 让控件在按下时立即响应
- 让拖拽和手势保持 1:1 跟随
- 让动效可以被打断，并继承释放速度
- 保持进入、退出和触发源之间的空间连续性
- 使用系统字体、合理的 tracking 和 leading
- 处理 reduced motion、reduced transparency、high contrast、键盘焦点和触控区域

### 材质层

所有玻璃表面必须使用以下四层：

| 层级 | 作用 |
| --- | --- |
| `liquid_glass-outer` | SVG 背景位移与边缘折射 |
| `liquid_glass-cover` | `rgba(0, 0, 0, .12)` 与 `blur(2px)` |
| `liquid_glass-sharp` | 清晰的边缘高光 |
| `liquid_glass-reflect` | 内部反射、厚度和暗部阴影 |

内容位于 `z-index: 4`，不能被折射层覆盖。

## 标准结构

```html
<svg style="display: none" aria-hidden="true">
  <defs>
    <filter id="liquid_glass_filter" x="0%" y="0%" width="100%" height="100%" filterUnits="objectBoundingBox">
      <feDisplacementMap scale="200" />
    </filter>
  </defs>
</svg>

<div class="liquid_glass-wrapper" style="--border-radius: 26px">
  <div class="liquid_glass-outer"></div>
  <div class="liquid_glass-cover"></div>
  <div class="liquid_glass-sharp"></div>
  <div class="liquid_glass-reflect"></div>

  <div class="liquid_glass-content">
    <!-- 页面内容 -->
  </div>
</div>
```

背景必须具有可见的空间细节，例如图片、渐变场、轮廓线、色块或纹理。没有背景变化，就无法观察到边缘折射。

## 使用流程

1. 阅读 [SKILL.md](./SKILL.md)。
2. 先完成设计 brief：目的、视觉方向、层级、材质分布、交互状态、动效和无障碍。
3. 再创建背景和页面内容。
4. 使用标准 SVG filter 和四层玻璃结构。
5. 在真实浏览器中检查桌面端、移动端、fallback 和控制台错误。

## 验证

```bash
python3 scripts/validate_skill.py .
python3 scripts/extract_html_example.py \
  --source references/vanilla-example.md \
  --output /tmp/luma-flow-fixture/index.html
```

浏览器验收至少确认：

- 每个 wrapper 都包含四个玻璃层
- 存在 `#liquid_glass_filter`
- `liquid_glass-outer` 使用 `url(#liquid_glass_filter)`
- cover 使用 `blur(2px)`
- 内容保持在 `z-index: 4`
- 设计目的、信息层级、交互状态和无障碍策略清晰
- SVG filter 不可用时页面仍然可读、可操作

## 文件结构

```text
SKILL.md                         主 Skill 规范
agents/openai.yaml               Skill 调用提示
references/vanilla-example.md   可运行的四层液态玻璃 fixture
references/verification.md      设计与材质验收清单
scripts/validate_skill.py       Skill 静态校验
scripts/extract_html_example.py 提取 HTML fixture
```

## 许可与来源

本 Skill 的液态玻璃实现方案基于公开的 [shuding/liquid-glass](https://github.com/shuding/liquid-glass) 代码思路整理；Apple 风格的设计原则被转译为 Web 页面设计与交互决策规则。
