"""
CORE-UI Design System Tokens for PySide6/Qt Applications

Usage:
    from design_system import CORE_UI
    app.setStyleSheet(CORE_UI.BASE_APP_STYLESHEET)
"""

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
    "display": ("Segoe UI, Inter, -apple-system, sans-serif", 32, "bold"),
    "h1": ("Segoe UI, Inter, -apple-system, sans-serif", 24, "bold"),
    "h2": ("Segoe UI, Inter, -apple-system, sans-serif", 20, "600"),
    "h3": ("Segoe UI, Inter, -apple-system, sans-serif", 16, "600"),
    "body-lg": ("Segoe UI, Inter, -apple-system, sans-serif", 16, "normal"),
    "body-md": ("Segoe UI, Inter, -apple-system, sans-serif", 14, "normal"),
    "body-sm": ("Segoe UI, Inter, -apple-system, sans-serif", 13, "500"),
    "caption": ("Segoe UI, Inter, -apple-system, sans-serif", 12, "500"),
}

CORE_UI_SPACING = {
    "4": "4px", "8": "8px", "12": "12px", "16": "16px",
    "20": "20px", "24": "24px", "32": "32px", "40": "40px",
    "48": "48px", "64": "64px", "80": "80px", "96": "96px",
}

CORE_UI_RADIUS = {
    "xs": "4px",
    "sm": "8px",
    "md": "12px",
    "lg": "16px",
    "full": "999px",
}

BASE_APP_STYLESHEET = f"""
QMainWindow {{
    background-color: {CORE_UI_COLORS['bg_page']};
}}

QWidget {{
    font-family: {CORE_UI_FONTS['body-md'][0]};
    color: {CORE_UI_COLORS['text_primary']};
    font-size: {CORE_UI_FONTS['body-md'][1]}px;
}}

QPushButton {{
    background-color: {CORE_UI_COLORS['state_info']};
    color: #FFFFFF;
    border: none;
    border-radius: {CORE_UI_RADIUS['sm']};
    padding: 8px 16px;
    font-size: 13px;
    font-weight: 500;
    min-height: 40px;
    min-width: 80px;
}}
QPushButton:hover {{
    background-color: #2563EB;
}}
QPushButton:pressed {{
    background-color: #1D4ED8;
    transform: scale(0.98);
}}
QPushButton:disabled {{
    background-color: {CORE_UI_COLORS['border_default']};
    color: {CORE_UI_COLORS['text_tertiary']};
}}

QPushButton#secondary {{
    background-color: transparent;
    color: {CORE_UI_COLORS['text_secondary']};
    border: 1px solid {CORE_UI_COLORS['border_default']};
}}
QPushButton#secondary:hover {{
    background-color: {CORE_UI_COLORS['bg_page']};
    border-color: #D1D5DB;
}}

QPushButton#screenshot {{
    background-color: {CORE_UI_COLORS['state_error']};
    color: #FFFFFF;
    font-weight: bold;
}}
QPushButton#screenshot:hover {{
    background-color: #C0392B;
}}
QPushButton#screenshot:pressed {{
    background-color: #B91C1C;
}}

QPushButton#nav {{
    background-color: transparent;
    color: {CORE_UI_COLORS['text_secondary']};
    border: none;
    border-radius: {CORE_UI_RADIUS['sm']};
    padding: 8px 12px;
}}
QPushButton#nav:hover {{
    background-color: {CORE_UI_COLORS['bg_page']};
}}

QLabel {{
    color: {CORE_UI_COLORS['text_primary']};
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
    color: {CORE_UI_COLORS['text_secondary']};
}}

QLabel#caption {{
    font-size: 12px;
    color: {CORE_UI_COLORS['text_tertiary']};
}}

QLabel#time {{
    font-size: 12px;
    color: #FFFFFF;
}}

QLabel#video {{
    background-color: #1F2937;
    border-radius: {CORE_UI_RADIUS['md']};
}}

QLabel#video-flash {{
    background-color: #1F2937;
    border: 4px solid {CORE_UI_COLORS['state_error']};
    border-radius: {CORE_UI_RADIUS['md']};
}}

QSlider::groove:horizontal {{
    height: 4px;
    background: {CORE_UI_COLORS['border_default']};
    border-radius: 2px;
}}
QSlider::handle:horizontal {{
    width: 16px;
    height: 16px;
    margin: -6px 0;
    background: {CORE_UI_COLORS['state_info']};
    border-radius: 8px;
}}
QSlider::handle:horizontal:hover {{
    background: #2563EB;
}}
QSlider::handle:horizontal:pressed {{
    background: #1D4ED8;
}}
QSlider::sub-page:horizontal {{
    background: {CORE_UI_COLORS['state_info']};
    border-radius: 2px;
}}

QScrollArea {{
    border: none;
    background-color: transparent;
}}

QFrame#card {{
    background-color: {CORE_UI_COLORS['bg_surface']};
    border-radius: {CORE_UI_RADIUS['md']};
    border: 1px solid {CORE_UI_COLORS['border_default']};
    padding: 24px;
}}

QFrame#gallery {{
    background-color: {CORE_UI_COLORS['bg_surface']};
    border-radius: {CORE_UI_RADIUS['sm']};
    border: 1px solid {CORE_UI_COLORS['border_default']};
}}
"""

PRIMARY_BUTTON = f"""
QPushButton {{
    background-color: {CORE_UI_COLORS['state_info']};
    color: #FFFFFF;
    border: none;
    border-radius: {CORE_UI_RADIUS['sm']};
    padding: 8px 16px;
    font-size: 13px;
    font-weight: 500;
    min-height: 40px;
}}
QPushButton:hover {{
    background-color: #2563EB;
}}
QPushButton:pressed {{
    background-color: #1D4ED8;
}}
QPushButton:disabled {{
    background-color: {CORE_UI_COLORS['border_default']};
    color: {CORE_UI_COLORS['text_tertiary']};
}}
"""

SECONDARY_BUTTON = f"""
QPushButton {{
    background-color: transparent;
    color: {CORE_UI_COLORS['text_secondary']};
    border: 1px solid {CORE_UI_COLORS['border_default']};
    border-radius: {CORE_UI_RADIUS['sm']};
    padding: 8px 16px;
    font-size: 13px;
    font-weight: 500;
    min-height: 40px;
}}
QPushButton:hover {{
    background-color: {CORE_UI_COLORS['bg_page']};
    border-color: #D1D5DB;
}}
"""

SCREENSHOT_BUTTON = f"""
QPushButton {{
    background-color: {CORE_UI_COLORS['state_error']};
    color: #FFFFFF;
    border: none;
    border-radius: {CORE_UI_RADIUS['sm']};
    padding: 8px 16px;
    font-size: 13px;
    font-weight: 600;
    min-height: 40px;
}}
QPushButton:hover {{
    background-color: #C0392B;
}}
QPushButton:pressed {{
    background-color: #B91C1C;
}}
"""

def get_secondary_button_style():
    return SECONDARY_BUTTON

def get_screenshot_button_style():
    return SCREENSHOT_BUTTON