import tkinter
import time
import pyautogui
import tkinter.ttk as ttk

# -------------------------------------------------------------------------------
# グローバル変数たち

# Pro-C2の「戻るボタン」の座標
c2_close_x, c2_close_y = 1318, 281
c2_close_x, c2_close_y = 2659, 332
c2_close_x, c2_close_y = 1318, 276

threshold = -28  # スレッショルドの指定
attack_time = 10  # ダミーのアタックタイム

one_minutes = 60000  # 1分の秒数(ms)

# 指定BPMの主要な音符の音価(リリースタイムに使う)を計算する。
note_1 = 4  # 全音符(ms)
note_2 = 2  # 2分音符(ms)
note_4 = 1  # 4分音符(ms)
note_8 = 1 / 2  # 8分音符(ms)
note_16 = 1 / 4  # 16分音符(ms)
note_32 = 1 / 8  # 32分音符(ms)
note_8thDot = 3 / 4  # 付点8分音符
note_16thDot = 3 / 8  # 付点16分音符

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
    temperature = int(input_temperature.get())
    speed_of_sound = round((temperature * 0.6 + 331.5), 2)
    print(f"気温は{temperature}℃\n音速は{speed_of_sound}m/sとして処理を行いました。")
    return speed_of_sound


def attackTimeCalc(button_num):  # アタックタイムを計算する関数
    speed_of_sound = soundSpeedCalc()  # 指定された気温での音速を計算する
    # ----------------------------------------------------------------
    count_num = len(tracks) - 1 - button_num
    attack_time = round((((8.25 - (0.25 * count_num)) / speed_of_sound) * 1000), 2)
    return attack_time


def releaseReleaseCalc(button_num, attack_time):  # リリースタイムを計算する関数
    # BPMの値を取得する
    bpm = int(input_bpm.get())
    # 指定BPMでの4分音符の音価(ms)を求める
    common_beat_time = int(one_minutes) / int(bpm)

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
    print(ReleaseType, r)
    # リリースタイムの長さを計算
    track_release_time = round((common_beat_time * r), 2)
    release_time = track_release_time - attack_time
    return release_time


def ProC2(button_num):  # fabfilter ProC-2に値を書き込む関数
    CubaseSelect()  # タスクバーからCubaseを選択

    # 現在の処理をターミナルに表示
    print(
        f"{tracks[len(tracks)-1 - button_num]['Num']}：{tracks[len(tracks)-1 - button_num]['Inst']}------"
    )

    # ----------------------------------------------------------------
    # 現在のマウス位置を記憶しておく
    home_x, home_y = pyautogui.position()

    # ----------------------------------------------------------------
    attack_time = attackTimeCalc(button_num)  # アタックタイムを計算する
    release_time = releaseReleaseCalc(button_num, attack_time)  # リリースタイムを計算する

    # ----------------------------------------------------------------
    # fabfilter ProC-2のアタックタイムの座標をクリック。
    pyautogui.click(c2_close_x - 344, c2_close_y + 330, 1, 0.5, "left")
    pyautogui.click(c2_close_x - 344, c2_close_y + 330, 2, 0.2, "left")

    # 指定したアタックタイムを入力。
    pyautogui.typewrite(f"{attack_time}")
    # エンターキーを押して確定。
    pyautogui.press("enter")
    print(f"attack time: {attack_time}(ms)")

    # ----------------------------------------------------------------
    # fabfilter ProC-2のリリースタイムの座標をクリック。
    pyautogui.click(c2_close_x - 214, c2_close_y + 330, 2, 0.2, "left")
    # アタックタイムを差し引いたリリースタイムを入力。
    pyautogui.typewrite(f"{release_time}")
    # エンターキーを押して確定。
    pyautogui.press("enter")
    print(f"release time: {release_time}(ms)")

    # ----------------------------------------------------------------
    # fabfilter ProC-2のウインドウを閉じる
    pyautogui.click(c2_close_x, c2_close_y, 1, 0, "left")
    pyautogui.moveTo(home_x, home_y)


def place(i, addx, addy, y):  # ボタン配置をズラすための関数
    addy += 1
    if i % 7 == 6:
        addx += 120
        y = 50
        addy = 0
    return addx, addy, y


# -------------------------------------------------------------------------------
# ウィンドウの作成
root = tkinter.Tk()
root.title("Cubase便利アイテム")  # ウィンドウのタイトル
root.geometry("600x400")  # ウィンドウのサイズ
root.geometry("+2500+2")  # ウィンドウの出現位置

# テキストボックス
lbl1 = tkinter.Label(text="BPM")
lbl1.place(x=10, y=0)
input_bpm = tkinter.Entry(width=10)
input_bpm.place(x=40, y=0)
input_bpm.insert(tkinter.END, 128)

lbl2 = tkinter.Label(text="気温(℃)")
lbl2.place(x=120, y=0)
input_temperature = tkinter.Entry(width=6)
input_temperature.place(x=170, y=0)
input_temperature.insert(tkinter.END, 15)

lbl3 = tkinter.Label(text="リリースタイム")
lbl3.place(x=250, y=0)
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

addx, addy, y = place(0, addx, addy, y)
button0 = tkinter.Button(
    root,
    text=f"{tracks[0]['Num']}.{tracks[0]['Inst']}",
    command=lambda: ProC2(len(tracks) - 0 - 1),
)
button0.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(1, addx, addy, y)
button1 = tkinter.Button(
    root,
    text=f"{tracks[1]['Num']}.{tracks[1]['Inst']}",
    command=lambda: ProC2(len(tracks) - 1 - 1),
)
button1.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(2, addx, addy, y)
button2 = tkinter.Button(
    root,
    text=f"{tracks[2]['Num']}.{tracks[2]['Inst']}",
    command=lambda: ProC2(len(tracks) - 2 - 1),
)
button2.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(3, addx, addy, y)
button3 = tkinter.Button(
    root,
    text=f"{tracks[3]['Num']}.{tracks[3]['Inst']}",
    command=lambda: ProC2(len(tracks) - 3 - 1),
)
button3.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(4, addx, addy, y)
button4 = tkinter.Button(
    root,
    text=f"{tracks[4]['Num']}.{tracks[4]['Inst']}",
    command=lambda: ProC2(len(tracks) - 4 - 1),
)
button4.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(5, addx, addy, y)
button5 = tkinter.Button(
    root,
    text=f"{tracks[5]['Num']}.{tracks[5]['Inst']}",
    command=lambda: ProC2(len(tracks) - 5 - 1),
)
button5.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(6, addx, addy, y)
button6 = tkinter.Button(
    root,
    text=f"{tracks[6]['Num']}.{tracks[6]['Inst']}",
    command=lambda: ProC2(len(tracks) - 6 - 1),
)
button6.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(7, addx, addy, y)
button7 = tkinter.Button(
    root,
    text=f"{tracks[7]['Num']}.{tracks[7]['Inst']}",
    command=lambda: ProC2(len(tracks) - 7 - 1),
)
button7.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(8, addx, addy, y)
button8 = tkinter.Button(
    root,
    text=f"{tracks[8]['Num']}.{tracks[8]['Inst']}",
    command=lambda: ProC2(len(tracks) - 8 - 1),
)
button8.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(9, addx, addy, y)
button9 = tkinter.Button(
    root,
    text=f"{tracks[9]['Num']}.{tracks[9]['Inst']}",
    command=lambda: ProC2(len(tracks) - 9 - 1),
)
button9.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(10, addx, addy, y)
button10 = tkinter.Button(
    root,
    text=f"{tracks[10]['Num']}.{tracks[10]['Inst']}",
    command=lambda: ProC2(len(tracks) - 10 - 1),
)
button10.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(11, addx, addy, y)
button11 = tkinter.Button(
    root,
    text=f"{tracks[11]['Num']}.{tracks[11]['Inst']}",
    command=lambda: ProC2(len(tracks) - 11 - 1),
)
button11.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(12, addx, addy, y)
button12 = tkinter.Button(
    root,
    text=f"{tracks[12]['Num']}.{tracks[12]['Inst']}",
    command=lambda: ProC2(len(tracks) - 12 - 1),
)
button12.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(13, addx, addy, y)
button13 = tkinter.Button(
    root,
    text=f"{tracks[13]['Num']}.{tracks[13]['Inst']}",
    command=lambda: ProC2(len(tracks) - 13 - 1),
)
button13.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(14, addx, addy, y)
button14 = tkinter.Button(
    root,
    text=f"{tracks[14]['Num']}.{tracks[14]['Inst']}",
    command=lambda: ProC2(len(tracks) - 14 - 1),
)
button14.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(15, addx, addy, y)
button15 = tkinter.Button(
    root,
    text=f"{tracks[15]['Num']}.{tracks[15]['Inst']}",
    command=lambda: ProC2(len(tracks) - 15 - 1),
)
button15.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(16, addx, addy, y)
button16 = tkinter.Button(
    root,
    text=f"{tracks[16]['Num']}.{tracks[16]['Inst']}",
    command=lambda: ProC2(len(tracks) - 16 - 1),
)
button16.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(17, addx, addy, y)
button17 = tkinter.Button(
    root,
    text=f"{tracks[17]['Num']}.{tracks[17]['Inst']}",
    command=lambda: ProC2(len(tracks) - 17 - 1),
)
button17.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(18, addx, addy, y)
button18 = tkinter.Button(
    root,
    text=f"{tracks[18]['Num']}.{tracks[18]['Inst']}",
    command=lambda: ProC2(len(tracks) - 18 - 1),
)
button18.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(19, addx, addy, y)
button19 = tkinter.Button(
    root,
    text=f"{tracks[19]['Num']}.{tracks[19]['Inst']}",
    command=lambda: ProC2(len(tracks) - 19 - 1),
)
button19.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(20, addx, addy, y)
button20 = tkinter.Button(
    root,
    text=f"{tracks[20]['Num']}.{tracks[20]['Inst']}",
    command=lambda: ProC2(len(tracks) - 20 - 1),
)
button20.place(x=10 + addx, y=50 + 30 * addy)


addx, addy, y = place(21, addx, addy, y)
button21 = tkinter.Button(
    root,
    text=f"{tracks[21]['Num']}.{tracks[21]['Inst']}",
    command=lambda: ProC2(len(tracks) - 21 - 1),
)
button21.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(22, addx, addy, y)
button22 = tkinter.Button(
    root,
    text=f"{tracks[22]['Num']}.{tracks[22]['Inst']}",
    command=lambda: ProC2(len(tracks) - 22 - 1),
)
button22.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(23, addx, addy, y)
button23 = tkinter.Button(
    root,
    text=f"{tracks[23]['Num']}.{tracks[23]['Inst']}",
    command=lambda: ProC2(len(tracks) - 23 - 1),
)
button23.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(24, addx, addy, y)
button24 = tkinter.Button(
    root,
    text=f"{tracks[24]['Num']}.{tracks[24]['Inst']}",
    command=lambda: ProC2(len(tracks) - 24 - 1),
)
button24.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(25, addx, addy, y)
button25 = tkinter.Button(
    root,
    text=f"{tracks[25]['Num']}.{tracks[25]['Inst']}",
    command=lambda: ProC2(len(tracks) - 25 - 1),
)
button25.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(26, addx, addy, y)
button26 = tkinter.Button(
    root,
    text=f"{tracks[26]['Num']}.{tracks[26]['Inst']}",
    command=lambda: ProC2(len(tracks) - 26 - 1),
)
button26.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(27, addx, addy, y)
button27 = tkinter.Button(
    root,
    text=f"{tracks[27]['Num']}.{tracks[27]['Inst']}",
    command=lambda: ProC2(len(tracks) - 27 - 1),
)
button27.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(28, addx, addy, y)
button28 = tkinter.Button(
    root,
    text=f"{tracks[28]['Num']}.{tracks[28]['Inst']}",
    command=lambda: ProC2(len(tracks) - 28 - 1),
)
button28.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(29, addx, addy, y)
button29 = tkinter.Button(
    root,
    text=f"{tracks[29]['Num']}.{tracks[29]['Inst']}",
    command=lambda: ProC2(len(tracks) - 29 - 1),
)
button29.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(30, addx, addy, y)
button30 = tkinter.Button(
    root,
    text=f"{tracks[30]['Num']}.{tracks[30]['Inst']}",
    command=lambda: ProC2(len(tracks) - 30 - 1),
)
button30.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(31, addx, addy, y)
button31 = tkinter.Button(
    root,
    text=f"{tracks[31]['Num']}.{tracks[31]['Inst']}",
    command=lambda: ProC2(len(tracks) - 31 - 1),
)
button31.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(32, addx, addy, y)
button32 = tkinter.Button(
    root,
    text=f"{tracks[32]['Num']}.{tracks[32]['Inst']}",
    command=lambda: ProC2(len(tracks) - 32 - 1),
)
button32.place(x=10 + addx, y=50 + 30 * addy)

addx, addy, y = place(33, addx, addy, y)
button33 = tkinter.Button(
    root,
    text=f"{tracks[33]['Num']}.{tracks[33]['Inst']}",
    command=lambda: ProC2(len(tracks) - 33 - 1),
)
button33.place(x=10 + addx, y=50 + 30 * addy)


# ウィンドウのループ処理
root.mainloop()

# 分と小節数を消す
