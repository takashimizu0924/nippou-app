#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    # パッケージ名
    name = "pkg_common",
    # バージョン番号
    version = "0.1",
    # 現在のディレクトリから自動的にパッケージを検索して返す関数
    packages = find_packages()
)