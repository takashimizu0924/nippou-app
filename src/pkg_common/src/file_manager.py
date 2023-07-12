""" ファイル管理 """
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# アノテーションパッケージ用
from typing import (Dict, List, Union)
# ファイルパス存在確認用
import os
import json
# スタックトレース取得用
import traceback

### ファイル入出力管理クラス定義 ###
class FileManager:
    """ファイル入出力管理クラス
    """
    def __init__(self) -> None:
        self._encode_type: str = "utf-8"

    def read(self, file_path: str) -> List[str]:
        """ファイル読み込み

        Args:
            file_path (str): 読み込むファイル名

        Returns:
            List[str]: 応答データ
        """
        # 応答データを作成
        _rsp = []
        # ファイル存在確認
        is_file = os.path.isfile(file_path)
        if not is_file:
            # ファイルじゃない場合はここでエラーを返す
            return _rsp

        # 読み込みデータを確認
        try:
            with open(file_path, "r", encoding = self._encode_type) as file:
                # splitで指定した改行コードを基準に配列化
                _rsp = file.read().split('\n')
                # 最後尾の空白文字を削除
                del _rsp[-1]
                print(_rsp)

        # 読み込みを失敗した場合ここに入る
        except PermissionError as error_msg:
            print(f"Error message: {error_msg}\n\
                Traceback: {traceback.format_exc()}")
            return _rsp

        except FileNotFoundError  as error_msg:
            print(f"Error message: {error_msg}\n\
                Traceback: {traceback.format_exc()}")
            return _rsp

        return _rsp

    def write(self, file_path: str, write_text_list: list) -> bool:
        """ファイル書き込み
            NOTE: 引数(write_text_list)には改行したい文字列毎に要素を区切って渡すこと
                  例: ["1行目の文字列", "2行目の文字列", "N行目の文字列"]

        Args:
            file_path (str): 書き込むファイル名
            write_text_list (list): 書き込む文字列リスト
        """
        # 書き込みデータを確認
        try:
            with open(file_path, "a", encoding = self._encode_type) as file:
                # 空のデータを作成
                _write_text_list = []
                for data in write_text_list:
                    # 配列の要素の最後尾1つ1つに改行コード追加
                    _write_text_list.append(str(data) + '\n')
                # リストをまとめて書き込む
                file.writelines(_write_text_list)

        #書き込みを失敗した場合ここに入る
        except PermissionError as error_msg:
            print(f"Error message: {error_msg}\n\
                Traceback: {traceback.format_exc()}")
            return False

        return True

    def json_read(self, json_file_path: str) -> Dict[str,Union[str, int]]:
        """Jsonファイル読み込み

        Args:
            json_file_path (str): 読み込むJsonファイル名

        Returns:
            Dict[str,Union[str, int]]: 応答データ
        """
        # 応答データを作成
        _rsp = {}
        # ファイル存在確認
        is_file = os.path.isfile(json_file_path)
        if not is_file:
            # ファイルじゃない場合はここでエラーを返す
            return _rsp

        # 読み込みデータを確認
        try:
            with open(json_file_path, "r", encoding = self._encode_type) as json_file:
                # splitで指定した改行コードを基準に配列化
                _rsp = json.load(json_file)

        # 読み込みを失敗した場合ここに入る
        except PermissionError as error_msg:
            print(f"Error message: {error_msg}\n\
                Traceback: {traceback.format_exc()}")
            return _rsp

        except FileNotFoundError  as error_msg:
            print(f"Error message: {error_msg}\n\
                Traceback: {traceback.format_exc()}")
            return _rsp

        return _rsp
