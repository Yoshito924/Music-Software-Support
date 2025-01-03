# Axe-FX Control Tool

Axe-FX用のGUIコントロールツールです。マウスの自動操作を利用してAxe-Editの設定を効率的に行うことができます。

## 機能

- アンプ設定の自動化
- GEQプリセットの適用
- ゲート設定の自動調整
- コンプレッサー設定の自動調整
- BPMと気温に基づいた最適なタイミング設定

## インストール

```bash
# リポジトリのクローン
git clone https://github.com/kimuyoshi/axe-fx-control.git
cd axe-fx-control

# 依存パッケージのインストール
pip install -r requirements.txt
```

## 使用方法

1. Axe-Editを起動し、編集したいプリセットを開きます。
2. 以下のコマンドでツールを起動します：

```bash
python -m axe_fx
```

3. GUIウィンドウが表示されたら、必要な設定（BPM、気温など）を入力します。
4. 各ボタンをクリックして、対応する設定を適用します。

## 注意事項

- このツールはマウスの自動操作を使用するため、操作中は他の作業を行わないでください。
- Axe-Editのウィンドウ位置が変更されると、正しく動作しない可能性があります。
- 設定を適用する前に、必ずプリセットのバックアップを取ることをお勧めします。
