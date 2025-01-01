import tkinter
import pyautogui
import tkinter.ttk as ttk
import json

# -------------------------------------------------------------------------------
# JSONファイルから設定を読み込む
def load_settings():
    with open('cubase.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data['settings'], data['tracks']

def save_settings(settings):
    with open('cubase.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    data['settings'] = settings
    with open('cubase.json', 'w', encoding='utf-8') as f:
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
    settings['temperature'] = temperature
    save_settings(settings)
    custom_print(f"気温は{temperature}℃ として処理を行いました。\n音速は{speed_of_sound}m/sとして処理を行いました。")
    return speed_of_sound


def attackTimeCalc(button_number):  # アタックタイムを計算する関数
    speed_of_sound = soundSpeedCalc()  # 指定された気温での音速を計算する
    # 一番最速のアタックタイムの値を取得する
    fastest = float(input_fastest.get())
    # 前後の距離の差の値を取得する
    distance_difference = float(input_distance_difference.get())
    # 設定を保存
    settings['fastest'] = fastest
    settings['distance_difference'] = distance_difference
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
    settings['bpm'] = bpm
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
input_bpm.insert(tkinter.END, settings['bpm'])

lbl2 = tkinter.Label(text="気温(℃)")
lbl2.place(x=65, y=0)
input_temperature = tkinter.Entry(width=7)
input_temperature.place(x=65, y=20)
input_temperature.insert(tkinter.END, settings['temperature'])

lbl3 = tkinter.Label(text="リリースタイム")
lbl3.place(x=260, y=0)

lbl4 = tkinter.Label(text="前後差(m)")
lbl4.place(x=120, y=0)
input_distance_difference = tkinter.Entry(width=7)
input_distance_difference.place(x=120, y=20)
input_distance_difference.insert(tkinter.END, settings['distance_difference'])

lbl5 = tkinter.Label(text="最速(ms)")
lbl5.place(x=185, y=0)
input_fastest = tkinter.Entry(width=7)
input_fastest.place(x=185, y=20)
input_fastest.insert(tkinter.END, settings['fastest'])

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
