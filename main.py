import tkinter as tk
import subprocess
root = tk.Tk()
root.title("比大小")
def ft ():
  number1 = 0.8
  number2 = 0.11
  if number1 > number2:
    label.config(text=number1 + "大")
  elif number1 < number2:
    label.config(text=number2 + "大")
  elif number1 == number2:
    label.config(text="两个数字相等")

def comparison():
       number1 = entry1.get()
       number2 = entry2.get()
       if number1 == "" and number2 == "":
           label.config(text="请输入两个数字")
           return
       if number1 == "":
           label.config(text="请输入第一个数字")
           return
       if number2 == "":
           label.config(text="请输入第二个数字")
           return
       if number1 > number2:
           label.config(text=number1 + "大")
       elif number1 < number2:
        label.config(text=number2 + "大")
       elif number1 == number2:
        label.config(text="两个数字相等")
#debug
          
root.geometry("400x200")
label = tk.Label(root, text="请输入两个数字：")
label.pack()
entry1 = tk.Entry(root)
entry1.pack()
entry2 = tk.Entry(root)
entry2.pack()
button = tk.Button(root, text="比较", command=comparison)
button.pack()
button2 = tk.Button(root, text="关闭", command=root.destroy)
button2.pack()
root.mainloop()
