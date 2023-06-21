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
        self._start_
        # ログマネージャインスタンス生成
        # self._log: LogManager = LogManager()

    def set_start(self, start_page_frame_dict: Dict[str, object]) -> bool:
        """スタートページ設定
            NOTE:以下のパラメータを与えてアプリ開始時のスタートページを設定する
                {"<スタートページタグ名>": <スタートページフレームオブジェクト>}

        Args:
            start_page_frame_dict (Dict[str, object]): スタートページ辞書データ

        Returns:
            bool: _description_
        """

    def add_frame(self, frame_list: List[object]) -> bool:
        """フレームをページに追加

        Args:
            frame_list (List[object]): 追加するフレーム配列
        """
        ### 応答データ作成
        _rsp: bool = False

        # 引数チェック
        if len(frame_list) <= 0:
            print(f'Page class:add_frame method --> Add frame failed. frame_list length is {len(frame_list)}')
            return _rsp

        # フレーム追加
        self._frame_list.extend(frame_list)
        _rsp = True

        # 応答
        return _rsp
    
    def clear(self) -> None:
        """ページクリア
        """