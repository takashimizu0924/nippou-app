#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    # パッケージ名
    name = "pkg_window",
    # バージョン番号
    version = "0.1.0",
    # パッケージ情報作成
    packages=['pkg_window'],
    # パッケージ対象のディレクトリ指定
    package_dir={'pkg_window':'src'}
)