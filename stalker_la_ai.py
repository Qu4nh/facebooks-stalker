import os
import tkinter as tk
from tkinter import messagebox
import webbrowser

current_directory = os.path.dirname(os.path.abspath(__file__))
input_file_path = os.path.join(current_directory, 'input.txt')

# Input

if os.path.exists(input_file_path) and os.path.getsize(input_file_path) > 0:
    with open(input_file_path, encoding='utf-8') as file:
        content = file.read()

    buddy_id = 'buddy_id'
    count = 0
    index = 0
    result_list = []

    # Đếm và đẩy vào mảng
    
    while index < len(content):
        index = content.find(buddy_id, index)
        if index == -1:
            break
        if count % 2 != 0:
            result_list.append(content[index+len(buddy_id)+3:index+len(buddy_id)+18])
        index += len(buddy_id)
        count += 1

    # Tạo cửa sổ
    
    root = tk.Tk()
    root.withdraw()
    root.wm_attributes("-topmost", 1) 
    
    for i, buddy in enumerate(result_list):
        answer = messagebox.askyesno("Count stalker (@Qu4nh)", f"Mở profile người #{i+1}\n\n") # Mở cửa sổ
        if not answer:
            break  # Đóng cửa sổ
        webbrowser.open(f"https://www.facebook.com/{buddy}")
    pass
else:
    messagebox.showinfo("Thông báo", "Tệp 'input.txt' không tồn tại hoặc trống. \nHãy đọc kĩ README")
