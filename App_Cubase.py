import tkinter
import pyautogui
import tkinter.ttk as ttk

# -------------------------------------------------------------------------------
# グローバル変数たち

set_bpm = 120
set_temperature = 15
set_distance_difference = 0.2
set_fastest = 10

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
note_8thDot = 3 / 4  # 付点8分音符
note_16thDot = 3 / 8  # 付点16分音符

# 座標
addx = 0
addy = 0
y = 0
x = 0

# -------------------------------------------------------------------------------

# コンプレッサーの情報を格納する配列
# 0トラック番号,1トラック名,2スレッショルド,3レシオ,4アタックタイム,5リリースタイム,6ゲイン
tracks = {
    0: {
        "Num": 34,
        "Inst": "Vocal 1",
        "Threshold": threshold,
        "Ratio": "7.5",
        "ReleaseTime": note_8,
        "Gain": "-5",
    },
    1: {
        "Num": 33,
        "Inst": "Solo 1",
        "Threshold": threshold,
        "Ratio": "7",
        "ReleaseTime": note_16,
        "Gain": "-5",
    },
    2: {
        "Num": 32,
        "Inst": "Kick",
        "Threshold": threshold,
        "Ratio": "6",
        "ReleaseTime": note_8,
        "Gain": "-5",
    },
    3: {
        "Num": 31,
        "Inst": "Kick sub",
        "Threshold": threshold,
        "Ratio": "5",
        "ReleaseTime": note_4,
        "Gain": "-5",
    },
    4: {
        "Num": 30,
        "Inst": "Snare 1",
        "Threshold": threshold,
        "Ratio": "7",
        "ReleaseTime": note_8,
        "Gain": "-5",
    },
    5: {
        "Num": 29,
        "Inst": "Clap",
        "Threshold": threshold,
        "Ratio": "7",
        "ReleaseTime": note_16,
        "Gain": "-5",
    },
    6: {
        "Num": 28,
        "Inst": "Solo 2",
        "Threshold": threshold,
        "Ratio": "9",
        "ReleaseTime": note_4,
        "Gain": "-10",
    },
    7: {
        "Num": 27,
        "Inst": "Hamori",
        "Threshold": threshold,
        "Ratio": "10",
        "ReleaseTime": note_4,
        "Gain": "-10",
    },
    8: {
        "Num": 26,
        "Inst": "Snare bottom",
        "Threshold": threshold,
        "Ratio": "8",
        "ReleaseTime": note_4,
        "Gain": "-5",
    },
    9: {
        "Num": 25,
        "Inst": "hihat Sample",
        "Threshold": threshold,
        "Ratio": "5.5",
        "ReleaseTime": note_8,
        "Gain": "0",
    },
    10: {
        "Num": 24,
        "Inst": "hihat",
        "Threshold": threshold,
        "Ratio": "4.5",
        "ReleaseTime": note_16,
        "Gain": "0",
    },
    11: {
        "Num": 23,
        "Inst": "Ride",
        "Threshold": threshold,
        "Ratio": "6.5",
        "ReleaseTime": note_4,
        "Gain": "0",
    },
    12: {
        "Num": 22,
        "Inst": "F-Gt",
        "Threshold": threshold,
        "Ratio": "5.5",
        "ReleaseTime": note_4,
        "Gain": "-10",
    },
    13: {
        "Num": 21,
        "Inst": "B-Gt clean",
        "Threshold": threshold,
        "Ratio": "5.5",
        "ReleaseTime": note_4,
        "Gain": "-10",
    },
    14: {
        "Num": 20,
        "Inst": "F-Instrument",
        "Threshold": threshold,
        "Ratio": "6.5",
        "ReleaseTime": note_8,
        "Gain": "-10",
    },
    15: {
        "Num": 19,
        "Inst": "M-Instrument",
        "Threshold": threshold,
        "Ratio": "5.5",
        "ReleaseTime": note_16,
        "Gain": "-10",
    },
    16: {
        "Num": 18,
        "Inst": "B-Instrument",
        "Threshold": threshold,
        "Ratio": "4.5",
        "ReleaseTime": note_4,
        "Gain": "-10",
    },
    17: {
        "Num": 17,
        "Inst": "Bass solo",
        "Threshold": threshold,
        "Ratio": "7.5",
        "ReleaseTime": note_4,
        "Gain": "-10",
    },
    18: {
        "Num": 16,
        "Inst": "Bass Bus",
        "Threshold": threshold,
        "Ratio": "5.5",
        "ReleaseTime": note_4,
        "Gain": "-10",
    },
    19: {
        "Num": 15,
        "Inst": "Synth Bass",
        "Threshold": threshold,
        "Ratio": "4",
        "ReleaseTime": note_8,
        "Gain": "-10",
    },
    20: {
        "Num": 14,
        "Inst": "Percussion",
        "Threshold": threshold,
        "Ratio": "5",
        "ReleaseTime": note_16,
        "Gain": "0",
    },
    21: {
        "Num": 13,
        "Inst": "Cymbal",
        "Threshold": threshold,
        "Ratio": "4",
        "ReleaseTime": note_4,
        "Gain": "-5",
    },
    22: {
        "Num": 12,
        "Inst": "Tom 1",
        "Threshold": threshold,
        "Ratio": "5",
        "ReleaseTime": note_4,
        "Gain": "0",
    },
    23: {
        "Num": 11,
        "Inst": "Tom 2",
        "Threshold": threshold,
        "Ratio": "5",
        "ReleaseTime": note_4,
        "Gain": "0",
    },
    24: {
        "Num": 10,
        "Inst": "Floor Tom",
        "Threshold": threshold,
        "Ratio": "4",
        "ReleaseTime": note_8,
        "Gain": "0",
    },
    25: {
        "Num": 9,
        "Inst": "Piano/E Piano",
        "Threshold": threshold,
        "Ratio": "3.2",
        "ReleaseTime": note_16,
        "Gain": "-5",
    },
    26: {
        "Num": 8,
        "Inst": "Over Head",
        "Threshold": threshold,
        "Ratio": "3",
        "ReleaseTime": note_4,
        "Gain": "0",
    },
    27: {
        "Num": 7,
        "Inst": "Mono",
        "Threshold": threshold,
        "Ratio": "4.5",
        "ReleaseTime": note_4,
        "Gain": "0",
    },
    28: {
        "Num": 6,
        "Inst": "Brass",
        "Threshold": threshold,
        "Ratio": "2.5",
        "ReleaseTime": note_4,
        "Gain": "-10",
    },
    29: {
        "Num": 5,
        "Inst": "Comp",
        "Threshold": threshold,
        "Ratio": "5.5",
        "ReleaseTime": note_8,
        "Gain": "0",
    },
    30: {
        "Num": 4,
        "Inst": "Room",
        "Threshold": threshold,
        "Ratio": "1.5",
        "ReleaseTime": note_16,
        "Gain": "0",
    },
    31: {
        "Num": 3,
        "Inst": "Strings",
        "Threshold": threshold,
        "Ratio": "1.5",
        "ReleaseTime": note_4,
        "Gain": "-10",
    },
    32: {
        "Num": 2,
        "Inst": "Amb",
        "Threshold": threshold,
        "Ratio": "2",
        "ReleaseTime": note_4,
        "Gain": "0",
    },
    33: {
        "Num": 1,
        "Inst": "Pad",
        "Threshold": threshold,
        "Ratio": "1.2",
        "ReleaseTime": note_4,
        "Gain": "-10",
    },
}

# -------------------------------------------------------------------------------
def CubaseSelect():  # タスクバーからCubaseを選択する関数
    pyautogui.hotkey("win", "2")


def soundSpeedCalc():  # 指定された気温での音速を計算する関数
    temperature = float(input_temperature.get())
    speed_of_sound = round((temperature * 0.6 + 331.5), 2)
    custom_print(f"気温は{temperature}℃ として処理を行いました。\n音速は{speed_of_sound}m/sとして処理を行いました。")
    return speed_of_sound


def attackTimeCalc(button_number):  # アタックタイムを計算する関数
    speed_of_sound = soundSpeedCalc()  # 指定された気温での音速を計算する
    # 一番最速のアタックタイムの値を取得する
    fastest = float(input_fastest.get())
    # 前後の距離の差の値を取得する
    distance_difference = float(input_distance_difference.get())
    # ----------------------------------------------------------------
    # 前後の距離の差進む時間(ms)を計算する。
    forward_time = distance_difference / (speed_of_sound / one_second)
    # アタックタイムを計算する
    attack_time = round((fastest + (forward_time * (button_number - 1))), 2)
    return attack_time


def releaseReleaseCalc(button_num, attack_time):  # リリースタイムを計算する関数
    # BPMの値を取得する
    bpm = float(input_bpm.get())
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
    elif ReleaseType == "8thDot":
        r = note_8thDot
    elif ReleaseType == "16thDot":
        r = note_8thDot
    else:
        r = tracks[button_num]["ReleaseTime"]
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
    button_number = float(tracks[len(tracks) - 1 - button_num]["Num"])

    # 現在の処理をターミナルに表示
    custom_print(
        f"\n【{int(button_number)}】{tracks[len(tracks)-1 - button_num]['Inst']} ------------------"
    )

    # ----------------------------------------------------------------
    # 現在のマウス位置を記憶しておく
    home_x, home_y = pyautogui.position()

    # ----------------------------------------------------------------
    attack_time = attackTimeCalc(button_number)  # アタックタイムを計算する
    release_time = releaseReleaseCalc(button_num, attack_time)  # リリースタイムを計算する

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
root.geometry("600x450")  # ウィンドウのサイズ
root.geometry("+2300+2")  # ウィンドウの出現位置

# テキストボックス
lbl1 = tkinter.Label(text="BPM")
lbl1.place(x=10, y=0)
input_bpm = tkinter.Entry(width=7)
input_bpm.place(x=10, y=20)
input_bpm.insert(tkinter.END, set_bpm)

lbl2 = tkinter.Label(text="気温(℃)")
lbl2.place(x=65, y=0)
input_temperature = tkinter.Entry(width=7)
input_temperature.place(x=65, y=20)
input_temperature.insert(tkinter.END, set_temperature)

lbl3 = tkinter.Label(text="リリースタイム")
lbl3.place(x=260, y=0)

lbl4 = tkinter.Label(text="前後差(m)")
lbl4.place(x=120, y=0)
input_distance_difference = tkinter.Entry(width=7)
input_distance_difference.place(x=120, y=20)
input_distance_difference.insert(tkinter.END, set_distance_difference)

lbl5 = tkinter.Label(text="最速(ms)")
lbl5.place(x=185, y=0)
input_fastest = tkinter.Entry(width=7)
input_fastest.place(x=185, y=20)
input_fastest.insert(tkinter.END, set_fastest)

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
    "8thDot",
    "16thDot",
)
combobox = ttk.Combobox(
    root,
    height=9,
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
        text=f"{tracks[i]['Num']}.{tracks[i]['Inst']}",
        command=lambda i=i: ProC2(len(tracks) - i - 1),
    )
    button.place(x=10 + addx, y=50 + 30 * addy)


# 1. Textウィジェットの追加
output_text = tkinter.Text(root, width=50, height=10)
output_text.place(x=10, y=280)

# ウィンドウのループ処理
root.mainloop()
