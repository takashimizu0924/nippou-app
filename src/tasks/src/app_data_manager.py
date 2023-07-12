""" アプリケーションデータ管理 """
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# アノテーション用パッケージ
from __future__ import annotations
from typing import (List, Dict, Union)
from dataclasses import dataclass
from pkg_common.log_manager import LogManager
# データベース制御パッケージ
from pkg_db.database import (TableDataType, DatabaseRetCode, Database)

class DataManager:
    """アプリケーションデータ制御クラス
        NOTE: アプリ特有のデータをデータベースと連携する機能を提供する
    """
    def __init__(self) -> None:
        """コンストラクタ
            NOTE: データベースの初期化処理を行う
        """
        # ログマネージャ生成
        self.log: LogManager = LogManager(save_path='')
        # データベース作成 (※NOTE:既にDBが存在する場合は接続)
        _database_name: str = "nippo_app"
        self._db_ctrl = Database(_database_name)

        # テーブル名を生成＆アプリ設定情報インスタンス生成
        self.db_table_name: str = "nippo"
        app_config: AppConfig = AppConfig()
        try:
            # テーブル作成
            ret = self._db_ctrl.create_table(self.db_table_name, app_config.db_table_data_dict)
            print(f"create_table ret = {ret}")
            # 戻り値チェック
            if not ret == DatabaseRetCode.SUCCESS:
                raise ValueError('[DataManager:__init__] -> target tabel is already exists. \
                    prosessing is SUCCESS.')

        except ValueError as error_msg:
            # 既に作成されているテーブルを指定した場合はSUCCESSを表示
            self.log.info(f'{error_msg}')

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
            self.log.error('[DataManager:register] -> Error occured. Request parameter is none.')
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
        ret: int = self._db_ctrl.insert_record(self.db_table_name, _req)

        # 戻り値チェック
        if not ret == DatabaseRetCode.SUCCESS:
            self.log.error('[DataManager:register] -> Error occured. Register data failed.')
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
        ## 応答生成
        _rsp: bool = False

        ## 引数チェック
        if req is None:
            # エラー応答
            self.log.error('[DataManager:update] -> Error occured. Request parameter is none.')
            return _rsp

        ## データ登録実行
        ret: int = self._db_ctrl.update_record(self.db_table_name, req.target_id, req.update_data)

        # 戻り値チェック
        if not ret == DatabaseRetCode.SUCCESS:
            self.log.error('[DataManager:update] -> Error occured. Update data failed.')
            return _rsp

        # 応答設定(正常)
        _rsp = True
        return _rsp

    def delete(self, req: DataDeleteReq) -> bool:
        """データ削除

        Args:
            req (DataDeleteReq): データ削除制御要求

        Returns:
            bool: 結果応答 (True: 成功 / False: 失敗)
        """
        ## 応答生成
        _rsp: bool = False

        ## 引数チェック
        if req is None:
            # エラー応答
            self.log.error('[DataManager:delete] -> Error occured. Request parameter is none.')
            return _rsp

        ## データ登録実行
        ret: int = self._db_ctrl.delete_record(self.db_table_name, req.target_id)

        # 戻り値チェック
        if not ret == DatabaseRetCode.SUCCESS:
            self.log.error('[DataManager:delete] -> Error occured. Delete data failed.')
            return _rsp

        # 応答設定(正常)
        _rsp = True
        return _rsp

    def fetch(self, req: DataFetchReq) -> List[DataFetchRsp]:
        """データ取得
            NOTE: DBでエラーが発生した場合は呼び出し元にNoneを応答する

        Args:
            req (DataFetchReq): データ取得制御要求

        Returns:
            List[DataFetchRsp]: データ取得応答リスト
        """
        ## 応答用配列生成
        _rsp_list: List[DataFetchRsp] = []

        ## 引数チェック
        if req is None:
            # エラー応答
            self.log.error('[DataManager:fetch] -> Error occured. Request parameter is none.')
            return _rsp_list

        ## 要求辞書データ作成
        _req: dict = {}
        if 0 < req.target_id:
            _req = {
                "target_id": req.target_id,
                "COMPANY_NAME": req.company_name
            }
        elif req.target_id == 0:
            _req = {
                "COMPANY_NAME": req.company_name
            }

        ## データ登録実行
        ret_code, ret_data = self._db_ctrl.get_record_data_from_dict(self.db_table_name, _req)

        # 戻り値チェック
        if not ret_code == DatabaseRetCode.SUCCESS:
            self.log.error('[DataManager:fetch] -> Error occured. Fetch data failed.')
            return _rsp_list

        # 応答解析
        for _fetch_data in ret_data:
            # 応答生成
            _rsp: DataFetchRsp = DataFetchRsp()
            # 応答データ設定
            _rsp.target_id          = _fetch_data[0]
            _rsp.work_date          = _fetch_data[1]
            _rsp.company_name       = _fetch_data[2]
            _rsp.work_place         = _fetch_data[3]
            _rsp.work_contents      = _fetch_data[4]
            _rsp.worker_num         = _fetch_data[5]
            _rsp.worker_cost        = _fetch_data[6]
            _rsp.material_cost      = _fetch_data[7]
            _rsp.proceeds           = _fetch_data[8]
            # 応答用配列に追加
            _rsp_list.append(_rsp)

        return _rsp_list

    def terminate(self) -> None:
        """終了処理
        """
        self._db_ctrl.disconnection()
        return


@dataclass
class AppConfig:
    """アプリ用設定データクラス
        NOTE: 引数説明
        - db_table_data_dict    : データベース設定用辞書データ NOTE:カラム情報
    """
    db_table_data_dict: Dict[str, TableDataType] = {
        "target_id": (f"{TableDataType.INT} {TableDataType.PRIMARY_KEY} {TableDataType.AUTO_INC}"),
        "WORK_DATE": TableDataType.STR,
        "COMPANY_NAME": TableDataType.STR,
        "WORK_PLACE": TableDataType.STR,
        "WORK_CONTENTS": TableDataType.STR,
        "WORKER_NUM": TableDataType.INT,
        "WORKER_COST": TableDataType.INT,
        "MATERIAL_COST": TableDataType.INT,
        "PROCEEDS": TableDataType.INT,
    }

@dataclass
class DataRegistReq:
    """データ登録制御 要求クラス
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
    work_date: str     = ""
    company_name: str  = ""
    work_place: str    = ""
    work_contents: str = ""
    worker_num: int    = 0
    worker_cost: int   = 0
    material_cost: int = 0
    proceeds: int      = 0

@dataclass
class DataUpdateReq:
    """データ更新制御 要求クラス
        NOTE: 引数説明
        - target_id     : 更新対象IDデータ
        - update_data   : 更新データ ※NOTE: キーは必ず更新対象のカラム名を指定すること
    """
    target_id: int                          = 0
    update_data: Dict[str, Union[int, str]] = {}

@dataclass
class DataDeleteReq:
    """データ削除制御 要求クラス
        NOTE: 引数説明
        - target_id: 削除対象IDデータ
    """
    target_id: int = 0

@dataclass
class DataFetchReq:
    """データ取得制御 要求クラス
        NOTE: 引数説明
        - target_id            : IDデータ
        - company_name  : 会社名データ
    """
    target_id: int      = 0
    company_name: str   = ""

@dataclass
class DataFetchRsp:
    """データ取得制御 応答クラス
        NOTE: 引数説明
        - target_id            : IDデータ
        - work_date     : 工事日データ NOTE:(YYYY/MM/DDの形式) 
        - company_name  : 会社名データ
        - work_place    : 現場名データ
        - work_contents : 作業内容データ
        - worker_num    : 作業員数データ
        - worker_cost   : 作業員代データ
        - material_cost : 材料費データ
        - proceeds      : 売上金額データ
    """
    target_id: int      = 0
    work_date: str      = ""
    company_name: str   = ""
    work_place: str     = ""
    work_contents: str  = ""
    worker_num: int     = 0
    worker_cost: int    = 0
    material_cost: int  = 0
    proceeds: int       = 0
