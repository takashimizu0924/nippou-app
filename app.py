import tkinter as tk
import frame as fr
import textbox as tb
from tkinter import messagebox



class Window():
    def __init__(self):
       self.root = tk.Tk()
       self.width = 1000
       self.height = 600
       self.root.geometry(f"{self.width}x{self.height}")
       self.root.title("日報兼売上管理アプリ")
       self.root.resizable(width=False,height=False)
       
       self.input_frame_inst = fr.InputFrame(self.root)
       self.input_frame = self.input_frame_inst.get_frame()
       self.input_frame.pack(padx=[70,0])
       
       self.browse_frame_inst = fr.BrowseFrame(self.root)
       self.browse_frame = self.browse_frame_inst.get_frame()
       self.browse_frame.pack(padx=[70,0])
       """       日報入力フレーム         """
       self.change_page_button = tk.Button(self.input_frame,text='日報閲覧',command=self.change_frame_browes,font=('meiryo',8),width=8)
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
       button = tk.Button(self.input_frame,text='登録',command=self.debag_print,font=('meiryo',15),width=15)
       button.grid(row=7,column=0,columnspan=4,pady=[30,0])
       
       """       日報閲覧フレーム         """
       self.change_page_button = tk.Button(self.browse_frame,text='日報入力',command=self.change_frame_input,font=('meiryo',8),width=8)
       self.browes_title = tk.Label(self.browse_frame,text='日報閲覧',font=('meiryo',15))
       self.company = tb.Company(self.browse_frame)
       
       self.change_page_button.grid(row=0,column=4,pady=(20,0))
       self.browes_title.grid(row=1,column=0,columnspan=4,pady=[30,30])
       self.company.label.grid(row=2,column=0,pady=20)
       self.company._conbobox.grid(row=2,column=1,columnspan=4,pady=20,padx=[10,0])
       
       self.root.mainloop()
    def debag_print(self):
        work_date = self.work_date.get_input_text()
        company = self.company.get_input_text()
        work_place = self.work_place.get_input_text()
        work_detail = self.work_detail.get_input_text()
        worker = self.worker.get_input_text()
        worker_cost = self.worker_cost.get_input_text()
        material_cost = self.material_cost.get_input_text()
        sales = self.sales.get_input_text()
        self.input_values = [work_date,company,work_place,work_detail]
        print(self.input_values)
        l = []
        for self.value in self.input_values:
            if self.value == "":
                l.append(self.value)

        if 0 < len(l):
            messagebox.showwarning("確認","全項目入力してください")
      
        else:
            self.work_date.delete_input_value()
            self.company.delete_input_value()
            self.work_place.delete_input_value()
            self.work_detail.delete_input_value()
            self.worker.delete_input_value()
            self.worker_cost.delete_input_value()
            self.material_cost.delete_input_value()
            self.sales.delete_input_value()
            
    def change_frame_input(self):
        print("change")
        self.browse_frame.pack_forget()
        self.input_frame.pack(padx=[70,0])
    
    def change_frame_browes(self):
        self.input_frame.pack_forget()
        self.browse_frame.pack(padx=[70,0])
            
    # def change_frame(self):
    #     if self.input_frame:
    #         self.input_frame.pack()
    #         self.browse_frame.pack_forget()
    #     else:
    #         self.input_frame.pa
        # print(frame)
        # if frame == self.browse_frame:
        #     self.input_frame.pack(padx=[70,0])
        #     self.browse_frame.pack_forget()
        # else:
        #     self.input_frame.pack_forget()
        #     self.browse_frame.pack(padx=[70,0])
                
        
        

    
if __name__ == "__main__":
    Window()