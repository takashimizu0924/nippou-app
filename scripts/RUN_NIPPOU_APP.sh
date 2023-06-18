#!/usr/bin/env bash

### 実行ディレクトリパス取得
DIR=`dirname ${0}`
cd ${DIR}

### Pythonパッケージをビルド＆インストールする
source ./INITIALIZE_SETUP.sh

### 共通環境変数のロード
source ../utility/use_common.env

### 対象のアプリケーションを起動
echo -e "\n\n\n"
echo -e "\e[32;1m----- アプリケーション開始 -----\e[m"

# アプリケーションディレクトリへ移動＆アプリ起動
cd ../src${APP_TASK_ROOT_DIR}${APP_PATH}
python3 -B ${APP_FILE_NAME}

### アプリケーション終了表示
echo ""
echo -e "\e[32;1m----- アプリケーション終了 -----\e[m"