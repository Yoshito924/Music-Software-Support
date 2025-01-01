import tkinter as tk
from .axe_fx_controller import AxeFxController
from .constants import DEFAULT_SETTINGS, GEQ_PRESETS

class AxeFxGui:
    def __init__(self):
        self.controller = AxeFxController()
        self.root = tk.Tk()
        self.setup_window()
        self.create_inputs()
        self.create_buttons()

    def setup_window(self):
        """ウィンドウの基本設定"""
        self.root.title("Axe-Edit Control")
        self.root.geometry("300x400+1600+10")

    def create_inputs(self):
        """入力フィールドの作成"""
        # BPM入力
        tk.Label(self.root, text="BPM").place(x=10, y=0)
        self.bpm_input = tk.Entry(self.root, width=10)
        self.bpm_input.place(x=40, y=0)
        self.bpm_input.insert(tk.END, DEFAULT_SETTINGS["default_bpm"])

        # 気温入力
        tk.Label(self.root, text="気温(℃)").place(x=120, y=0)
        self.temp_input = tk.Entry(self.root, width=6)
        self.temp_input.place(x=170, y=0)
        self.temp_input.insert(tk.END, DEFAULT_SETTINGS["default_temperature"])

        # プロクシミティー入力
        tk.Label(self.root, text="プロクシミリティー E2:40 G2:43 B2:47").place(x=10, y=150)
        self.proximity_input = tk.Entry(self.root, width=6)
        self.proximity_input.place(x=10, y=180)
        self.proximity_input.insert(tk.END, DEFAULT_SETTINGS["default_proximity_value"])

    def create_buttons(self):
        """ボタンの作成"""
        # アンプ関連ボタン
        tk.Button(self.root, text="Amp All", command=self.amp_all).place(x=10, y=30)
        tk.Button(self.root, text="Amp", command=self.amp_only).place(x=80, y=30)
        tk.Button(self.root, text="Amp GEQ", command=self.amp_geq).place(x=120, y=30)
        tk.Button(self.root, text="Amp basic2", command=self.amp_basic2).place(x=190, y=30)

        # GEQプリセットボタン
        y_pos = 180
        tk.Button(self.root, text="GEQ Metal", 
                 command=lambda: self.controller.set_geq_settings("metal")).place(x=10, y=y_pos)
        tk.Button(self.root, text="GEQ Rock",
                 command=lambda: self.controller.set_geq_settings("rock")).place(x=80, y=y_pos)
        tk.Button(self.root, text="GEQ Reggae",
                 command=lambda: self.controller.set_geq_settings("reggae")).place(x=150, y=y_pos)

        # キャビネット関連ボタン
        tk.Button(self.root, text="Cab", command=self.cab).place(x=10, y=70)
        tk.Button(self.root, text="Stereo Cab", command=self.stereo_cab).place(x=50, y=70)

        # エフェクト関連ボタン
        tk.Button(self.root, text="Gate", command=self.gate).place(x=10, y=110)
        tk.Button(self.root, text="Comp", command=self.comp).place(x=50, y=110)

    def get_input_values(self):
        """入力値の取得"""
        return {
            'bpm': int(self.bpm_input.get()),
            'temperature': int(self.temp_input.get()),
            'proximity': int(self.proximity_input.get())
        }

    def amp_all(self):
        """全アンプ設定の適用"""
        self.controller.store_home_position()
        self.controller.set_basic_amp_settings()
        self.controller.set_geq_settings()
        self.controller.restore_home_position()

    def amp_only(self):
        """アンプのみの設定"""
        self.controller.store_home_position()
        self.controller.set_basic_amp_settings()
        self.controller.restore_home_position()

    def amp_geq(self):
        """アンプとGEQの設定"""
        self.controller.store_home_position()
        self.controller.set_geq_settings()
        self.controller.restore_home_position()

    def amp_basic2(self):
        """基本アンプ設定2の適用"""
        self.controller.store_home_position()
        settings = {
            "input_drive": "8.1",
            "input_trim": "1.8",
            "bass": "1.1",
            "mid": "1.8",
            "treble": "8.9",
            "presence": "4.5",
            "saturation_drive": "4",
            "master_volume_trim": "1",
            "master_volume": "3"
        }
        self.controller.set_basic_amp_settings(settings)
        self.controller.restore_home_position()

    def gate(self):
        """ゲート設定の適用"""
        values = self.get_input_values()
        self.controller.store_home_position()
        self.controller.set_gate_settings(values['bpm'], values['temperature'])
        self.controller.restore_home_position()

    def comp(self):
        """コンプレッサー設定の適用"""
        values = self.get_input_values()
        self.controller.store_home_position()
        self.controller.set_compressor_settings(values['bpm'], values['temperature'])
        self.controller.restore_home_position()

    def cab(self):
        """キャビネット設定の適用"""
        # TODO: Implement cab settings
        pass

    def stereo_cab(self):
        """ステレオキャビネット設定の適用"""
        # TODO: Implement stereo cab settings
        pass

    def run(self):
        """GUIの実行"""
        self.root.mainloop()

if __name__ == "__main__":
    app = AxeFxGui()
    app.run()
