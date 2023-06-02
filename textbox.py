import tkinter as tk
import tkinter.ttk as ttk

# テキストボックスの基底クラスを作成
# 工事日テキストボックスクラス
class TextBox:
    def __init__(self, frame, label_text:str, box_width:int) -> None:
        self.label = tk.Label(frame,text=label_text,font=('meiryo',10))
        self.input_entry = tk.StringVar()
        if box_width <= 0:
            self._textbox = tk.Entry(frame,textvariable=self.input_entry,font=('meiryo',10),bg='lightgrey')
        else:
            self._textbox = tk.Entry(frame,textvariable=self.input_entry,font=('meiryo',10),bg='lightgrey',width=box_width)
        self.input_combo = tk.StringVar()
        self._conbobox = ttk.Combobox(frame,textvariable=self.input_combo,font=('meiryo',10),background='lightgrey')

    def get_input_text(self) -> str:
        return self._textbox.get()
    
    def delete_input_value(self) -> None:
        self._textbox.delete(0,tk.END)
        return
    
    # def label_pack(self):
    #     return self.label.pack()

    
    # def textbox_pack(self):
    #     self._textbox.pack()
    #     return
    
class Title(TextBox):
    def __init__(self, frame, box_width=0) -> None:
        self.label_text = "日報入力"
        super().__init__(frame, self.label_text, box_width)   
        
          
class WorkDate(TextBox):
    def __init__(self, frame, box_width=0) -> None:
        self.label_text = "工事日"
        super().__init__(frame,self.label_text,box_width)
    

class Company(TextBox):
    def __init__(self, frame, box_width=0) -> None:
        self.label_text = "会社名"
        super().__init__(frame,self.label_text,box_width)

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
        super().__init__(frame,self.label_text,box_width)

class WorkerCost(TextBox):
    def __init__(self, frame, box_width=0) -> None:
        self.label_text = "作業員代"
        super().__init__(frame,self.label_text,box_width)
    
    def get_input_text(self) -> int:
        return int(self._textbox.get())


class MaterialCost(TextBox):
    def __init__(self, frame, box_width=0) -> None:
        self.label_text = "材料費"
        super().__init__(frame,self.label_text,box_width)
    
    def get_input_text(self) -> int:
        return int(self._textbox.get())

        
class Sales(TextBox):
    def __init__(self, frame, box_width=0) -> None:
        self.label_text = "売上"
        super().__init__(frame,self.label_text,box_width)

    def get_input_text(self) -> int:
        return int(self._textbox.get())
