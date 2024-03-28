import tkinter as tk

window = tk.Tk()

text_box = tk.Text()
text_box.pack()

text_box.insert("1.0", "Good")
text_box.insert("2.0", "\nMorning")



window.mainloop()