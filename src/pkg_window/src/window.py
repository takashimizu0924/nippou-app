""" 基底クラス(ウィンドウクラス) """
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# アノテーション用パッケージ
from __future__ import annotations
from typing import (Optional,)
# tkinter
from tkinter import Frame
# 抽象クラス
from abc import ABCMeta, abstractmethod
# ログ用パッケージ
from pkg_common.log_manager import LogManager


class Base(metaclass = ABCMeta):
    """ウィンドウクラス(抽象クラス)
    """
    def __init__(self, window_name_tag: str, master: Optional[Frame]) -> None:
        """コンストラクタ

        Args:
            window_name_tag (str): ウィンドウ名タグ文字列
            master (Optional[Frame]): tkinterのフレームオブジェクト
        """
        # ウィンドウ情報生成
        self._window_name_tag: str = window_name_tag
        self._master_frame: Frame = master
        # ウィンドウ状態値
        self._is_active: bool = False
        # ログマネージャインスタンス生成
        self._log: LogManager = LogManager(save_path='')

    def setup(self) -> None:
        """セットアップ

        Raises:
            NotImplementedError: 抽象メソッドの実装無しエラー
        """
        raise NotImplementedError()

    def get_name_tag(self) -> str:
        """ウィンドウタグ名取得

        Returns:
            str: ウィンドウタグ名
        """
        return self._window_name_tag

    def set_active(self, active: bool) -> None:
        """ウィンドウの有効・無効状態設定

        Args:
            active (bool): 設定する状態 [True:有効 / False:無効]
        """
        if not active is self._is_active:
            self._is_active = active

    def get_active(self) -> bool:
        """ウィンドウの有効・無効状態取得

        Returns:
            bool: True:有効 / False:無効
        """
        return self._is_active

    @abstractmethod
    def clear(self) -> None:
        """ウィンドウクリア

        Raises:
            NotImplementedError: 抽象メソッドの実装無しエラー
        """
        raise NotImplementedError()

    @abstractmethod
    def destroy(self) -> None:
        """ウィンドウ削除

        Raises:
            NotImplementedError: 抽象メソッドの実装無しエラー
        """
        raise NotImplementedError()
