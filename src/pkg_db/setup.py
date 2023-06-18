#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    # パッケージ名
    name = "pkg_db",
    # バージョン番号
    version = "0.1.0",
    # パッケージ情報作成
    packages=['pkg_db'],
    # パッケージ対象のディレクトリ指定
    package_dir={'pkg_db':'src'}
)