import tkinter

import pyautogui
import pyperclip
import time

# ----------------------
# 平均律の周波数
Freq = [
    0,
    0,
    0,
    0,
    0,
    0,  # 5
    0,
    0,
    0,
    13.75,  # 9(MIDIﾉｰﾄﾅﾝﾊﾞｰ)
    14.5676175474403,
    15.4338531642538,
    16.3515978312874,
    17.3239144360545,
    18.3540479948379,
    19.44543648263,
    20.6017223070543,
    21.8267644645627,
    23.1246514194771,
    24.4997147488593,
    25.9565435987465,
    27.4999999999999,
    29.1352350948806,
    30.8677063285077,
    32.7031956625748,
    34.6478288721089,
    36.7080959896759,
    38.89087296526,
    41.2034446141087,
    43.6535289291254,
    46.2493028389542,
    48.9994294977186,
    51.9130871974931,
    54.9999999999999,
    58.2704701897611,
    61.7354126570154,
    65.4063913251495,
    69.2956577442179,
    73.4161919793518,
    77.7817459305201,
    82.4068892282174,
    87.3070578582508,
    92.4986056779085,
    97.9988589954372,
    103.826174394986,
    110,
    116.540940379522,
    123.470825314031,
    130.812782650299,
    138.591315488436,
    146.832383958704,
    155.56349186104,
    164.813778456435,
    174.614115716502,
    184.997211355817,
    195.997717990875,
    207.652348789972,
    220,
    233.081880759045,
    246.941650628062,
    261.625565300599,
    277.182630976872,
    293.664767917407,
    311.126983722081,
    329.62755691287,
    349.228231433004,
    369.994422711634,
    391.995435981749,
    415.304697579945,
    440,
    466.16376151809,
    493.883301256124,
    523.251130601197,
    554.365261953744,
    587.329535834815,
    622.253967444162,
    659.25511382574,
    698.456462866008,
    739.988845423269,
    783.990871963499,
    830.609395159891,
    880,
    932.32752303618,
    987.766602512249,
    1046.5022612024,
    1108.73052390749,
    1174.65907166963,
    1244.50793488832,
    1318.51022765148,
    1396.91292573202,
    1479.97769084654,
    1567.981743927,
    1661.21879031978,
    1760,
    1864.65504607236,
    1975.5332050245,
    2093.00452240479,
    2217.46104781498,
    2349.31814333926,
    2489.01586977665,
    2637.02045530296,
    2793.82585146403,
    2959.95538169308,
    3135.963487854,
    3322.43758063956,
    3520,
    3729.31009214472,
    3951.066410049,
    4186.00904480958,
    4434.92209562996,
    4698.63628667853,
    4978.0317395533,
    5274.04091060593,
    5587.65170292807,
    5919.91076338616,
    6271.926975708,
    6644.87516127913,
    7040.00000000001,
    7458.62018428945,
    7902.132820098,
    8372.01808961917,
    8869.84419125993,
    9397.27257335706,
    9956.06347910661,
    10548.0818212119,
    11175.3034058561,
    11839.8215267723,
    12543.853951416,
    13289.7503225583,
    14080,
    14917.2403685789,
    15804.265640196,
    16744.0361792384,
    17739.6883825199,
    18794.5451467141,
    19912.1269582132,
    21096.1636424237,
]

setting_array = [
    3,  # マイクの選択（67Cond）
    5,  # プリアンプ・タイプ（モダン）
    2,  # プロクシミティー
]

# ----------------------

# MIDIノートナンバーを周波数へ変換する関数


def MIDINoteNumberToFreq(MIDINoteNumber):
    frequency = 2 ** ((MIDINoteNumber - 69) / 12) * 440
    return frequency


# AXE-EDITを起動する。
def axe_edit_select():
    pyautogui.hotkey("win", "1")
    time.sleep(0.3)


def amp_axe_basic():
    axe_edit_select()  # AXE-EDITを起動する。
    # -----------------------------------------
    # Basicを選択
    pyautogui.click(306, 653, 1, 0, "left")

    # input drive
    pyautogui.click(435, 651, 1, 0, "left")
    pyautogui.typewrite("5")
    pyautogui.press("enter")

    # input trim
    pyautogui.click(439, 830, 1, 0, "left")
    pyautogui.typewrite("1")
    pyautogui.press("enter")

    # Bass
    pyautogui.click(642, 656, 1, 0, "left")
    pyautogui.typewrite("5")
    pyautogui.press("enter")

    # Mid
    pyautogui.click(754, 656, 1, 0, "left")
    pyautogui.typewrite("5")
    pyautogui.press("enter")

    # Treb
    pyautogui.click(843, 654, 1, 0, "left")
    pyautogui.typewrite("5")
    pyautogui.press("enter")

    # プレゼンス
    pyautogui.click(1073, 647, 1, 0, "left")
    pyautogui.typewrite("5")
    pyautogui.press("enter")

    # デプス
    # pyautogui.click(1169, 646, 1, 0, 'left')
    # pyautogui.typewrite('5')
    # pyautogui.press('enter')

    # サチュレーション・ドライブ
    pyautogui.click(1174, 821, 1, 0, "left")
    pyautogui.typewrite("5")
    pyautogui.press("enter")

    # マスターボリューム・トリム
    pyautogui.click(1255, 822, 1, 0, "left")
    pyautogui.typewrite("1")
    pyautogui.press("enter")

    # マスターボリューム
    pyautogui.click(1274, 648, 1, 0, "left")
    pyautogui.typewrite("5")
    pyautogui.press("enter")


def amp_axe_basic2():
    axe_edit_select()  # AXE-EDITを起動する。
    # -----------------------------------------
    # Basicを選択
    pyautogui.click(306, 653, 1, 0, "left")

    # input drive
    pyautogui.click(435, 651, 1, 0, "left")
    pyautogui.typewrite("8.1")
    pyautogui.press("enter")

    # input trim
    pyautogui.click(439, 830, 1, 0, "left")
    pyautogui.typewrite("1.8")
    pyautogui.press("enter")

    # Bass
    pyautogui.click(642, 656, 1, 0, "left")
    pyautogui.typewrite("1.1")
    pyautogui.press("enter")

    # Mid
    pyautogui.click(754, 656, 1, 0, "left")
    pyautogui.typewrite("1.8")
    pyautogui.press("enter")

    # Treb
    pyautogui.click(843, 654, 1, 0, "left")
    pyautogui.typewrite("8.9")
    pyautogui.press("enter")

    # プレゼンス
    pyautogui.click(1073, 647, 1, 0, "left")
    pyautogui.typewrite("4.5")
    pyautogui.press("enter")

    # デプス
    # pyautogui.click(1169, 646, 1, 0, 'left')
    # pyautogui.typewrite('5')
    # pyautogui.press('enter')

    # サチュレーション・ドライブ
    pyautogui.click(1174, 821, 1, 0, "left")
    pyautogui.typewrite("4")
    pyautogui.press("enter")

    # マスターボリューム・トリム
    pyautogui.click(1255, 822, 1, 0, "left")
    pyautogui.typewrite("1")
    pyautogui.press("enter")

    # マスターボリューム
    pyautogui.click(1274, 648, 1, 0, "left")
    pyautogui.typewrite("3")
    pyautogui.press("enter")


def amp_axe_GEQ():
    # GEQを選択
    pyautogui.click(297, 701, 1, 0, "left")

    # EQタイプを5Band(Mark)
    pyautogui.click(474, 714, 1, 0, "left")
    for i in range(4):
        pyautogui.press("down")
    pyautogui.press("enter")

    time.sleep(0.5)

    # 80Hz
    pyautogui.click(647, 654, 1, 0, "left")
    pyautogui.typewrite(f"4.8")
    pyautogui.press("enter")

    # 240Hz
    pyautogui.click(733, 656, 1, 0, "left")
    pyautogui.typewrite(f"2.6")
    pyautogui.press("enter")

    # 750Hz
    pyautogui.click(836, 657, 1, 0, "left")
    pyautogui.typewrite(f"-4.5")
    pyautogui.press("enter")

    # 2200Hz
    pyautogui.click(926, 656, 1, 0, "left")
    pyautogui.typewrite(f"-0.2")
    pyautogui.press("enter")

    # 6600Hz
    pyautogui.click(1020, 655, 1, 0, "left")
    pyautogui.typewrite(f"-0.2")
    pyautogui.press("enter")

    # EQを差し込む場所をプリアンプ前に
    pyautogui.click(487, 875, 1, 0, "left")
    for i in range(1):
        pyautogui.press("down")
    pyautogui.press("enter")


def amp_axe_GEQ8(ferq1, ferq2, ferq3, ferq4, ferq5, ferq6, ferq7, ferq8):
    # GEQを選択
    pyautogui.click(297, 701, 1, 0, "left")

    # EQタイプを5Band(Mark)
    pyautogui.click(474, 714, 1, 0, "left")
    for i in range(9):
        pyautogui.press("down")
    pyautogui.press("enter")

    time.sleep(0.5)

    # 63Hz
    pyautogui.click(647, 654, 1, 0, "left")
    pyautogui.typewrite(f"{ferq1}")
    pyautogui.press("enter")

    # 125Hz
    pyautogui.click(733, 656, 1, 0, "left")
    pyautogui.typewrite(f"{ferq2}")
    pyautogui.press("enter")

    # 250Hz
    pyautogui.click(836, 657, 1, 0, "left")
    pyautogui.typewrite(f"{ferq3}")
    pyautogui.press("enter")

    # 500Hz
    pyautogui.click(926, 656, 1, 0, "left")
    pyautogui.typewrite(f"{ferq4}")
    pyautogui.press("enter")

    # 1000Hz
    pyautogui.click(1020, 655, 1, 0, "left")
    pyautogui.typewrite(f"{ferq5}")
    pyautogui.press("enter")

    # 2000Hz
    pyautogui.click(1099, 655, 1, 0, "left")
    pyautogui.typewrite(f"{ferq6}")
    pyautogui.press("enter")

    # 4000Hz
    pyautogui.click(1209, 658, 1, 0, "left")
    pyautogui.typewrite(f"{ferq7}")
    pyautogui.press("enter")

    # 8000Hz
    pyautogui.click(1293, 658, 1, 0, "left")
    pyautogui.typewrite(f"{ferq8}")
    pyautogui.press("enter")

    # EQを差し込む場所をプリアンプ前に
    pyautogui.click(487, 875, 1, 0, "left")
    for i in range(1):
        pyautogui.press("down")
    pyautogui.press("enter")


def amp_axe2():

    proximity = int(input_proximity.get())
    # -----------------------------------------
    # Preampを選択
    pyautogui.click(300, 744, 1, 0, "left")

    # Triode1 Plate Freq
    pyautogui.click(846, 651, 1, 0, "left")
    pyautogui.typewrite(f"{Freq[95]}")
    pyautogui.press("enter")

    # Triode2 Plate Freq
    pyautogui.click(945, 653, 1, 0, "left")
    pyautogui.typewrite(f"{Freq[100]}")
    pyautogui.press("enter")

    # トーンフリーケンシー
    pyautogui.click(748, 819, 1, 0, "left")
    pyautogui.typewrite(f"{Freq[59]}")
    pyautogui.press("enter")

    # ローカットフリーケンシー
    pyautogui.click(860, 822, 1, 0, "left")
    pyautogui.typewrite(f"{Freq[16]}")
    pyautogui.press("enter")

    # ハイカットフリーケンシー
    pyautogui.click(945, 822, 1, 0, "left")
    pyautogui.typewrite(f"{Freq[119]}")
    pyautogui.press("enter")

    # ----------------------
    # Speakerを選択
    pyautogui.click(304, 880, 1, 0, "left")
    time.sleep(0.1)

    # ローレスフリーケンシー
    pyautogui.click(430, 655, 1, 0, "left")
    pyautogui.typewrite(f"{Freq[proximity]}")
    pyautogui.press("enter")

    # ローレスQ
    pyautogui.click(530, 655, 1, 0, "left")
    pyautogui.typewrite("2")
    pyautogui.press("enter")

    # ローレスポンス
    pyautogui.click(630, 655, 1, 0, "left")
    pyautogui.typewrite("5")
    pyautogui.press("enter")

    # ハイフリーケンシー
    pyautogui.click(760, 655, 1, 0, "left")
    pyautogui.typewrite(f"{Freq[88]}")
    pyautogui.press("enter")

    # ハイフリーケンシースロープ
    pyautogui.click(860, 655, 1, 0, "left")
    pyautogui.typewrite("4")
    pyautogui.press("enter")

    # ハイレスポンス
    pyautogui.click(950, 655, 1, 0, "left")
    pyautogui.typewrite("7")
    pyautogui.press("enter")

    # XFormer ローフリーケンシー（ローカット）
    pyautogui.click(430, 820, 1, 0, "left")
    pyautogui.typewrite("20")
    pyautogui.press("enter")

    # XFormer ハイフリーケンシー（ハイカット）
    pyautogui.click(530, 820, 1, 0, "left")
    pyautogui.typewrite("40000")
    pyautogui.press("enter")

    # ----------------------
    # ベーシックを選択
    pyautogui.click(301, 651, 1, 0, "left")


def amp_axe():
    home_x, home_y = pyautogui.position()
    amp_axe_basic()
    amp_axe_GEQ()
    amp_axe2()
    pyautogui.moveTo(home_x, home_y)
    # ウィンドウのループ処理
    root.mainloop()


def cab_axe():
    home_x, home_y = pyautogui.position()
    axe_edit_select()  # AXE-EDITを起動する。
    proximity = int(input_proximity.get())
    # エフェクトタイプをウルトラレスに
    pyautogui.click(100, 774, 1, 0, "left")
    for i in range(1):
        pyautogui.press("down")
    pyautogui.press("enter")

    # ----------------------
    # # ボリューム
    # pyautogui.click(1407, 651, 1, 0, 'left')
    # pyautogui.typewrite(f'-7')
    # pyautogui.press('enter')

    # ----------------------
    # キャビネットを選択
    pyautogui.click(298, 657, 1, 0, "left")

    # # マイクの選択
    # pyautogui.click(574, 886, 1, 0, 'left')
    # for i in range(setting_array[0]):
    #     pyautogui.press('down')
    # pyautogui.press('enter')

    # スピーカー・サイズ
    pyautogui.click(856, 651, 1, 0, "left")
    pyautogui.typewrite(f"1")
    pyautogui.press("enter")

    # ディフェーズ（デジタルっぽさを抑える）
    pyautogui.click(954, 651, 1, 0, "left")
    pyautogui.typewrite(f"2")
    pyautogui.press("enter")

    # ディレイ（マイクの距離をシミュレート）
    pyautogui.click(851, 826, 1, 0, "left")
    pyautogui.typewrite(f"0")
    pyautogui.press("enter")

    # プロクシミティー（近接効果）
    # pyautogui.click(958, 824, 1, 0, 'left')
    # pyautogui.typewrite(f'2')
    # pyautogui.press('enter')

    # プロクシミティー・フリーケンシー
    pyautogui.click(1061, 827, 1, 0, "left")
    pyautogui.typewrite(f"{Freq[proximity]}")
    pyautogui.press("enter")

    # ローカット
    pyautogui.click(1159, 652, 1, 0, "left")
    pyautogui.typewrite(f"{Freq[16]}")
    pyautogui.press("enter")

    # ハイカット
    pyautogui.click(1270, 650, 1, 0, "left")
    pyautogui.typewrite(f"20000")
    pyautogui.press("enter")

    # フィルター・スロープ
    pyautogui.click(1199, 886, 1, 0, "left")
    # 6dB/オクターブ
    pyautogui.press("down")
    pyautogui.press("enter")
    # 12dB/オクターブ
    # pyautogui.press('down')
    # pyautogui.press('down')
    # pyautogui.press('enter')

    # ----------------------
    # Pre＋Drvを選択
    pyautogui.click(298, 704, 1, 0, "left")

    # プリアンプ・タイプを選択する。
    pyautogui.click(474, 708, 1, 0, "left")
    for i in range(setting_array[1]):
        pyautogui.press("down")
    pyautogui.press("enter")

    # プリアンプ・モードをハイクオリティにする。
    pyautogui.click(473, 890, 1, 0, "left")
    pyautogui.press("down")
    pyautogui.press("down")
    pyautogui.press("enter")

    # モニタードライブ
    pyautogui.click(648, 822, 1, 0, "left")
    pyautogui.typewrite(f"0.25")
    pyautogui.press("enter")

    # モニタータイムコンスト
    pyautogui.click(744, 821, 1, 0, "left")
    pyautogui.typewrite(f"200")
    pyautogui.press("enter")

    # ----------------------
    # Roomを選択
    pyautogui.click(297, 737, 1, 0, "left")

    # ルームレベル
    pyautogui.click(428, 654, 1, 0, "left")
    pyautogui.typewrite(f"30")
    pyautogui.press("enter")

    # ルームサイズ
    pyautogui.click(535, 653, 1, 0, "left")
    pyautogui.typewrite(f"3")
    pyautogui.press("enter")

    # マイクスペーシング
    pyautogui.click(636, 651, 1, 0, "left")
    pyautogui.typewrite(f"15")
    pyautogui.press("enter")

    # エア
    pyautogui.click(846, 654, 1, 0, "left")
    pyautogui.typewrite(f"20")
    pyautogui.press("enter")

    # エアフリーケンシー
    pyautogui.click(962, 655, 1, 0, "left")
    pyautogui.typewrite(f"{Freq[119]}")
    pyautogui.press("enter")

    # ----------------------
    # キャビネットを選択
    pyautogui.click(298, 657, 1, 0, "left")

    pyautogui.moveTo(home_x, home_y)
    # ウィンドウのループ処理
    root.mainloop()


def stereo_cab_axe():
    home_x, home_y = pyautogui.position()
    axe_edit_select()  # AXE-EDITを起動する。
    proximity = int(input_proximity.get())
    # エフェクトタイプをステレオ・ウルトラレスに
    pyautogui.click(100, 774, 1, 0, "left")
    for i in range(4):
        pyautogui.press("down")
    pyautogui.press("enter")

    time.sleep(0.5)
    # ----------------------
    # キャビネットを選択
    pyautogui.click(300, 654, 1, 0, "left")

    time.sleep(0.3)
    # マイクL
    pyautogui.click(568, 770, 1, 0, "left")
    for i in range(setting_array[0]):
        pyautogui.press("down")
    pyautogui.press("enter")

    # マイクR
    pyautogui.click(582, 932, 1, 0, "left")
    for i in range(setting_array[0]):
        pyautogui.press("down")
    pyautogui.press("enter")

    # プロクシミティーL（近接効果）
    pyautogui.click(1164, 648, 1, 0, "left")
    pyautogui.typewrite(f"2")
    pyautogui.press("enter")

    # プロクシミティーR（近接効果）
    pyautogui.click(1166, 823, 1, 0, "left")
    pyautogui.typewrite(f"2")
    pyautogui.press("enter")

    # ----------------------
    # Pre＋Drvを選択
    pyautogui.click(298, 697, 1, 0, "left")

    # プリアンプ・タイプを選択する。
    pyautogui.click(474, 708, 1, 0, "left")
    for i in range(setting_array[1]):
        pyautogui.press("down")
    pyautogui.press("enter")

    # プリアンプ・モードをハイクオリティにする。
    pyautogui.click(473, 890, 1, 0, "left")
    pyautogui.press("down")
    pyautogui.press("down")
    pyautogui.press("enter")

    # モニタードライブ
    pyautogui.click(648, 822, 1, 0, "left")
    pyautogui.typewrite(f"0.25")
    pyautogui.press("enter")

    # モニタータイムコンスト
    pyautogui.click(744, 821, 1, 0, "left")
    pyautogui.typewrite(f"200")
    pyautogui.press("enter")

    # ----------------------
    # Roomを選択
    pyautogui.click(294, 741, 1, 0, "left")

    # ルームレベル
    pyautogui.click(428, 654, 1, 0, "left")
    pyautogui.typewrite(f"30")
    pyautogui.press("enter")

    # ルームサイズ
    pyautogui.click(535, 653, 1, 0, "left")
    pyautogui.typewrite(f"3")
    pyautogui.press("enter")

    # マイクスペーシング
    pyautogui.click(636, 651, 1, 0, "left")
    pyautogui.typewrite(f"15")
    pyautogui.press("enter")

    # エア
    pyautogui.click(846, 654, 1, 0, "left")
    pyautogui.typewrite(f"20")
    pyautogui.press("enter")

    # エアフリーケンシー
    pyautogui.click(962, 655, 1, 0, "left")
    pyautogui.typewrite(f"{Freq[119]}")
    pyautogui.press("enter")

    # ----------------------
    # Advancedを選択
    pyautogui.click(295, 784, 1, 0, "left")
    time.sleep(0.1)

    # ローカットする帯域
    pyautogui.click(425, 651, 1, 0, "left")
    pyautogui.typewrite(f"{Freq[16]}")
    pyautogui.press("enter")

    # ハイカットする帯域
    pyautogui.click(537, 653, 1, 0, "left")
    pyautogui.typewrite(f"20000")
    pyautogui.press("enter")

    # DEPHASE（位相が揃った状態から不揃いの状態になること）「より "アンプ・イン・ザ・ルーム "な体験をもたらします。」
    pyautogui.click(432, 827, 1, 0, "left")
    pyautogui.typewrite(f"2")
    pyautogui.press("enter")

    # proximity frequency（近接効果が発生する周波数帯域を調整）
    pyautogui.click(533, 826, 1, 0, "left")
    pyautogui.typewrite(f"{Freq[proximity]}")
    pyautogui.press("enter")

    # フィルタースロープを6db/Octへ
    pyautogui.click(757, 712, 1, 0, "left")
    pyautogui.moveTo(755, 742)
    pyautogui.click(755, 742, 1, 0, "left")

    # フィルタースロープを12db/Octへ
    # pyautogui.click(757, 712, 1, 0, 'left')
    # pyautogui.moveTo(755, 742)
    # pyautogui.click(752, 757, 1, 0, 'left')

    # # ローレスフリーケンシー
    # pyautogui.click(430, 655, 1, 0, 'left')
    # pyautogui.typewrite(f'{Freq[43]}')
    # pyautogui.press('enter')

    # # ローレスQ
    # pyautogui.click(530, 655, 1, 0, 'left')
    # pyautogui.typewrite('2')
    # pyautogui.press('enter')

    # # ローレスポンス
    # pyautogui.click(630, 655, 1, 0, 'left')
    # pyautogui.typewrite('5')
    # pyautogui.press('enter')

    # ----------------------
    # キャビネットを選択
    pyautogui.click(300, 654, 1, 0, "left")
    pyautogui.moveTo(home_x, home_y)
    # ウィンドウのループ処理
    root.mainloop()


def gate_axe():

    home_x, home_y = pyautogui.position()
    axe_edit_select()  # AXE-EDITを起動する。

    one_minutes = 60000  # 1分の秒数(ms)
    bpm = int(input_bpm.get())
    temperature = int(input_temperature.get())
    speed_of_sound = round((temperature * 0.6 + 331.5), 2)  # 指定された気温での音速を計算する

    # 指定BPMの主要な音符の音価(リリースタイムに使う)を計算する。
    note_1 = 4  # 全音符(ms)
    note_2 = 2  # 2分音符(ms)
    note_4 = 1  # 4分音符(ms)
    note_8 = 1 / 2  # 8分音符(ms)
    note_16 = 1 / 4  # 16分音符(ms)
    note_32 = 1 / 8  # 32分音符(ms)

    speed_of_sound = round((temperature * 0.6 + 331.5), 2)  # 指定された気温での音速を計算する

    # 指定BPMでの基本的な「1拍」の音価であり,4分音符の音価(ms)
    common_beat_time = int(one_minutes) / int(bpm)

    # ノートの長さを計算
    note = round((common_beat_time * note_16), 2)

    attack_time = round(
        (((8.25 - (0.25 * -2)) / speed_of_sound) * 1000), 2
    )  # アタックタイムの計算

    # BPM
    pyautogui.click(1197, 50, 1, 0, "left")
    pyautogui.typewrite(f"{bpm}")
    pyautogui.press("enter")

    # ゲートエキスパンダー
    # pyautogui.click(206, 336, 1, 0, 'left')
    time.sleep(0.5)

    # スレッショルド
    pyautogui.click(437, 654, 1, 0, "left")
    pyautogui.typewrite(f"-40")
    pyautogui.press("enter")

    # レシオ
    pyautogui.click(539, 654, 1, 0, "left")
    pyautogui.typewrite(f"2")
    pyautogui.press("enter")

    # アタックタイム
    pyautogui.click(650, 654, 1, 0, "left")
    pyautogui.typewrite(f"{attack_time}")
    pyautogui.press("enter")

    # ホールド
    pyautogui.click(747, 661, 1, 0, "left")
    pyautogui.typewrite(f"10")
    pyautogui.press("enter")

    # リリースタイム
    pyautogui.click(845, 657, 1, 0, "left")
    pyautogui.typewrite(f"{note-attack_time}")
    pyautogui.press("enter")

    # ローカット
    pyautogui.click(440, 827, 1, 0, "left")
    pyautogui.typewrite(f"20.6")
    pyautogui.press("enter")

    # ハイカット
    pyautogui.click(537, 824, 1, 0, "left")
    pyautogui.typewrite(f"20000")
    pyautogui.press("enter")

    pyautogui.moveTo(home_x, home_y)
    # ウィンドウのループ処理
    root.mainloop()


def comp_axe():
    home_x, home_y = pyautogui.position()
    axe_edit_select()  # AXE-EDITを起動する。

    one_minutes = 60000  # 1分の秒数(ms)
    bpm = int(input_bpm.get())
    temperature = int(input_temperature.get())
    speed_of_sound = round((temperature * 0.6 + 331.5), 2)  # 指定された気温での音速を計算する

    # 指定BPMの主要な音符の音価(リリースタイムに使う)を計算する。
    note_1 = 4  # 全音符(ms)
    note_2 = 2  # 2分音符(ms)
    note_4 = 1  # 4分音符(ms)
    note_8 = 1 / 2  # 8分音符(ms)
    note_16 = 1 / 4  # 16分音符(ms)
    note_32 = 1 / 8  # 32分音符(ms)

    speed_of_sound = round((temperature * 0.6 + 331.5), 2)  # 指定された気温での音速を計算する

    # 指定BPMでの基本的な「1拍」の音価であり,4分音符の音価(ms)
    common_beat_time = int(one_minutes) / int(bpm)

    # ノートの長さを計算
    note = round((common_beat_time * note_16), 2)

    attack_time = round(
        (((8.25 - (0.25 * -2)) / speed_of_sound) * 1000), 2
    )  # アタックタイムの計算

    # BPM
    pyautogui.click(1197, 50, 1, 0, "left")
    pyautogui.typewrite(f"{bpm}")
    pyautogui.press("enter")

    time.sleep(0.4)

    # スタジオコンプを選択
    pyautogui.click(102, 779, 1, 0, "left")
    for i in range(6):
        pyautogui.press("down")
    pyautogui.press("enter")

    time.sleep(0.4)

    # スレッショルド
    pyautogui.click(436, 652, 1, 0, "left")
    pyautogui.typewrite(f"-40")
    pyautogui.press("enter")

    # レシオ
    pyautogui.click(538, 653, 1, 0, "left")
    pyautogui.typewrite(f"2")
    pyautogui.press("enter")

    # ニー
    pyautogui.click(679, 709, 1, 0, "left")
    for i in range(2):
        pyautogui.press("down")
    pyautogui.press("enter")

    # アタックタイム
    pyautogui.click(863, 656, 1, 0, "left")
    pyautogui.typewrite(f"{attack_time}")
    pyautogui.press("enter")

    # リリースタイム
    pyautogui.click(973, 652, 1, 0, "left")
    pyautogui.typewrite(f"{note-attack_time}")
    pyautogui.press("enter")

    # オートボタン
    pyautogui.click(1109, 711, 1, 0, "left")

    # ルックアヘッド
    pyautogui.click(437, 831, 1, 0, "left")
    pyautogui.typewrite(f"0")
    pyautogui.press("enter")

    # フィルター
    pyautogui.click(528, 826, 1, 0, "left")
    pyautogui.typewrite(f"{Freq[48]}")
    pyautogui.press("enter")

    # Emphasis
    pyautogui.click(646, 823, 1, 0, "left")
    pyautogui.typewrite(f"0.8")
    pyautogui.press("enter")

    # Detect
    pyautogui.click(760, 885, 1, 0, "left")
    for i in range(4):
        pyautogui.press("down")
    pyautogui.press("enter")

    pyautogui.moveTo(home_x, home_y)
    # ウィンドウのループ処理
    root.mainloop()


# ----------------------
# ウィンドウの作成
root = tkinter.Tk()
root.title("Axe-Edit Edit")
# root.iconbitmap('icon.ico')
root.geometry("300x400")
root.geometry("+1600+10")

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

lbl3 = tkinter.Label(text="プロクシミリティー E2:40 G2:43 B2:47")
lbl3.place(x=10, y=150)
input_proximity = tkinter.Entry(width=6)
input_proximity.place(x=10, y=180)
input_proximity.insert(tkinter.END, 43)

amp_all = tkinter.Button(root, text=f"Amp All", command=amp_axe)
amp_all.place(x=10, y=30)

amp = tkinter.Button(root, text=f"Amp", command=amp_axe2)
amp.place(x=80, y=30)

ampGEQ = tkinter.Button(root, text=f"Amp GEQ", command=amp_axe_GEQ)
ampGEQ.place(x=120, y=30)

ampbasic2 = tkinter.Button(root, text=f"Amp basic2", command=amp_axe_basic2)
ampbasic2.place(x=190, y=30)

ampGEQ_DS = tkinter.Button(
    root,
    text=f"GEQ Metal",
    command=lambda: amp_axe_GEQ8(5, -2, -8.6, -3.1, 2.1, 3.3, 8.6, 7.6),
)
ampGEQ_DS.place(x=10, y=180)

ampGEQ_Rock = tkinter.Button(
    root,
    text=f"GEQ Rock",
    command=lambda: amp_axe_GEQ8(-3.5, 4, 6, 0.2, -0.2, 2.3, -4, 0),
)
ampGEQ_Rock.place(x=80, y=180)

ampGEQ_Reggae = tkinter.Button(
    root,
    text=f"GEQ Reggae",
    command=lambda: amp_axe_GEQ8(5, 4, 4.5, 2, -0.2, -5, -4, -8),
)
ampGEQ_Reggae.place(x=150, y=180)


ampGEQ_DS = tkinter.Button(
    root,
    text=f"2GEQ Metal",
    command=lambda: amp_axe_GEQ8(5, -2, -8.6, -3.1, 2.1, 3.3, 8.6, 7.6),
)
ampGEQ_DS.place(x=10, y=280)

ampGEQ_Rock = tkinter.Button(
    root,
    text=f"2GEQ Rock",
    command=lambda: amp_axe_GEQ8(-3.5, 4, 6, 0.2, -0.2, 2.3, -4, 0),
)
ampGEQ_Rock.place(x=80, y=280)

ampGEQ_Reggae = tkinter.Button(
    root,
    text=f"2GEQ Reggae",
    command=lambda: amp_axe_GEQ8(5, 4, 4.5, 2, -0.2, -5, -4, -8),
)
ampGEQ_Reggae.place(x=150, y=280)

cab = tkinter.Button(root, text=f"Cab", command=cab_axe)
cab.place(x=10, y=70)

stereo_cab = tkinter.Button(root, text=f"Stereo Cab", command=stereo_cab_axe)
stereo_cab.place(x=50, y=70)

gate = tkinter.Button(root, text=f"Gate", command=gate_axe)
gate.place(x=10, y=110)


comp = tkinter.Button(root, text=f"Comp", command=comp_axe)
comp.place(x=50, y=110)


# ウィンドウのループ処理
root.mainloop()
