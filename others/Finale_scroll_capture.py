# -*- coding: utf-8 -*-

# Finaleをスクロール表示でキャプチャーできるような画面に整えるスクリプト

# PyAutoGUIのモジュール
import pyautogui
# プロセスを制御するためにOS周りのモジュール
import time

# --------------------------------------
# 休符を移動させる範囲を選択した後にスクリプトを実行させる。
# --------------------------------------
# Finaleを選択
pyautogui.hotkey("win", "4")

# Finaleを全画面表示
pyautogui.hotkey("win", "up")

# 表示
pyautogui.click(250, 35, 1, 0, 'left')
time.sleep(0.4)

# 表示方法
pyautogui.moveTo(274, 93)
time.sleep(0.4)

# 移動
pyautogui.moveTo(630, 100)
time.sleep(0.4)

# 移動
pyautogui.moveTo(630, 200)
time.sleep(0.4)

# 縦方向に表示
pyautogui.click(650, 200, 1, 0, 'left')

# 虫眼鏡ツールに切り替える
pyautogui.click(770, 55, 1, 0, 'left')

# 拡大する
pyautogui.click(1200, 292, 1, 0, 'left')

# 選択ツールに切り替える
# pyautogui.click(37, 55, 1, 0, 'left')
