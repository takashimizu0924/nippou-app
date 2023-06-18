#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pkg_common.file_manager import FileManager
from pkg_common.log_manager import LogLevel, LogControl

log = LogControl()
log.debug("this is test3")

def app() -> None:
    """日報管理アプリのエントリーポイント
    """
    # FileManager()
    # log = LogControl()
    # log.debug("this is test3")
    pass

### アプリケーション実行(GUI起動)
if __name__ == '__main__':
    print('Test1')
    app()
    
