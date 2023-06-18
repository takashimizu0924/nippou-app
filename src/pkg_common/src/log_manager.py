#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
# from file_manager import read

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

class LogControl:
    """ログデータ制御クラス
    """
    def __init__(self, save_file_name: str = '', level = LogLevel.WARNING) -> None:
        """コンストラクタ
        """
        # ログファイル名
        self._FILE_NAME: str   = "sample.log"
        # ロガーの名前設定
        self.logger = logging.getLogger(__name__)
        self.__file_handler(save_file_name, level)
        self.__console_handler(level)
    
    def __file_handler(self, logfile_name:str, level:LogLevel) -> None:
        """ファイルハンドラーをロギングインスタンスに設定

        Args:
            logfile_name (str): 出力するファイル名
            level (LogLevel): ログレベル
        """
        _logfile_name = logfile_name
        if _logfile_name == '':
           _logfile_name = self._FILE_NAME

        fh = logging.FileHandler(_logfile_name)
        # ログレベルの設定
        fh.setLevel(level)
        # フォーマッタの定義
        fh_fmt = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", "%Y-%m-%d %T%H:%M:%S")
        fh.setFormatter(fh_fmt)
        # フォーマッタをハンドラに紐づける
        self.logger.addHandler(fh)
        return
    
    def __console_handler(self, level:LogLevel) -> None:
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
        # フォーマッタをハンドラに紐づける
        self.logger.addHandler(ch)
        return
    
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


if __name__ == '__main__':
    # お試しの場合はここに追加
    log_ctrl = LogControl()

    #log出力のテスト
    log_ctrl.debug("this is test3")