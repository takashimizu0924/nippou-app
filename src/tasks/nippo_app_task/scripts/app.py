""" 日報管理アプリ エントリ"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from pkg_common.file_manager import FileManager
from pkg_common.log_manager import LogLevel, LogManager
# from main_window import Window
# from login import Login

class App:
    """アプリ全体のTOPレベル層
    """
    def __init__(self) -> None:
        """コンストラクタ
        """
        # GUI画面のルートオブジェクト生成
        self.root = tk.Tk()

        ### 設定値定義
        # NOTE: アプリメイン画面
        self._app_window_title: str = "業務管理アプリ"
        self._app_window_width: int = 1000
        self._app_window_height: int = 700
        self._app_window_pos_x: int = 400
        self._app_window_pos_y: int = 150
        self._app_window_resize_x: bool = False
        self._app_window_resize_y: bool = False

        # NOTE: 日報入力画面
        # self._input_window_title: str = "日報入力"
        # self._input_window_width: int = 750
        # self._input_window_height: int = 450
        # self._input_window_pos_x: int = 520
        # self._input_window_pos_y: int = 250

    def initialize(self) -> None:
        """初期化処理
        """
        ### 初期設定
        # タイトル文字設定
        self.root.title(self._app_window_title)
        # 画面サイズ設定
        _window_size: str = f'{self._app_window_width}x{self._app_window_height}'
        _window_pos: str = f'{self._app_window_pos_x}+{self._app_window_pos_y}'
        # ジオメトリ設定
        self.root.geometry(f"{_window_size}+{_window_pos}")
        # 画面リサイズ設定
        self.root.resizable(width=self._app_window_resize_x, height=self._app_window_resize_y)

        # ウィンドウオブジェクト生成
        # window = Window(self.root)
        # ウィンドウオブジェクト生成
        # self.login = Login(self.root, window)

    def start(self) -> None:
        """GUI表示処理開始
        """
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.initialize()
    app.start()
