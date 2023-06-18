#!/usr/bin/env bash

### シェルスクリプトのエントリー
# スクリプト用変数定義
START_COMMENT="INITIALIZING START"
END_COMMENT="INITIALIZING FINISHED"
OK_COMMENT="\e[34;42;1m OK \e[m"
NG_COMMENT="\e[37;41;1m NG \e[m"
SUCCESS_COMMENT="\e[32;44;1m SUCCESS \e[m"
FAILED_COMMENT="\e[33;41;1m FAILED \e[m"
echo ""
echo -e "\e[30;47;1m ----------------------------------------------------------- \e[m"
echo -e "\e[30;47;1m -------------------- ${START_COMMENT} ------------------- \e[m"
echo -e "\e[30;47;1m ----------------------------------------------------------- \e[m"

### 処理開始時刻表示
START_TIME=`date "+%Y/%m/%d %H:%M:%S"`
echo "Finished time--------------> [${START_TIME}]"
echo ""

### ビルド前にコマンド存在チェック
# スクリプト内で利用するコマンド名配列を定義
COMMAND_NAME_LIST[0]="python3"
COMMAND_NAME_LIST[1]="pip3"

# コマンドチェック実行
for command in ${COMMAND_NAME_LIST[@]}
    do
        # コマンド存在チェック実行
        if type ${command} > /dev/null 2>&1; then
            echo -e "[\e[33;1mCOMMAND-EXISTS-CHECKING\e[m]:---------->[${OK_COMMENT}]----------'${command}'"
        else
            echo -e "[\e[33;1mCOMMAND-EXISTS-CHECKING\e[m]:---------->[${NG_COMMENT}]----------'${command}'"
            echo -e "\e[31;1m'${command}' command is not found. Please 'sudo apt install ${command}', and retry.\e[m"
            exit -1
        fi
    done


### ビルド前にインストール済みPythonパッケージの存在チェック
# Pythonパッケージ存在チェックで利用する変数定義
IS_NOT_EXISTS=false
# スクリプト内で利用するPythonパッケージ確認コマンド配列を定義
PIP_PKG_NAME_LIST[0]="sdist "

# パッケージチェック実行
for package in ${PIP_PKG_NAME_LIST[@]}
    do
        # パッケージ存在チェック実行
        if pip show ${package} > /dev/null 2>&1; then
            echo -e "[\e[33;1mPIP-PACKAGE-EXISTS-CHECKING\e[m]:------>[${OK_COMMENT}]----------'${package}'" 
        else
            echo -e "[\e[33;1mPIP-PACKAGE-EXISTS-CHECKING\e[m]:------>[${NG_COMMENT}]----------'${package}'"
            IS_NOT_EXISTS=true
        fi

        if ${IS_NOT_EXISTS}; then
            # パッケージが存在しなければインストール
            pip install ${package}
            echo ""
            echo "[\e[37;44m----- Installed '${package}' -----\e[m"
            echo ""
        fi

    done


### 作業ディレクトリへ移動
cd ../src/

### ビルド対象のパッケージ配列作成
# 利用する変数定義
FILE_PATH="./dist/*"
FILE_NAME=""
# 追加するパッケージがあれば以下に追加
PYTHON_PKG_NAME_LIST[0]="pkg_common"
PYTHON_PKG_NAME_LIST[1]="pkg_db"
PYTHON_PKG_NAME_LIST[2]="pkg_window_widgets"
PYTHON_PKG_NAME_LIST[3]="tasks"

### Pythonのsetup.pyを呼び出し各パッケージのビルド＆インストール
for PKG in ${PYTHON_PKG_NAME_LIST[@]}
    do
        if ! [ -d ${PKG} ]; then
            # ビルド対象のパッケージディレクトリが存在しない場合はエラー表示して処理スキップ
            echo -e "\e[31;1mDirectory does not exists.\e[m Directory name: ['\e[30;47;1m ./${PKG} \e[m']"
            continue
        fi

        # パッケージディレクトリへ移動
        cd ${PKG}

        ## パッケージのビルド
        python3 setup.py sdist
        if [ $? -eq 0 ]; then
            echo -e "\e[33;1mBuilding ['${PKG}'] is\e[m ${SUCCESS_COMMENT}"
        else
            echo -e "\e[31;1mBuilding ['${PKG}'] is\e[m ${FAILED_COMMENT}"
            echo -e "\e[33;1mPlease check if thre are any errors in the './${PKG}/setup.py' file.\e[m"
            continue
        fi

        if ! [ -f ${FILE_PATH} ]; then
            # インストール対象のファイルがない場合はエラー表示して処理スキップ
            echo -e "\e[31;1mFile does not exists.\e[m File name: ['\e[30;47;1m ${FILE_PATH} \e[m']"
            continue
        fi

        ## パッケージのインストール
        pip3 install ${FILE_PATH}
        if [ $? -eq 0 ]; then
            echo -e "\e[33;1mInstall ['${PKG}'] is\e[m ${SUCCESS_COMMENT}"

        else
            echo -e "\e[31;1mInstall ['${PKG}'] is\e[m ${FAILED_COMMENT}"
            echo -e "\e[33;1mPlease check if thre are any errors in the './${PKG}/setup.py' file.\e[m"
            continue            
        fi

        ## インストール後のパッケージディレクトリを削除
        rm -rf ./dist ./${PKG}*

        # 次のパッケージのインストール準備
        cd ../
    done

### ビルド＆インストールした

### 初期化完了 ###
echo ""
echo -e "\e[30;47;1m ----------------------------------------------------------- \e[m"
echo -e "\e[30;47;1m ------------------ ${END_COMMENT} ------------------ \e[m"
echo -e "\e[30;47;1m ----------------------------------------------------------- \e[m"

### 処理終了時刻表示
FINISHED_TIME=`date "+%Y/%m/%d %H:%M:%S"`
echo "Finished time--------------> [${FINISHED_TIME}]"