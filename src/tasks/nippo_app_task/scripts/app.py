#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pkg_common.file_manager import FileManager
from pkg_common.log_manager import LogLevel, LogManager


def app() -> None:
    """日報管理アプリのエントリーポイント
    """
    ### ファイルマネージャ生成
    config_file_name: str = "global_setting.json"
    config_file_path: str = f'../../../../config/{config_file_name}'
    file_mng: FileManager = FileManager()
    ## 設定ファイル読み込み
    config_data: dict = file_mng.json_read(config_file_path)
    
    ### プロジェクト設定情報
    project_dir_path: str = config_data["PROJECT_DIR_PATH"]
    
    ### ログマネージャ生成
    log_config: dict = config_data["LOG"]
    log_file_path = f'{project_dir_path}{log_config["SAVE_PATH"]}{log_config["SAVE_FILE_NAME"]}'
    log = LogManager(log_file_path)

    log.debug("日報管理アプリ開始")
    log.debug(f'Load config data. config file name={config_file_name}, config data={config_data}')

### アプリケーション実行(GUI起動)
if __name__ == '__main__':
    app()
    
