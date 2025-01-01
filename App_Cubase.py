#!/usr/bin/env python3
import tkinter
import pyautogui
import tkinter.ttk as ttk
import json
import pyperclip
import re
import sys


# -------------------------------------------------------------------------------
# JSONファイルから設定を読み込む
def load_settings():
    with open("cubase.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        return data["settings"], data["tracks"]


def save_settings(settings):
    with open("cubase.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    data["settings"] = settings
    with open("cubase.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)


# 設定とトラックデータを読み込む
settings, tracks = load_settings()

# Pro-C2の「戻るボタン」の座標
c2_close_x, c2_close_y = 1318, 281
c2_close_x, c2_close_y = 2659, 332
c2_close_x, c2_close_y = 1318, 276

threshold = -28  # スレッショルドの指定
attack_time = 10  # ダミーのアタックタイム

one_minutes = 60000  # 1分の秒数(ms)
one_second = 1000  # 1秒は1000ms

# 指定BPMの主要な音符の音価(リリースタイムに使う)を計算する。
note_1 = 4  # 全音符(ms)
note_2 = 2  # 2分音符(ms)
note_4 = 1  # 4分音符(ms)
note_8 = 1 / 2  # 8分音符(ms)
note_16 = 1 / 4  # 16分音符(ms)
note_32 = 1 / 8  # 32分音符(ms)
note_64 = 1 / 16  # 64分音符(ms)
note_128 = 1 / 32  # 128分音符(ms)
note_256 = 1 / 64  # 256分音符(ms)
note_8thDot = 3 / 4  # 付点8分音符
note_16thDot = 3 / 8  # 付点16分音符

# 座標
addx = 0
addy = 0
y = 0
x = 0

# -------------------------------------------------------------------------------

# 読み込んだデータにthresholdを設定
threshold = -28  # スレッショルドの指定
for track in tracks.values():
    track["Threshold"] = threshold


# -------------------------------------------------------------------------------
def CubaseSelect():  # タスクバーからCubaseを選択する関数
    pyautogui.hotkey("win", "2")


def soundSpeedCalc():  # 指定された気温での音速を計算する関数
    temperature = float(input_temperature.get())
    speed_of_sound = round((temperature * 0.6 + 331.5), 2)
    # 設定を保存
    settings["temperature"] = temperature
    save_settings(settings)
    custom_print(
        f"気温は{temperature}℃ として処理を行いました。\n音速は{speed_of_sound}m/sとして処理を行いました。"
    )
    return speed_of_sound


def attackTimeCalc(button_number):  # アタックタイムを計算する関数
    speed_of_sound = soundSpeedCalc()  # 指定された気温での音速を計算する
    # 一番最速のアタックタイムの値を取得する
    fastest = float(input_fastest.get())
    # 前後の距離の差の値を取得する
    distance_difference = float(input_distance_difference.get())
    # 設定を保存
    settings["fastest"] = fastest
    settings["distance_difference"] = distance_difference
    save_settings(settings)
    # ----------------------------------------------------------------
    # 前後の距離の差進む時間(ms)を計算する。
    forward_time = distance_difference / (speed_of_sound / one_second)
    # アタックタイムを計算する
    attack_time = round((fastest + (forward_time * (button_number - 1))), 2)
    return attack_time


def releaseReleaseCalc(button_num, attack_time):  # リリースタイムを計算する関数
    # BPMの値を取得する
    bpm = float(input_bpm.get())
    # 設定を保存
    settings["bpm"] = bpm
    save_settings(settings)
    # 指定BPMでの4分音符の音価(ms)を求める
    common_beat_time = float(one_minutes) / float(bpm)
    ReleaseType = combobox.get()

    if ReleaseType == "whole":
        r = note_1
    elif ReleaseType == "Half":
        r = note_2
    elif ReleaseType == "Quarter":
        r = note_4
    elif ReleaseType == "8th":
        r = note_8
    elif ReleaseType == "16th":
        r = note_16
    elif ReleaseType == "32nd":
        r = note_32
    elif ReleaseType == "64th":
        r = note_64
    elif ReleaseType == "128th":
        r = note_128
    elif ReleaseType == "256th":
        r = note_256
    elif ReleaseType == "8thDot":
        r = note_8thDot
    elif ReleaseType == "16thDot":
        r = note_8thDot
    else:
        r = tracks[str(button_num)]["ReleaseTime"]
    custom_print(f"リリースタイムに使用する音符の種類：{ReleaseType},{r}")
    # リリースタイムの長さを計算
    track_release_time = round((common_beat_time * r), 2)
    # 主要な音符の音価からアタックタイム引いた値をリリースタイムにする
    release_time = track_release_time - attack_time
    return release_time


# カスタムprint関数の定義
def custom_print(message):
    output_text.insert(tkinter.END, message + "\n")
    output_text.see(tkinter.END)


def ProC2(button_num):  # fabfilter ProC-2に値を書き込む関数
    # CubaseSelect()  # タスクバーからCubaseを選択
    track_key = str(len(tracks) - 1 - button_num)
    button_number = float(tracks[track_key]["Num"])

    # 現在の処理をターミナルに表示
    custom_print(
        f"\n【{int(button_number)}】{tracks[track_key]['Inst']} ------------------"
    )

    # ----------------------------------------------------------------
    # 現在のマウス位置を記憶しておく
    home_x, home_y = pyautogui.position()

    # ----------------------------------------------------------------
    attack_time = attackTimeCalc(button_number)  # アタックタイムを計算する
    release_time = releaseReleaseCalc(
        button_num, attack_time
    )  # リリースタイムを計算する

    # ----------------------------------------------------------------
    # fabfilter ProC-2のアタックタイムの座標をクリック。
    pyautogui.click(c2_close_x - 344, c2_close_y + 330, 1, 0.5, "left")
    pyautogui.click(c2_close_x - 344, c2_close_y + 330, 2, 0.2, "left")

    # 指定したアタックタイムを入力。
    pyautogui.typewrite(f"{attack_time}")
    # エンターキーを押して確定。
    pyautogui.press("enter")
    custom_print(f"Attack time: {attack_time}(ms)")

    # ----------------------------------------------------------------
    # fabfilter ProC-2のリリースタイムの座標をクリック。
    pyautogui.click(c2_close_x - 214, c2_close_y + 330, 2, 0.2, "left")
    # （アタックタイムを引いた）リリースタイムを入力。
    pyautogui.typewrite(f"{release_time}")
    # エンターキーを押して確定。
    pyautogui.press("enter")
    custom_print(f"Release time: {release_time}(ms)")

    # ----------------------------------------------------------------
    # fabfilter ProC-2のウインドウを閉じる
    pyautogui.click(c2_close_x, c2_close_y, 1, 0, "left")
    pyautogui.moveTo(home_x, home_y)


# -------------------------------------------------------------------------------
def place(i, addx, addy, y):  # ボタン配置をズラすための関数
    addy += 1
    if i % 7 == 6:
        addx += 120
        y = 50
        addy = 0
    return addx, addy, y


# ウィンドウの作成
root = tkinter.Tk()
root.title("Cubase便利アイテム")  # ウィンドウのタイトル

# JSONから読み込んだウィンドウ設定を適用
window_geometry = f"{settings['window_width']}x{settings['window_height']}+{settings['window_x']}+{settings['window_y']}"
root.geometry(window_geometry)


def save_window_position(event=None):
    # ウィンドウの位置とサイズを取得
    geometry = root.geometry()
    match = re.match(r"(\d+)x(\d+)\+(-?\d+)\+(-?\d+)", geometry)
    if match:
        width, height, x, y = map(int, match.groups())
        settings["window_width"] = width
        settings["window_height"] = height
        settings["window_x"] = x
        settings["window_y"] = y
        save_settings(settings)


# ウィンドウの移動や大きさの変更を検知してJSONに保存
root.bind("<Configure>", save_window_position)

# テキストボックス
lbl1 = tkinter.Label(text="BPM")
lbl1.place(x=10, y=0)
input_bpm = tkinter.Entry(width=7)
input_bpm.place(x=10, y=20)
input_bpm.insert(tkinter.END, settings["bpm"])

lbl2 = tkinter.Label(text="気温(℃)")
lbl2.place(x=65, y=0)
input_temperature = tkinter.Entry(width=7)
input_temperature.place(x=65, y=20)
input_temperature.insert(tkinter.END, settings["temperature"])

lbl3 = tkinter.Label(text="リリースタイム")
lbl3.place(x=260, y=0)

lbl4 = tkinter.Label(text="前後差(m)")
lbl4.place(x=120, y=0)
input_distance_difference = tkinter.Entry(width=7)
input_distance_difference.place(x=120, y=20)
input_distance_difference.insert(tkinter.END, settings["distance_difference"])

lbl5 = tkinter.Label(text="最速(ms)")
lbl5.place(x=185, y=0)
input_fastest = tkinter.Entry(width=7)
input_fastest.place(x=185, y=20)
input_fastest.insert(tkinter.END, settings["fastest"])

# -----------------------------------------
# ドロップダウンリスト
module = (
    "None",
    "Whole",
    "Half",
    "Quarter",
    "8th",
    "16th",
    "32nd",
    "64th",
    "128th",
    "256th",
    "8thDot",
    "16thDot",
)
combobox = ttk.Combobox(
    root,
    height=12,
    width=7,
    values=module,
)
combobox.pack(pady=25)

# -----------------------------------------
# ボタンを生成する
for i in range(34):
    addx, addy, y = place(i, addx, addy, y)
    button = tkinter.Button(
        root,
        text=f"{tracks[str(i)]['Num']}.{tracks[str(i)]['Inst']}",
        command=lambda i=i: ProC2(len(tracks) - i - 1),
    )
    button.place(x=10 + addx, y=50 + 30 * addy)


# 1. Textウィジェットの追加
output_text = tkinter.Text(root, width=50, height=10)
output_text.place(x=10, y=280)

# 音価を表示するフレームを作成
note_frame = tkinter.Frame(root)
note_frame.place(x=10, y=400)

# 単位切り替えの状態を保持する変数
show_seconds = tkinter.BooleanVar(value=False)


def toggle_unit():
    show_seconds.set(not show_seconds.get())
    calculate_note_values()


def format_time(ms_value):
    if show_seconds.get():
        return f"{round(ms_value/1000, 3)}s"
    return f"{round(ms_value, 2)}ms"


def calculate_note_values():
    try:
        bpm = float(input_bpm.get())
        ms_per_beat = one_minutes / bpm

        notes = {
            "全音符": ms_per_beat * 4,
            "2分音符": ms_per_beat * 2,
            "4分音符": ms_per_beat,
            "8分音符": ms_per_beat / 2,
            "16分音符": ms_per_beat / 4,
            "32分音符": ms_per_beat / 8,
            "64分音符": ms_per_beat / 16,
            "128分音符": ms_per_beat / 32,
            "256分音符": ms_per_beat / 64,
            "付点8分音符": ms_per_beat * 0.75,
            "付点16分音符": ms_per_beat * 0.375,
        }

        # 既存のボタンを削除
        for widget in note_frame.winfo_children():
            widget.destroy()

        # 単位切り替えボタンを作成
        unit_btn = tkinter.Button(
            note_frame, text="ms⇔s", command=toggle_unit, width=6, height=2
        )
        unit_btn.grid(row=0, column=0, padx=2)

        # 新しい音価ボタンを作成
        items = list(notes.items())
        row1_items = items[:6]  # 全音符から32分音符まで
        row2_items = items[6:]  # 64分音符以降と付点音符

        # 1行目のボタンを作成
        for i, (name, value) in enumerate(row1_items):

            def make_copy_command(v=value):
                return lambda: pyperclip.copy(str(round(v, 2)))

            btn = tkinter.Button(
                note_frame,
                text=f"{name}\n{format_time(value)}",
                command=make_copy_command(),
                width=10,
                height=2,
            )
            btn.grid(
                row=0, column=i + 1, padx=2
            )  # column=i+1 because column 0 is for unit toggle

        # 2行目のボタンを作成
        for i, (name, value) in enumerate(row2_items):

            def make_copy_command(v=value):
                return lambda: pyperclip.copy(str(round(v, 2)))

            btn = tkinter.Button(
                note_frame,
                text=f"{name}\n{format_time(value)}",
                command=make_copy_command(),
                width=10,
                height=2,
            )
            btn.grid(
                row=1, column=i + 1, padx=2
            )  # Start from column 1 to align with first row

    except ValueError:
        pass


# BPMの入力欄の値が変更されたときに音価を更新
input_bpm.bind("<KeyRelease>", lambda e: calculate_note_values())

# 初期表示
calculate_note_values()

def main():
    # ウィンドウのループ処理
    root.mainloop()

if __name__ == "__main__":
    main()
