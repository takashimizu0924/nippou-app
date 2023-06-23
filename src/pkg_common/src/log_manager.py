#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from pkg_common.file_manager import FileManager

class LogLevel:
    """ログレベルデータ型クラス
    """
    # NOTE:ロガーに設定したロギングレベルより以下のログは出力されない
    NOTSET: str     = logging.NOTSET
    DEBUG: str      = logging.DEBUG
    INFO: str       = logging.INFO
    WARNING: str    = logging.WARNING
    ERROR: str      = logging.ERROR
    CRITICAL: str   = logging.CRITICAL

class LogManager:
    """ログデータ制御クラス
    """
    def __init__(self, save_path: str = '', level: LogLevel = LogLevel.DEBUG) -> None:
        """コンストラクタ

        Args:
            save_path (str, optional): 保存先パス. Defaults to ''.
            level (LogLevel, optional): ログレベル. Defaults to LogLevel.WARNING.
        """
        _save_path: str = save_path
        # 引数チェック
        if _save_path == '':
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
            _save_path = f'{project_dir_path}{log_config["SAVE_PATH"]}{log_config["SAVE_FILE_NAME"]}'

        # ロガーの名前設定
        self.logger = logging.getLogger("nippou_app")
        self.logger.setLevel(level)
        fh = self._file_handler(_save_path, level)
        ch = self._console_handler(level)

        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    
    def _file_handler(self, save_path:str, level:LogLevel) -> logging.FileHandler:
        """ファイルハンドラーをロギングインスタンスに設定

        Args:
            logfile_name (str): 出力するファイル名
            level (LogLevel): ログレベル
        """
        fh = logging.FileHandler(save_path)
        # ログレベルの設定
        fh.setLevel(level)
        # フォーマッタの定義
        fh_fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", "%Y-%m-%d %T%H:%M:%S")
        fh.setFormatter(fh_fmt)
        # # フォーマッタをハンドラに紐づける
        self.logger.addHandler(fh)
        return fh
    
    def _console_handler(self, level:LogLevel) -> logging.StreamHandler:
        """コンソールハンドラーをロギングインスタンスに設定

        Args:
            level (LogLevel): ログレベル
        """
        # コンソールに標準出力設定
        ch = logging.StreamHandler()
        # ログレベルの設定
        ch.setLevel(level)
        # フォーマッタの定義
        ch_fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", "%Y-%m-%d %T%H:%M:%S")
        ch.setFormatter(ch_fmt)
        # # フォーマッタをハンドラに紐づける
        self.logger.addHandler(ch)
        return ch
    
    def debug(self, text: str) -> None:
        """debugレベルのログ出力

        Args:
            text (str): 出力するログテキスト
        """
        self.logger.debug(text)
        return
    
    def info(self, text: str) -> None:
        """infoレベルのログ出力

        Args:
            text (str): 出力するログテキスト
        """
        self.logger.info(text)
        return
    
    def warning(self, text: str) -> None:
        """warningレベルのログ出力

        Args:
            text (str): 出力するログテキスト
        """
        self.logger.warning(text)
        return

    def error(self, text: str) -> None:
        """errorレベルのログ出力

        Args:
            text (str): 出力するログテキスト
        """
        self.logger.error(text)
        return
    
    def critical(self, text: str) -> None:
        """criticalレベルのログ出力

        Args:
            text (str): 出力するログテキスト
        """
        self.logger.critical(text)
        return


# if __name__ == '__main__':
#     # お試しの場合はここに追加
#     log_ctrl = LogManager()

#     #log出力のテスト
#     log_ctrl.debug("this is test3")