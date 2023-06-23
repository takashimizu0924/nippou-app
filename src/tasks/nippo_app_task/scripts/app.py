#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pkg_common.file_manager import FileManager
from pkg_common.log_manager import LogLevel, LogManager


def app() -> None:
    """日報管理アプリのエントリーポイント
    """
    log = LogManager()
    log.error("日報管理アプリ開始")
    

### アプリケーション実行(GUI起動)
if __name__ == '__main__':
    app()
    
