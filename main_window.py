import tkinter as tk 
import tkinter.ttk as ttk
from db import DatabaseControl


class Window():
    """ウィンドウ(画面表示)クラス
    """
    def __init__(self, root:tk.Tk) -> None:
        """メイン画面表示
           各ウィンドウサイズ設定
        """
        self.root = root
        self.user_name: str = ""
        self._APP_TITLE: str = "業務管理アプリ"
        self._APP_WIDTH: int = 1000
        self._APP_HEIGHT: int = 700
        self._APP_POSITION_X: int = 400
        self._APP_POSITION_Y: int = 150
        self._RESIZE_WINDOW_X: bool = False
        self._RESIZE_WINDOW_Y: bool = False
        
        self._INPUT_DATA_TITLE: str = "日報入力"
        self._INPUT_DATA_WIDTH: int = 750
        self._INPUT_DATA_HEIGHT: int = 450
        self._INPUT_DATA_POSITION_X: int = 520
        self._INPUT_DATA_POSITION_Y: int = 250
        
        #各Frame
        self.login_frame = tk.Frame()
        
        #データ用
        self.data_dict = {
            "user_name": str,
            "work_date": str,
            "company_name": str,
            "work_place": str,
            "work_detail": str,
            "worker": int,
            "worker_cost": int,
            "material_cost": int,
            "sales": int
        }
        
        
    def main_window(self, username) -> None:
        self.user_name = username
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()
        label = tk.Label(self.main_frame, text=f"{self.user_name}")
        label2 = tk.Label(self.main_frame, text="test")
        label.pack()
        label2.pack()
    
    #ログイン画面作成
    def login_window(self) -> None:
        #見出し
        self.login_frame.pack()
        
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
        
    #日報入力画面作成
    def input_data_window(self) -> None:
        window = tk.Toplevel()
        window.title(self._INPUT_DATA_TITLE)
        window.geometry(f"{self._INPUT_DATA_WIDTH}x{self._INPUT_DATA_HEIGHT}+{self._INPUT_DATA_POSITION_X}+{self._INPUT_DATA_POSITION_Y}")
        #登録ページ用フレーム作成
        title_frame = tk.Frame(window)
        main_frame = tk.Frame(window)
        submit_frame = tk.Frame(window)
        title_frame.pack()
        main_frame.pack(fill="x")
        submit_frame.pack()
        
        title_label = tk.Label(title_frame, text="日報入力"+f"{self.user_name}", font=("meiryo",15,"bold"))
        title_label.grid(row=0, column=0, pady=(30,50))
        
        date_label = tk.Label(main_frame, text="工事日", font=("meiryo", 10))
        company_label = tk.Label(main_frame, text="会社名", font=("meiryo", 10))
        workplace_label = tk.Label(main_frame, text="現場名", font=("meiryo", 10))
        workdetail_label = tk.Label(main_frame, text="作業内容", font=("meiryo", 10))
        worker_label = tk.Label(main_frame, text="作業員", font=("meiryo", 10))
        workercost_label = tk.Label(main_frame, text="作業員代", font=("meiryo", 10))
        materialcost_label = tk.Label(main_frame, text="材料費", font=("meiryo", 10))
        salese_label = tk.Label(main_frame, text="売上", font=("meiryo", 10))
        
        date_label.grid(row=1, column=0, padx=(38,5), pady=(10,10), sticky=tk.E)
        company_label.grid(row=2, column=0, padx=(38,5), pady=(10,10), sticky=tk.E)
        workplace_label.grid(row=2, column=2, padx=(38,5), pady=(10,10), sticky=tk.E)
        workdetail_label.grid(row=3, column=0, padx=(38,5), pady=(10,10), sticky=tk.E)
        worker_label.grid(row=4, column=0, padx=(38,5), pady=(10,10), sticky=tk.E)
        workercost_label.grid(row=4, column=2, padx=(38,5), pady=(10,10), sticky=tk.E)
        materialcost_label.grid(row=5, column=0, padx=(38,5), pady=(10,10), sticky=tk.E)
        salese_label.grid(row=5, column=2, padx=(38,5), pady=(10,10), sticky=tk.E)
        
        date_label_entry = tk.Entry(main_frame, width=20, font=("meiryo", 8))
        company_entry = ttk.Combobox(main_frame, width=25, font=("meiryo", 8))
        workplace_entry = tk.Entry(main_frame, width=30, font=("meiryo", 8))
        workdetail_entry = tk.Entry(main_frame, width=30, font=("meiryo", 8))
        worker_entry = tk.Entry(main_frame, width=15, font=("meiryo", 8), justify="right")
        workercost_entry = tk.Entry(main_frame, width=30, font=("meiryo", 8), justify="right")
        materialcost_entry = tk.Entry(main_frame, width=30, font=("meiryo", 8), justify="right")
        sales_entry = tk.Entry(main_frame, width=30, font=("meiryo", 8), justify="right")
        
        date_label_entry.grid(row=1, column=1, padx=(20,10), pady=(10,10),sticky="w")
        company_entry.grid(row=2, column=1, padx=(20,10), pady=(10,10), sticky=tk.W)
        workplace_entry.grid(row=2, column=3, padx=(20,10), pady=(10,10), sticky=tk.EW)
        workdetail_entry.grid(row=3, column=1, padx=(20,10), pady=(10,10), columnspan=4, sticky=tk.EW)
        worker_entry.grid(row=4, column=1, padx=(20,10), pady=(10,10), sticky=tk.W)
        workercost_entry.grid(row=4, column=3, padx=(20,10), pady=(10,10), sticky=tk.EW)
        materialcost_entry.grid(row=5, column=1, padx=(20,10), pady=(10,10), sticky=tk.EW)
        sales_entry.grid(row=5, column=3, padx=(20,10), pady=(10,10), sticky=tk.EW)
        
        submit = tk.Button(submit_frame, text="登録", width=10)
        submit.pack(pady=(30,5))
    
    #Userの登録データを取得
    def get_data(self, username) -> str:
        db_ctr = DatabaseControl()
        print("username",username)
        data_list = db_ctr.fetch_data(username)
        print(data_list)
    
    #Userの入力データを登録
    def add_data(self):
        user_name = self.user_name
        work_date = self.date_label_entry.get()
        company_name = self.company_entry.get()
        work_place = self.workplace_entry.get()
        work_detail = self.workdetail_entry.get()
        worker = self.worker_entry.get()
        worker_cost = self.workercost_entry.get()
        material_cost = self.materialcost_entry.get()
        sales = self.sales_entry.get()
        
        self.data_dict["user_name"] = user_name
        self.data_dict["work_date"] = work_date
        self.data_dict["company_name"] = company_name
        self.data_dict["work_place"] = work_place
        self.data_dict["work_detail"] = work_detail
        self.data_dict["worker"] = int(worker)
        self.data_dict["worker_cost"] = int(worker_cost)
        self.data_dict["material_cost"] = int(material_cost)
        self.data_dict["sales"] = int(sales)
        print(self.data_dict["user_name"])
        db_ctr = DatabaseControl()
        db_ctr.insert_data(user_name, work_date, company_name, work_place, work_detail, int(worker), int(worker_cost), int(material_cost), int(sales))
            
            
            
    #アプリを終了する関数
    def quit_app(self) -> None:
        self.root.quit()
    
    def open_setting(self) -> None:
        subwindow = tk.Toplevel()
        subwindow.title("設定")
        subwindow.geometry("500x500+600+300")
        
        subwindow_label = tk.Label(subwindow, text="設定画面です")
        subwindow_label.pack()
    
    #ツリービューの編集ボタン押下関数
    def edit_data(self) -> None:
        selected_id = self.tree.selection()
        print(selected_id)


    #ツリービューの削除ボタン押下関数
    def delete_data(self) -> None:
        selected_id = self.tree.selection()
        for item_id in selected_id:
            self.tree.delete(item_id)

    # 日報入力用ページ
    def open_add_inputdata(self) -> None:
        
        subwindow = tk.Toplevel()
        subwindow.title(f"{self.user_name+'さんの日報入力'}")
        subwindow.geometry("750x450+520+250")
        #登録ページ用フレーム作成
        title_frame = tk.Frame(subwindow)
        main_frame = tk.Frame(subwindow)
        submit_frame = tk.Frame(subwindow)
        title_frame.pack()
        main_frame.pack(fill="x")
        submit_frame.pack()
        
        title_label = tk.Label(title_frame, text="日報入力", font=("meiryo",15,"bold"))
        title_label.grid(row=0, column=0, pady=(30,50))
        
        date_label = tk.Label(main_frame, text="工事日", font=("meiryo", 10))
        company_label = tk.Label(main_frame, text="会社名", font=("meiryo", 10))
        workplace_label = tk.Label(main_frame, text="現場名", font=("meiryo", 10))
        workdetail_label = tk.Label(main_frame, text="作業内容", font=("meiryo", 10))
        worker_label = tk.Label(main_frame, text="作業員", font=("meiryo", 10))
        workercost_label = tk.Label(main_frame, text="作業員代", font=("meiryo", 10))
        materialcost_label = tk.Label(main_frame, text="材料費", font=("meiryo", 10))
        salese_label = tk.Label(main_frame, text="売上", font=("meiryo", 10))
        
        date_label.grid(row=1, column=0, padx=(38,5), pady=(10,10), sticky=tk.E)
        company_label.grid(row=2, column=0, padx=(38,5), pady=(10,10), sticky=tk.E)
        workplace_label.grid(row=2, column=2, padx=(38,5), pady=(10,10), sticky=tk.E)
        workdetail_label.grid(row=3, column=0, padx=(38,5), pady=(10,10), sticky=tk.E)
        worker_label.grid(row=4, column=0, padx=(38,5), pady=(10,10), sticky=tk.E)
        workercost_label.grid(row=4, column=2, padx=(38,5), pady=(10,10), sticky=tk.E)
        materialcost_label.grid(row=5, column=0, padx=(38,5), pady=(10,10), sticky=tk.E)
        salese_label.grid(row=5, column=2, padx=(38,5), pady=(10,10), sticky=tk.E)
        
        self.date_label_entry = tk.Entry(main_frame, width=20, font=("meiryo", 8))
        self.company_entry = ttk.Combobox(main_frame, width=25, font=("meiryo", 8))
        self.workplace_entry = tk.Entry(main_frame, width=30, font=("meiryo", 8))
        self.workdetail_entry = tk.Entry(main_frame, width=30, font=("meiryo", 8))
        self.worker_entry = tk.Entry(main_frame, width=15, font=("meiryo", 8), justify="right")
        self.workercost_entry = tk.Entry(main_frame, width=30, font=("meiryo", 8), justify="right")
        self.materialcost_entry = tk.Entry(main_frame, width=30, font=("meiryo", 8), justify="right")
        self.sales_entry = tk.Entry(main_frame, width=30, font=("meiryo", 8), justify="right")
        
        self.date_label_entry.grid(row=1, column=1, padx=(20,10), pady=(10,10),sticky="w")
        self.company_entry.grid(row=2, column=1, padx=(20,10), pady=(10,10), sticky=tk.W)
        self.workplace_entry.grid(row=2, column=3, padx=(20,10), pady=(10,10), sticky=tk.EW)
        self.workdetail_entry.grid(row=3, column=1, padx=(20,10), pady=(10,10), columnspan=4, sticky=tk.EW)
        self.worker_entry.grid(row=4, column=1, padx=(20,10), pady=(10,10), sticky=tk.W)
        self.workercost_entry.grid(row=4, column=3, padx=(20,10), pady=(10,10), sticky=tk.EW)
        self.materialcost_entry.grid(row=5, column=1, padx=(20,10), pady=(10,10), sticky=tk.EW)
        self.sales_entry.grid(row=5, column=3, padx=(20,10), pady=(10,10), sticky=tk.EW)
        
        
        submit = tk.Button(submit_frame, text="登録", width=10, command=self.add_data)
        submit.pack(pady=(30,5))
    
    #閲覧ページ　最初の呼び出しはこのページ        
    def browse_data_window(self, username) -> None:
        self.get_data(username)
        self.user_name = username
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        #メニューバーの項目を作成
        setting_menu = tk.Menu(menubar,tearoff=False)
        menubar.add_cascade(label="設定",menu=setting_menu)

        #メニューバー内のプルダウンを作成
        setting_menu.add_command(label="日報登録",command=self.open_add_inputdata)
        setting_menu.add_command(label="環境設定",command=self.open_setting)
        setting_menu.add_command(label="終了",command=self.quit_app)

        #閲覧ページ用フレームの作成
        title_frame = tk.Frame(self.root, pady=20)
        top_frame = tk.Frame(self.root, pady=10)
        tree_frame = tk.Frame(self.root,pady=30)
        button_frame = tk.Frame(self.root)
        title_frame.pack()
        top_frame.pack(fill="x")
        tree_frame.pack(fill="y")
        button_frame.pack()

        #閲覧用ページ
        #上部
        page_title = tk.Label(title_frame,text=f"{self.user_name+'の集計閲覧'}", font=("meiryo",15,"bold"))
        page_title.grid(row=0, column=0)
        
        company_label = tk.Label(top_frame, text="取引先名", font=("meiryo",10))
        company = ttk.Combobox(top_frame,width=25, font=("meiryo",10),style="TCombobox")
        total_cost_label = tk.Label(top_frame,text="合計経費", font=("meiryo",10))
        total_sales_label = tk.Label(top_frame, text="合計売上", font=("meiryo",10))
        total_cost_data = tk.Label(top_frame, text="￥1223213", relief="sunken", anchor="e", width=35, font=("meiryo",10), justify="right", padx=10)
        total_sales_data = tk.Label(top_frame, text="￥1223213", relief="sunken", anchor="e", width=35, font=("meiryo",10), justify="right", padx=10)

        company_label.grid(row=0,column=0, padx=(60,30), pady=(30,15))
        company.grid(row=0,column=1, pady=(30,15), sticky=tk.W)
        total_cost_label.grid(row=1, column=0, padx=(60,30), pady=(30,15))
        total_cost_data.grid(row=1, column=1, pady=(30,15))
        total_sales_label.grid(row=1, column=2, padx=(60,30), pady=(30,15))
        total_sales_data.grid(row=1, column=3, pady=(30,15))


        #ツリービュー作成

        self.tree = ttk.Treeview(tree_frame,height=15)
        self.tree['columns'] = (1, 2, 3, 4, 5)
        self.tree['show'] = 'headings'

        #ツリービューのカラムの設定
        self.tree.column(1, width=80)
        self.tree.column(2, width=500)
        self.tree.column(3, width=75, anchor=tk.E)
        self.tree.column(4, width=150, anchor=tk.E)
        self.tree.column(5, width=150, anchor=tk.E)



        #ツリービューのカラムの見出し設定
        self.tree.heading(1, text="日付")
        self.tree.heading(2, text="現場名")
        self.tree.heading(3, text="作業員数")
        self.tree.heading(4, text="経費")
        self.tree.heading(5, text="売上")

        for i in range(50):
            self.tree.insert("","end", values=("2023/6/26", "ＲＧ石城町", "1", "20,000", "50,000"))


        #スクロールバーを作成
        scroll_v = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        scroll_v.grid(row=0, column=1, sticky=tk.NS)

        self.tree.configure(yscrollcommand=scroll_v.set)
        self.tree.grid(row=0, column=0, sticky=tk.NSEW)

        add_button = tk.Button(button_frame, text="追加", width=10, command=self.open_add_inputdata)
        edit_button = tk.Button(button_frame, text="編集", width=10, command=self.edit_data)
        del_button = tk.Button(button_frame, text="削除", width=10, background="red", command=self.delete_data)
        add_button.grid(row=0, column=0, padx=30)
        edit_button.grid(row=0, column=1, padx=30)
        del_button.grid(row=0, column=2, padx=30)