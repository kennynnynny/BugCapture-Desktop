import os
import sys
import cv2
import numpy as np
from datetime import datetime
from pathlib import Path

import subprocess
import re

from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QHBoxLayout,
    QLabel, QPushButton, QSlider, QFileDialog, QMessageBox,
    QScrollArea, QListWidget, QListWidgetItem, QSizePolicy
)
from PySide6.QtCore import QThread, Signal, QTimer, Qt
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from PySide6.QtGui import QPixmap, QImage, QKeyEvent

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
    font-family: 'Segoe UI', 'Inter', -apple-system, sans-serif;
    color: {CORE_UI_COLORS['text_primary']};
    font-size: 14px;
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
"""

SCREENSHOTS_DIR = "screenshots"
TEMP_DIR = "temp"


class VideoWorker(QThread):
    """Поток для чтения кадров из видео через OpenCV."""
    frame_ready = Signal(np.ndarray)
    finished = Signal()

    def __init__(self, video_path: str, fps: float, parent=None):
        super().__init__(parent)
        self.video_path = video_path
        self.fps = fps
        self._is_running = False
        self._is_paused = False
        self._should_stop = False
        self.cap = None
        self.current_frame = None

    def run(self):
        """Основной цикл потока: читает кадры из видео."""
        self.cap = cv2.VideoCapture(self.video_path)
        if not self.cap.isOpened():
            self.finished.emit()
            return

        self._is_running = True
        frame_delay = int(1000 / self.fps) if self.fps > 0 else 33

        while not self._should_stop:
            if self._is_paused:
                self.msleep(50)
                continue

            ret, frame = self.cap.read()
            if not ret:
                self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                ret, frame = self.cap.read()
                if not ret:
                    break

            self.current_frame = frame.copy()
            self.frame_ready.emit(frame.copy())

            self.msleep(frame_delay)

        self.cap.release()
        self._is_running = False
        self.finished.emit()

    def pause(self):
        self._is_paused = True

    def resume(self):
        self._is_paused = False

    def stop(self):
        self._should_stop = True
        if self.cap:
            self.cap.release()

    def set_position(self, position_ms: int):
        """Перемотка видео на указанную позицию в миллисекундах."""
        if self.cap and self.cap.isOpened():
            frame_number = int(position_ms * self.fps / 1000)
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)

    def get_current_frame(self) -> np.ndarray:
        return self.current_frame


class MainWindow(QMainWindow):
    """Главное окно приложения Bug Reporter."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bug Reporter - Этап 1")
        self.resize(900, 600)

        self.video_worker = None
        self.video_path = None
        self.video_fps = 30.0
        self.video_duration_ms = 0
        self.is_playing = False
        self.current_frame = None

        self.media_player = None
        self.audio_output = None
        self.temp_audio_path = None

        self.screenshots = []
        self.current_screenshot_index = -1

        self._create_dirs()
        self._setup_ui()
        self._setup_audio()
        self._apply_styles()
        self._load_existing_screenshots()

    def _create_dirs(self):
        """Создание необходимых папок."""
        Path(SCREENSHOTS_DIR).mkdir(exist_ok=True)
        Path(TEMP_DIR).mkdir(exist_ok=True)

    def _load_existing_screenshots(self):
        """Загрузка существующих скриншотов из папки."""
        self.screenshots = []
        if Path(SCREENSHOTS_DIR).exists():
            for f in sorted(Path(SCREENSHOTS_DIR).glob("bug_*.png")):
                self.screenshots.append(str(f))
        if self.screenshots:
            self.current_screenshot_index = len(self.screenshots) - 1
        else:
            self.current_screenshot_index = -1
        self._update_gallery()

    def _setup_ui(self):
        """Настройка пользовательского интерфейса."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.video_label = QLabel()
        self.video_label.setObjectName("video")
        self.video_label.setAlignment(Qt.AlignCenter)
        self.video_label.setMinimumSize(640, 360)
        layout.addWidget(self.video_label, 1)

        self.time_label = QLabel("00:00 / 00:00")
        self.time_label.setObjectName("time")
        self.time_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.time_label)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setEnabled(False)
        self.slider.sliderMoved.connect(self._on_sliderMoved)
        self.slider.sliderPressed.connect(self._on_sliderPressed)
        self.slider.sliderReleased.connect(self._on_sliderReleased)
        layout.addWidget(self.slider)

        controls_layout = QHBoxLayout()

        self.open_btn = QPushButton("Открыть видео")
        self.open_btn.setObjectName("secondary")
        self.open_btn.clicked.connect(self._open_video)
        controls_layout.addWidget(self.open_btn)

        self.play_pause_btn = QPushButton("▶ Play")
        self.play_pause_btn.setEnabled(False)
        self.play_pause_btn.clicked.connect(self._toggle_play_pause)
        controls_layout.addWidget(self.play_pause_btn)

        self.screenshot_btn = QPushButton("📸 Сделать скриншот")
        self.screenshot_btn.setObjectName("screenshot")
        self.screenshot_btn.setEnabled(False)
        self.screenshot_btn.clicked.connect(self._take_screenshot)
        controls_layout.addWidget(self.screenshot_btn)

        layout.addLayout(controls_layout)

        gallery_layout = QHBoxLayout()

        self.prev_screenshot_btn = QPushButton("◀")
        self.prev_screenshot_btn.setObjectName("nav")
        self.prev_screenshot_btn.setFixedWidth(40)
        self.prev_screenshot_btn.clicked.connect(self._prev_screenshot)
        gallery_layout.addWidget(self.prev_screenshot_btn)

        self.gallery_label = QLabel("Нет скриншотов")
        self.gallery_label.setAlignment(Qt.AlignCenter)
        self.gallery_label.setMinimumHeight(80)
        self.gallery_label.setScaledContents(True)
        self.gallery_label.setObjectName("gallery")
        gallery_layout.addWidget(self.gallery_label, 1)

        self.next_screenshot_btn = QPushButton("▶")
        self.next_screenshot_btn.setObjectName("nav")
        self.next_screenshot_btn.setFixedWidth(40)
        self.next_screenshot_btn.clicked.connect(self._next_screenshot)
        gallery_layout.addWidget(self.next_screenshot_btn)

        self.screenshot_count_label = QLabel("0/0")
        self.screenshot_count_label.setObjectName("caption")
        self.screenshot_count_label.setFixedWidth(40)
        gallery_layout.addWidget(self.screenshot_count_label)

        layout.addLayout(gallery_layout)

        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self._update_slider_position)

    def _setup_audio(self):
        """Настройка аудиоплеера."""
        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)

    def _apply_styles(self):
        """Применение CORE-UI дизайн системы."""
        self.setStyleSheet(BASE_APP_STYLESHEET)

    def _open_video(self):
        """Открытие видеофайла."""
        downloads_path = str(Path.home() / "Downloads")
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Выбрать видеофайл",
            downloads_path,
            "Видеофайлы (*.mp4 *.avi *.mkv *.mov *.webm);;Все файлы (*.*)"
        )

        if not file_path:
            return

        self._stop_video()

        self.video_path = file_path
        self._clear_temp_audio()
        self._extract_audio(file_path)

        cap = cv2.VideoCapture(file_path)
        if not cap.isOpened():
            QMessageBox.warning(self, "Ошибка", "Не удалось открыть видео")
            return

        self.video_fps = cap.get(cv2.CAP_PROP_FPS)
        if self.video_fps == 0:
            self.video_fps = 30.0

        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        if frame_count <= 0:
            cap.release()
            try:
                cmd = ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file_path]
                result = subprocess.run(cmd, capture_output=True, text=True, creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0)
                duration = float(result.stdout.strip())
                self.video_duration_ms = int(duration * 1000)
            except Exception:
                QMessageBox.warning(self, "Ошибка", "Не удалось определить длительность видео")
                return
        else:
            self.video_duration_ms = int(frame_count / self.video_fps * 1000)

        if self.video_duration_ms < 0 or self.video_duration_ms > 2147483647:
            self.video_duration_ms = 60000
        cap.release()

        self.slider.setMaximum(self.video_duration_ms)
        self.slider.setEnabled(True)
        self.play_pause_btn.setEnabled(True)
        self.screenshot_btn.setEnabled(True)

        self._start_video_worker()

    def _extract_audio(self, video_path: str):
        """Извлечение аудио из видео с помощью ffmpeg."""
        try:
            self.temp_audio_path = os.path.join(TEMP_DIR, "temp_audio.wav")

            import subprocess
            cmd = [
                'ffmpeg', '-i', video_path,
                '-vn', '-acodec', 'pcm_s16le',
                '-ar', '44100', '-ac', '2',
                '-y', self.temp_audio_path
            ]

            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                creationflags=subprocess.CREATE_NO_WINDOW if sys.platform == 'win32' else 0
            )

            if result.returncode != 0:
                stderr = result.stderr
                if "Output file" in stderr and "must be specified" in stderr:
                    pass
                else:
                    print(f"Ошибка ffmpeg: {stderr}")
                    self.temp_audio_path = None
                    return

            if not os.path.exists(self.temp_audio_path):
                print("Аудиофайл не был создан")
                self.temp_audio_path = None
                return

            url = "file:///" + self.temp_audio_path.replace("\\", "/")
            self.media_player.setSource(url)
            print(f"Аудио извлечено: {self.temp_audio_path}")

        except FileNotFoundError:
            print("ffmpeg не найден. Установите ffmpeg для извлечения аудио.")
            self.temp_audio_path = None
        except Exception as e:
            print(f"Ошибка извлечения аудио: {e}")
            self.temp_audio_path = None

    def _clear_temp_audio(self):
        """Очистка временного аудиофайла."""
        if self.temp_audio_path and os.path.exists(self.temp_audio_path):
            try:
                os.remove(self.temp_audio_path)
            except Exception:
                pass
            self.temp_audio_path = None

    def _start_video_worker(self):
        """Запуск потока видео."""
        self.video_worker = VideoWorker(
            self.video_path,
            self.video_fps
        )
        self.video_worker.frame_ready.connect(self._on_frame_ready)
        self.video_worker.finished.connect(self._on_video_finished)
        self.video_worker.start()

        if self.temp_audio_path:
            self.media_player.play()

        self.is_playing = True
        self.play_pause_btn.setText("⏸ Pause")
        self.update_timer.start(100)

    def _stop_video(self):
        """Остановка видео и освобождение ресурсов."""
        self.update_timer.stop()

        if self.video_worker:
            self.video_worker.stop()
            self.video_worker.wait(1000)
            self.video_worker = None

        self.media_player.stop()
        self._clear_temp_audio()

        self.is_playing = False
        self.play_pause_btn.setText("▶ Play")
        self.slider.setValue(0)
        self.time_label.setText("00:00 / 00:00")

    def _toggle_play_pause(self):
        """ПереключениеPlay/Pause."""
        if not self.video_worker:
            return

        if self.is_playing:
            self.video_worker.pause()
            self.media_player.pause()
            self.is_playing = False
            self.play_pause_btn.setText("▶ Play")
        else:
            self.video_worker.resume()
            if self.temp_audio_path:
                self.media_player.play()
            self.is_playing = True
            self.play_pause_btn.setText("⏸ Pause")

    def _on_frame_ready(self, frame: np.ndarray):
        """Обработка нового кадра от видеопотока."""
        self.current_frame = frame.copy()

        h, w = frame.shape[:2]
        bytes_per_line = w * 3
        qt_image = QImage(
            frame.data, w, h, bytes_per_line, QImage.Format_RGB888
        ).rgbSwapped()

        pixmap = QPixmap.fromImage(qt_image)
        scaled_pixmap = pixmap.scaled(
            self.video_label.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
        self.video_label.setPixmap(scaled_pixmap)

    def _on_video_finished(self):
        """Обработка окончания видео."""
        pass

    def _on_sliderPressed(self):
        """Пауза при начале перемотки."""
        if self.is_playing:
            self.video_worker.pause()
            self.media_player.pause()

    def _on_sliderReleased(self):
        """Возобновл��ни�� после перемотки."""
        if self.is_playing:
            self.video_worker.resume()
            if self.temp_audio_path:
                self.media_player.play()

    def _on_sliderMoved(self):
        """Обработка перемотки ползунка."""
        position_ms = self.slider.value()
        if self.video_worker:
            self.video_worker.set_position(position_ms)

        if self.temp_audio_path:
            self.media_player.setPosition(position_ms)

    def _update_slider_position(self):
        """Обновление позиции ползунка."""
        if not self.video_worker or not self.is_playing:
            return

        if self.temp_audio_path:
            position_ms = self.media_player.position()
        else:
            if self.video_worker.cap:
                frame_pos = self.video_worker.cap.get(cv2.CAP_PROP_POS_FRAMES)
                position_ms = int(frame_pos / self.video_fps * 1000)
            else:
                position_ms = self.slider.value()

        self.slider.blockSignals(True)
        self.slider.setValue(position_ms)
        self.slider.blockSignals(False)

        self._update_time_label(position_ms)

    def _update_time_label(self, position_ms: int):
        """Обновление метки времени."""
        current = self._format_time(position_ms)
        total = self._format_time(self.video_duration_ms)
        self.time_label.setText(f"{current} / {total}")

    def _format_time(self, ms: int) -> str:
        """Форматирование времени в MM:SS."""
        seconds = ms // 1000
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

    def _take_screenshot(self):
        """Сохранение текущего кадра."""
        if self.current_frame is None:
            return

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"bug_{timestamp}.png"
        save_path = os.path.join(SCREENSHOTS_DIR, filename)

        cv2.imwrite(save_path, self.current_frame)
        print(f"Скриншот сохранен: {save_path}")

        self.screenshots.append(save_path)
        self.current_screenshot_index = len(self.screenshots) - 1
        self._update_gallery()

        self._flash_border()

    def _update_gallery(self):
        """Обновление галереи скриншотов."""
        if not self.screenshots:
            self.gallery_label.setText("Нет скриншотов")
            self.screenshot_count_label.setText("0/0")
            self.prev_screenshot_btn.setEnabled(False)
            self.next_screenshot_btn.setEnabled(False)
            return

        self.prev_screenshot_btn.setEnabled(True)
        self.next_screenshot_btn.setEnabled(True)

        idx = self.current_screenshot_index + 1
        total = len(self.screenshots)
        self.screenshot_count_label.setText(f"{idx}/{total}")

        pixmap = QPixmap(self.screenshots[self.current_screenshot_index])
        scaled = pixmap.scaled(
            160, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation
        )
        self.gallery_label.setPixmap(scaled)

    def _prev_screenshot(self):
        """Предыдущий скриншот."""
        if not self.screenshots:
            return
        self.current_screenshot_index = (
            self.current_screenshot_index - 1
        ) % len(self.screenshots)
        self._update_gallery()

    def _next_screenshot(self):
        """Следующий скриншот."""
        if not self.screenshots:
            return
        self.current_screenshot_index = (
            self.current_screenshot_index + 1
        ) % len(self.screenshots)
        self._update_gallery()

    def _flash_border(self):
        """Визуальная вспышка рамки при скриншоте."""
        self.video_label.setObjectName("video-flash")
        self.setStyleSheet(BASE_APP_STYLESHEET)
        QTimer.singleShot(150, lambda: self._clear_flash())

    def _clear_flash(self):
        """Сброс эффекта вспышки."""
        self.video_label.setObjectName("video")
        self.setStyleSheet(BASE_APP_STYLESHEET)

    def keyPressEvent(self, event: QKeyEvent):
        """Обработка нажатия клавиш."""
        if event.key() == Qt.Key_Space:
            self._take_screenshot()
        else:
            super().keyPressEvent(event)

    def closeEvent(self, event):
        """Закрытие приложения, освобождение ресурсов."""
        self._stop_video()
        self.media_player.stop()
        self._clear_temp_audio()
        event.accept()


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())