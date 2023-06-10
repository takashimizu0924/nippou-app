#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app_gui_manager import (GuiManager)


def app() -> None:
    """日報管理アプリのエントリーポイント
    """
    GuiManager()

### アプリケーション実行(GUI起動)
if __name__ == '__manin__':
    app()