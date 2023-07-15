""" 入力画面 """
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# アノテーション用パッケージ
from __future__ import annotations
from typing import (List, Tuple, Dict, Optional, Union)
from pkg_window.page import Page

class Input(Page):
    """入力画面クラス
        NOTE: 入力クラスが実装すべき基底ページクラスを継承
    """
    def __init__(self, page_name_tag: str) -> None:
        super().__init__(page_name_tag)
