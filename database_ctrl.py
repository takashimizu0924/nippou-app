#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
from typing import (Union, List, Dict, Tuple)

### データクラス定義 ###
# テーブル関連
class TableDataType:
    """テーブルデータ型クラス
    """
    NULL: str           = "NULL"
    INT: str            = "INTEGER"
    FLOAT: str          = "REAL"
    STR: str            = "TEXT"
    BYTES: str          = "BLOB"
    PRIMARY_KEY: str    = "PRIMARY KEY"
    AUTO_INC: str       = "AUTOINCREMENT"

class DatabaseRetCode:
    """データベースリターンコード
    """
    SUCCESS: int                        = 0
    DB_CONNECTION_ERROR: int            = -1
    DB_CREATE_TABLE_ERROR: int          = -2
    DB_TABLE_ACCESS_ERROR: int          = -3
    DB_TABLE_INSERT_RECORD_ERROR: int   = -4
    DB_TABLE_UPDATE_RECORD_ERROR: int   = -5
    DB_TABLE_DELETE_RECORD_ERROR: int   = -6
    DB_TABLE_FETCH_RECORD_ERROR: int    = -7
    DB_DISCONNECTION_ERROR: int         = -8
    DB_OTHER_ERROR: int                 = -9


### 制御クラス定義 ###
class DatabaseControl:
    """データベース制御クラス
    """
    def __init__(self, database_name: str) -> None:
        """コンストラクタ
        """
        # NOTE:データベースに接続する処理を記述する
        self._conn = sqlite3.connect(database_name)
        self._cur = self._conn.cursor()

    def __execute(self, sql: str) -> None:
        """sql文を実行

        Args:
            sql (str): 実行するクエリ
        """
        self._cur.execute(sql)
        return
    
    def __commit(self) -> None:
        """変更適用
        """
        self._conn.commit()
        return
    
    def create_table(self, table_name: str, table_data_dict: Dict[str, TableDataType]) -> int:
        """テーブル作成

        Args:
            table_name (str): テーブル名
            table_data_dict (Dict[str, TableDataType]): テーブルデータ(辞書データ)

        Returns:
            int: データベースリターンコード
        """
        # 引数チェック
        if table_name == "":
            print("指定されたテーブル名が空のためエラー")
            return DatabaseRetCode.DB_CREATE_TABLE_ERROR
        
        # 引数チェック
        if table_data_dict == {} or table_data_dict == None:
            print("指定されたテーブルデータが空のためエラー")
            return DatabaseRetCode.DB_CREATE_TABLE_ERROR

        # クエリー作成用変数定義
        _query: str = ""
        for record, record_type in table_data_dict.items():
            # テーブル作成用のクエリーで指定するレコードと型をクエリー作成用変数に設定
            _query += f"{record} {record_type},"
           
        # 末尾のカンマは不要なため削除
        _query = _query.rstrip(',')
        # 実行用sqlを生成
        _sql: str = f'CREATE TABLE {table_name}({_query})'
        # sql文を確認
        print(f"{_sql}")

        # sql文を実行
        self.__execute(_sql)
        # 変更を適用する
        self.__commit()

        return DatabaseRetCode.SUCCESS
    
    def insert_record(self, table_name: str, record_data_dict: Dict[str, Union[int, str]]) -> int:
        """レコードデータ挿入

        Args:
            table_name (str): テーブル名
            record_data_dict (Dict[str, Union[int, str]]): レコードデータ(辞書データ)

        Returns:
            int: データベースリターンコード
        """
        # 引数チェック
        if table_name == "":
            print("指定されたテーブル名が空のためエラー")
            return DatabaseRetCode.DB_TABLE_INSERT_RECORD_ERROR
        
        # 引数チェック
        if record_data_dict == {} or record_data_dict == None:
            print("指定されたレコードデータが空のためエラー")
            return DatabaseRetCode.DB_TABLE_INSERT_RECORD_ERROR

        # NOTE: テーブルへのレコードデータ挿入処理を記述する
        # クエリー作成用変数定義
        _column_names: str = ""
        _values: str = ""
        for column_name, value in record_data_dict.items():
            # カラム名をまとめた文字列を作成
            _column_names += f"{column_name},"

            ## カラムにいれるデータのタイプチェック
            # カラムに設定する値をまとめた文字列を作成
            if type(value) is str:
                # 値が文字列型(str型)の場合
                _values += f"'{value}',"
            
            else:
                # 値が数値型(int型)の場合
                _values += f"{value},"

        # 末尾のカンマは不要なため削除
        _column_names = _column_names.rstrip(',')
        _values = _values.rstrip(',')

        # 実行用sqlを生成
        _sql: str = f'INSERT INTO {table_name}({_column_names}) VALUES({_values})'
        # sql文を確認
        print(f"{_sql}")

        # sql文を実行
        self.__execute(_sql)
        # 変更を適用する
        self.__commit()

        return DatabaseRetCode.SUCCESS

    def update_record(self, table_name: str, id: int, update_record_data_dict: Dict[str, Union[int, str]]) -> int:
        """レコードデータ更新

        Args:
            table_name (str): テーブル名
            id (int): 更新対象のID
            update_record_data_dict (Dict[str, Union[int, str]]): レコード更新データ(辞書データ)

        Returns:
            int: データベースリターンコード
        """
        # 引数チェック
        if table_name == "":
            print("指定されたテーブル名が空のためエラー")
            return DatabaseRetCode.DB_TABLE_UPDATE_RECORD_ERROR
        
        # 引数チェック
        if id <= 0:
            print("指定されたIDが 0 以下のためエラー")
            return DatabaseRetCode.DB_TABLE_UPDATE_RECORD_ERROR
        
        # 引数チェック
        if update_record_data_dict == {} or update_record_data_dict == None:
            print("指定されたレコードデータが空のためエラー")
            return DatabaseRetCode.DB_TABLE_UPDATE_RECORD_ERROR

        # クエリー作成用変数定義
        _query: str = ""
        for column_name, value in update_record_data_dict.items():
            # カラム名をまとめるための文字列を作成
            _values: str = ""

            ## カラムにいれるデータのタイプチェック
            # カラムに設定する値をまとめた文字列を作成
            if type(value) is str:
                # 値が文字列型(str型)の場合
                _values = f'"{value}",'
            
            else:
                # 値が数値型(int型)の場合
                _values = f"{value},"

            _query += f"{column_name} = {_values},"

        # 末尾のカンマは不要なため削除
        _query = _query.rstrip(',')

        # 実行用sqlを生成
        _sql: str = f'UPDATE {table_name} SET {_query} WHERE ID = {id}'
        # sql文を確認
        print(f"{_sql}")

        # sql文を実行
        self.__execute(_sql)
        # 変更を適用する
        self.__commit()

        return DatabaseRetCode.SUCCESS

    def delete_record(self, table_name: str, id: int) -> int:
        """レコードデータ削除

        Args:
            table_name (str): テーブル名
            id (int): 削除対象のID

        Returns:
            int: データベースリターンコード
        """

        # 引数チェック
        if table_name == "":
            print("指定されたテーブル名が空のためエラー")
            return DatabaseRetCode.DB_TABLE_DELETE_RECORD_ERROR

        # 引数チェック
        if id <= 0:
            print("指定されたIDが 0 以下のためエラー")
            return DatabaseRetCode.DB_TABLE_DELETE_RECORD_ERROR

        _sql: str = f'DELETE FROM {table_name} WHERE ID = {id}'
        # sql文を確認
        print(f"{_sql}")

        # sql文を実行
        self.__execute(_sql)
        # 変更を適用する
        self.__commit()

        return DatabaseRetCode.SUCCESS

    def get_record_data_from_dict(self, table_name: str, req_data_dict: dict) -> Tuple[int, List[Tuple[Union[int, str]]]]:
        """レコードデータ取得
            NOTE: データベースリターンコードが「SUCCESS」の場合のみ、辞書データが設定される
                    ※データベースリターンコードが「SUCCESS」以外の場合、辞書データは空で応答する

        Args:
            table_name (str): テーブル名
            req_data_dict (dict): 取得要求辞書データ

        Returns:
            Tuple[int, List[Tuple[Union[int, str]]]]: データベースリターンコード, 応答リストデータ
        """
        # 引数チェック
        if table_name == "":
            print("指定されたテーブル名が空のためエラー")
            return DatabaseRetCode.DB_TABLE_FETCH_RECORD_ERROR, {}
        
         # クエリー作成用変数定義
        _query: str = ""
        
        # 複数条件判定用変数定義
        _is_multiple: bool = False
        
        # 要求データありの場合
        if not (req_data_dict == {} or req_data_dict == None):
            # SQLに取得条件を追加
            _query += " WHERE "
            for column_name, value in req_data_dict.items():
                # 複数条件判定
                if _is_multiple:
                    _query += " AND "

                # カラム名をまとめるための文字列を作成
                _values: str = ""

                ## カラムにいれるデータのタイプチェック
                if type(value) is str:
                    # 値が文字列型(str型)の場合
                    _values = f'"{value}"'
                
                else:
                    # 値が数値型(int型)の場合
                    _values = f"{value}"

                _query += f"{column_name} = {_values}"
                # 複数条件判定用フラグを立てる
                _is_multiple = True
        
        # 実行用sqlを生成
        _sql: str = f'SELECT * FROM {table_name}{_query}'
        # sql文を確認
        print(f"{_sql}")

        # sql文を実行
        self.__execute(_sql)

        # 応答生成
        rsp_list = self._cur.fetchall()
        print(f"{rsp_list}")
        
        return DatabaseRetCode.SUCCESS, rsp_list

    def disconnection(self) -> int:
        """データベース切断

        Returns:
            int: データベースリターンコード
        """
        # NOTE: データベース切断処理を記述する
        self._cur.close()
        self._conn.close()
        print("データベース切断完了")
        return DatabaseRetCode.SUCCESS