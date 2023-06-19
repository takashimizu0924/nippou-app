#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# アノテーション用パッケージ
from __future__ import annotations
from typing import (List, Tuple, Dict, Optional, Union)
# ログ用パッケージ
from pkg_common.log_manager import LogManager


class Page:
    """ページクラス
    """
    def __init__(self, page_name_tag: str) -> None:
        """コンストラクタ

        Args:
            page_name_tag (str): ページ名タグ文字列
        """
        self._name_tag: str = page_name_tag
        self._frame_list: List[object] = []

    def add_frame(self, frame_list: List[object]):
        """フレームをページに追加

        Args:
            frame_list (List[object]): 追加するフレーム配列
        """
        # 引数チェック
        if len(frame_list) <= 0:
            
            return

        self._frame_list
    
    def clear(self) -> None:
        """ページクリア
        """