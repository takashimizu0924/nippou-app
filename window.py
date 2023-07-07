import tkinter as tk
import tkinter.ttk as ttk

root = tk.Tk()
root.title("業務管理アプリ")
root.geometry("1000x700+400+150")
root.resizable(False,False)

#アプリを終了する関数
def quit_app():
    root.quit()
    
#設定画面を開く関数
def open_setting():
    subwindow = tk.Toplevel()
    subwindow.title("設定")
    subwindow.geometry("500x500+600+300")
    
    subwindow_label = tk.Label(subwindow, text="設定画面です")
    subwindow_label.pack()

"""日報入力用関数"""
def open_add_inputdata():
    
    subwindow = tk.Toplevel()
    subwindow.title("日報入力")
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
    
#ツリービューの編集ボタン押下関数
def edit_data():
    selected_id = tree.selection()
    print(selected_id)


#ツリービューの削除ボタン押下関数
def delete_data():
    selected_id = tree.selection()
    for item_id in selected_id:
        tree.delete(item_id)
       
#ttk用スタイル
style = ttk.Style()
style.configure("TCombobox", fieldbackground="lightgray")
style.configure("Treeview.Heading", font=("meiryo", 12))
style.map(
    "Treeview",
    background=[
        ("selected", "gray")
    ]
)

#メニューバーを作成
menubar = tk.Menu(root)
root.config(menu=menubar)

#メニューバーの項目を作成
setting_menu = tk.Menu(menubar,tearoff=False)
menubar.add_cascade(label="設定",menu=setting_menu)

#メニューバー内のプルダウンを作成
setting_menu.add_command(label="日報登録",command=open_add_inputdata)
setting_menu.add_command(label="環境設定",command=open_setting)
setting_menu.add_command(label="終了",command=quit_app)





#閲覧ページ用フレームの作成
title_frame = tk.Frame(root, pady=20)
top_frame = tk.Frame(root, pady=10)
tree_frame = tk.Frame(root,pady=30)
button_frame = tk.Frame(root)
title_frame.pack()
top_frame.pack(fill="x")
tree_frame.pack(fill="y")
button_frame.pack()

#閲覧用ページ
#上部
page_title = tk.Label(title_frame,text="集計閲覧", font=("meiryo",15,"bold"))
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

tree = ttk.Treeview(tree_frame,height=15)
tree['columns'] = (1, 2, 3, 4, 5)
tree['show'] = 'headings'

#ツリービューのカラムの設定
tree.column(1, width=80)
tree.column(2, width=500)
tree.column(3, width=75, anchor=tk.E)
tree.column(4, width=150, anchor=tk.E)
tree.column(5, width=150, anchor=tk.E)



#ツリービューのカラムの見出し設定
tree.heading(1, text="日付")
tree.heading(2, text="現場名")
tree.heading(3, text="作業員数")
tree.heading(4, text="経費")
tree.heading(5, text="売上")

#ツリービューにデータの追加
# tree.insert("","end",values=("2023/6/24","食料品","4500"))
# tree.insert("","end",values=("2023/6/24","食料品","4500"))
# tree.insert("","end",values=("2023/6/24","食料品","4500"))
for i in range(50):
    tree.insert("","end", values=("2023/6/26", "ＲＧ石城町", "1", "20,000", "50,000"))


#スクロールバーを作成
scroll_v = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
scroll_v.grid(row=0, column=1, sticky=tk.NS)

# scroll_h = ttk.Scrollbar(tree_frame, orient="horizontal", command=tree.xview)
# scroll_h.grid(row=1,column=0, sticky=tk.EW)
tree.configure(yscrollcommand=scroll_v.set)
tree.grid(row=0, column=0, sticky=tk.NSEW)

add_button = tk.Button(button_frame, text="追加", width=10, command=open_add_inputdata)
edit_button = tk.Button(button_frame, text="編集", width=10, command=edit_data)
del_button = tk.Button(button_frame, text="削除", width=10, background="red", command=delete_data)
add_button.grid(row=0, column=0, padx=30)
edit_button.grid(row=0, column=1, padx=30)
del_button.grid(row=0, column=2, padx=30)

root.mainloop()