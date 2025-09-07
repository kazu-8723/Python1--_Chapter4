# ウィンドウを表示するモジュール
import tkinter as tk
# ファイルダイアログを使うモジュール
import tkinter.filedialog as fd
# 画像を扱うモジュール
import PIL.Image
# tkinterで作成した画面上に画像を表示させるモジュール
import PIL.ImageTk

# 画像ファイルを表示する関数
def dispPhoto(path):
    # 画像を読み込み、グレースケールに変換
    newImage = PIL.Image.open(path).convert("L").resize((300,300))
    # そのイメージをラベルに表示する
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

# ファイルダイアログを開く関数
def openFile():
    # ファイルダイアログを開いて、選択したファイル名を取得する
    fpath = fd.askopenfilename()
    # もしファイル名があったらそのファイル名で関数を呼び出す
    if fpath:
        dispPhoto(fpath)

# 画面を作る
root = tk.Tk()
root.geometry("400x350")

# ボタンを作って関数を設定する
btn = tk.Button(text = "ファイルを開く", command = openFile)
# 画面表示用のラベルを作成
imageLabel = tk.Label()
# 画面にボタンを配置
btn.pack()
# 画面にラベルを配置
imageLabel.pack()
# 作ったウィンドウを表示
tk.mainloop()
