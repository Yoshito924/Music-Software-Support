import tkinter

import pyautogui
import pyperclip
import time

# Pro-C2の戻るボタンの座標
c2_close_x, c2_close_y = 1318, 281

count_num = 0  # 現在何回目の試行かをカウントする。

temperature = 15  # 気温の想定(℃)
speed_of_sound = round((temperature*0.6+331.5), 2)  # 指定された気温での音速を計算する

threshold = -28  # スレッショルドの指定
attack_time = 10  # ダミーのアタックタイム

one_minutes = 60000  # 1分の秒数(ms)

# 指定BPMの主要な音符の音価(リリースタイムに使う)を計算する。
note_1 = 4  # 全音符(ms)
note_2 = 2  # 2分音符(ms)
note_4 = 1  # 4分音符(ms)
note_8 = 1/2  # 8分音符(ms)
note_16 = 1/4  # 16分音符(ms)
note_32 = 1/8  # 32分音符(ms)
# -------------------------------------------------------------------------------

# コンプレッサーの情報を格納する配列
# 0トラック番号,1トラック名,2スレッショルド,3レシオ,4アタックタイム,5リリースタイム,6ゲイン
tracks = [
    ['34', 'Vocal 1', threshold, '7.5', 'attack_time', note_8, '-5'],
    ['33', 'Solo 1', threshold, '7', 'attack_time', note_16, '-5'],
    ['32', 'Kick', threshold, '6', 'attack_time', note_8, '-5'],
    ['31', 'Kick sub', threshold, '5', 'attack_time', note_4, '-5'],
    ['30', 'Snare 1', threshold, '7', 'attack_time', note_8, '-5'],

    ['29', 'Clap', threshold, '7', 'attack_time', note_16, '-5'],
    ['28', 'Solo 2', threshold, '9', 'attack_time', note_4, '-10'],
    ['27', 'Hamori', threshold, '10', 'attack_time', note_4, '-10'],
    ['26', 'Snare bottom', threshold, '8', 'attack_time', note_4, '-5'],
    ['25', 'hihat Sample', threshold, '5.5', 'attack_time', note_8, '0'],
    ['24', 'hihat', threshold, '4.5', 'attack_time', note_16, '0'],
    ['23', 'Ride', threshold, '6.5', 'attack_time', note_4, '0'],
    ['22', 'F-Gt', threshold, '5.5', 'attack_time', note_4, '-10'],
    ['21', 'B-Gt clean', threshold, '5.5', 'attack_time', note_4, '-10'],
    ['20', 'F-Instrument', threshold, '6.5', 'attack_time', note_8, '-10'],

    ['19', 'M-Instrument', threshold, '5.5', 'attack_time', note_16, '-10'],
    ['18', 'B-Instrument', threshold, '4.5', 'attack_time', note_4, '-10'],
    ['17', 'Bass solo', threshold, '7.5', 'attack_time', note_4, '-10'],
    ['16', 'Bass Bus', threshold, '5.5', 'attack_time', note_4, '-10'],
    ['15', 'Synth Bass', threshold, '4', 'attack_time', note_8, '-10'],
    ['14', 'Percussion', threshold, '5', 'attack_time', note_16, '0'],
    ['13', 'Cymbal', threshold, '4', 'attack_time', note_4, '-5'],
    ['12', 'Tom 1', threshold, '5', 'attack_time', note_4, '0'],
    ['11', 'Tom 2', threshold, '5', 'attack_time', note_4, '0'],

    ['10', 'Floor Tom', threshold, '4', 'attack_time', note_8, '0'],
    ['9', 'Piano/E Piano', threshold, '3.2', 'attack_time', note_16, '-5'],
    ['8', 'Over Head', threshold, '3', 'attack_time', note_4, '0'],
    ['7', 'Mono', threshold, '4.5', 'attack_time', note_4, '0'],
    ['6', 'Brass', threshold, '2.5', 'attack_time', note_4, '-10'],
    ['5', 'Comp', threshold, '5.5', 'attack_time', note_8, '0'],
    ['4', 'Room', threshold, '1.5', 'attack_time', note_16, '0'],
    ['3', 'Strings', threshold, '1.5', 'attack_time', note_4, '-10'],
    ['2', 'Amb', threshold, '2', 'attack_time', note_4, '0'],
    ['1', 'Pad', threshold, '1.2', 'attack_time', note_4, '-10']
]

# tracks = tracks.reverse()
# -------------------------------------------------------------------------------

# Cubaseを選択


def CubaseSelect():
    pyautogui.hotkey("win", "8")


def ProC2(button_num):
    CubaseSelect()
    print(
        f'{tracks[len(tracks)-1 - button_num][0]}：{tracks[len(tracks)-1 - button_num][1]}------')
    CubaseSelect()
    home_x, home_y = pyautogui.position()
    count_num = len(tracks)-1 - button_num
    bpm = int(input_bpm.get())
    temperature = int(input_temperature.get())
    speed_of_sound = round((temperature*0.6+331.5), 2)  # 指定された気温での音速を計算する

    # 指定BPMでの基本的な「1拍」の音価であり,4分音符の音価(ms)
    common_beat_time = int(one_minutes) / int(bpm)
    # ノートの長さを計算
    note = round((common_beat_time * tracks[button_num][5]), 2)

    attack_time = round(
        (((8.25-(0.25*count_num))/speed_of_sound)*1000), 2)  # アタックタイムの計算

    pyautogui.click(1067, 10, 1, 0, 'left')
    # print(f'ratio: {tracks[count_num][3]}:1')
    # pyautogui.click(c2_close_x-554, c2_close_y+330, 2, 0.2, 'left')        #レシオの座標をクリック。
    # pyautogui.typewrite(f'{tracks[count_num][3]}')    #指定したレシオの値を入力。
    # pyautogui.press('enter')                          #エンターキーを押して確定。

    print(f'attack time: {attack_time}(ms)')
    pyautogui.click(c2_close_x-344, c2_close_y+330, 2, 0.2,
                    'left')  # アタックタイムの座標をクリック。
    pyautogui.typewrite(f'{attack_time}')  # 指定したアタックタイムを入力。
    pyautogui.press('enter')  # エンターキーを押して確定。
    print(f'release time: {note-attack_time}(ms)')
    pyautogui.click(c2_close_x-214, c2_close_y+330, 2, 0.2,
                    'left')  # リリースタイムの座標をクリック。
    # アタックタイムを差し引いたリリースタイムを入力。
    pyautogui.typewrite(f'{note-attack_time}')
    pyautogui.press('enter')  # エンターキーを押して確定。
    pyautogui.click(c2_close_x, c2_close_y, 1, 0, 'left')
    pyautogui.moveTo(home_x, home_y)


def all_comp():
    CubaseSelect()
    home_x, home_y = pyautogui.position()
    # カウント用の数字
    loop_num = 34  # トラック数
    track_num = 34  # トラックの表示のために使う
    count_num = 0  # 現在何回目の試行かをカウントする。
    bpm = int(input_bpm.get())
    temperature = int(input_temperature.get())

    speed_of_sound = round((temperature*0.6+331.5), 2)  # 指定された気温での音速を計算する

    threshold = -28  # スレッショルドの指定
    attack_time = 10  # ダミーのアタックタイム

    # 指定BPMでの基本的な「1拍」の音価であり,4分音符の音価(ms)
    common_beat_time = int(one_minutes) / int(bpm)

    print(f'3秒以内に、InspectorのInsertsのPro-C2にカーソルを合わせてください。')

    time.sleep(3)  # プログラムを実行してから、Cubaseの画面を手動で選択するまでの猶予時間

    # InspectorのInsertsのPro-C2の座標を取得
    c2_position_x, c2_position_y = pyautogui.position()

    print(f'3秒以内に、開始位置のトラックにカーソルを合わせてクリックしてください。')
    time.sleep(3)
    position_x, position_y = pyautogui.position()  # 開始地点の座標を取得

    # ループ処理をキメる。
    for i in range(loop_num):
        # ノートの長さを計算
        note = round((common_beat_time * tracks[count_num][5]), 2)
        attack_time = round(
            (((8.25-(0.25*count_num))/speed_of_sound)*1000), 2)  # アタックタイムの計算

        # 現在処理中の工程の値をコンソールに表示する
        print(f'\n{tracks[count_num][0]}.{tracks[count_num][1]}')

        pyautogui.click(position_x, position_y, 2, 0.2, 'left')  # トラックを選択
        # pyautogui.typewrite(f'{tracks[count_num][0]}.{tracks[count_num][1]}')    #指定したトラック名を入力。
        # pyautogui.press('enter')                                                 #エンターキーを押して確定。

        # InspectorのInsertsのPro-C2を選択して起動
        pyautogui.click(c2_position_x, c2_position_y, 1, 0, 'left')
        time.sleep(0.1)

        # print(f'threshold: {tracks[count_num][2]}db')
        # pyautogui.click(c2_close_x-654, c2_close_y+330, 2, 0.2, 'left')        #スレッショルドの座標をクリック。
        # pyautogui.typewrite(f'{tracks[count_num][2]}')    #指定したスレッショルドの値を入力。
        # pyautogui.press('enter')                          #エンターキーを押して確定。

        # print(f'ratio: {tracks[count_num][3]}:1')
        # pyautogui.click(c2_close_x-554, c2_close_y+330, 2, 0.2, 'left')        #レシオの座標をクリック。
        # pyautogui.typewrite(f'{tracks[count_num][3]}')    #指定したレシオの値を入力。
        # pyautogui.press('enter')                          #エンターキーを押して確定。

        print(f'attack time: {attack_time}(ms)')
        pyautogui.click(c2_close_x-344, c2_close_y+330, 2, 0.2,
                        'left')  # アタックタイムの座標をクリック。
        pyautogui.typewrite(f'{attack_time}')  # 指定したアタックタイムを入力。
        pyautogui.press('enter')  # エンターキーを押して確定。

        print(f'release time: {note-attack_time}(ms)')
        pyautogui.click(c2_close_x-214, c2_close_y+330, 2, 0.2,
                        'left')  # リリースタイムの座標をクリック。
        # アタックタイムを差し引いたリリースタイムを入力。
        pyautogui.typewrite(f'{note-attack_time}')
        pyautogui.press('enter')  # エンターキーを押して確定。

        # print(f'gain: {tracks[count_num][6]}db')
        # pyautogui.click(c2_close_x-134, c2_close_y+330, 2, 0.2, 'left')        #ゲインの座標をクリック。
        # pyautogui.typewrite(f'{tracks[count_num][6]}')    #指定したゲインを入力。
        # pyautogui.press('enter')                          #エンターキーを押して確定。

        pyautogui.click(c2_close_x, c2_close_y, 1,
                        0, 'left')  # 入力したPro-C2を閉じる。

        position_y += 22  # 一つ下のトラックを選択するために座標を上書き
        count_num += 1  # カウント用の変数に＋1する。
        track_num -= 1  # カウント用の変数に＋1する。
        # pyautogui.click(1904, 41, 1, 0, 'left')  # 入力したPro-C2を閉じる。

    print(f'BPM={bpm}\n気温は{temperature}℃\n音速は{speed_of_sound}m/sとして処理を行いました。')
    pyautogui.moveTo(home_x, home_y)


def routing():
    time.sleep(2)
    position_x, position_y = pyautogui.position()
    loopCount = int(loopNum.get())
    rName = routingName.get()
    for i in range(loopCount):
        pyautogui.click(position_x, position_y, 1, 0, 'left')
        time.sleep(0.5)
        pyautogui.typewrite(f'{rName}')
        time.sleep(0.5)
        pyautogui.press('enter')  # エンターキーを押して確定。
        position_x += 95

    home_x, home_y = pyautogui.position()
    pyautogui.moveTo(home_x, home_y)


def loopClick():
    time.sleep(2)
    position_x, position_y = pyautogui.position()
    loopCount = int(loopNum.get())
    for i in range(loopCount):
        pyautogui.click(position_x, position_y, 1, 0, 'left')
        position_x += 95

    home_x, home_y = pyautogui.position()
    pyautogui.moveTo(home_x, home_y)


# -------------------------------------------------------------------------------
# ウィンドウの作成
root = tkinter.Tk()
root.title('Cubase便利アイテム')
root.geometry('600x400')
root.geometry('+2200+50')

# テキストボックス
lbl1 = tkinter.Label(text='BPM')
lbl1.place(x=10, y=0)
input_bpm = tkinter.Entry(width=10)
input_bpm.place(x=40, y=0)
input_bpm.insert(tkinter.END, 128)

lbl2 = tkinter.Label(text='気温(℃)')
lbl2.place(x=120, y=0)
input_temperature = tkinter.Entry(width=6)
input_temperature.place(x=170, y=0)
input_temperature.insert(tkinter.END, 15)

lbl3 = tkinter.Label(text='繰り返し')
lbl3.place(x=310, y=280)
loopNum = tkinter.Entry(width=6)
loopNum.place(x=360, y=280)
loopNum.insert(tkinter.END, 5)

all = tkinter.Button(
    root, text=f'一気に入力する', command=all_comp)
all.place(x=340, y=0)

lbl3 = tkinter.Label(
    text=f'下準備：Cubaseを上書き保存してください。\n下準備：トラックの幅を最小から「Shift+H」1回分広げてください。\n下準備：入力を半角にしてください。\n下準備：InspectorのInsertsの一番上にPro-C2をセットしてください。')
lbl3.place(x=0, y=300)


def place(i, addx, addy, y):
    addy += 1
    if i % 7 == 6:
        addx += 120
        y = 50
        addy = 0
    return addx, addy, y


addx = 0
addy = 0
y = 0
x = 0

for i in range(33):
    addx, addy, y = place(i, addx, addy, y)
    button0 = tkinter.Button(
        root, text=f'{tracks[i][0]}.{tracks[i][1]}', command=lambda: ProC2(len(tracks)-1 - 0))
    button0.place(x=10+addx, y=50+30*addy)


routingButton = tkinter.Button(
    root, text=f'ルーティング', command=routing)
routingButton.place(x=340, y=300)

routingButton = tkinter.Button(
    root, text=f'連続クリック', command=loopClick)
routingButton.place(x=420, y=300)

lbl4 = tkinter.Label(text='文言')
lbl4.place(x=480, y=280)
routingName = tkinter.Entry(width=6)
routingName.place(x=520, y=300)
routingName.insert(tkinter.END, 'ste')

# ウィンドウのループ処理
root.mainloop()

# 分と小節数を消す
