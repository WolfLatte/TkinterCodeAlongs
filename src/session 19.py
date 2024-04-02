import tkinter as tk

# window = tk.Tk()

# text_box = tk.Text()
# text_box.pack()

# #first number is line num and second is char num

# text_box.insert("1.0", "Good")
# text_box.insert("2.0", "\nMorning")
# text_box.insert(tk.END,"\nDarling")

# text_box.delete("1.0")

# newtext=text_box.get("1.0")
# newtext=text_box.get("1.0",tk.END)
# print(newtext)


# window.mainloop()

# frm_a=tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
# frm_b=tk.Frame()

# lab1=tk.Label(master=frm_a, text="Im a Frame")
# lab1.pack()
# lab2=tk.Label(master=frm_b, text="Im also a Frame")
# lab2.pack()

# frm_a.pack()
# frm_b.pack()

# window.mainloop()

top = tk.Tk()

B1 = tk.Button(top, text ="FLAT", relief=tk.FLAT )
B2 = tk.Button(top, text ="RAISED", relief=tk.RAISED )
B3 = tk.Button(top, text ="SUNKEN", relief=tk.SUNKEN )
B4 = tk.Button(top, text ="GROOVE", relief=tk.GROOVE )
B5 = tk.Button(top, text ="RIDGE", relief=tk.RIDGE )

B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
top.mainloop()
top.mainloop()