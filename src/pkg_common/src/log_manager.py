""" ログ管理 """
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
from dataclasses import dataclass
from pkg_common.file_manager import FileManager

@dataclass
class LogLevel:
    """ログレベルデータ型クラス
    """
    # NOTE:ロガーに設定したロギングレベルより以下のログは出力されない
    notset: str     = logging.NOTSET
    debug: str      = logging.DEBUG
    info: str       = logging.INFO
    warning: str    = logging.WARNING
    error: str      = logging.ERROR
    critical: str   = logging.CRITICAL

class LogManager:
    """ログデータ制御クラス
    """
    def __init__(self, save_path: str = '', level: LogLevel = LogLevel.debug) -> None:
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
            _save_path = f'{project_dir_path}{log_config["SAVE_PATH"]}\
                {log_config["SAVE_FILE_NAME"]}'

        # ロガーの名前設定
        self.logger = logging.getLogger("nippou_app")
        self.logger.setLevel(level)
        file_handler = self._create_file_handler(_save_path, level)
        console_handler = self._create_console_handler(level)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def _create_file_handler(self, save_path:str, level:LogLevel) -> logging.FileHandler:
        """ファイルハンドラーをロギングインスタンスに設定

        Args:
            logfile_name (str): 出力するファイル名
            level (LogLevel): ログレベル
        """
        file_handler = logging.FileHandler(save_path)
        # ログレベルの設定
        file_handler.setLevel(level)
        # フォーマッタの定義
        fh_fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", \
            "%Y-%m-%d %T%H:%M:%S")
        file_handler.setFormatter(fh_fmt)
        # # フォーマッタをハンドラに紐づける
        self.logger.addHandler(file_handler)
        return file_handler

    def _create_console_handler(self, level:LogLevel) -> logging.StreamHandler:
        """コンソールハンドラーをロギングインスタンスに設定

        Args:
            level (LogLevel): ログレベル
        """
        # コンソールに標準出力設定
        console_handler = logging.StreamHandler()
        # ログレベルの設定
        console_handler.setLevel(level)
        # フォーマッタの定義
        ch_fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", \
            "%Y-%m-%d %T%H:%M:%S")
        console_handler.setFormatter(ch_fmt)
        # # フォーマッタをハンドラに紐づける
        self.logger.addHandler(console_handler)
        return console_handler

    def debug(self, text: str) -> None:
        """debugレベルのログ出力

        Args:
            text (str): 出力するログテキスト
        """
        self.logger.debug(text)

    def info(self, text: str) -> None:
        """infoレベルのログ出力

        Args:
            text (str): 出力するログテキスト
        """
        self.logger.info(text)

    def warning(self, text: str) -> None:
        """warningレベルのログ出力

        Args:
            text (str): 出力するログテキスト
        """
        self.logger.warning(text)

    def error(self, text: str) -> None:
        """errorレベルのログ出力

        Args:
            text (str): 出力するログテキスト
        """
        self.logger.error(text)

    def critical(self, text: str) -> None:
        """criticalレベルのログ出力

        Args:
            text (str): 出力するログテキスト
        """
        self.logger.critical(text)
