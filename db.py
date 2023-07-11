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
        print(_sql)
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
    def insert_data(self, user_name: str, date: str, company_name: str,work_place: str, work_detail: str, worker: int, worker_cost: int, material_cost: int, sales: int) -> None:
        """データ挿入

        Args:
            date (str): _description_
            company_name (str): _description_
            work_place (str): _description_
            work_detail (str): _description_
            worker (int): _description_
            worker_cost (int): _description_
            material_cost (int): _description_
            sales (int): _description_
        """
        _sql: str = f"INSERT INTO '{user_name}' (user_name, workdate, company_name, work_place, work_detail, worker, worker_cost, material_cost, sales)VALUES ('{user_name}','{date}','{company_name}','{work_place}','{work_detail}','{worker}', '{worker_cost}', '{material_cost}', '{sales}')"
        
        self.__execute(_sql)
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
        
    
    def fetch_data(self, table_name: str) -> list:
        """ユーザーのデータを全て取得

        Args:
            table_name (str): テーブル名 = ユーザー名

        Returns:
            list: 取得したデータのリスト
        """
        print(f"{table_name},koko")
        if table_name == "":
            return DatabaseRetCode.DB_CREATE_TABLE_ERROR
        
        #実行用sql文を作成
        _sql: str = f"SELECT * FROM {table_name}"
        
        #実行用sql文を実行
        self.__execute(_sql)
        
        res_list = self._cur.fetchall()
        print(f"fetch_dataで取得したデータ--->{res_list}")
        
        return DatabaseRetCode.SUCCESS, res_list
        
        
        