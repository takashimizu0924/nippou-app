import tkinter as tk 
import tkinter.ttk as ttk
from tkinter import messagebox
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
    
    #Userの登録データを取得
    def get_data(self, companyname, username) -> str:
        db_ctr = DatabaseControl()
        tablename = companyname + username
        _, data_list = db_ctr.fetch_data(tablename)
        return data_list
    
    #Userの入力データを登録
    def add_data(self):
        table_name = self.company_name + self.user_name
        work_date = self.date_label_entry.get()
        company_name = self.company_entry.get()
        work_place = self.workplace_entry.get()
        work_detail = self.workdetail_entry.get()
        worker = self.worker_entry.get()
        worker_cost = self.workercost_entry.get()
        material_cost = self.materialcost_entry.get()
        sales = self.sales_entry.get()
        
        self.data_dict["user_name"] = self.user_name
        self.data_dict["work_date"] = work_date
        self.data_dict["company_name"] = company_name
        self.data_dict["work_place"] = work_place
        self.data_dict["work_detail"] = work_detail
        self.data_dict["worker"] = int(worker)
        self.data_dict["worker_cost"] = int(worker_cost)
        self.data_dict["material_cost"] = int(material_cost)
        self.data_dict["sales"] = int(sales)
        db_ctr = DatabaseControl()
        db_ctr.insert_data(table_name, work_date, company_name, work_place, work_detail, int(worker), int(worker_cost), int(material_cost), int(sales))
        self.subwindow.destroy()
        
        self._update_window()
           
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
        if len(selected_id) > 1:
            messagebox.showinfo("確認", "複数選択されています。\n １項目のみ選択可能です")
        elif not selected_id:
            messagebox.showinfo("確認", "編集する項目を選択してください")
        
        else:
            selected_data = self.tree.item(selected_id, "values")
            print(selected_data)
            self.edit_data_window(selected_data)

    def _update_window(self) -> None:
        self.browes_title_frame.destroy()
        self.browes_top_frame.destroy()
        self.browes_tree_frame.destroy()
        self.browes_button_frame.destroy()
        self.browse_data_window(self.company_name, self.user_name)
    #ツリービューの削除ボタン押下関数
    def delete_data(self) -> None:
        selected_id = self.tree.selection()
        for item_id in selected_id:
            self.tree.delete(item_id)

    # 日報入力用ページ
    def open_add_inputdata(self) -> None:
        
        self.subwindow = tk.Toplevel()
        self.subwindow.title(f"{self.user_name+'さんの日報入力'}")
        self.subwindow.geometry("750x450+520+250")
        #登録ページ用フレーム作成
        self.input_title_frame = tk.Frame(self.subwindow)
        self.input_main_frame = tk.Frame(self.subwindow)
        self.input_submit_frame = tk.Frame(self.subwindow)
        self.input_title_frame.pack()
        self.input_main_frame.pack(fill="x")
        self.input_submit_frame.pack()
        
        title_label = tk.Label(self.input_title_frame, text="日報入力", font=("meiryo",15,"bold"))
        title_label.grid(row=0, column=0, pady=(30,50))
        
        date_label = tk.Label(self.input_main_frame, text="工事日", font=("meiryo", 10))
        company_label = tk.Label(self.input_main_frame, text="会社名", font=("meiryo", 10))
        workplace_label = tk.Label(self.input_main_frame, text="現場名", font=("meiryo", 10))
        workdetail_label = tk.Label(self.input_main_frame, text="作業内容", font=("meiryo", 10))
        worker_label = tk.Label(self.input_main_frame, text="作業員", font=("meiryo", 10))
        workercost_label = tk.Label(self.input_main_frame, text="作業員代", font=("meiryo", 10))
        materialcost_label = tk.Label(self.input_main_frame, text="材料費", font=("meiryo", 10))
        salese_label = tk.Label(self.input_main_frame, text="売上", font=("meiryo", 10))
        
        date_label.grid(row=1, column=0, padx=(38,5), pady=(10,10), sticky=tk.E)
        company_label.grid(row=2, column=0, padx=(38,5), pady=(10,10), sticky=tk.E)
        workplace_label.grid(row=2, column=2, padx=(38,5), pady=(10,10), sticky=tk.E)
        workdetail_label.grid(row=3, column=0, padx=(38,5), pady=(10,10), sticky=tk.E)
        worker_label.grid(row=4, column=0, padx=(38,5), pady=(10,10), sticky=tk.E)
        workercost_label.grid(row=4, column=2, padx=(38,5), pady=(10,10), sticky=tk.E)
        materialcost_label.grid(row=5, column=0, padx=(38,5), pady=(10,10), sticky=tk.E)
        salese_label.grid(row=5, column=2, padx=(38,5), pady=(10,10), sticky=tk.E)
        
        self.date_label_entry = tk.Entry(self.input_main_frame, width=20, font=("meiryo", 8))
        self.company_entry = ttk.Combobox(self.input_main_frame, width=25, font=("meiryo", 8))
        self.workplace_entry = tk.Entry(self.input_main_frame, width=30, font=("meiryo", 8))
        self.workdetail_entry = tk.Entry(self.input_main_frame, width=30, font=("meiryo", 8))
        self.worker_entry = tk.Entry(self.input_main_frame, width=15, font=("meiryo", 8), justify="right")
        self.workercost_entry = tk.Entry(self.input_main_frame, width=30, font=("meiryo", 8), justify="right")
        self.materialcost_entry = tk.Entry(self.input_main_frame, width=30, font=("meiryo", 8), justify="right")
        self.sales_entry = tk.Entry(self.input_main_frame, width=30, font=("meiryo", 8), justify="right")
        
        self.date_label_entry.grid(row=1, column=1, padx=(20,10), pady=(10,10),sticky="w")
        self.company_entry.grid(row=2, column=1, padx=(20,10), pady=(10,10), sticky=tk.W)
        self.workplace_entry.grid(row=2, column=3, padx=(20,10), pady=(10,10), sticky=tk.EW)
        self.workdetail_entry.grid(row=3, column=1, padx=(20,10), pady=(10,10), columnspan=4, sticky=tk.EW)
        self.worker_entry.grid(row=4, column=1, padx=(20,10), pady=(10,10), sticky=tk.W)
        self.workercost_entry.grid(row=4, column=3, padx=(20,10), pady=(10,10), sticky=tk.EW)
        self.materialcost_entry.grid(row=5, column=1, padx=(20,10), pady=(10,10), sticky=tk.EW)
        self.sales_entry.grid(row=5, column=3, padx=(20,10), pady=(10,10), sticky=tk.EW)
        
        
        submit = tk.Button(self.input_submit_frame, text="登録", width=10, command=self.add_data)
        submit.pack(pady=(30,5))
        
    #編集ページ
    def edit_data_window(self, selected_data):
        self.subwindow = tk.Toplevel()
        self.subwindow.title(f"{self.user_name+'さんの日報編集'}")
        self.subwindow.geometry("750x450+520+250")
        #登録ページ用フレーム作成
        title_frame = tk.Frame(self.subwindow)
        main_frame = tk.Frame(self.subwindow)
        submit_frame = tk.Frame(self.subwindow)
        title_frame.pack()
        main_frame.pack(fill="x")
        submit_frame.pack()
        
        title_label = tk.Label(title_frame, text="日報編集", font=("meiryo",15,"bold"))
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
        
        self.date_label_entry.insert(0, selected_data[1])
        self.company_entry.insert(0, selected_data[2])
        self.workplace_entry.insert(0, selected_data[3])
        self.workdetail_entry.insert(0, selected_data[4])
        self.worker_entry.insert(0, selected_data[5])
        self.workercost_entry.insert(0, selected_data[6])
        self.materialcost_entry.insert(0, selected_data[7])
        self.sales_entry.insert(0, selected_data[8])
        
        
        submit = tk.Button(submit_frame, text="登録", width=10, command=self.add_data)
        submit.pack(pady=(30,5))
    
    #閲覧ページ　最初の呼び出しはこのページ        
    def browse_data_window(self, companyname, username) -> None:
        self.user_name = username
        self.company_name = companyname
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        #メニューバーの項目を作成
        setting_menu = tk.Menu(menubar,tearoff=False)
        menubar.add_cascade(label="設定",menu=setting_menu)

        #メニューバー内のプルダウンを作成
        setting_menu.add_command(label="日報登録",command=self.open_add_inputdata)
        # setting_menu.add_command(label="環境設定",command=self.open_setting)
        setting_menu.add_command(label="終了",command=self.quit_app)

        #閲覧ページ用フレームの作成
        self.browes_title_frame = tk.Frame(self.root, pady=20)
        self.browes_top_frame = tk.Frame(self.root, pady=10)
        self.browes_tree_frame = tk.Frame(self.root,pady=30)
        self.browes_button_frame = tk.Frame(self.root)
        self.browes_title_frame.pack()
        self.browes_top_frame.pack(fill="x")
        self.browes_tree_frame.pack(fill="y")
        self.browes_button_frame.pack()

        #閲覧用ページ
        #上部
        page_title = tk.Label(self.browes_title_frame,text=f"{self.user_name+'の集計閲覧'}", font=("meiryo",15,"bold"))
        page_title.grid(row=0, column=0)
        
        company_label = tk.Label(self.browes_top_frame, text="取引先名", font=("meiryo",10))
        company = ttk.Combobox(self.browes_top_frame,width=25, font=("meiryo",10),style="TCombobox")
        total_cost_label = tk.Label(self.browes_top_frame,text="合計経費", font=("meiryo",10))
        total_sales_label = tk.Label(self.browes_top_frame, text="合計売上", font=("meiryo",10))
        total_cost_data = tk.Label(self.browes_top_frame, text="￥1223213", relief="sunken", anchor="e", width=35, font=("meiryo",10), justify="right", padx=10)
        total_sales_data = tk.Label(self.browes_top_frame, text="￥1223213", relief="sunken", anchor="e", width=35, font=("meiryo",10), justify="right", padx=10)

        company_label.grid(row=0,column=0, padx=(60,30), pady=(30,15))
        company.grid(row=0,column=1, pady=(30,15), sticky=tk.W)
        total_cost_label.grid(row=1, column=0, padx=(60,30), pady=(30,15))
        total_cost_data.grid(row=1, column=1, pady=(30,15))
        total_sales_label.grid(row=1, column=2, padx=(60,30), pady=(30,15))
        total_sales_data.grid(row=1, column=3, pady=(30,15))


        #ツリービュー作成

        self.tree = ttk.Treeview(self.browes_tree_frame,height=15)
        self.tree['columns'] = ("id", "date", "company_name", "work_place", "work_detail", "worker", "cost", "material_cost", "sales")
        self.tree['displaycolumns'] = ["date","work_place", "worker", "cost", "sales"]
        self.tree['show'] = 'headings'

        #ツリービューのカラムの設定
        self.tree.column("date", width=80)
        self.tree.column("work_place", width=500)
        self.tree.column("worker", width=75, anchor=tk.E)
        self.tree.column("cost", width=150, anchor=tk.E)
        self.tree.column("sales", width=150, anchor=tk.E)



        #ツリービューのカラムの見出し設定
        self.tree.heading("date", text="日付")
        self.tree.heading("work_place", text="現場名")
        self.tree.heading("worker", text="作業員数")
        self.tree.heading("cost", text="経費")
        self.tree.heading("sales", text="売上")
        
        _data = self.get_data(self.company_name, self.user_name)
        for data in _data:
            self.tree.insert("","end", values=(data[0], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]))
        # for i in range(50):
        #     self.tree.insert("","end", values=("2023/6/26", "ＲＧ石城町", "1", "20,000", "50,000"))


        #スクロールバーを作成
        scroll_v = ttk.Scrollbar(self.browes_tree_frame, orient="vertical", command=self.tree.yview)
        scroll_v.grid(row=0, column=1, sticky=tk.NS)

        self.tree.configure(yscrollcommand=scroll_v.set)
        self.tree.grid(row=0, column=0, sticky=tk.NSEW)

        add_button = tk.Button(self.browes_button_frame, text="追加", width=10, command=self.open_add_inputdata)
        edit_button = tk.Button(self.browes_button_frame, text="編集", width=10, command=self.edit_data)
        del_button = tk.Button(self.browes_button_frame, text="削除", width=10, background="red", command=self.delete_data)
        add_button.grid(row=0, column=0, padx=30)
        edit_button.grid(row=0, column=1, padx=30)
        del_button.grid(row=0, column=2, padx=30)