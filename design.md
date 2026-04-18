используй uxui skil и систему ниже обнови дизайн приложения и создай дизайн систему, на которую будешь полагаться в дальнейшем в этом проекте

# 📘 DESIGN SYSTEM: `CORE-UI`
*Масштабируемая, проект-независимая система интерфейсных токенов и компонентов. Готова к внедрению в веб, десктоп и мобильные приложения.*

---

##  1. ЦВЕТОВАЯ СИСТЕМА (TOKENS)

### Primitive Colors (Базовые палитры)
| Токен | HEX | RGB | Назначение |
|-------|-----|-----|------------|
| `gray-50`  | `#F9FAFB` | 249,250,251 | Фоны секций, hover легкие |
| `gray-100` | `#F3F4F6` | 243,244,246 | Границы, разделители |
| `gray-200` | `#E5E7EB` | 229,231,235 | Disabled бордеры, инпуты |
| `gray-400` | `#9CA3AF` | 156,163,175 | Второстепенный текст, иконки |
| `gray-600` | `#4B5563` | 75,85,99  | Третичный текст |
| `gray-800` | `#1F2937` | 31,41,55  | Основной текст |
| `gray-900` | `#111827` | 17,24,39  | Заголовки, акцентный текст |
| `blue-500` | `#3B82F6` | 59,130,246 | Primary action, links |
| `green-500`| `#22C55E` | 34,197,94 | Success, positive trend |
| `red-500`  | `#EF4444` | 239,68,68 | Error, negative trend, warning |
| `orange-500`| `#F97316`| 249,115,22 | Warning, attention |
| `surface`  | `#FFFFFF` | 255,255,255| Карточки, модалки, панели |

### Semantic Mapping (Смысловые токены)
| Семантика | Токен | fallback |
|-----------|-------|----------|
| `bg-page` | `gray-50` | |
| `bg-surface` | `surface` | |
| `text-primary` | `gray-900` | |
| `text-secondary` | `gray-600` | |
| `text-tertiary` | `gray-400` | |
| `border-default` | `gray-200` | |
| `border-focus` | `blue-500` | |
| `state-success` | `green-500` | |
| `state-warning` | `orange-500` | |
| `state-error` | `red-500` | |
| `state-info` | `blue-500` | |

---

## 🔤 2. ТИПОГРАФИКА

**Шрифт:** `Inter, system-ui, -apple-system, sans-serif`

| Токен | Size | Weight | Line-height | Letter-spacing | Применение |
|-------|------|--------|-------------|----------------|------------|
| `display-xl` | 32px | 700 | 120% | -0.02em | Hero-заголовки |
| `h1` | 24px | 700 | 130% | -0.01em | Заголовки страниц/секций |
| `h2` | 20px | 600 | 130% | 0 | Заголовки карточек |
| `h3` | 16px | 600 | 140% | 0 | Подзаголовки, лейблы групп |
| `body-lg` | 16px | 400 | 150% | 0 | Основной контент |
| `body-md` | 14px | 400 | 150% | 0 | Текст в таблицах, описания |
| `body-sm` | 13px | 500 | 140% | 0.01em | Табы, навигация, кнопки |
| `caption` | 12px | 500 | 140% | 0.02em | Подписи, даты, метаданные |
| `metric-value` | 24px | 700 | 120% | -0.01em | Числовые показатели |
| `metric-label` | 12px | 500 | 140% | 0.02em | Названия метрик |

---

## 📐 3. ОТСТУПЫ, СЕТКА, СКРУГЛЕНИЯ

### Spacing Scale (Base: 4px)
`4 | 8 | 12 | 16 | 20 | 24 | 32 | 40 | 48 | 64 | 80 | 96`

### Layout Grid
- **Columns:** 12 (desktop), 8 (tablet), 4 (mobile)
- **Gutter:** 24px → 16px → 12px
- **Margin:** 24px → 16px → 12px
- **Max-width:** `1440px` (container)

### Border Radius
| Токен | Value | Применение |
|-------|-------|------------|
| `radius-xs` | 4px | Чекбоксы, маленькие инпуты |
| `radius-sm` | 8px | Кнопки, теги, аватары |
| `radius-md` | 12px | Карточки, дропдауны, панели |
| `radius-lg` | 16px | Модалки, сайдбары |
| `radius-full` | 999px | Pill-кнопки, бейджи, прогресс-бары |

### Elevation (Shadows)
| Токен | Value | Применение |
|-------|-------|------------|
| `shadow-xs` | `0 1px 2px rgba(0,0,0,0.05)` | Инпуты, чипы |
| `shadow-sm` | `0 2px 4px rgba(0,0,0,0.06)` | Кнопки, дропдауны |
| `shadow-md` | `0 4px 12px rgba(0,0,0,0.08)` | Карточки, тултипы |
| `shadow-lg` | `0 8px 24px rgba(0,0,0,0.12)` | Модалки, popovers |

---

## 🧩 4. БАЗОВЫЕ КОМПОНЕНТЫ

###  Button
| Параметр | Value |
|----------|-------|
| Height | S: 32px \| M: 40px \| L: 48px |
| Padding | S: 0 12px \| M: 0 16px \| L: 0 20px |
| Radius | `radius-sm` |
| Font | `body-sm` (500) |
| Variants | `primary` (filled), `secondary` (outline), `ghost` (transparent), `destructive` |
| States | default, hover (`opacity: 0.9`), active (`scale: 0.98`), disabled (`opacity: 0.5, pointer-events: none`), loading (spinner + disabled) |

### 🃏 Card
| Параметр | Value |
|----------|-------|
| Padding | 24px (desktop), 16px (mobile) |
| Radius | `radius-md` |
| Shadow | `shadow-md` |
| Background | `bg-surface` |
| Structure | Header (optional) → Body → Footer (optional) |
| Hover | `transform: translateY(-2px)`, `shadow-lg` (опционально) |

###  Tabs
| Параметр | Value |
|----------|-------|
| Layout | Horizontal flex, gap 24px |
| Height | 40px |
| Font | `body-sm` (500) |
| Active | Color: `text-primary`, Weight: 600, Border-bottom: 2px `state-info` |
| Inactive | Color: `text-secondary` |
| Indicator | Animated underline (width 100%, height 2px, transition 0.2s) |

### 🏷️ Badge / Tag
| Параметр | Value |
|----------|-------|
| Height | 24px |
| Padding | 0 8px |
| Radius | `radius-full` |
| Font | `caption` (500) |
| Variants | `neutral` (bg: gray-100, text: gray-600), `success`, `warning`, `error`, `info` |
| Dot Indicator | 6px circle, left of text, margin-right 4px |

### 📊 Metric Block
| Параметр | Value |
|----------|-------|
| Layout | Flex column, gap 4px |
| Label | `metric-label`, `text-secondary` |
| Value | `metric-value`, `text-primary` |
| Trend | Row, gap 4px, `caption`, icon (↑/↓), delta value |
| Trend Colors | Positive: `state-success`, Negative: `state-error`, Neutral: `text-tertiary` |

### 📜 Action List Item
| Параметр | Value |
|----------|-------|
| Height | 48px |
| Padding | 0 16px |
| Layout | Flex row, space-between, align center |
| Left | Icon (16px) + `body-md` text, gap 12px |
| Right | Chevron (16px) or Badge |
| Hover | `bg-page`, border-radius `radius-sm` |
| Border | Bottom 1px `border-default` (кроме последнего) |

### 📥 Input / Select
| Параметр | Value |
|----------|-------|
| Height | 40px |
| Padding | 0 12px |
| Radius | `radius-sm` |
| Border | 1px `border-default` |
| Focus | Border `border-focus`, ring 0 0 0 3px `rgba(59,130,246,0.2)` |
| Placeholder | `text-tertiary` |
| Error State | Border `state-error`, helper text `caption` `state-error` |

---

## ⚡ 5. СОСТОЯНИЯ И ИНТЕРАКТИВНОСТЬ

| Состояние | Правило |
|-----------|---------|
| **Hover** | `transition: all 0.15s ease` | Изменение фона/тени/прозрачности |
| **Active/Press** | `transform: scale(0.98)` или уменьшение elevation |
| **Focus** | Outline 2px `border-focus` + ring 3px (accessibility mandatory) |
| **Disabled** | `opacity: 0.5`, `cursor: not-allowed`, `pointer-events: none` |
| **Loading** | Skeleton (bg: gray-200, animation pulse 1.5s) или spinner в кнопке |
| **Empty State** | Illustration (48-64px) + `h3` + `body-md` + CTA button |

---

## ️ 6. CSS-VARIABLES (COPY-PASTE READY)

```css
:root {
  /* Colors */
  --color-bg-page: #F9FAFB;
  --color-bg-surface: #FFFFFF;
  --color-text-primary: #111827;
  --color-text-secondary: #4B5563;
  --color-text-tertiary: #9CA3AF;
  --color-border-default: #E5E7EB;
  --color-border-focus: #3B82F6;
  --color-state-success: #22C55E;
  --color-state-warning: #F97316;
  --color-state-error: #EF4444;
  --color-state-info: #3B82F6;

  /* Spacing */
  --space-4: 4px; --space-8: 8px; --space-12: 12px;
  --space-16: 16px; --space-20: 20px; --space-24: 24px;
  --space-32: 32px; --space-40: 40px; --space-48: 48px;
  --space-64: 64px; --space-80: 80px; --space-96: 96px;

  /* Radius */
  --radius-xs: 4px; --radius-sm: 8px; --radius-md: 12px;
  --radius-lg: 16px; --radius-full: 999px;

  /* Shadows */
  --shadow-xs: 0 1px 2px rgba(0,0,0,0.05);
  --shadow-sm: 0 2px 4px rgba(0,0,0,0.06);
  --shadow-md: 0 4px 12px rgba(0,0,0,0.08);
  --shadow-lg: 0 8px 24px rgba(0,0,0,0.12);

  /* Typography */
  --font-family: 'Inter', system-ui, -apple-system, sans-serif;
  --font-display: 700 32px/1.2 var(--font-family);
  --font-h1: 700 24px/1.3 var(--font-family);
  --font-h2: 600 20px/1.3 var(--font-family);
  --font-h3: 600 16px/1.4 var(--font-family);
  --font-body-lg: 400 16px/1.5 var(--font-family);
  --font-body-md: 400 14px/1.5 var(--font-family);
  --font-body-sm: 500 13px/1.4 var(--font-family);
  --font-caption: 500 12px/1.4 var(--font-family);
  --font-metric-value: 700 24px/1.2 var(--font-family);
  --font-metric-label: 500 12px/1.4 var(--font-family);

  /* Transitions */
  --transition-fast: 0.15s ease;
  --transition-base: 0.2s ease;
}

/* Dark Mode Support (optional) */
@media (prefers-color-scheme: dark) {
  :root {
    --color-bg-page: #0B0F19;
    --color-bg-surface: #151A25;
    --color-text-primary: #F3F4F6;
    --color-text-secondary: #9CA3AF;
    --color-text-tertiary: #6B7280;
    --color-border-default: #2A3040;
    --shadow-xs: 0 1px 2px rgba(0,0,0,0.3);
    --shadow-sm: 0 2px 4px rgba(0,0,0,0.4);
    --shadow-md: 0 4px 12px rgba(0,0,0,0.5);
    --shadow-lg: 0 8px 24px rgba(0,0,0,0.6);
  }
}
```

---

##  7. ПРАВИЛА ИСПОЛЬЗОВАНИЯ

1. **Единство токенов:** Никогда не используйте хардкод цветов/размеров. Всегда ссылайтесь на `--color-*` и `--space-*`.
2. **Иерархия:** Максимум 3 уровня заголовков на экране. Метрики визуально доминируют над подписями.
3. **Контраст:** Текст на фоне ≥ 4.5:1 (WCAG AA). Интерактивные элементы ≥ 3:1.
4. **Touch Targets:** Минимальный размер кликабельной области 40×40px.
5. **Адаптивность:** 
   - Desktop: 2-4 колонки метрик, горизонтальные табы
   - Tablet: 2 колонки, табы с прокруткой
   - Mobile: 1 колонка, табы → аккордеон или bottom nav
6. **Состояния:** Каждый компонент обязан иметь `:hover`, `:focus-visible`, `:disabled`, `loading`.
7. **Иконки:** Stroke 1.5px, size 16px (list), 20px (headers), 24px (empty states). Монохромные, наследуют `currentColor`.
8. **Анимации:** Только `transform` и `opacity`. Длительность 150-200ms. Без `width/height` анимаций в layout.

