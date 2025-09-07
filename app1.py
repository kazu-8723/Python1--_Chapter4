# tkinterをインポート、tkと略して使用
import tkinter as tk
# 画面作成
root = tk.Tk()
# 画面の大きさ設定
root.geometry("200x100")
# ラベル作成
lbl = tk.Label(text = "LABEL")
# ボタン作成
btn = tk.Button(text = "PUSH")
# 画面にラベルを配置
lbl.pack()
# 画面にボタンを配置
btn.pack()
# 作成したウィンドウを表示
tk.mainloop()
