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
        
        # self._APP_TITLE: str = "業務管理アプリ"
        # self._APP_WIDTH: int = 1000
        # self._APP_HEIGHT: int = 700
        # self._APP_POSITION_X: int = 400
        # self._APP_POSITION_Y: int = 150
        # self._RESIZE_WINDOW_X: bool = False
        # self._RESIZE_WINDOW_Y: bool = False
        
        # self.__create_root(self._APP_TITLE, self._APP_WIDTH, self._APP_HEIGHT, self._APP_POSITION_X, self._APP_POSITION_Y, self._RESIZE_WINDOW_X, self._RESIZE_WINDOW_Y)
        
    def __create_root(self, app_title: str, width: int, height: int, position_x: int, position_y: int, resize_window_x: bool, resize_window_y: bool):
        """メイン画面の設定

        Args:
            title (str): アプリケーションタイトル
            width (int): メイン画面の横幅
            height (int): メイン画面の高さ
            position_x (int): メイン画面のX座標
            position_y (int): メイン画面のY座標
            resize_window_x (bool): メイン画面の横幅サイズの可変の有無
            resize_window_y (bool): メイン画面の高さサイズの可変の有無
        """
        # self.root = tk.Tk()
        # self.root.title(app_title)
        # self.root.geometry(f"{width}x{height}+{position_x}+{position_y}")
        # self.root.resizable(width=resize_window_x, height=resize_window_y)
        # return
    
    def start(self):
        self.root = tk.Tk()
        self.root.title(self._APP_TITLE)
        self.root.geometry(f"{self._APP_WIDTH}x{self._APP_HEIGHT}+{self._APP_POSITION_X}+{self._APP_POSITION_Y}")
        self.root.resizable(width=self._RESIZE_WINDOW_X, height=self._RESIZE_WINDOW_Y)
        # self.window = Window()
        self.login =Login(self.root)
        self.login.input_widget()
        window = Window(self.root, self.login._USER_NAME)
        window.input_data_window()
        
        
        # if self.login.flag == False:
        #     self.login.input_widget()
            # self.user_name =self.login.login()
            # self.user_name = self.login
            # window = Window(self.root, self.user_name)
            # window.input_data_window()
             
        self.root.mainloop()
        
        
        

def main():
    app = App()
    app.start()

if __name__ == "__main__":
    main()