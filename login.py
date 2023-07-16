import tkinter as tk 
from tkinter import messagebox
from db import DatabaseControl
from main_window import Window

class Login:
    def __init__(self, root, main_window: Window) -> None:
        
        self.root = root
        self.flag: bool = False
        self.main_window = main_window
        self._COMPANY_NAME: str = ""
        self._USER_NAME: str = ""
        self._USER_PASSWORD: int
        
        #テスト用仮想データベース
        self.db_ctr = DatabaseControl()
        
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack()
        self.input_login_widget()
        
    #ログイン       
    def input_login_widget(self) -> None:
        """ログイン入力用ウィジェットを配置"""
        #見出し
        self.input_title_label = tk.Label(self.login_frame, text="Login", font=("", 15, "bold"))
        self.input_title_label.grid(row=0, column=0, columnspan=2, pady=(30, 30))
        
        #会社名入力用
        self.company_name_label = tk.Label(self.login_frame, text="会社名")
        self.company_name_label.grid(row=1, column=0, pady=(10, 20))
        self.company_name_entry = tk.Entry(self.login_frame)
        self.company_name_entry.grid(row=1, column=1, pady=(10, 20))
        self.user_name_label = tk.Label(self.login_frame, text="ユーザー名")
        self.user_name_label.grid(row=2, column=0, pady=(10, 20))
        self.user_name_entry = tk.Entry(self.login_frame)
        self.user_name_entry.grid(row=2, column=1, pady=(10, 20))
        self.password_label = tk.Label(self.login_frame, text="パスワード")
        self.password_label.grid(row=3, column=0, pady=(10, 20))
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=3, column=1, pady=(10, 20))
        
        #ログインボタン
        self.login_button = tk.Button(self.login_frame, text="ログイン", command=self.login)
        self.login_button.grid(row=4, column=0, columnspan=2)
    #ユーザー登録
    def add_user_widget(self) -> None:
        
        self.add_user_frame = tk.Frame(self.root)
        self.add_user_frame.pack()
        
        self.input_title_label = tk.Label(self.add_user_frame, text="新規登録", font=("", 15, "bold"))
        self.input_title_label.grid(row=0, column=0, columnspan=2, pady=(30, 30))
        
        #会社名入力用
        self.company_name_label = tk.Label(self.add_user_frame, text="会社名")
        self.company_name_label.grid(row=1, column=0, pady=(10, 20))
        self.company_name_entry = tk.Entry(self.add_user_frame)
        self.company_name_entry.grid(row=1, column=1, pady=(10, 20))
        self.user_name_label = tk.Label(self.add_user_frame, text="ユーザー名")
        self.user_name_label.grid(row=2, column=0, pady=(10, 20))
        self.user_name_entry = tk.Entry(self.add_user_frame)
        self.user_name_entry.grid(row=2, column=1, pady=(10, 20))
        self.password_label = tk.Label(self.add_user_frame, text="パスワード")
        self.password_label.grid(row=3, column=0, pady=(10, 20))
        self.password_entry = tk.Entry(self.add_user_frame, show="*")
        self.password_entry.grid(row=3, column=1, pady=(10, 20))
        
        #登録ボタン
        self.login_button = tk.Button(self.add_user_frame, text="登録", command=self.add)
        self.login_button.grid(row=4, column=0, columnspan=2)
    
    def __login_check(self, company_name, user_name, password) -> bool:
        """データベースに登録情報があるか確認
        """
        user_list = self.db_ctr.fetch_user(company_name, user_name, password)
        # _, user_from_company = self.db_ctr.fetch_select_company(company_name)
        print(user_list)
        # for user in user_from_company:
        #     if user[2] == user_name:
        #         messagebox.showinfo("確認", "すでに同じ名前で登録されています")
        #         return
        
        #ユーザーリストにデータがない場合登録画面に遷移させるための返り値を返す
        if user_list[1] == []:
            messagebox.showinfo("確認", "未登録なのでそのまま登録してください")
            # self.login_frame.destroy()
            # self.add_user_widget()
            # self.login_button.config(text="登録", command=self.__add_user(company_name, user_name, password))
            return False
        
        return True
        
    def __add_check(self, company_name, user_name) -> bool:
        _, user = self.db_ctr.fetch_select_company(company_name)
        print(len(user))
        print(company_name, user_name)
        if len(user) == 0:
            return True
        for user in user:
            if user[2] == user_name:
                return False
            elif not user:
                return True
            else:
                return True
        return False    
    
    def add(self) -> None:
        self._COMPANY_NAME = self.company_name_entry.get()
        self._USER_NAME = self.user_name_entry.get()
        self._USER_PASSWORD = self.password_entry.get()

        if self._COMPANY_NAME == "" or self._USER_NAME == "" or self._USER_PASSWORD == "":
            messagebox.showwarning("警告", "入力内容に不備があります。\nすべての項目を入力してください")
            return
        if self.__add_check(self._COMPANY_NAME, self._USER_NAME):
            self.db_ctr.insert_user(self._COMPANY_NAME, self._USER_NAME, self._USER_PASSWORD)
            messagebox.showinfo("確認", "登録完了")
            self.add_user_frame.destroy()
            tablename = self._COMPANY_NAME + self._USER_NAME
            self.db_ctr.create_data_table(table_name = tablename)
            self.main_window.browse_data_window(self._COMPANY_NAME, self._USER_NAME)   
            
        elif not self.__add_check(self._COMPANY_NAME, self._USER_NAME):
            messagebox.showinfo("確認", "すでに同じ名前で登録されています")
            return
    def login(self) -> None:
        """ログインを実行する
        ログイン完了後閲覧ページに遷移
        """
        
        self._COMPANY_NAME = self.company_name_entry.get()
        self._USER_NAME = self.user_name_entry.get()
        self._USER_PASSWORD = self.password_entry.get()
        table_name = self._COMPANY_NAME + self._USER_NAME
        
        if self._COMPANY_NAME == "" or self._USER_NAME == "" or self._USER_PASSWORD == "":
            messagebox.showwarning("警告", "入力内容に不備があります。\nすべての項目を入力してください")
        else:
            r = self.__login_check(self._COMPANY_NAME, self._USER_NAME, self._USER_PASSWORD)
            if r :
                self.login_frame.destroy()
                self.db_ctr.create_data_table(table_name)
                self.main_window.browse_data_window(self._COMPANY_NAME,self._USER_NAME)
            else:
                self.login_frame.destroy()
                self.add_user_widget()
                
    def login_user(self) -> str:
        return self._USER_NAME 
        # self.window = Window(self.root, self._USER_NAME)
        # self.window.input_data_window()
         
        # self.__login_check()
        # self.__add_user(self._COMPANY_NAME, self._USER_NAME, self._USER_PASSWORD)
        # try:
        #     if len(self.database) > 0:
        #         print("ok")
        # except:
        #     print("Not in database...")
        #     return