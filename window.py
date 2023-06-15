#!/usr/bin/env python3
# -*- coding: utf-8 -*-

### Tkinterパッケージ
from tkinter import (Button, Canvas, Frame, Label, Scrollbar, Tk)
from textbox import (Title, WorkDate, Company, WorkPlace, WorkDetail, Worker, WorkerCost, MaterialCost, Sales)
### アプリケーションデータ制御モジュール
from app_data_control import (AppDataControl)
from app_data_control import (DataDeleteReq, DataFetchReq, DataRegistReq, DataUpdateReq)
from app_data_control import (DataFetchRsp)


class Window():
    """メインウィンドウクラス
    """
    def __init__(self) -> None:
        """コンストラクタ
        """
        ### アプリケーションデータマネージャ ###
        # インスタンス生成
        self.app_data_mng: AppDataControl = AppDataControl()

        ### Tkinterメインウィンドウ ###
        # 設定情報定義
        self._WINDOW_TITLE: str     = "日報兼売上管理アプリ" 
        self._WINDOW_WIDTH: int     = 1000
        self._WINDOW_HEIGHT: int    = 600
        self.root: Tk = None
        # メインウィンドウ作成
        self.__create_root(self._WINDOW_TITLE, self._WINDOW_WIDTH, self._WINDOW_HEIGHT)

        ### 日報入力画面 ###
        # 全体で利用する変数定義
        self.input_frame: Frame = None

        ### 日報閲覧画面 ###
        # 設定情報提議
        self._WG_BROWSE_CANVAS_WIDTH: int = 950
        self._WG_BROWSE_CANVAS_HEIGHT: int = 250
        self._SCRL_REGION_WEST: int = 0
        self._SCRL_REGION_NORTH: int = 0
        self._SCRL_REGION_EAST: int = 500
        self._SCRL_REGION_SOUTH: int = 500
        # 全体で利用する変数定義
        self.browse_frame: Frame = None
        self.scroll_frame: Frame = None
        
        # アプリ起動時の初期ページを作成
        self.create_input_page()

    def __create_root(self, title_text: str, width: int, height: int, resizeable_width: bool=True,resizeable_height: bool=True) -> None:
        """Tkinterウィンドウ作成
            NOTE: メインウィンドウのタイトル、縦横幅サイズ設定、サイズ変更可否設定を行う

        Args:
            title_text (str): メインウィンドウのタイトル文字列
            width (int): メインウィンドウの横幅サイズ
            height (int): メインウィンドウの縦幅サイズ
            resizeable_width (bool, optional): 横幅サイズの変更可否(True:変更可/False:変更不可). Defaults to True.
            resizeable_height (bool, optional): 縦幅サイズの変更可否(True:変更可/False:変更不可). Defaults to True.
        """
        self.root = Tk()
        self.root.title(title_text)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(width=resizeable_width,height=resizeable_height)
        return

    def __create_input_window_widgets(self) -> None:
        """日報入力画面のウィジェット作成
            NOTE: フレーム、ボタン、ラベルなどのウィジェットを作成する
        """
        self.input_frame = Frame(self.root)
        self.input_frame.pack()
        return

    def __create_browse_window_widgets(self) -> None:
        """日報入力画面のウィジェット作成
            NOTE: フレーム、ボタン、ラベルなどのウィジェットを作成する
                  ※pack()メソッドを呼び出すタイミングにも注意を払う必要がある
        """
        self.browse_frame = Frame(self.root)
        self.browse_frame.pack(side="top")
        _parent_canvas_frame = Frame(self.browse_frame)
        _parent_canvas_frame.update_idletasks()
        _parent_canvas_frame.grid(row=6,column=0,columnspan=5,sticky='w',pady=[20,10])
        _canvas = Canvas(
            _parent_canvas_frame, 
            width=self._WG_BROWSE_CANVAS_WIDTH,
            height=self._WG_BROWSE_CANVAS_HEIGHT,
            scrollregion=(self._SCRL_REGION_WEST, self._SCRL_REGION_NORTH, self._SCRL_REGION_EAST, self._SCRL_REGION_SOUTH)
        )
        _scrollbar = Scrollbar(_parent_canvas_frame,orient="vertical", command=_canvas.yview)
        self.scroll_frame = Frame(_canvas)
        _canvas.configure(yscrollcommand=_scrollbar.set)
        self.scroll_frame.pack(padx=[5,0])
        _scrollbar.pack(side="right", fill="y", padx=[10,0])
        _canvas.pack(side="left", fill="both", padx=[0,0])
        _canvas.create_window((0,0),window=self.scroll_frame,anchor="nw")
        return
        
        
    def create_input_page(self) -> None:
        # ウィジェット作成
        self.__create_input_window_widgets()

        self.change_page_button = Button(self.input_frame,text='日報閲覧',command=self.change_frame_browse,font=('meiryo',8),width=8)
        self.input_title = Label(self.input_frame,text='日報入力',font=('meiryo',15))
        self.work_date = WorkDate(self.input_frame)
        values = self.get_company_name()
        self.company = Company(self.input_frame,values=values)
        self.work_place = WorkPlace(self.input_frame)
        self.work_detail = WorkDetail(self.input_frame,80)
        self.worker = Worker(self.input_frame)
        self.worker_cost = WorkerCost(self.input_frame)
        self.material_cost = MaterialCost(self.input_frame)
        self.sales = Sales(self.input_frame)
        
        self.change_page_button.grid(row=1,column=4)
        self.input_title.grid(row=1,column=1,columnspan=4,pady=[30,30],padx=[10,20])
        self.work_date.label.grid(row=2,column=0,pady=20)
        self.work_date._textbox.grid(row=2,column=1,pady=20)
        self.company.label.grid(row=3,column=0,pady=20)
        self.company._conbobox.grid(row=3,column=1,pady=20,padx=[10,0])
        self.work_place.label.grid(row=3,column=2,pady=20)
        self.work_place._textbox.grid(row=3,column=3,pady=20)
        self.work_detail.label.grid(row=4,column=0,pady=20)
        self.work_detail._textbox.grid(row=4,column=1,columnspan=3,padx=[58,0],pady=20)
        self.worker.label.grid(row=5,column=0,pady=20)
        self.worker._conbobox.grid(row=5,column=1,pady=20,padx=[10,0])
        self.worker_cost.label.grid(row=5,column=2,pady=20)
        self.worker_cost._textbox.grid(row=5,column=3,pady=20)
        self.material_cost.label.grid(row=6,column=0,pady=20)
        self.material_cost._textbox.grid(row=6,column=1,pady=20)
        self.sales.label.grid(row=6,column=2,pady=20)
        self.sales._textbox.grid(row=6,column=3,pady=20)
        button = Button(self.input_frame,text='登録',command=self.add_data,font=('meiryo',15),width=15)
        button.grid(row=7,column=0,columnspan=4,pady=[30,0])
        return

    def create_browse_page(self) -> None:
        """データベースからの任意の情報を取得し、表示させる
        
            会社名 : company_name
            X月合計経費 : total_cost
            X月合計売上 : total_sales
            日付 : date
            現場名 : work_place
            作業員 : worker
            経費 : cost
            売上 : sales
            
        """
        # ウィジェット作成
        self.__create_browse_window_widgets()

        self.company_name = ""
        self.total_cost = "0"
        self.total_sales = "0"
        
        self.date = "2023/6/5"
        self.work_place = "下大利"
        self.worker = "0"
        self.cost = 1235
        self.sales = 55555
        self._change_page_button = Button(self.browse_frame,text='日報入力',command=self.change_frame_input,font=('meiryo',8),width=8)
        self.browes_title = Label(self.browse_frame,text='日報閲覧',font=('meiryo',15))
        values = self.get_company_name()
        self.company = Company(self.browse_frame,values=values)
        self.total_cost_label = Label(self.browse_frame,text="X月合計経費",font=('meiryo',10))
        self.show_total_cost = Label(self.browse_frame,text="¥"+self.total_cost,relief="sunken",anchor='e',width=35)
        self.total_sales_label = Label(self.browse_frame,text="X月合計売上",font=('meiryo',10))
        self.show_total_sales = Label(self.browse_frame,text="¥"+self.total_cost,relief="sunken",anchor='e',width=35)
        
        self.date_label = Label(self.browse_frame,text="日付",font=('meiryo',10),borderwidth=2,relief="ridge",width=9)
        self.work_place_label = Label(self.browse_frame,text="現場名",font=('meiryo',10),borderwidth=2,relief="ridge",padx=10,width=50)
        self.worker_label = Label(self.browse_frame,text="作業員数",font=('meiryo',10),borderwidth=2,relief="ridge",width=8)
        self.cost_label = Label(self.browse_frame,text="経費",font=('meiryo',10),borderwidth=2,relief="ridge",width=15)
        self.sales_label = Label(self.browse_frame,text="売上",font=('meiryo',10),borderwidth=2,relief="ridge",width=15)
        
        self._change_page_button.grid(row=1,column=4)
        self.browes_title.grid(row=1,column=1,columnspan=4,pady=[30,30],padx=[10,20])
        self.company.label.grid(row=2,column=0,pady=[20,10])
        self.company._conbobox.grid(row=2,column=1,sticky='w',padx=[30,0],pady=[20,10])
        self.total_cost_label.grid(row=3,column=0,pady=[10,10])
        self.show_total_cost.grid(row=3,column=1,pady=[10,10],columnspan=1,)
        self.total_sales_label.grid(row=3,column=2,pady=[10,10])
        self.show_total_sales.grid(row=3,column=3,pady=[10,10],columnspan=3)
        
        self.date_label.grid(row=5,column=0,sticky='we')
        self.work_place_label.grid(row=5,column=1,columnspan=2,sticky='we')
        self.worker_label.grid(row=5,column=2,sticky='e')
        self.cost_label.grid(row=5,column=3,sticky='we')
        self.sales_label.grid(row=5,column=4,sticky='we',padx=[0,5])
        
        for i in range(20):
            
            self.get_date_label = Label(self.scroll_frame,text="2023/6/7",font=('meiryo',10),borderwidth=2,relief="ridge",width=9)
            self.get_work_place_label = Label(self.scroll_frame,text="下大利",font=('meiryo',10),borderwidth=2,relief="ridge",anchor='w',padx=10,width=41)
            self.get_worker_label = Label(self.scroll_frame,text=i,font=('meiryo',10),borderwidth=2,relief="ridge",width=8,anchor='e')
            self.get_cost_label = Label(self.scroll_frame,text="2534",font=('meiryo',10),borderwidth=2,relief="ridge",width=15,anchor='e')
            self.get_sales_label = Label(self.scroll_frame,text="55000",font=('meiryo',10),borderwidth=2,relief="ridge",width=15,anchor='e')
            self.delete_button = Button(self.scroll_frame,text="削除",command=self.get_data)
            self.update_button = Button(self.scroll_frame,text="変更")

            self.get_date_label.grid(row=i,column=0,columnspan=1,sticky='we')
            self.get_work_place_label.grid(row=i,column=1,sticky='we')
            self.get_worker_label.grid(row=i,column=2)
            self.get_cost_label.grid(row=i,column=3)
            self.get_sales_label.grid(row=i,column=4)
            self.delete_button.grid(row=i,column=5,padx=[5,2])
            self.update_button.grid(row=i,column=6,padx=[2,5])

        return

    def change_frame_input(self) -> None:
        self.browse_frame.pack_forget()
        self.create_input_page()
        return
        
    def change_frame_browse(self) -> None:
        self.input_frame.pack_forget()
        self.create_browse_page()
        return

    def change_frame(self, now_frame,next_frame) -> None:
        self.now_frame = now_frame
        self.next_frame = next_frame
        self.now_frame.pack_forget()
        self.next_frame.pack()
        return

    def get_company(self):
        """登録済みの会社名をデータベースから取得
        """
        
        return 

    def add_data(self):
        """データベースに登録
        id -> primary_key
        date -> work_date
        comapany -> company
        work_place -> work_place
        work_detail -> work_detail
        worker -> worker
        worker_cost -> worker_cost
        material_cost -> material_cost
        sales -> sales
        """
        _req = DataRegistReq()
        _req.work_date = self.work_date.get_input_text()
        _req.company_name = self.company.get_input_text()
        _req.work_place = self.work_place.get_input_text()
        _req.work_contents = self.work_detail.get_input_text()
        _req.worker_num = self.worker.get_input_text()
        _req.worker_cost = self.worker_cost.get_input_text()
        _req.material_cost = self.material_cost.get_input_text()
        _req.proceeds = self.sales.get_input_text()
        
        print(f'add_data: execute:\n\
            work_date = {_req.work_date}\n\
            company_name = {_req.company_name}\n\
            work_place = {_req.work_place}\n\
            work_contents = {_req.work_contents}\n\
            worker_num = {_req.worker_num}\n\
            worker_cost = {_req.worker_cost}\n\
            material_cost = {_req.material_cost}\n\
            proceeds = {_req.proceeds}\n\
        ')

        s = self.app_data_mng.register(self.register_data)
        print(s)
        self.clear_input_area()
    
    def clear_input_area(self):
        self.work_date.delete_input_value()
        self.work_date.set_today()
        self.company.clear_field()
        self.work_place.delete_input_value()
        self.work_detail.delete_input_value()
        self.worker.clear_field()
        self.worker_cost.delete_input_value()
        self.material_cost.delete_input_value()
        self.sales.delete_input_value()
    
    def get_data(self):
        _req = DataFetchReq()
        _req.fetch.id = -1
        _req.fetch.company_name = "株式会社新栄輸送"
        print(self.fetch(self.fetch))
        data_list = self.app_data_mng.fetch(_req)
        
        # name_list = []
        # for v in data_list:
        #     name_list.append(v.company_name)
        #     for v in name_list:
        #        name_list[]
        
        
        # for i, v in enumerate(data_list):
        #     # print(i,v.company_name)
        #     # if v.company_name == name_list[i]:
        #     #     continue
        #     if len(name_list[1]) != v.company_name or name_list == []:
        #         name_list.append(v.company_name)
        # print(name_list[5],len(name_list),len(data_list))
        # print(name_list)
        
    def get_company_name(self) -> list[str]:
        _req = DataFetchReq()
        _req.id = -1
        data_list = self.app_data_mng.fetch(_req)
        name_list = []

        for data in data_list:
            # 名前リストに該当する名前が存在する場合は追加しない
            if data.company_name in name_list:
                continue

            # 名前リストに会社名を追加する
            name_list.append(data.company_name)
        
        print(f'get_company_name:\n\
            name_list = {name_list}\
        ')  
        return name_list

    def cyle(self) -> None:
        """メインウィンドウ処理
        """
        self.root.mainloop()
        return
            
if __name__ == "__main__":
    nippo_app_window = Window()
    nippo_app_window.cyle()