import tkinter as tk 
import tkinter.ttk as ttk


class Window():
    """ウィンドウ(画面表示)クラス
    """
    def __init__(self, root, user_name) -> None:
        """メイン画面表示
           各ウィンドウサイズ設定
        """
        self.root = root
        self.user_name = user_name
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
        
        # self.root = tk.Tk()
        # self.root.title(self._APP_TITLE)
        # self.root.geometry(f"{self._APP_WIDTH}x{self._APP_HEIGHT}+{self._APP_POSITION_X}+{self._APP_POSITION_Y}")
        # self.root.resizable(width=self._RESIZE_WINDOW_X, height=self._RESIZE_WINDOW_Y)
        
        # self.root.mainloop()
    
    
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
        
    