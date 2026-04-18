# CORE-UI Design System

Масштабируемая, проект-независимая система интерфейсных токенов и компонентов для PySide6/Qt приложений.

---

## 1. Цветовая система (Tokens)

### Primitive Colors (Базовые палитры)

| Token | HEX | RGB | Назначение |
|-------|-----|-----|------------|
| `gray-50` | `#F9FAFB` | 249,250,251 | Фоны секций, hover легкие |
| `gray-100` | `#F3F4F6` | 243,244,246 | Границы, разделители |
| `gray-200` | `#E5E7EB` | 229,231,235 | Disabled бордеры, инпуты |
| `gray-400` | `#9CA3AF` | 156,163,175 | Второстепенный текст, иконки |
| `gray-600` | `#4B5563` | 75,85,99 | Третичный текст |
| `gray-800` | `#1F2937` | 31,41,55 | Основной текст |
| `gray-900` | `#111827` | 17,24,39 | Заголовки, акцентный текст |
| `blue-500` | `#3B82F6` | 59,130,246 | Primary action, links |
| `green-500` | `#22C55E` | 34,197,94 | Success, positive trend |
| `red-500` | `#EF4444` | 239,68,68 | Error, negative trend, warning |
| `orange-500` | `#F97316` | 249,115,22 | Warning, attention |
| `surface` | `#FFFFFF` | 255,255,255 | Карточки, модалки, панели |

### Semantic Mapping (Смысловые токены)

| Семантика | Token | Fallback |
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

## 2. Типографика

**Шрифт:** `Inter, Segoe UI, -apple-system, sans-serif`

| Token | Size | Weight | Line-height | Letter-spacing | Применение |
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

## 3. Отступы, сетка, скругления

### Spacing Scale (Base: 4px)

`4 | 8 | 12 | 16 | 20 | 24 | 32 | 40 | 48 | 64 | 80 | 96`

### Layout Grid

- **Columns:** 12 (desktop), 8 (tablet), 4 (mobile)
- **Gutter:** 24px → 16px → 12px
- **Margin:** 24px → 16px → 12px
- **Max-width:** `1440px` (container)

### Border Radius

| Token | Value | Применение |
|-------|-------|------------|
| `radius-xs` | 4px | Чекбоксы, маленькие инпуты |
| `radius-sm` | 8px | Кнопки, теги, аватары |
| `radius-md` | 12px | Карточки, дропдауны, панели |
| `radius-lg` | 16px | Модалки, сайдбары |
| `radius-full` | 999px | Pill-кнопки, бе��джи, прогресс-бары |

### Elevation (Shadows)

| Token | Value | Применение |
|-------|-------|------------|
| `shadow-xs` | `0 1px 2px rgba(0,0,0,0.05)` | Инпуты, чипы |
| `shadow-sm` | `0 2px 4px rgba(0,0,0,0.06)` | Кнопки, дропдауны |
| `shadow-md` | `0 4px 12px rgba(0,0,0,0.08)` | Карточки, тултипы |
| `shadow-lg` | `0 8px 24px rgba(0,0,0,0.12)` | Модалки, popovers |

---

## 4. Базовые компоненты (PySide6/Qt Styles)

### Button (QPushButton)

| Параметр | Value |
|----------|-------|
| Height | S: 32px \| M: 40px \| L: 48px |
| Padding | S: 0 12px \| M: 0 16px \| L: 0 20px |
| Radius | `radius-sm` (8px) |
| Font | `body-sm` (13px, 500) |
| Variants | `primary` (filled), `secondary` (outline), `ghost` (transparent), `destructive` |

**Primary Button:**
```python
QPushButton {
    background-color: #3B82F6;
    color: #FFFFFF;
    border: none;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 13px;
    font-weight: 500;
}
QPushButton:hover {
    background-color: #2563EB;
}
QPushButton:pressed {
    background-color: #1D4ED8;
}
QPushButton:disabled {
    background-color: #E5E7EB;
    color: #9CA3AF;
}
```

**Secondary Button:**
```python
QPushButton {
    background-color: transparent;
    color: #4B5563;
    border: 1px solid #E5E7EB;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 13px;
    font-weight: 500;
}
QPushButton:hover {
    background-color: #F3F4F6;
    border-color: #D1D5DB;
}
```

**Destructive Button:**
```python
QPushButton {
    background-color: #EF4444;
    color: #FFFFFF;
    border: none;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 13px;
    font-weight: 500;
}
QPushButton:hover {
    background-color: #DC2626;
}
```

### Card (QFrame/QWidget)

| Параметр | Value |
|----------|-------|
| Padding | 24px (desktop), 16px (mobile) |
| Radius | `radius-md` (12px) |
| Shadow | `shadow-md` |
| Background | `bg-surface` (#FFFFFF) |

```python
QFrame#card {
    background-color: #FFFFFF;
    border-radius: 12px;
    border: 1px solid #E5E7EB;
    padding: 24px;
}
```

### Label (QLabel)

```python
QLabel#h1 {
    font-size: 24px;
    font-weight: 700;
    color: #111827;
}
QLabel#h2 {
    font-size: 20px;
    font-weight: 600;
    color: #111827;
}
QLabel#h3 {
    font-size: 16px;
    font-weight: 600;
    color: #111827;
}
QLabel#body-lg {
    font-size: 16px;
    font-weight: 400;
    color: #111827;
}
QLabel#body-md {
    font-size: 14px;
    font-weight: 400;
    color: #4B5563;
}
QLabel#body-sm {
    font-size: 13px;
    font-weight: 500;
    color: #4B5563;
}
QLabel#caption {
    font-size: 12px;
    font-weight: 500;
    color: #9CA3AF;
}
```

### Slider (QSlider)

```python
QSlider::groove:horizontal {
    height: 4px;
    background: #E5E7EB;
    border-radius: 2px;
}
QSlider::handle:horizontal {
    width: 16px;
    height: 16px;
    margin: -6px 0;
    background: #3B82F6;
    border-radius: 8px;
}
QSlider::handle:horizontal:hover {
    background: #2563EB;
}
QSlider::sub-page:horizontal {
    background: #3B82F6;
    border-radius: 2px;
}
```

### Video Label (QLabel for video display)

```python
QLabel#videoDisplay {
    background-color: #1F2937;
    border-radius: 12px;
}
```

---

## 5. Состояния и интерактивность

| Состояние | Правило |
|----------|---------|
| **Hover** | Изменение фона/тени/прозрачности, transition: 150ms |
| **Active/Press** | Уменьшение scale или elevation |
| **Focus** | Border 2px `#3B82F6` + ring (для accessibility) |
| **Disabled** | `opacity: 0.5`, `cursor: not-allowed` |
| **Loading** | Spinner или skeleton |

---

## 6. Qt StyleSheet Constants (Copy-Paste Ready)

```python
CORE_UI_COLORS = {
    "bg_page": "#F9FAFB",
    "bg_surface": "#FFFFFF",
    "text_primary": "#111827",
    "text_secondary": "#4B5563",
    "text_tertiary": "#9CA3AF",
    "border_default": "#E5E7EB",
    "border_focus": "#3B82F6",
    "state_success": "#22C55E",
    "state_warning": "#F97316",
    "state_error": "#EF4444",
    "state_info": "#3B82F6",
}

CORE_UI_FONTS = {
    "display": ("Inter", 32, "bold"),
    "h1": ("Inter", 24, "bold"),
    "h2": ("Inter", 20, "600"),
    "h3": ("Inter", 16, "600"),
    "body-lg": ("Inter", 16, "normal"),
    "body-md": ("Inter", 14, "normal"),
    "body-sm": ("Inter", 13, "500"),
    "caption": ("Inter", 12, "500"),
}

CORE_UI_SPACING = [4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96]

CORE_UI_RADIUS = {
    "xs": "4px",
    "sm": "8px",
    "md": "12px",
    "lg": "16px",
    "full": "999px",
}

CORE_UI_SHADOWS = {
    "xs": "0 1px 2px rgba(0,0,0,0.05)",
    "sm": "0 2px 4px rgba(0,0,0,0.06)",
    "md": "0 4px 12px rgba(0,0,0,0.08)",
    "lg": "0 8px 24px rgba(0,0,0,0.12)",
}
```

---

## 7. Полные QSS Stylesheets

### Base Application Stylesheet

```python
BASE_APP_STYLESHEET = """
QMainWindow {
    background-color: {bg_page};
}

QWidget {
    font-family: 'Inter', 'Segoe UI', -apple-system, sans-serif;
    color: {text_primary};
}

QPushButton {
    background-color: {state_info};
    color: #FFFFFF;
    border: none;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 13px;
    font-weight: 500;
    min-height: 40px;
    min-width: 80px;
}
QPushButton:hover {{
    background-color: #2563EB;
}}
QPushButton:pressed {{
    background-color: #1D4ED8;
}}
QPushButton:disabled {{
    background-color: #E5E7EB;
    color: #9CA3AF;
}}

QPushButton#secondary {{
    background-color: transparent;
    color: {text_secondary};
    border: 1px solid {border_default};
}}
QPushButton#secondary:hover {{
    background-color: #F3F4F6;
}}

QPushButton#destructive {{
    background-color: {state_error};
}}
QPushButton#destructive:hover {{
    background-color: #DC2626;
}}

QPushButton#screenshot {{
    background-color: {state_error};
    color: #FFFFFF;
    font-weight: bold;
}}
QPushButton#screenshot:hover {{
    background-color: #C0392B;
}}

QLabel {{
    color: {text_primary};
    font-size: 14px;
}}

QLabel#title {{
    font-size: 24px;
    font-weight: 700;
}}

QLabel#subtitle {{
    font-size: 16px;
    font-weight: 600;
}}

QLabel#body-sm {{
    font-size: 13px;
    color: {text_secondary};
}}

QLabel#caption {{
    font-size: 12px;
    color: {text_tertiary};
}}

QLabel#time {{
    font-size: 12px;
    color: #FFFFFF;
}}

QSlider::groove:horizontal {{
    height: 4px;
    background: {border_default};
    border-radius: 2px;
}}
QSlider::handle:horizontal {{
    width: 16px;
    height: 16px;
    margin: -6px 0;
    background: {state_info};
    border-radius: 8px;
}}
QSlider::handle:horizontal:hover {{
    background: #2563EB;
}}
QSlider::sub-page:horizontal {{
    background: {state_info};
    border-radius: 2px;
}}

QScrollArea {{
    border: none;
    background-color: transparent;
}}
"""
```

### Example Usage in Python

```python
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

STYLES = {
    "bg_page": "#F9FAFB",
    "bg_surface": "#FFFFFF",
    "text_primary": "#111827",
    "text_secondary": "#4B5563",
    "text_tertiary": "#9CA3AF",
    "border_default": "#E5E7EB",
    "state_info": "#3B82F6",
    "state_error": "#EF4444",
}

button_style = f"""
QPushButton {{
    background-color: {STYLES['state_info']};
    color: #FFFFFF;
    border: none;
    border-radius: 8px;
    padding: 8px 16px;
    font-size: 13px;
    font-weight: 500;
}}
QPushButton:hover {{
    background-color: #2563EB;
}}
"""

app.setStyleSheet(button_style)
```

---

## 8. Правила использования

1. **Единство токенов:** Никогда не используйте хардкод цветов/размеров. Всегда ссылайтесь на CORE_UI_COLORS и CORE_UI_* константы.
2. **Иерархия:** Максимум 3 уровня заголовков на экране. Метрики визуально доминируют над подписями.
3. **Контраст:** Текст на фоне ≥ 4.5:1 (WCAG AA).
4. **Touch Targets:** Минимальный размер кликабельной области 40×40px.
5. **Состояния:** Каждый компонент обязан иметь `:hover`, `:focus`, `:disabled`, `:pressed` стили.
6. **Иконки:** Stroke 1.5px, size 16px (list), 20px (headers), 24px (empty states).
7. **Анимации:** Только `opacity` и `transform`. Длительность 150-200ms.

---

## Changelog

- **2026-04-18** - Initial CORE-UI design system created for BugCapture-Desktop