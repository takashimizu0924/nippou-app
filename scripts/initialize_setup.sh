#!/usr/bin/env bash

### シェルスクリプトのエントリー
# スクリプト用変数定義
START_COMMENT="INITIALIZING START"
OK_COMMENT="\e[34;1mOK\e[m"
NG_COMMENT="\e[31;1mNG\e[m"

echo -e "\e[44;1m -----${START_COMMENT}----- \e[m"


### ビルド前にコマンド存在チェック
# スクリプト内で利用するコマンド名配列を定義
COMMAND_NAME_LIST[0]="python3"
COMMAND_NAME_LIST[1]="pip"

# コマンドチェック実行
for command in ${COMMAND_NAME_LIST[@]}
    do
        # コマンド存在チェック実行
        if type ${command} > /dev/null 2>&1; then
            echo -e "[\e[33;1mCOMMAND-EXISTS-CHECKING\e[m]:----->[${OK_COMMENT}]----------'${command}'"
        else
            echo -e "[\e[33;1mCOMMAND-EXISTS-CHECKING\e[m]:----->[${NG_COMMENT}]----------'${command}'"
            exit -1
        fi
    done


### ビルド前にインストール済みPythonパッケージの存在チェック
# Pythonパッケージ存在チェックで利用する変数定義
IS_NOT_EXISTS=false
# スクリプト内で利用するPythonパッケージ確認コマンド配列を定義
PIP_PKG_NAME_LIST[0]="sdist "
PIP_PKG_NAME_LIST[1]="pandas "

# コマンドチェック実行
for package in ${PIP_PKG_NAME_LIST[@]}
    do
        # コマンド存在チェック実行
        if pip show ${package} > /dev/null 2>&1; then
            echo -e "[\e[33;1mPIP-PACKAGE-EXISTS-CHECKING\e[m]:->[${OK_COMMENT}]----------'${package}'" 
        else
            echo -e "[\e[33;1mPIP-PACKAGE-EXISTS-CHECKING\e[m]:->[${NG_COMMENT}]----------'${package}'"
            exit -1
        fi
    done


### 作業ディレクトリへ移動
cd ../src/


### ビルド対象のパッケージ配列作成
# 追加するパッケージがあれば以下に追加
PYTHON_PKG_NAME_LIST[0]="pkg_common"
PYTHON_PKG_NAME_LIST[1]="pkg_db"
PYTHON_PKG_NAME_LIST[2]="pkg_window_widgets"


### Pythonのsetup.pyを呼び出し各パッケージのビルド
for PKG in ${PYTHON_PKG_NAME_LIST[@]}
    do
        # cd ${PKG} && python3 setup.py sdist
        echo ${PKG}
    done