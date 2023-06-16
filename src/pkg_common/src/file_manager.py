#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ファイルパス存在確認用
import os

### ファイル入出力管理クラス定義 ###
class FileManager:
    """ファイル入出力管理クラス
    """
    def __init__(self) -> None:
        self._ENCODE_TYPE: str = "utf-8"

    def read(self, file_path: str) -> list:
        """ファイル読み込み

        Args:
            file_path (str): 読み込むファイル名
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
            with open(file_path, "r", encoding = self._ENCODE_TYPE) as file:
                # splitで指定した改行コードを基準に配列化
                _rsp = file.read().split('\n')
                # 最後尾の空白文字を削除
                del _rsp[-1]
                print(_rsp)
        
        # 読み込みを失敗した場合ここに入る
        except Exception as e:
            print(f"Error message: {e}")
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
            with open(file_path, "a", encoding = self._ENCODE_TYPE) as file:
                # 空のデータを作成
                _write_text_list = []
                for data in write_text_list:
                    # 配列の要素の最後尾1つ1つに改行コード追加
                    _write_text_list.append(str(data) + '\n')
                # リストをまとめて書き込む
                file.writelines(_write_text_list)

        #書き込みを失敗した場合ここに入る
        except Exception as e:
            print(f"Error message: {e}")
            return False

        return True

# if __name__ == '__main__':
    # お試しの場合はここに追加
    # test_path: str = "/home/natsuki/work/project/nippou-app/src/pkg_common/scripts/test.txt"
    # path = os.getcwd()
    # print(path)
    # test_path: str = f"{path}/test.txt"
    # is_file = os.path.isfile(test_path)
    # if is_file:
    #     print("file exists")
    # else:
    #     print("does not exists")

    # クラスのインスタンス化
    # file_manager = FileManager()
    # # 書き込む対象のテキストファイルの絶対パスを作成
    # path = "/home/natsuki/work/project/nippou-app/data/sample.txt"
    # # 書き込むデータを作成
    # data = [
    #     "1行目に書き込むデータ",
    #     "2行目に書き込むデータ",
    #     "3行目に書き込むデータ"
    # ]
    # file_manager.read(path)

    # # 指定したパスのファイルにデータを書き込む
    # is_ok = file_manager.write(path, data)
    # if is_ok:
    #     print("write success")
    # else:
    #     print("write failure")