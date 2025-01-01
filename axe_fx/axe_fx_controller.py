from typing import List
import pyautogui
import time
from .constants import FREQUENCIES, DEFAULT_SETTINGS, GEQ_PRESETS
from .utils import calculate_note_timing, safe_click, type_and_enter, select_from_dropdown

class AxeFxController:
    def __init__(self):
        self.home_position = (0, 0)

    def store_home_position(self):
        """マウスの現在位置を保存"""
        self.home_position = pyautogui.position()

    def restore_home_position(self):
        """マウスを保存位置に戻す"""
        pyautogui.moveTo(*self.home_position)

    def select_axe_edit(self):
        """AXE-EDITを起動する"""
        pyautogui.hotkey("win", "1")
        time.sleep(0.3)

    def set_basic_amp_settings(self, settings: dict = None):
        """基本的なアンプ設定を行う"""
        if settings is None:
            settings = {
                "input_drive": "5",
                "input_trim": "1",
                "bass": "5",
                "mid": "5",
                "treble": "5",
                "presence": "5",
                "saturation_drive": "5",
                "master_volume_trim": "1",
                "master_volume": "5"
            }

        # Basicを選択
        safe_click(306, 653)
        
        # 各パラメータを設定
        parameter_positions = {
            "input_drive": (435, 651),
            "input_trim": (439, 830),
            "bass": (642, 656),
            "mid": (754, 656),
            "treble": (843, 654),
            "presence": (1073, 647),
            "saturation_drive": (1174, 821),
            "master_volume_trim": (1255, 822),
            "master_volume": (1274, 648)
        }

        for param, value in settings.items():
            pos = parameter_positions.get(param)
            if pos:
                safe_click(*pos)
                type_and_enter(value)

    def set_geq_settings(self, preset_name: str = None, custom_values: List[float] = None):
        """GEQの設定を行う"""
        # GEQを選択
        safe_click(297, 701)

        # EQタイプを5Band(Mark)に設定
        safe_click(474, 714)
        select_from_dropdown(4)
        time.sleep(0.5)

        # プリセットまたはカスタム値を適用
        values = GEQ_PRESETS.get(preset_name, custom_values) if preset_name else custom_values
        if not values or len(values) != 8:
            values = [4.8, 2.6, -4.5, -0.2, -0.2, 0, 0, 0]

        positions = [
            (647, 654), (733, 656), (836, 657), (926, 656),
            (1020, 655), (1099, 655), (1209, 658), (1293, 658)
        ]

        for pos, value in zip(positions, values):
            safe_click(*pos)
            type_and_enter(value)

        # EQを差し込む場所をプリアンプ前に設定
        safe_click(487, 875)
        select_from_dropdown(1)

    def set_gate_settings(self, bpm: int, temperature: int):
        """ゲートの設定を行う"""
        self.select_axe_edit()
        note, attack_time = calculate_note_timing(bpm, temperature)

        # BPMを設定
        safe_click(1197, 50)
        type_and_enter(bpm)

        time.sleep(0.5)

        # 各パラメータを設定
        parameters = [
            ((437, 654), "-40"),  # スレッショルド
            ((539, 654), "2"),    # レシオ
            ((650, 654), str(attack_time)),  # アタックタイム
            ((747, 661), "10"),   # ホールド
            ((845, 657), str(note-attack_time)),  # リリースタイム
            ((440, 827), "20.6"), # ローカット
            ((537, 824), "20000") # ハイカット
        ]

        for pos, value in parameters:
            safe_click(*pos)
            type_and_enter(value)

    def set_compressor_settings(self, bpm: int, temperature: int):
        """コンプレッサーの設定を行う"""
        self.select_axe_edit()
        note, attack_time = calculate_note_timing(bpm, temperature)

        # BPMを設定
        safe_click(1197, 50)
        type_and_enter(bpm)

        time.sleep(0.4)

        # スタジオコンプを選択
        safe_click(102, 779)
        select_from_dropdown(6)

        time.sleep(0.4)

        # 各パラメータを設定
        parameters = [
            ((436, 652), "-40"),  # スレッショルド
            ((538, 653), "2"),    # レシオ
            ((863, 656), str(attack_time)),  # アタックタイム
            ((973, 652), str(note-attack_time)),  # リリースタイム
            ((437, 831), "0"),    # ルックアヘッド
            ((528, 826), str(FREQUENCIES[48])),  # フィルター
            ((646, 823), "0.8"),  # Emphasis
        ]

        for pos, value in parameters:
            safe_click(*pos)
            type_and_enter(value)

        # ニーの設定
        safe_click(679, 709)
        select_from_dropdown(2)

        # オートボタン
        safe_click(1109, 711)

        # Detect設定
        safe_click(760, 885)
        select_from_dropdown(4)
