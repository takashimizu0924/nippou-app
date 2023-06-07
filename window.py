import tkinter as tk
import textbox as tb

import database_ctrl
import app_data_control as ctl

class Window():
    
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.width = 1000
        self.height = 600
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.title("日報兼売上管理アプリ")
        self.root.resizable(width=False,height=False)
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack()
        self.browse_frame = tk.Frame(self.root)
        # self.change_frame_input()
        self.input_window()
        self.root.mainloop()
        
    def input_window(self):
        self.change_page_button = tk.Button(self.input_frame,text='日報閲覧',command=self.change_frame_browse,font=('meiryo',8),width=8)
        self.input_title = tk.Label(self.input_frame,text='日報入力',font=('meiryo',15))
        self.work_date = tb.WorkDate(self.input_frame)
        self.company = tb.Company(self.input_frame)
        self.work_place = tb.WorkPlace(self.input_frame)
        self.work_detail = tb.WorkDetail(self.input_frame,80)
        self.worker = tb.Worker(self.input_frame)
        self.worker_cost = tb.WorkerCost(self.input_frame)
        self.material_cost = tb.MaterialCost(self.input_frame)
        self.sales = tb.Sales(self.input_frame)
        
        self.change_page_button.grid(row=0,column=4,pady=(20,0))
        self.input_title.grid(row=1,column=0,columnspan=4,pady=[30,30])
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
        button = tk.Button(self.input_frame,text='登録',command=self.add_data,font=('meiryo',15),width=15)
        button.grid(row=7,column=0,columnspan=4,pady=[30,0])

    def browse_window(self):
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
        self.company_name = ""
        self.total_cost = "0"
        self.total_sales = "0"
        
        self.date = "2023/6/5"
        self.work_place = "下大利"
        self.worker = "0"
        self.cost = 1235
        self.sales = 55555
        self.change_page_button = tk.Button(self.browse_frame,text='日報入力',command=self.change_frame_input,font=('meiryo',8),width=8)
        self.browes_title = tk.Label(self.browse_frame,text='日報閲覧',font=('meiryo',15))
        self.company = tb.Company(self.browse_frame)
        self.total_cost_label = tk.Label(self.browse_frame,text="X月合計経費",font=('meiryo',10))
        self.show_total_cost = tk.Label(self.browse_frame,text="¥"+self.total_cost,relief="sunken",anchor=tk.E,width=35)
        self.total_sales_label = tk.Label(self.browse_frame,text="X月合計売上",font=('meiryo',10))
        self.show_total_sales = tk.Label(self.browse_frame,text="¥"+self.total_cost,relief="sunken",anchor=tk.E,width=35)
        
        self.date_label = tk.Label(self.browse_frame,text="日付",font=('meiryo',10),borderwidth=2,relief="ridge")
        self.work_place_label = tk.Label(self.browse_frame,text="現場名",font=('meiryo',10),borderwidth=2,relief="ridge",padx=10,width=60)
        self.worker_label = tk.Label(self.browse_frame,text="作業員数",font=('meiryo',10),borderwidth=2,relief="ridge",width=8)
        self.cost_label = tk.Label(self.browse_frame,text="経費",font=('meiryo',10),borderwidth=2,relief="ridge")
        self.sales_label = tk.Label(self.browse_frame,text="売上",font=('meiryo',10),borderwidth=2,relief="ridge")
        
       
        # self.change_page_button.pack(side='top',anchor=tk.E)
        # # self.change_page_button.place(x=700,y=50)
        # self.browes_title.pack()
        # self.company.label.pack(side='top',anchor=tk.W)
        # self.company._conbobox.pack(side='top',anchor=tk.W)
        # self.total_cost_label.pack()
        # self.show_total_cost.pack()
        # self.total_sales_label.pack()
        # self.show_total_sales.pack()
        
        # self.date_label.pack()
        # self.work_place_label.pack()
        # self.worker_label.pack()
        # self.cost_label.pack()
        # self.sales_label.pack()
        
        self.change_page_button.grid(row=0,column=5,sticky=tk.E,pady=[20,10])
        # self.change_page_button.place(x=700,y=50)
        self.browes_title.grid(row=1,column=1,columnspan=4,pady=[30,30],padx=[10,20])
        self.company.label.grid(row=2,column=0,pady=[20,10])
        self.company._conbobox.grid(row=2,column=1,sticky=tk.W,padx=[30,0],pady=[20,10])
        self.total_cost_label.grid(row=3,column=0,pady=[10,10])
        self.show_total_cost.grid(row=3,column=1,pady=[10,10],columnspan=1,)
        self.total_sales_label.grid(row=3,column=2,pady=[10,10])
        self.show_total_sales.grid(row=3,column=3,pady=[10,10],columnspan=3)
        
        self.date_label.grid(row=5,column=0,sticky=tk.W+tk.E)
        self.work_place_label.grid(row=5,column=1,columnspan=2,sticky=tk.W+tk.E)
        self.worker_label.grid(row=5,column=2,sticky=tk.E)
        self.cost_label.grid(row=5,column=3,sticky=tk.W+tk.E)
        self.sales_label.grid(row=5,column=4,sticky=tk.W+tk.E)
        
        self.get_date_label = tk.Label(self.browse_frame,text="2023/6/7",font=('meiryo',10),borderwidth=2,relief="ridge")
        self.get_work_place_label = tk.Label(self.browse_frame,text="下大利",font=('meiryo',10),borderwidth=2,relief="ridge",anchor=tk.W,padx=10)
        self.get_worker_label = tk.Label(self.browse_frame,text="0",font=('meiryo',10),borderwidth=2,relief="ridge",width=8,anchor=tk.E)
        self.get_cost_label = tk.Label(self.browse_frame,text="2534",font=('meiryo',10),borderwidth=2,relief="ridge",width=15,anchor=tk.E)
        self.get_sales_label = tk.Label(self.browse_frame,text="55000",font=('meiryo',10),borderwidth=2,relief="ridge",width=15,anchor=tk.E)
        self.delete_button = tk.Button(self.browse_frame,text="削除")
        self.update_button = tk.Button(self.browse_frame,text="変更")
        
        self.get_date_label.grid(row=6,column=0,columnspan=1,sticky=tk.W+tk.E)
        self.get_work_place_label.grid(row=6,column=1,columnspan=2,sticky=tk.W+tk.E)
        self.get_worker_label.grid(row=6,column=2,sticky=tk.E)
        self.get_cost_label.grid(row=6,column=3,sticky=tk.W+tk.E)
        self.get_sales_label.grid(row=6,column=4,sticky=tk.W+tk.E)
        self.delete_button.grid(row=6,column=5)
        self.update_button.grid(row=6,column=6)
        
        
    
    def change_frame_input(self):
        self.browse_frame.pack_forget()
        self.input_frame.pack()
        self.input_window()
        
    def change_frame_browse(self):
        self.input_frame.pack_forget()
        self.browse_frame.pack()
        self.browse_window()
        
    def change_frame(self, now_frame,next_frame):
        self.now_frame = now_frame
        self.next_frame = next_frame
        self.now_frame.pack_forget()
        self.next_frame.pack()
        
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
        
        self.ctl = ctl.AppDataControl
        self.register_data = ctl.DataRegistReq()
        # self.register_data.work_date = self.work_date
        # self.register_data.company_name = self.company_name
        # self.register_data.work_place = self.work_place
        # self.register_data.work_contents = self.work_detail
        # self.register_data.worker_num = self.worker
        # self.register_data.worker_cost = self.worker_cost
        # self.register_data.material_cost = self.material_cost
        # self.register_data.proceeds = self.sales
        
        self.register_data.work_date = "2023/6/7"
        self.register_data.company_name = "株式会社ラグレス"
        self.register_data.work_place = "福岡市東区松島１丁目"
        self.register_data.work_contents = "専用回路増設工事"
        self.register_data.worker_num = 1
        self.register_data.worker_cost = 15000
        self.register_data.material_cost = 2500
        self.register_data.proceeds = 55000
        
        s = self.ctl.register(self.ctl,req=self.register_data)
        print(s)
    
    def get_data(self):
        return
            
if __name__ == "__main__":
    Window()