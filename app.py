import tkinter as tk
from main_window import Window
from login import Login

class App:
    """アプリ全体のTOPレベル層
    """
    def __init__(self) -> None:
        """コンストラクタ"""
        """メイン画面表示
           各ウィンドウサイズ設定
        """
        self._APP_TITLE: str = "業務管理アプリ"
        self._APP_WIDTH: int = 1000
        self._APP_HEIGHT: int = 700
        self._APP_POSITION_X: int = 400
        self._APP_POSITION_Y: int = 150
        self._RESIZE_WINDOW_X: bool = False
        self._RESIZE_WINDOW_Y: bool = False
        
        self._INPUT_DATA_TITLE: str = "日報入力"
        self._INPUT_DATA_WIDTH: int = 750
        self._INPUT_DATA_HEIGHT: int = 450
        self._INPUT_DATA_POSITION_X: int = 520
        self._INPUT_DATA_POSITION_Y: int = 250
        
    
    def start(self):
        self.root = tk.Tk()
        self.root.title(self._APP_TITLE)
        self.root.geometry(f"{self._APP_WIDTH}x{self._APP_HEIGHT}+{self._APP_POSITION_X}+{self._APP_POSITION_Y}")
        self.root.resizable(width=self._RESIZE_WINDOW_X, height=self._RESIZE_WINDOW_Y)
        window = Window(self.root)
        
        self.login = Login(self.root, window)
             
        self.root.mainloop()
        
        
        



if __name__ == "__main__":
    app = App()
    app.start()