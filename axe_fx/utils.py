from typing import Tuple, List
import pyautogui
import time
from .constants import ONE_MINUTE_MS

def calculate_note_timing(bpm: int, temperature: int) -> Tuple[float, float]:
    """
    BPMと気温から音符のタイミングを計算する
    """
    speed_of_sound = (temperature * 0.6 + 331.5)
    common_beat_time = ONE_MINUTE_MS / bpm
    note = round((common_beat_time * (1/4)), 2)  # 16分音符
    attack_time = round((((8.25 - (0.25 * -2)) / speed_of_sound) * 1000), 2)
    return note, attack_time

def midi_note_to_freq(note_number: int, tuning: float = 0.0) -> float:
    """
    MIDIノートナンバーを周波数へ変換する
    """
    a4 = 440.0  # A4の周波数は440Hz
    c0 = a4 * pow(2.0, -4.75)  # MIDIノートナンバー0の周波数を求める
    return c0 * pow(2.0, (note_number + tuning) / 12.0)

def safe_click(x: int, y: int, clicks: int = 1, interval: float = 0.0, button: str = "left"):
    """
    安全なクリック操作を提供する
    """
    pyautogui.click(x, y, clicks, interval, button)
    time.sleep(0.1)  # 安全のため少し待機

def type_and_enter(text: str):
    """
    テキストを入力してEnterを押す
    """
    pyautogui.typewrite(str(text))
    pyautogui.press("enter")
    time.sleep(0.1)

def select_from_dropdown(clicks_down: int):
    """
    ドロップダウンメニューから項目を選択する
    """
    for _ in range(clicks_down):
        pyautogui.press("down")
    pyautogui.press("enter")
    time.sleep(0.1)
