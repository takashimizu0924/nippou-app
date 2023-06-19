#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pkg_common.file_manager import FileManager
from pkg_common.log_manager import LogLevel, LogManager

file_name = "app.log"
file_path = f'../../../../log/{file_name}'
log = LogManager(file_path)
log.debug("this is test3")

def app() -> None:
    """日報管理アプリのエントリーポイント
    """
    # FileManager()
    # log = LogManager()
    # log.debug("this is test3")
    log.debug("日報管理アプリ開始")

### アプリケーション実行(GUI起動)
if __name__ == '__main__':
    print('Test1')
    app()
    
