import tkinter as tk

window = tk.Tk()

frame1 = tk.Frame(master=window, width=100,bg="blue")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame2 = tk.Frame(master=window, width=50,bg="purple")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frame3 = tk.Frame(master=window, width=25, bg="green")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


# frame3 = tk.Frame(master=window, width=25, bg="green")
# frame3.pack(fill=tk.Y, side=tk.LEFT)

window.mainloop()

# frame1 = tk.Frame(master=window, height=100,bg="blue")
# frame1.pack(fill=tk.X)

# frame2 = tk.Frame(master=window, height=50,bg="purple")
# frame2.pack(fill=tk.X)

# frame3 = tk.Frame(master=window, height=25,bg="green")
# frame3.pack(fill=tk.X)