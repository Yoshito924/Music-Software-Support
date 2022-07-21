import tkinter

import pyautogui
import pyperclip
import time

# パーカッションの変更を行うスクリプト
# 「パーカッションの変更」画面を出した上でスクリプトを実行する

# 各パーカッションの変更のために移動するパターンの値
move = [
    [1, 1, 0, 1, 0],  # 0 スネア
    [2, 1, 0, 1, 0],  # 1 バスドラム

    [3, 1, 3, 1, 0],  # 2 クローズハット
    [3, 1, 3, 1, 1],  # 3 オープンハット

    [3, 1, 3, 1, 2],  # 4 ハイハットペダル

    [3, 1, 2, 1, 0],  # 5 ライド

    [3, 1, 0, 1, 0],  # 6 クラッシュ1
    [3, 1, 0, 1, 1],  # 7 クラッシュ2

    [3, 1, 4, 1, 0],  # 8 スプラッシュ
    [3, 1, 6, 1, 0],  # 9 チャイナ

    [4, 1, 0, 1, 0],  # 10 ハイタム
    [4, 1, 1, 1, 0],  # 11 ハイミッドタム
    [4, 1, 2, 1, 0],  # 12 ローミッドタム
    [4, 1, 3, 1, 0],  # 13 ロータム
    [4, 1, 9, 0, 0],  # 14 フロアタム1
    [4, 1, 10, 0, 0],  # 15 フロアタム2

    [1, 1, 0, 1, 21],  # 16 クローズドリムショット
    [3, 1, 2, 1, 4],   # 17 ライドベル
    [1, 1, 0, 1, 3],  # 18 スネアゴーストノート
]


# 処理する順番を格納した配列
# order_array = [1, 1, 4]  # 足の処理順（キック2種類とハイハットペダル）

order_array = [
    1,
    1,

    0,
    # ------------------------
    0,
    3,
    14,

    # ------------------------

    12,

    2,
    # ------------------------
    10,

    6,
    5,
    # ------------------------
    17,

    8,
    9,
    # ------------------------

    7,
]  # 手の処理順

# 「選択した楽器タイプを編集」の座標
x = 1059
y = 609

# 各種関数--------------------------


def FinaleSelect():
    # Finaleを選択
    pyautogui.hotkey("win", "4")
    # Finaleを全画面表示
    pyautogui.hotkey("win", "up")


# ペースト対象項目をウインドウを開く
def paste():
    # Finaleを選択する関数
    FinaleSelect()
    # ペースト対象項目をウインドウを開く
    pyautogui.hotkey("ctrl", "shift", "alt", "f")


# ペースト対象項目をウインドウを開く
def FinaleScript():
    # Finaleを選択する関数
    FinaleSelect()
    # ペースト対象項目をウインドウを開く
    pyautogui.hotkey("ctrl", "shift", "a", )


# パーカッションの変更を行う関数
def inst_replace(inst):
    # Finaleを選択する関数
    FinaleSelect()
    # [選択した楽器タイプを編集]のボタンを押す
    pyautogui.click(x, y, 1, 0, 'left')

    # 大カテゴリのタテ移動
    for i in range(move[inst][0]):
        pyautogui.press('down')

    # 中カテゴリへヨコ移動
    for i in range(move[inst][1]):
        pyautogui.press('right')

    # 中カテゴリのタテ移動
    for i in range(move[inst][2]):
        pyautogui.press('down')

    # 小カテゴリへヨコ移動
    for i in range(move[inst][3]):
        pyautogui.press('right')

    # 小カテゴリのタテ移動
    for i in range(move[inst][4]):
        pyautogui.press('down')

    pyautogui.press('enter')
    pyautogui.moveTo(x, y)
    root.mainloop()


def inst_replace_all():
    home_x, home_y = pyautogui.position()
    # Finaleを選択する関数
    FinaleSelect()
    pyautogui.hotkey('alt', 's')
    time.sleep(0.6)

    # 変更したいパーカッションの初期座標
    inst_type_x = 1000
    inst_type_y = 390
    # 変更したいパーカッションを選択
    pyautogui.click(inst_type_x, inst_type_y, 1, 0, 'left')

    for j in range(len(order_array)):
        pyautogui.press('up')

    # --------------------------
    # for文で順番に処理をしていく
    loop = 0

    for i in range(len(order_array)):

        # 変更したいパーカッションを選択
        pyautogui.click(inst_type_x, inst_type_y, 1, 0, 'left')
        inst = order_array[i]

        if i >= 10:
            loop = loop+1
            for j in range(loop):
                pyautogui.press('up')

        for k in range(i):
            pyautogui.press('down')

        # [選択した楽器タイプを編集]のボタンを押す
        pyautogui.click(x, y, 1, 0, 'left')

        # 大カテゴリのタテ移動
        for i in range(move[inst][0]):
            pyautogui.press('down')

        # 中カテゴリへヨコ移動
        for i in range(move[inst][1]):
            pyautogui.press('right')

        # 中カテゴリのタテ移動
        for i in range(move[inst][2]):
            pyautogui.press('down')

        # 小カテゴリへヨコ移動
        for i in range(move[inst][3]):
            pyautogui.press('right')

        # 小カテゴリのタテ移動
        for i in range(move[inst][4]):
            pyautogui.press('down')

        pyautogui.press('enter')

    if len(order_array) <= 3:
        # OKを押す
        pyautogui.press('enter')

        # 符頭の向きを揃える
        time.sleep(0.3)
        pyautogui.hotkey('ctrl', 'down')

        # プラグインを選択
        pyautogui.click(509, 35, 1, 0, 'left')
        time.sleep(0.2)

        # 音符関連を選択
        pyautogui.moveTo(530, 230)
        time.sleep(0.5)

        # パターソンプラグインへ移動
        pyautogui.moveTo(680, 230)
        time.sleep(0.5)

        # 休符の移動
        pyautogui.click(682, 357, 1, 0, 'left')
        # 6ステップを手動で入力
    else:
        # OKを押す
        pyautogui.press('enter')

        # 符頭の向きを揃える
        time.sleep(0.3)
        pyautogui.hotkey('ctrl', 'up')

    print("処理が終了しました。")
    pyautogui.moveTo(home_x, home_y)
    root.mainloop()


# ドラムMIDIの上半身部分の下ごしらえをする関数
def hand_MIDI():
    FinaleSelect()
    # レイヤー1から2へ移動
    pyautogui.hotkey('ctrl', 'alt', 'g')
    time.sleep(3)

    # 楽譜を選択
    pyautogui.click(84, 148, 2, 0.2, 'left')
    time.sleep(0.2)
    # 楽譜を全選択
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.2)

    # 和音に集約する
    # ユーティリティ
    pyautogui.click(181, 31, 1, 0, 'left')

    # 和音に集約
    pyautogui.press('i')
    time.sleep(0.2)
    # 組段の一番下に新たな五線を作成
    pyautogui.press('n')
    time.sleep(0.2)
    pyautogui.press('enter')
    time.sleep(1.5)
    pyautogui.press('delete')
    root.mainloop()


# 休符の移動を行う関数
def rest():
    home_x, home_y = pyautogui.position()
    # Finaleを選択する関数
    FinaleSelect()
    # プラグインを選択
    pyautogui.click(509, 35, 1, 0, 'left')
    time.sleep(0.2)

    # 音符関連を選択
    pyautogui.moveTo(530, 230)
    time.sleep(0.5)

    # パターソンプラグインへ移動
    pyautogui.moveTo(680, 230)
    time.sleep(0.5)

    # 休符の移動
    pyautogui.click(682, 357, 1, 0, 'left')
    pyautogui.moveTo(home_x, home_y)
    root.mainloop()


def futouMuki(muki):
    home_x, home_y = pyautogui.position()
    # Finaleを選択する関数
    FinaleSelect()
    # ユーティリティ
    pyautogui.click(181, 31, 1, 0, 'left')

    pyautogui.press('s')
    # 符頭の向き
    pyautogui.press(muki)
    pyautogui.moveTo(home_x, home_y)
    root.mainloop()


# 歌詞を入力するための関数
def kashi():
    # Finaleを選択する関数
    FinaleSelect()

    # 歌詞を格納する変数
    lyric = txt.get()

    # 歌詞を配列に分割する
    lyricArray = list(lyric)
    # 配列の要素数を取得
    count = len(lyricArray)

    print(f'{count}文字が配列に含まれています。')

    num = 0
    for i in range(count):
        # YouTubeURL
        pyperclip.copy(f'{lyricArray[num]}')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.1)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        num += 1

    print(f'入力が終了しました。')
    root.mainloop()

# テキストボックスを空にする関数


def kashi_delete():
    txt.delete(0, tkinter.END)


def title_delete():
    title_txt.delete(0, tkinter.END)


# 楽譜を自動で書き出すスクリプト

# ヴォーカルあり曲-----------------------------------------
# パート譜の名前を配列に格納する。
score_type = ['Full',  # 0
              'Keyboard',  # 1
              'Guitar',  # 2
              'Bass',  # 3
              'Drums',  # 4
              'Vocals',  # 5
              'Lead guitar',  # 6
              'Baking guitar']  # 7
# #並び順は「パート譜の管理」から合わせる。

# # インスト曲-----------------------------------------
# # パート譜の名前を配列に格納する。
# score_type = ['Full',  # 0
#               'Keyboard',  # 1
#               'Guitar',  # 2
#               'Bass',  # 3
#               'Drums',  # 4
#               'Lead guitar',  # 6
#               'Baking guitar']  # 7

# 【並び順は「パート譜の管理」から合わせる。】-----------------------


def all_score_export():
    # Finaleを選択する関数
    FinaleSelect()
    # 楽譜を切り替えるのに使う変数
    type_num = 0
    # 歌詞を格納する変数
    score_name = title_txt.get()
    # タイトルが空なら処理を終了する
    if score_name == '':
        return
    score_num = score_nun_text.get()
    # どの楽譜が表示されていても正しく処理を行うために、表示を「スコア譜」に切り替える。
    pyautogui.moveTo(x=720, y=10)  # Finaleの画面を選択する
    pyautogui.click(300, 30, 1, 0, 'left')  # タブから「書類」を選択
    time.sleep(0.5)
    pyautogui.press("s")  # pdfを選択
    time.sleep(1.2)

    # for文で処理を繰り返して実行
    for i in range(int(score_num)):
        print(
            f'{type_num+1}つ目の楽譜「{score_name}_{score_type[type_num]} score」を処理中…')
        pyautogui.click(60, 30, 1, 0, 'left')  # タブから「ファイル」を選択
        time.sleep(0.3)
        pyautogui.press("t")  # エクスポートを選択
        time.sleep(0.3)
        pyautogui.press("p")  # pdfを選択
        if type_num == 0:
            time.sleep(3.5)
        else:
            time.sleep(1.5)
        # ファイル名をクリップボードにコピー
        pyperclip.copy(f'{str(score_name)}_{score_type[type_num]} score')
        time.sleep(0.3)
        pyautogui.hotkey('ctrl', 'v')  # ファイル名をショートカットキーを使ってペースト
        time.sleep(0.3)
        pyautogui.press('enter')  # ファイル名を決定のためエンターキーをプレス
        time.sleep(0.3)
        pyautogui.moveTo(x=720, y=10)  # Finaleの画面を選択する
        time.sleep(0.3)
        pyautogui.hotkey('ctrl', 'alt', '.')  # 次の譜面に切り替え
        time.sleep(0.3)
        type_num += 1  # スコア名配列の切り替え用の数字

    # Finaleを選択する関数
    FinaleSelect()
    # 表示を「スコア譜」に戻す。
    pyautogui.hotkey('ctrl', 'alt', '/')
    pyautogui.hotkey('ctrl', 'alt', '/')
    print(f'{score_name}の楽譜pdf書き出しが完了しました。')
    root.mainloop()


def score_export():
    # Finaleを選択する関数
    FinaleSelect()
    # 歌詞を格納する変数
    score_name = title_txt.get()
    pyautogui.click(60, 30, 1, 0, 'left')  # タブから「ファイル」を選択
    time.sleep(0.3)
    pyautogui.press("t")  # エクスポートを選択
    time.sleep(0.3)
    pyautogui.press("p")  # pdfを選択
    # タイトルが空なら処理を終了する
    if score_name == '':
        return
    time.sleep(3.5)
    # ファイル名をクリップボードにコピー
    pyperclip.copy(f'{str(score_name)}_score')
    time.sleep(0.3)
    pyautogui.hotkey('ctrl', 'v')  # ファイル名をショートカットキーを使ってペースト
    time.sleep(0.3)
    pyautogui.press('enter')  # ファイル名を決定のためエンターキーをプレス
    time.sleep(0.3)
    pyautogui.moveTo(x=720, y=10)  # Finaleの画面を選択する
    time.sleep(0.3)
    root.mainloop()


def score_export_support():
    # Finaleを選択する関数
    FinaleSelect()
    # 歌詞を格納する変数
    score_name = title_txt.get()
    pyautogui.click(60, 30, 1, 0, 'left')  # タブから「ファイル」を選択
    time.sleep(0.3)
    pyautogui.press("t")  # エクスポートを選択
    time.sleep(0.3)
    pyautogui.press("p")  # pdfを選択


# 指定した座標に、指定した数値を入力する関数


def suchiTyping(x_position, y_position, copy_num):
    pyperclip.copy(f'{copy_num}')
    time.sleep(0.1)
    pyautogui.click(x_position, y_position, 1, 0, 'left')
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.1)
    pyautogui.hotkey('ctrl', 'v')


# 1ページになるべく多くの組段を詰め込む…m
# 各ページの現在の組段の数を保持する…d
bunpai = 'm'

# 組段単体のマージン管理


def kumidanMargin():
    time.sleep(0.1)
    # ページレイアウトツールを選択
    pyautogui.click(666, 62, 1, 0, 'left')
    time.sleep(0.1)
    # タブからページレイアウトを選択
    pyautogui.click(597, 32, 1, 0, 'left')

    # 組段マージン
    pyautogui.press('s')
    # マージン編集
    pyautogui.press('e')

    top = top_value.get()
    bottom = bottom_value.get()

    time.sleep(0.3)
    # 上
    suchiTyping(198, 203, 1.2)
    # 左
    suchiTyping(171, 225, 0.8)
    # 右
    suchiTyping(227, 224, 0)
    # 下
    suchiTyping(204, 248, bottom)

    # 対象範囲最初の組段
    suchiTyping(258, 324, 1)

    # 対象範囲最後の組段
    suchiTyping(257, 348, 1)

    # 適用
    time.sleep(0.1)
    pyautogui.click(154, 435, 1, 0, 'left')

    # 閉じる
    time.sleep(0.1)
    pyautogui.click(169, 460, 1, 0, 'left')

    # 2以降-------------------------------------------
    # ページレイアウトツールを選択
    pyautogui.click(666, 62, 1, 0, 'left')
    time.sleep(0.1)
    # タブからページレイアウトを選択
    pyautogui.click(597, 32, 1, 0, 'left')

    # 組段マージン
    pyautogui.press('s')
    # 組段マージン編集
    pyautogui.press('e')

    time.sleep(0.3)
    # 上
    suchiTyping(198, 203, top)
    # 左
    suchiTyping(171, 225, 0.42)
    # 右
    suchiTyping(227, 224, 0)
    # 下
    suchiTyping(204, 248, bottom)

    # 対象範囲最初の組段
    suchiTyping(258, 324, 2)

    # 対象範囲最後の組段
    suchiTyping(257, 348, '')

    # 適用
    time.sleep(0.1)
    pyautogui.click(154, 435, 1, 0, 'left')

    # 閉じる
    time.sleep(0.1)
    pyautogui.click(169, 460, 1, 0, 'left')

# ページ全体のマージン管理


def pageMargin():
    # ページレイアウトツールを選択
    pyautogui.click(666, 62, 1, 0, 'left')
    time.sleep(0.1)
    # タブからページレイアウトを選択
    pyautogui.click(597, 32, 1, 0, 'left')

    # ページマージン
    pyautogui.press('g')
    # ページマージン編集
    pyautogui.press('e')

    time.sleep(0.3)
    # 上
    suchiTyping(217, 188, 0.21)
    # 左
    suchiTyping(190, 214, 0.22)
    # 右
    suchiTyping(240, 214, 0.15)
    # 下
    suchiTyping(214, 237, 0.65)

    # 1ページ目のみ
    pyautogui.click(97, 287, 1, 0, 'left')
    time.sleep(0.1)

    # 適用
    time.sleep(0.1)
    pyautogui.click(149, 438, 1, 0, 'left')

    # 閉じる
    time.sleep(0.1)
    pyautogui.click(178, 475, 1, 0, 'left')


def pageMarginTwo():
    # 2ページ目以降-------------------------------------------
    # ページレイアウトツールを選択
    pyautogui.click(666, 62, 1, 0, 'left')
    time.sleep(0.1)
    # タブからページレイアウトを選択
    pyautogui.click(597, 32, 1, 0, 'left')

    # ページマージン
    pyautogui.press('g')
    # ページマージン編集
    pyautogui.press('e')

    time.sleep(0.3)
    # 上
    suchiTyping(217, 188, 0.21)
    # 左
    suchiTyping(190, 214, 0.22)
    # 右
    suchiTyping(240, 214, 0.15)
    # 下
    suchiTyping(214, 237, 0.2)

    # 適応するページの範囲
    pyautogui.click(97, 356, 1, 0, 'left')
    time.sleep(0.1)

    # から
    suchiTyping(164, 377, 2)
    # まで
    suchiTyping(263, 379, '')

    # 適用
    time.sleep(0.1)
    pyautogui.click(149, 438, 1, 0, 'left')
    # 閉じる
    time.sleep(0.1)
    pyautogui.click(178, 475, 1, 0, 'left')


def layout(bunpai):
    time.sleep(0.1)
    pyautogui.click(77, 878, 1, 0, 'left')
    time.sleep(0.1)
    pyautogui.vscroll(2000)
    # ページレイアウトツールを選択
    pyautogui.click(666, 62, 1, 0, 'left')
    time.sleep(0.1)
    # タブからページレイアウトを選択
    pyautogui.click(597, 32, 1, 0, 'left')
    time.sleep(0.1)
    # 組段の均等配置
    pyautogui.press('e')

    time.sleep(0.3)
    # 全てのページ
    pyautogui.press('g')
    # 1ページになるべく多くの組段を詰め込む
    pyautogui.press(bunpai)
    # 決定
    pyautogui.press('enter')


def Shiage():
    time.sleep(0.1)
    # 選択ツールへ切り替える
    pyautogui.press('esc')
    time.sleep(0.1)

    # 楽譜を全選択
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(0.1)

    # 楽譜を整える
    pyautogui.hotkey('ctrl', '4')

    # 選択を解除
    time.sleep(0.3)
    pyautogui.click(461, 154, 1, 0, 'left')

    time.sleep(0.3)

    # レイアウト更新
    pyautogui.click(508, 124, 1, 0, 'left')
    time.sleep(0.3)


def page_margin():
    # Finaleを選択する関数
    FinaleSelect()

    pageMargin()
    pageMarginTwo()
    kumidanMargin()
    layout(bunpai)
    Shiage()

    time.sleep(0.3)
    pageMarginTwo()
    Shiage()


def scriptpallet():
    # Finaleを選択する関数
    FinaleSelect()
    # 書類→スコア譜
    pyautogui.click(303, 32, 1, 0, 'left')
    pyautogui.press('s')
    time.sleep(0.2)
    # Finalescriptパレットを起動
    pyautogui.hotkey('ctrl', 'alt', 'shift', 'o')


# -------------------------------------------------------------------------------
# ウィンドウの作成
root = tkinter.Tk()
root.title('Finale便利アイテム')
# root.iconbitmap('icon.ico')
root.geometry('700x600')
root.geometry('+2000+50')

# ボタンの作成
button_0 = tkinter.Button(root, text='スネアドラム', command=lambda: inst_replace(0))
button_0.place(x=80, y=0)
button_1 = tkinter.Button(root, text='バスドラム', command=lambda: inst_replace(1))
button_1.place(x=5, y=0)
button_2 = tkinter.Button(root, text='クローズハット',
                          command=lambda: inst_replace(2))
button_2.place(x=5, y=30)
button_3 = tkinter.Button(root, text='オープンハット',
                          command=lambda: inst_replace(3))
button_3.place(x=80, y=30)
button_4 = tkinter.Button(root, text='ハイハットペダル',
                          command=lambda: inst_replace(4))
button_4.place(x=160, y=30)
button_5 = tkinter.Button(root, text='ライドシンバル',
                          command=lambda: inst_replace(5))
button_5.place(x=5, y=60)
button_6 = tkinter.Button(root, text='クラッシュ1', command=lambda: inst_replace(6))
button_6.place(x=80, y=60)
button_7 = tkinter.Button(root, text='クラッシュ2', command=lambda: inst_replace(7))
button_7.place(x=160, y=60)
button_8 = tkinter.Button(root, text='スプラッシュ', command=lambda: inst_replace(8))
button_8.place(x=5, y=90)
button_9 = tkinter.Button(root, text='チャイナ', command=lambda: inst_replace(9))
button_9.place(x=80, y=90)
button_10 = tkinter.Button(
    root, text='ハイタム', command=lambda: inst_replace(10))
button_10.place(x=5, y=120)
button_11 = tkinter.Button(
    root, text='ハイミッドタム', command=lambda: inst_replace(11))
button_11.place(x=80, y=120)
button_12 = tkinter.Button(
    root, text='ローミッドタム', command=lambda: inst_replace(12))
button_12.place(x=160, y=120)
button_13 = tkinter.Button(
    root, text='ロータム', command=lambda: inst_replace(13))
button_13.place(x=5, y=150)
button_14 = tkinter.Button(
    root, text='フロアタム1', command=lambda: inst_replace(14))
button_14.place(x=80, y=150)
button_15 = tkinter.Button(
    root, text='フロアタム2', command=lambda: inst_replace(15))
button_15.place(x=160, y=150)
button_16 = tkinter.Button(
    root, text='クローズド・リムショット', command=lambda: inst_replace(16))
button_16.place(x=160, y=0)
button_17 = tkinter.Button(
    root, text='ライドベル', command=lambda: inst_replace(17))
button_17.place(x=160, y=90)
button_18 = tkinter.Button(
    root, text='スネア（ゴースト・ノート）', command=lambda: inst_replace(18))
button_18.place(x=280, y=0)

# --------------------
button_inst_replace_all = tkinter.Button(
    root, text='全てのパーカッションの入れ替え', command=inst_replace_all)
button_inst_replace_all.place(x=420, y=60)

# --------------------
button_ue = tkinter.Button(
    root, text='符頭を上向きに', command=lambda: futouMuki('u'))
button_ue.place(x=5, y=200)
button_shita = tkinter.Button(
    root, text='符頭を下向きに', command=lambda: futouMuki('d'))
button_shita.place(x=100, y=200)
button_default = tkinter.Button(
    root, text='符頭をデフォルトの向きに', command=lambda: futouMuki('s'))
button_default.place(x=200, y=200)

button_rest = tkinter.Button(
    root, text='休符を移動する', command=rest)
button_rest.place(x=5, y=230)

# テキストボックス
lbl = tkinter.Label(text='歌詞')
lbl.place(x=5, y=280)
txt = tkinter.Entry(width=80)
txt.place(x=60, y=280)

button_kashi = tkinter.Button(
    root, text='歌詞を入力する', command=kashi)
button_kashi.place(x=5, y=310)

button_kashi_delete = tkinter.Button(
    root, text='歌詞を削除する', command=kashi_delete)
button_kashi_delete.place(x=120, y=310)
# --------------------
button_hand_MIDI = tkinter.Button(
    root, text='ドラムMIDIの下ごしらえ（手）', command=hand_MIDI)
button_hand_MIDI.place(x=420, y=30)

# --------------------
# 書き出す楽譜の枚数指定
lbl1 = tkinter.Label(text='書き出す数')
lbl1.place(x=5, y=350)
score_nun_text = tkinter.Entry(width=10)
score_nun_text.place(x=80, y=350)
score_nun_text.insert(tkinter.END, 5)

lbl1_5 = tkinter.Label(text='※「上書きしますか？」が出ないように出力先フォルダを整理しておく')
lbl1_5.place(x=160, y=350)

# 曲のタイトルを指定
lbl2 = tkinter.Label(text='タイトル')
lbl2.place(x=5, y=380)
title_txt = tkinter.Entry(width=80)
title_txt.place(x=50, y=380)

button_all_score_export_support = tkinter.Button(
    root, text='pdfへ', command=score_export_support)
button_all_score_export_support.place(x=5, y=410)

button_score_export = tkinter.Button(
    root, text='楽譜を書き出す', command=score_export)
button_score_export.place(x=60, y=410)

button_all_score_export = tkinter.Button(
    root, text='楽譜を一括で書き出す', command=all_score_export)
button_all_score_export.place(x=160, y=410)

button_title_delete = tkinter.Button(
    root, text='タイトルを削除する', command=title_delete)
button_title_delete.place(x=300, y=410)
# --------------------
# Bottomの値
lbl_top = tkinter.Label(text='トップのマージンを設定する：')
lbl_top.place(x=5, y=450)

lbl_bottom = tkinter.Label(
    text='ボトムのマージンを設定する：　　　　　※8弦(0.64) , ドラム(0.38) , ベース(0.42)')
lbl_bottom.place(x=5, y=480)

top_value = tkinter.Entry(width=8)
top_value.place(x=140, y=450)
top_value.insert(tkinter.END, 0.6)

bottom_value = tkinter.Entry(width=8)
bottom_value.place(x=140, y=480)
bottom_value.insert(tkinter.END, 0.38)

button_page_margin = tkinter.Button(
    root, text='ページマージンを調整する', command=page_margin)
button_page_margin.place(x=140, y=510)

button_page_margin = tkinter.Button(
    root, text='ペースト対象項目ウインドウ', command=paste)
button_page_margin.place(x=10, y=550)

button_page_margin = tkinter.Button(
    root, text='FinaleScriptパレット', command=FinaleScript)
button_page_margin.place(x=180, y=550)


# ウィンドウのループ処理
root.mainloop()


# 分と小節数を消す
