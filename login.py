import tkinter as tk 
from tkinter import messagebox
from db import DatabaseControl
from main_window import Window

class Login:
    def __init__(self, root) -> None:
        
        self.root = root
        self.flag = False
        
        self._COMPANY_NAME: str = ""
        self._USER_NAME: str = ""
        self._USER_PASSWORD: int = 0
        
        
        #テスト用仮想データベース
        self.db_ctr = DatabaseControl()
        self.dic = dict.fromkeys(["会社名", "ユーザー名", "パスワード"])
        self.dic["ユーザー名"] = "たかし"
        self.database = [self.dic]
        
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        # self.input_widget()
        
        
        
        
    def input_widget(self):
        """入力用ウィジェットを配置"""
        #見出し
        self.input_title_label = tk.Label(self.frame, text="Login", font=("", 15, "bold"))
        self.input_title_label.grid(row=0, column=0, columnspan=2, pady=(30, 30))
        
        #会社名入力用
        self.company_name_label = tk.Label(self.frame, text="会社名")
        self.company_name_label.grid(row=1, column=0, pady=(10, 20))
        self.company_name_entry = tk.Entry(self.frame)
        self.company_name_entry.grid(row=1, column=1, pady=(10, 20))
        self.user_name_label = tk.Label(self.frame, text="ユーザー名")
        self.user_name_label.grid(row=2, column=0, pady=(10, 20))
        self.user_name_entry = tk.Entry(self.frame)
        self.user_name_entry.grid(row=2, column=1, pady=(10, 20))
        self.password_label = tk.Label(self.frame, text="パスワード")
        self.password_label.grid(row=3, column=0, pady=(10, 20))
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=3, column=1, pady=(10, 20))
        
        #ログインボタン
        self.login_button = tk.Button(self.frame, text="ログイン", command=self.login)
        self.login_button.grid(row=4, column=0, columnspan=2)
    
    def __login_check(self, company_name, user_name, password):
        """データベースに登録情報があるか確認
        """
        
        user_list = self.db_ctr.fetch_user(company_name, user_name, password)
        print(user_list)
        if user_list[1] == []:
            print("none")
            messagebox.showinfo("確認", "未登録なのでそのまま登録してください")
            self.login_button.config(text="登録", command=self.__add_user(company_name, user_name, password))
            self.flag = True
        self.flag = True
        self.frame.destroy()
    def __add_user(self, company_name, user_name, user_password):
        self.db_ctr.insert_user(company_name, user_name, user_password)
    
    def login(self) -> str:
        """ログインを実行する"""
        self._COMPANY_NAME = self.company_name_entry.get()
        self._USER_NAME = self.user_name_entry.get()
        self._USER_PASSWORD = self.password_entry.get()
        
        if self._COMPANY_NAME == "" or self._USER_NAME == "" or self._USER_PASSWORD == "":
            messagebox.showwarning("警告", "入力内容に不備があります。\nすべての項目を入力してください")
        
        else:
            self.__login_check(self._COMPANY_NAME, self._USER_NAME, self._USER_PASSWORD)
        
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