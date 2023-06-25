#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# アノテーション用パッケージ
from __future__ import annotations
from typing import (List, Tuple, Dict, Optional, Union)
# ログ用パッケージ
from pkg_common.log_manager import LogManager
# 内部共通パッケージ
from pkg_common import check_arg_type, check_args_type
# ページモジュールのベースページクラス
from page import Base

class PageController:
    """ページ制御クラス
    """
    def __init__(self) -> None:
        """コンストラクタ
        """
        ### バッファで保持するページ情報用
        self._start_page: Optional[Base] = None
        self._page_dict: Optional[Dict[str, Base]] = None
        self._current_page_name_tag: str = ""
        self._is_registered_pages: bool = False
        self._is_start_page_set: bool = False
        self._is_exist_enable_page: bool = False

        # ログマネージャインスタンス生成
        self._log_header: str = "[PageController class] "
        self._log: LogManager = LogManager()

    def register_pages(self, pages_list: Optional[Base]) -> bool:
        """ページリスト登録

        Args:
            pages_list (Optional[Base]): 登録するページオブジェクトのリスト

        Returns:
            bool: True:成功 / False:失敗
        """
        ### 引数チェック
        if check_args_type(pages_list, Base) is False:
            ## 失敗: 引数型エラー
            self._log.error(f'{self._log_header}register_pages: arguments type error.')
            return False

        ### バッファにページリストを登録
        for page in pages_list:
            self._page_dict[page._page_name_tag] = page

        ### 結果応答
        return True

    def set_start_page(self, start_page: Base) -> bool:
        """スタートページ設定

        Args:
            start_page (Base): スタートページオブジェクト

        Returns:
            bool: True:成功 / False:失敗
        """
        ### 引数チェック
        if check_arg_type(start_page, Base) is False:
            ## 失敗: 引数型エラー
            self._log.error(f'{self._log_header}set_start_page: argument type error.')
            return False

        ### バッファにスタートページを設定
        self._start_page = start_page

        ### 結果応答
        return True

    def show_start_page(self) -> bool:
        """スタートページ表示

        Returns:
            bool: True:成功 / False:失敗
        """
        ### 応答生成
        _rsp: bool = False

        ### スタートページ設定チェック
        if self._start_page is False:
            ## 失敗: 引数型エラー
            self._log.error(f'{self._log_header}show_start_page: not set start page yet.')
            return _rsp
            
        ### 応答データ更新
        _rsp = True

        ### スタートページ表示状態チェック
        if self._start_page.get_enable() is True:
            # 既に表示中のため正常値を結果応答
            return _rsp

        ### スタートページ表示実行
        self._start_page.set_enable(_rsp)
        # バッファ情報更新
        self._is_exist_enable_page = _rsp
        self._current_page_name_tag = self._start_page._page_name_tag

        ### 結果応答
        return _rsp

    def refresh(self) -> bool:
        """ページリフレッシュ
            NOTE: 現在開いているページ情報をクリアし、リフレッシュする

        Args:
            target_page_name_tag (str): リフレッシュ対象

        Returns:
            bool: True:成功 / False:失敗
        """
        ### 応答生成
        _rsp: bool = False

        ### ページ有効状態チェック
        if self._is_exist_enable_page is False:
            ## 失敗: 引数型エラー
            self._log.error(f'{self._log_header}refresh: does not exists enabled page.')
            return _rsp

        ### 現在有効なページのリフレッシュ実行
        _rsp = True
        self._page_dict[self._current_page_name_tag].clear()

        ### 結果応答
        return _rsp

    def change(self, page_name_tag: str) -> bool:
        """ページ切り替え

        Args:
            page_name_tag (str): 切り替え対象のページ名タグ文字列

        Returns:
            bool: True:成功 / False:失敗
        """
        ### 引数チェック
        if check_arg_type(page_name_tag, str) is False:
            ## 失敗: 引数型エラー
            self._log.error(f'{self._log_header}change: argument type error.')
            return False

        ### 現在の有効ページタグ名チェック
        if page_name_tag == self._current_page_name_tag:
            # すでに同じタグ名のページが有効の場合は正常値の結果を応答
            return True

        ### 応答生成
        _rsp: bool = False

        try:
            # 切り替え対象ページの有効状態チェック
            if self._page_dict[page_name_tag].get_enable() is True:
                # 既に表示中のため正常値を結果応答
                return True

            # 現在のページを無効に設定
            self._page_dict[self._current_page_name_tag].set_enable(False)
            # 切り替え対象のページを有効化
            self._page_dict[page_name_tag].set_enable(True)
            # バッファ情報更新
            self._current_page_name_tag = page_name_tag
            # 応答データ更新
            _rsp = True

        except Exception as e:
            ## 失敗: 存在しないページへの参照エラー
            self._log.error(f'{self._log_header}change: does not exists target page name in buffer. target page name: {page_name_tag}')

        # 結果応答
        return _rsp