import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from datetime import datetime as dt 


# テキストボックスの基底クラスを作成
# 工事日テキストボックスクラス
class TextBox:
    def __init__(self, frame, label_text:str, box_width:int, defalut_text:str = "") -> None:
        self.label = tk.Label(frame,text=label_text,font=('meiryo',10))
        self.input_entry = tk.StringVar()
        if box_width <= 0:
            self._textbox = tk.Entry(frame,textvariable=self.input_entry,font=('meiryo',10),bg='lightgrey')
        else:
            self._textbox = tk.Entry(frame,textvariable=self.input_entry,font=('meiryo',10),bg='lightgrey',width=box_width)
        self.input_combo = tk.StringVar()
        if not defalut_text == "":
            self._textbox.insert(0,defalut_text)

    def get_input_text(self) -> str:
        return self._textbox.get()
    
    def delete_input_value(self) -> None:
        self._textbox.delete(0,tk.END)
        return
    
    def validate_input_text(self) -> str:
        self.input_text = self._textbox.get()
        if self.input_text == "":
            messagebox.showwarning("確認","全項目入力してください")
        return self.input_text


class Title(TextBox):
    def __init__(self, frame, box_width=0) -> None:
        self.label_text = "日報入力"
        super().__init__(frame, self.label_text, box_width)   
        
          
class WorkDate(TextBox):
    def __init__(self, frame, box_width=0) -> None:
        self.label_text = "工事日"
        tdatetime = dt.now() 
        tstr = tdatetime.strftime('%Y/%m/%d')
        defalut_text = tstr
        super().__init__(frame,self.label_text,box_width,defalut_text)
    

class Company(TextBox):
    def __init__(self, frame, box_width=0,values=[]) -> None:
        s = ttk.Style()
        s.theme_use('default')
        s.configure('Combo.TCombobox',fieldbackground="lightgrey")
        self.label_text = "会社名"
        super().__init__(frame,self.label_text,box_width)
        self._conbobox = ttk.Combobox(frame,textvariable=self.input_combo,values=values,font=('meiryo',10),style='Combo.TCombobox',)
        self._conbobox.bind(
            '<<ComboboxSelected>>', 
            self.selected_cb
        )

    def selected_cb(self, event) -> None:
        print("Pressed")
        return
    
    def get_input_text(self) -> str:
        self.input_text = self.input_combo.get()
        if self.input_text == "":
            messagebox.showwarning("確認","'"+self.label_text+"'"+"は必ず入力するかプルダウンから選択してください")
        else:
            return str(self.input_text)


class WorkPlace(TextBox):
    def __init__(self, frame, box_width=0) -> None:
        self.label_text = "現場名"
        super().__init__(frame,self.label_text,box_width)


class WorkDetail(TextBox):
    def __init__(self, frame, box_width=0) -> None:
        self.label_text = "作業内容"
        super().__init__(frame,self.label_text,box_width)


class Worker(TextBox):
    def __init__(self, frame, box_width=0) -> None:
        self.label_text = "作業員"
        s = ttk.Style()
        s.theme_use('default')
        s.configure('Combo.TCombobox',fieldbackground="lightgrey")
        super().__init__(frame,self.label_text,box_width)
        self.option = [0,1,2,3,4,5,6,7,8,9,10]
        self._conbobox = ttk.Combobox(frame,textvariable=self.input_combo,values=self.option,font=('meiryo',10),style='Combo.TCombobox',)

    def get_input_text(self) -> str:
        self.input_text = self.input_combo.get()
        if self.input_text == "":
            messagebox.showwarning("確認","'"+self.label_text+"'"+"は必ず入力するかプルダウンから選択してください")
        else:
            return str(self.input_text)


class WorkerCost(TextBox):
    def __init__(self, frame, box_width=0) -> None:
        self.label_text = "作業員代"
        super().__init__(frame,self.label_text,box_width)

    def get_input_text(self) -> int:
        self.input_text = self._textbox.get()
        if self.input_text == "":
            messagebox.showwarning("確認","'"+self.label_text+"'"+"は数値で入力してください")
        else:
            return int(self.input_text)


class MaterialCost(TextBox):
    def __init__(self, frame, box_width=0) -> None:
        self.label_text = "材料費"
        super().__init__(frame,self.label_text,box_width)

    def get_input_text(self) -> int:
        self.input_text = self._textbox.get()
        if self.input_text == "":
            messagebox.showwarning("確認","'"+self.label_text+"'"+"は数値で入力してください")
        else:
            return int(self.input_text)


class Sales(TextBox):
    def __init__(self, frame, box_width=0) -> None:
        self.label_text = "売上"
        super().__init__(frame,self.label_text,box_width)

    def get_input_text(self) -> int:
        self.input_text = self._textbox.get()
        if self.input_text == "":
            messagebox.showwarning("確認","'"+self.label_text+"'"+"は数値で入力してください")
        else:
            return int(self.input_text)       