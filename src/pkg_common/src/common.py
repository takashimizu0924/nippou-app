#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# アノテーション用パッケージ
from __future__ import annotations
from typing import (List, Tuple, Dict, Optional, Union)


def check_arg_type(target: object, check_type: object) -> bool:
    """引数型チェック

    Args:
        target (object): チェック対象
        check_type (object): チェックする型

    Returns:
        bool: True=対象はチェックする型と等しい / False=対象とチェックする型は異なる
    """
    ### 応答
    return isinstance(target, check_type)

def check_args_type(target_list: List[object], check_type: object) -> bool:
    """配列型の引数型チェック
        NOTE: チェックする引数が配列の場合はこちらのメソッドを利用する

    Args:
        target_list (List[object]): チェック対象リスト
        check_type (object): チェックする型

    Returns:
        bool: True=対象はチェックする型と等しい / False=対象とチェックする型は異なる
    """
    ### 対象引数リストのサイズチェック
    if len(target_list) <= 0:
        # チェック対象無し
        return False
    
    ### 引数型チェック
    for arg in target_list:
        if not isinstance(arg, check_type):
            return False

    ### 応答
    return True