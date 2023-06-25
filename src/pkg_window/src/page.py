#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# アノテーション用パッケージ
from __future__ import annotations
from typing import (List, Tuple, Dict, Optional, Union)
# tkinter
from tkinter import Frame
# 抽象クラス
from abc import ABCMeta, abstractmethod
# ログ用パッケージ
from pkg_common.log_manager import LogManager


class Base(metaclass = ABCMeta):
    """ページクラス(抽象クラス)
    """
    def __init__(self, page_name_tag: str, master: Optional[Frame]) -> None:
        """コンストラクタ

        Args:
            page_name_tag (str): ページ名タグ文字列
        """
        # ページ情報生成
        self._page_name_tag: str = page_name_tag
        self._master_frame: Frame = master
        # ログマネージャインスタンス生成
        self._log: LogManager = LogManager()

    def setup(self) -> None:
        """セットアップ

        Raises:
            NotImplementedError: 抽象メソッドの実装無しエラー
        """
        raise NotImplementedError()

    @abstractmethod
    def set_enable(self, enable: bool) -> None:
        """ページ有効・無効状態設定

        Args:
            enable (bool): 設定する状態 [True:有効 / False:無効]

        Raises:
            NotImplementedError: 抽象メソッドの実装無しエラー
        """
        raise NotImplementedError()

    @abstractmethod
    def get_enable(self) -> bool:
        """ページ有効・無効状態取得

        Raises:
            NotImplementedError: 抽象メソッドの実装無しエラー

        Returns:
            bool: True:有効 / False:無効
        """
        raise NotImplementedError()

    @abstractmethod
    def clear(self) -> None:
        """ページクリア

        Raises:
            NotImplementedError: 抽象メソッドの実装無しエラー
        """
        raise NotImplementedError()