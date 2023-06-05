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
        # データベース作成 (※NOTE:既にDBが存在する場合は接続)
        _database_name: str = "nippo_app"
        self._db_ctrl = DatabaseControl(_database_name)

        # テーブル名を生成＆アプリ設定情報インスタンス生成
        self.db_table_name: str = "nippo"
        app_config: AppConfig = AppConfig()
        try:
            # テーブル作成
            ret = self._db_ctrl.create_table(self.db_table_name, app_config.db_table_data_dict)
            print(f"create_table ret = {ret}")
            # 戻り値チェック
            if not ret == DatabaseRetCode.SUCCESS:
                raise Exception()
            
        except Exception:
            # DB切断して呼び出し元にエラーを通知 NOTE: 不要なら削除する
            self._db_ctrl.disconnection()
            raise Exception("__init__:[AppDataControl Class]-> Error occured. Create database table error.")

    def register(self, req: DataRegistReq) -> bool:
        """データ登録

        Args:
            req (DataRegistReq): データ登録制御要求

        Returns:
            bool: 結果応答 (True: 成功 / False: 失敗)
        """
        ## 応答生成
        _rsp: bool = False
        
        ## 引数チェック
        if req is None:
            # エラー応答
            print(f"register:[AppDataControl Class]-> Error occured. Request parameter is none.")
            return _rsp
        
        ## 要求生成
        _req: dict = {
            "WORK_DATE": req.work_date,
            "COMPANY_NAME": req.company_name,
            "WORK_PLACE": req.work_place,
            "WORK_CONTENTS": req.work_contents,
            "WORKER_NUM": req.worker_num,
            "WORKER_COST": req.worker_cost,
            "MATERIAL_COST": req.material_cost,
            "PROCEEDS": req.proceeds,
        }

        ## データ登録実行
        ret: int = self._db_ctrl.insert_recoed(self.db_table_name, _req)

        # 戻り値チェック
        if not ret == DatabaseRetCode.SUCCESS:
            print(f"register:[AppDataControl Class]-> Error occured. Request parameter is none.")
            return _rsp
        
        # 応答設定(正常)
        _rsp = True
        return _rsp

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


class AppConfig:
    """アプリ用設定データクラス
    """
    def __init__(self) -> None:
        """コンストラクタ
            NOTE: 引数説明
            - db_table_data_dict    : データベース設定用辞書データ NOTE:カラム情報
        """
        self.db_table_data_dict: Dict[str, TableDataType] = {
            "ID": (f"{TableDataType.INT} {TableDataType.PRIMARY_KEY} {TableDataType.AUTO_INC}"),
            "WORK_DATE": TableDataType.STR,
            "COMPANY_NAME": TableDataType.STR,
            "WORK_PLACE": TableDataType.STR,
            "WORK_CONTENTS": TableDataType.STR,
            "WORKER_NUM": TableDataType.INT,
            "WORKER_COST": TableDataType.INT,
            "MATERIAL_COST": TableDataType.INT,
            "PROCEEDS": TableDataType.INT,
        }

class DataRegistReq:
    """データ登録制御 要求クラス
    """
    def __init__(self) -> None:
        """コンストラクタ
            NOTE: 引数説明
            - work_date     : 工事日データ NOTE:(YYYY/MM/DDの形式) 
            - company_name  : 会社名データ
            - work_place    : 現場名データ
            - work_contents : 作業内容データ
            - worker_num    : 作業員数データ
            - worker_cost   : 作業員代データ
            - material_cost : 材料費データ
            - proceeds      : 売上金額データ
        """
        self.work_date: str     = ""
        self.company_name: str  = ""
        self.work_place: str    = ""
        self.work_contents: str = ""
        self.worker_num: int    = 0
        self.worker_cost: int   = 0
        self.material_cost: int = 0
        self.proceeds: int      = 0

class DataUpdateReq:
    """データ更新制御 要求クラス
    """
    def __init__(self) -> None:
        """コンストラクタ
            NOTE: 引数説明
            - target_id     : 更新対象IDデータ
            - update_data   : 更新データ ※NOTE: キーは必ず更新対象のカラム名を指定すること
        """
        self.target_id: int                             = 0
        self.update_data: Dict[str, Union[int, str]]    = {}

class DataDeleteReq:
    """データ削除制御 要求クラス
    """
    def __init__(self) -> None:
        """コンストラクタ
            NOTE: 引数説明
            - target_id: 削除対象IDデータ
        """
        self.target_id: int = 0

class DataFetchReq:
    """データ取得制御 要求クラス
    """
    def __init__(self) -> None:
        """コンストラクタ
            NOTE: 引数説明
            - company_name: 会社名データ
        """
        self.company_name: str = ""

class DataFetchRsp:
    """データ取得制御 応答クラス
    """
    def __init__(self) -> None:
        """コンストラクタ
            NOTE: 引数説明
            - id            : IDデータ
            - work_date     : 工事日データ NOTE:(YYYY/MM/DDの形式) 
            - company_name  : 会社名データ
            - work_place    : 現場名データ
            - work_contents : 作業内容データ
            - worker_num    : 作業員数データ
            - worker_cost   : 作業員代データ
            - material_cost : 材料費データ
            - proceeds      : 売上金額データ
        """
        self.id: int            = ""
        self.work_date: str     = ""
        self.company_name: str  = ""
        self.work_place: str    = ""
        self.work_contents: str = ""
        self.worker_num: int    = 0
        self.worker_cost: int   = 0
        self.material_cost: int = 0
        self.proceeds: int      = 0