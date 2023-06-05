#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# アノテーション用パッケージ
from __future__ import annotations
from typing import TYPE_CHECKING
from typing import (List, Tuple, Dict, Optional, Union)

# データベース制御パッケージ
if TYPE_CHECKING:
    from database_ctrl import (TableDataType, DatabaseRetCode, DatabaseControl)

class AppDataControl:
    """アプリケーションデータ制御クラス
        NOTE: アプリ特有のデータをデータベースと連携する機能を提供する
    """
    def __init__(self) -> None:
        """コンストラクタ
            NOTE: データベースの初期化処理を行う
        """
        pass

    def register(self, req: DataRegistReq) -> bool:
        """データ登録

        Args:
            req (DataRegistReq): データ登録制御要求

        Returns:
            bool: 結果応答 (True: 成功 / False: 失敗)
        """
        pass

    def update(self, req: DataUpdateReq) -> bool:
        """データ更新

        Args:
            req (DataUpdateReq): データ更新制御要求

        Returns:
            bool: 結果応答 (True: 成功 / False: 失敗)
        """
        pass

    def delete(self, req: DataDeleteReq) -> bool:
        """データ削除

        Args:
            req (DataDeleteReq): データ削除制御要求

        Returns:
            bool: 結果応答 (True: 成功 / False: 失敗)
        """
        pass

    def fetch(self, req: DataFetchReq) -> DataFetchRsp:
        """データ取得

        Args:
            req (DataFetchReq): データ取得制御要求

        Returns:
            DataFetchRsp: データ取得応答
        """
        pass


class DbConfigData:
    """データベース設定用データ
    """
    def __init__(self) -> None:
        """コンストラクタ
            NOTE: 引数説明
            - column_work_date      : 工事日情報 NOTE:(YYYY/MM/DDの形式) ※文字列
            - column_company_name   : 会社名情報 ※文字列
            - column_work_place     : 現場名情報 ※文字列
            - column_work_contents  : 作業内容情報 ※文字列
            - column_worker_num     : 作業員数情報 ※数値
            - column_worker_cost    : 作業員代情報 ※数値
            - column_material_cost  : 材料費情報 ※数値
            - column_proceeds       : 売上金額情報 ※数値
        """
        self.column_work_date: Dict[str,TableDataType]      = {"WORK_DATE": TableDataType.STR}
        self.column_company_name: Dict[str,TableDataType]   = {"COMPANY_NAME": TableDataType.STR}
        self.column_work_place: Dict[str,TableDataType]     = {"WORK_PLACE": TableDataType.STR}
        self.column_work_contents: Dict[str,TableDataType]  = {"WORK_CONTENTS": TableDataType.STR}
        self.column_worker_num: Dict[str,TableDataType]     = {"WORKER_NUM": TableDataType.INT}
        self.column_worker_cost: Dict[str,TableDataType]    = {"WORKER_COST": TableDataType.INT}
        self.column_material_cost: Dict[str,TableDataType]  = {"MATERIAL_COST": TableDataType.INT}
        self.column_proceeds: Dict[str,TableDataType]       = {"PROCEEDS": TableDataType.INT}

class DataRegistReq:
    """データ登録制御 要求クラス
    """
    def __init__(self) -> None:
        """コンストラクタ
            NOTE: 引数説明
            - XXX: ～～データ
        """
        pass

class DataUpdateReq:
    """データ更新制御 要求クラス
    """
    def __init__(self) -> None:
        """コンストラクタ
            NOTE: 引数説明
            - XXX: ～～データ
        """
        pass

class DataDeleteReq:
    """データ削除制御 要求クラス
    """
    def __init__(self) -> None:
        """コンストラクタ
            NOTE: 引数説明
            - XXX: ～～データ
        """
        pass

class DataFetchReq:
    """データ取得制御 要求クラス
    """
    def __init__(self) -> None:
        """コンストラクタ
            NOTE: 引数説明
            - XXX: ～～データ
        """
        pass

class DataFetchRsp:
    """データ取得制御 応答クラス
    """
    def __init__(self) -> None:
        """コンストラクタ
            NOTE: 引数説明
            - XXX: ～～データ
        """
        pass