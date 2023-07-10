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
        self.login: Login = None
        self.window: Window = None
        self.__create_root()
                
    def __create_root(self) -> None:
        """メイン画面の設定
        """
        self.root = tk.Tk()
        self.root.title(self._APP_TITLE)
        self.root.geometry(f"{self._APP_WIDTH}x{self._APP_HEIGHT}+{self._APP_POSITION_X}+{self._APP_POSITION_Y}")
        self.root.resizable(width=self._RESIZE_WINDOW_X, height=self._RESIZE_WINDOW_Y)
    
    def start(self) -> None:     
        self.root.mainloop()

    def show_login_page(self) -> None:
        self.login = Login(self.root)

    def show_main_page(self) -> None:
        self.window = Window(self.root, self.login._USER_NAME)


def main():
    app = App()
    app.start()
    app.show_login_page()
    app.show_main_page()

if __name__ == "__main__":
    main()