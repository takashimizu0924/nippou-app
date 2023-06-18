#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    # パッケージ名
    name = "pkg_common",
    # バージョン番号
    version = "0.1.0",
    # 現在のディレクトリから自動的にパッケージを検索して返す関数
    # packages=['src'],
    # packages=find_packages(),
    packages=['pkg_common'],
    package_dir={'pkg_common':'src'}
)