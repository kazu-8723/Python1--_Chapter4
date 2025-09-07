# tkinterをインポート、tkと略して使用
import tkinter as tk
# randomをインポート
import random

# 関数追加
def dispLabel():
# おみくじのリストを用意
    kuji = ['大吉', '中吉', '小吉', '凶']
# ランダムに1つ選び出され表示
    lbl.configure(text = random.choice(kuji))

# 画面作成
root = tk.Tk()
# 画面の大きさ設定
root.geometry("200x100")
# ラベル作成
lbl = tk.Label(text = "LABEL")
# 関数を実行できるボタン作成
btn = tk.Button(text = "PUSH", command = dispLabel)
# 画面にラベルを配置
lbl.pack()
# 画面にボタンを配置
btn.pack()
# 作成したウィンドウを表示
tk.mainloop()
