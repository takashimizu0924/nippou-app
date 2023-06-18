#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pkg_common.file_manager import FileManager


def app() -> None:
    """日報管理アプリのエントリーポイント
    """
    FileManager()
    print('Test1')

### アプリケーション実行(GUI起動)
if __name__ == '__manin__':
    app()
    print('Test2')