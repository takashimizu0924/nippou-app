""" ウィンドウ管理 """
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# アノテーション用パッケージ
from __future__ import annotations
from typing import (List, Tuple, Dict, Optional, Union)
# ログ用パッケージ
from pkg_common.log_manager import LogManager
# 内部共通パッケージ
from pkg_common import check_arg_type, check_args_type
# ウィンドウモジュールのベースウィンドウクラス
from window import Base

class WindowManager:
    """ウィンドウ管理クラス
    """
    def __init__(self) -> None:
        """コンストラクタ
        """
        ### バッファで保持するウィンドウ情報用
        self._start_window: Optional[Base] = None
        self._window_dict: Optional[Dict[str, Base]] = {}
        self._current_window_name_tag: str = ""
        self._is_registered_windows: bool = False
        self._is_start_window_set: bool = False
        self._is_exist_enable_window: bool = False

        # ログマネージャインスタンス生成
        self._log_header: str = "[PageController class] "
        self._log: LogManager = LogManager()

    def register_windows(self, windows_list: Optional[Base]) -> bool:
        """ウィンドウリスト登録

        Args:
            windows_list (Optional[Base]): 登録するウィンドウオブジェクトのリスト

        Returns:
            bool: True:成功 / False:失敗
        """
        ### 引数チェック
        if check_args_type(windows_list, Base) is False:
            ## 失敗: 引数型エラー
            self._log.error(f'{self._log_header}register_windows: arguments type error.')
            return False

        ### バッファにウィンドウリストを登録
        for window in windows_list:
            self._window_dict[window.get_name_tag()] = window

        ### 結果応答
        return True

    def set_start_window(self, start_window: Base) -> bool:
        """スタートウィンドウ設定

        Args:
            start_window (Base): スタートウィンドウオブジェクト

        Returns:
            bool: True:成功 / False:失敗
        """
        ### 引数チェック
        if check_arg_type(start_window, Base) is False:
            ## 失敗: 引数型エラー
            self._log.error(f'{self._log_header}set_start_window: argument type error.')
            return False

        ### バッファにスタートウィンドウを設定
        self._start_window = start_window

        ### 結果応答
        return True

    def show_start_window(self) -> bool:
        """スタートウィンドウ表示

        Returns:
            bool: True:成功 / False:失敗
        """
        ### 応答生成
        _rsp: bool = False

        ### スタートウィンドウ設定チェック
        if self._start_window is False:
            ## 失敗: 引数型エラー
            self._log.error(f'{self._log_header}show_start_window: not set start window yet.')
            return _rsp

        ### 応答データ更新
        _rsp = True

        ### スタートウィンドウ表示状態チェック
        if self._start_window.get_active() is True:
            # 既に表示中のため正常値を結果応答
            return _rsp

        ### スタートウィンドウ表示実行
        self._start_window.set_active(_rsp)
        # バッファ情報更新
        self._is_exist_enable_window = _rsp
        self._current_window_name_tag = self._start_window.get_name_tag()

        ### 結果応答
        return _rsp

    def refresh(self) -> bool:
        """ウィンドウリフレッシュ
            NOTE: 現在開いているウィンドウ情報をクリアし、リフレッシュする

        Args:
            target_window_name_tag (str): リフレッシュ対象

        Returns:
            bool: True:成功 / False:失敗
        """
        ### 応答生成
        _rsp: bool = False

        ### ウィンドウ有効状態チェック
        if self._is_exist_enable_window is False:
            ## 失敗: 引数型エラー
            self._log.error(f'{self._log_header}refresh: does not exists enabled window.')
            return _rsp

        ### 現在有効なウィンドウのリフレッシュ実行
        _rsp = True
        self._window_dict[self._current_window_name_tag].clear()

        ### 結果応答
        return _rsp

    def change(self, window_name_tag: str) -> bool:
        """ウィンドウ切り替え

        Args:
            window_name_tag (str): 切り替え対象のウィンドウ名タグ文字列

        Returns:
            bool: True:成功 / False:失敗
        """
        ### 引数チェック
        if check_arg_type(window_name_tag, str) is False:
            ## 失敗: 引数型エラー
            self._log.error(f'{self._log_header}change: argument type error.')
            return False

        ### 現在の有効ウィンドウタグ名チェック
        if window_name_tag == self._current_window_name_tag:
            # すでに同じタグ名のウィンドウが有効の場合は正常値の結果を応答
            return True

        ### 応答生成
        _rsp: bool = False

        try:
            # 切り替え対象ウィンドウの有効状態チェック
            if self._window_dict[window_name_tag].get_active() is True:
                # 既に表示中のため正常値を結果応答
                return True

            # 現在のウィンドウを無効に設定
            self._window_dict[self._current_window_name_tag].set_active(False)
            # 切り替え対象のウィンドウを有効化
            self._window_dict[window_name_tag].set_active(True)
            # バッファ情報更新
            self._current_window_name_tag = window_name_tag
            # 応答データ更新
            _rsp = True

        except ValueError as error_msg:
            ## 失敗: 存在しないウィンドウへの参照エラー
            self._log.error(f'{self._log_header}change: does not exists target window name in buffer. target window name: {window_name_tag}, Error: {error_msg}')

        # 結果応答
        return _rsp
