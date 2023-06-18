#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import annotations

### デバッグモード対応 ###
# NOTE: 不要になったら削除
DEBUG_MODE: bool = False
if DEBUG_MODE:  
    from typing import TYPE_CHECKING
    if TYPE_CHECKING:
        from typing import Dict, List, Optional, Tuple, Union

else:
    from typing import Dict, List, Optional, Tuple, Union


def check_arg_type(target: object, check_type: object) -> bool:
    """引数型チェック

    Args:
        target (object): チェック対象
        check_type (object): チェックする型

    Returns:
        bool: True=対象はチェックする型と等しい / False=対象とチェックする型は異なる
    """
    return isinstance(target, check_type)