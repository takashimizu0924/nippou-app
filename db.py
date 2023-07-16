import sqlite3

class DatabaseRetCode:
    """リターンコード"""
    
    SUCCESS: int                        = 0
    DB_CONNECTION_ERROR: int            = -1
    DB_CREATE_TABLE_ERROR: int          = -2
    DB_TABLE_ACCESS_ERROR: int          = -3
    DB_TABLE_INSERT_RECORD_ERROR: int   = -4
    DB_TABLE_UPDATE_RECORD_ERROR: int   = -5
    DB_TABLE_DELETE_RECORD_ERROR: int   = -6
    DB_TABLE_FETCH_RECORD_ERROR: int    = -7
    DB_DISCONNECTION_ERROR: int         = -8
    DB_OTHER_ERROR: int                 = -9
    
class DatabaseControl:
    """データベース制御
    """
    def __init__(self) -> None:
        """コンストラクタ
        """
        #データベース接続
        database_name: str = "work_manager"
        self._conn = sqlite3.connect(database_name)
        self._cur = self._conn.cursor()
        # self._conn.execute("DROP TABLE user")
        self.create_user_table()
        
    def __execute(self, sql: str) -> None:
        """sql文を実行

        Args:
            sql (str): 実行するクエリ
        """
        self._cur.execute(sql)
        return
    
    def __commit(self) -> None:
        """変更適用
        """
        self._conn.commit()
        return
    
    def create_user_table(self):
        """ユーザー登録用テーブル作成
        
        Args:
            
            table_culumn : company_name, user_name, password 
        Returns:
            int: データベースリターンコード
        """
        table_name: str = "user"
        #実行用sql文を作成
        _sql: str = f"CREATE TABLE IF NOT EXISTS {table_name}(id INTEGER PRIMARY KEY AUTOINCREMENT, company_name TEXT, user_name TEXT, password INTGER)"
        
        #実行用sql文を実行
        self.__execute(_sql)
        
        self.__commit()
        
        return DatabaseRetCode.SUCCESS
    
    def create_data_table(self, table_name: str) -> None:
        """ユーザーのデータ用テーブル作成

        Args:
            table_name (str): テーブル名 = ユーザー名
        """
        if table_name == "":
            return DatabaseRetCode.DB_CREATE_TABLE_ERROR
        
        #実行用sql文を作成
        #NOTE: テーブルカラム -> user_name, workdate, company_name, work_place, work_detail, worker, worker_cost, material_cost, sales  
        _sql: str = f"CREATE TABLE IF NOT EXISTS {table_name}(id INTEGER PRIMARY KEY AUTOINCREMENT, user_name TEXT, workdate DATETIME, company_name TEXT, work_place TEXT, work_detail TEXT, worker INTEGER, worker_cost INTEGER, material_cost INTEGER, sales INTEGER)"
        
        #実行用sql文を実行
        self.__execute(_sql)
        
        self.__commit()
        
        return DatabaseRetCode.SUCCESS
    
    def insert_user(self, company_name: str, user_name: str, password: str) -> None:
        """ユーザー情報を登録

        Args:
            company_name (_type_): _description_
            user_name (_type_): _description_
            password (_type_): _description_
        """
        if company_name == "" or user_name == "" or password == "":
            print("登録内容に不備があります")
        _sql: str = f"INSERT INTO user (company_name, user_name, password)VALUES ('{company_name}','{user_name}','{password}')"
        self.__execute(_sql)
        self.__commit()
        
    def insert_data(self, tabele_name: str, target_data_dict: dict) -> None:
        """データ挿入

        Args:
            tabele_name (str): テーブル名
            target_data_dict (dict): 挿入対象データ
        """
        ### クエリに挿入するデータ)生成
        # 挿入対象キー
        target_data_key: str = '(workdate, company_name, work_place, \
            work_detail, worker, worker_cost, material_cost, sales)'

        # 挿入対象データ
        target_data_value: str = f'(\
            \'{target_data_dict["date"]}\',\'{target_data_dict["company_name"]}\',\
            \'{target_data_dict["work_place"]}\',\'{target_data_dict["work_detail"]}\',\
            \'{target_data_dict["worker"]}\',\'{target_data_dict["worker_cost"]}\',\
            \'{target_data_dict["material_cost"]}\',\'{target_data_dict["sales"]}\'\
        )'

        ### クエリ生成
        _sql: str = f"INSERT INTO '{tabele_name}' {target_data_key} VALUES {target_data_value}"
        ### クエリ実行
        self.__execute(_sql)
        ### 実行結果を反映
        self.__commit()

    def fetch_user_all(self) -> str:
        """ユーザーテーブルを全て取得

        Args:
            company_name (_type_): _description_
            user_name (_type_): _description_
            password (_type_): _description_

        Returns:
            list: _description_
        """
        table_name: str = "user"
        #実行用sql文を作成
        _sql: str = f"SELECT * FROM {table_name}"
        #実行用sql文を実行
        self.__execute(_sql)
        
        res_list = self._cur.fetchall()
       
        
        return DatabaseRetCode.SUCCESS, res_list
    
    def fetch_user(self, company_name, user_name, password) -> list:
        """ユーザーテーブルに登録されているユーザーを取得

        Args:
            table_name (str): _description_

        Returns:
            list: _description_
        """
        table_name: str = "user"
        #実行用sql文を作成
        _sql: str = f"SELECT * FROM {table_name} WHERE company_name = '{company_name}' AND user_name = '{user_name}' AND password = '{password}' "
        
        #実行用sql文を実行
        self.__execute(_sql)
        
        res_list = self._cur.fetchall()
        
        return DatabaseRetCode.SUCCESS, res_list
        
    def fetch_select_company(self, company_name) -> list:
        """会社名からユーザーを取得

        Args:
            companyname (_type_): _description_

        Returns:
            list: _description_
        """
        table_name: str = "user"
        #実行用sql文を作成
        _sql: str = f"SELECT * FROM {table_name} WHERE company_name = '{company_name}'"
        
        #実行用sql文を実行
        self.__execute(_sql)
        
        res_list = self._cur.fetchall()
        
        return DatabaseRetCode.SUCCESS, res_list
        
    def fetch_data(self, table_name: str) -> str:
        """ユーザーのデータを全て取得

        Args:
            table_name (str): テーブル名 = ユーザー名

        Returns:
            list: 取得したデータのリスト
        """
        if table_name == "":
            return DatabaseRetCode.DB_CREATE_TABLE_ERROR
        
        #実行用sql文を作成
        _sql: str = f"SELECT * FROM {table_name}"
        
        #実行用sql文を実行
        self.__execute(_sql)
        
        res_list = self._cur.fetchall()
        print(f"fetch_dataで取得したデータ--->{res_list}")
        
        return DatabaseRetCode.SUCCESS, res_list
    
    def update_data(self, table_name: str, target_id: int, update_data_dict: dict) -> None:
        """データ更新

        Args:
            table_name (str): テーブル名
            target_id (int): 更新対象ID
            update_data_dict (dict): 更新データ
        """
        # 引数チェック
        if update_data_dict == {} or update_data_dict is None:
            print('指定された更新データが空のためエラー')
            return

        # クエリー作成用変数定義
        _query: str = ""
        for key, value in update_data_dict.items():
            # カラム名をまとめるための文字列を作成
            _values: str = ""

            ## カラムにいれるデータのタイプチェック
            # カラムに設定する値をまとめた文字列を作成
            if isinstance(value) is str:
                # 値が文字列型(str型)の場合
                _values = f'"{value}",'

            else:
                # 値が数値型(int型)の場合
                _values = f"{value},"

            _query += f"{key} = {_values},"

        # 末尾のカンマは不要なため削除
        _query = _query.rstrip(',')

        # 実行用sqlを生成
        _sql: str = f'UPDATE {table_name} SET {_query} WHERE target_id = {target_id}'
        # クエリを実行
        self.__execute(_sql)
        # 変更を適用する
        self.__commit()

    def delete_data(self, table_name: str, target_id: int) -> None:
        """データ削除

        Args:
            table_name (str): テーブル名
            target_id (int): 対象ID
        """
        # 引数チェック
        if table_name == "":
            print('指定されたテーブル名が空のためエラー')
            return

        # 引数チェック
        if target_id <= 0:
            print('指定されたIDが 0 以下のためエラー')
            return

        # クエリ生成
        _sql: str = f'DELETE FROM {table_name} WHERE target_id = {target_id}'
        # クエリ実行
        self.__execute(_sql)
        # 変更を適用する
        self.__commit()
