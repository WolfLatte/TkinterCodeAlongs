import tkinter as tk

# window = tk.Tk()

# frame1 = tk.Frame(master=window, width=100,bg="blue")
# frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# frame2 = tk.Frame(master=window, width=50,bg="purple")
# frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

# frame3 = tk.Frame(master=window, width=25, bg="green")
# frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)


# frame3 = tk.Frame(master=window, width=25, bg="green")
# frame3.pack(fill=tk.Y, side=tk.LEFT)

# window.mainloop()

# frame1 = tk.Frame(master=window, height=100,bg="blue")
# frame1.pack(fill=tk.X)

# frame2 = tk.Frame(master=window, height=50,bg="purple")
# frame2.pack(fill=tk.X)

# frame3 = tk.Frame(master=window, height=25,bg="green")
# frame3.pack(fill=tk.X)

##################

# window = tk.Tk()

# frame1 = tk.Frame(master=window, width=150, height=150,bg="blue")
# frame1.pack()

# label1=tk.Label(master=frame1,text="Im at (0,0)", bg="purple")
# label1.place(x=0,y=0)


# label2=tk.Label(master=frame1,text="Im at (75,75)", bg="purple")
# label2.place(x=75,y=75)

########## 3x3 frames
# window = tk.Tk()
# for i in range(3):
#     window.columnconfigure(i,weight=1,minsize=80)
#     window.rowconfigure(i,weight=1,minsize=60)
#     for m in range(3):
#         frame=tk.Frame(
#             master=window, 
#             relief=tk.RAISED,
#             borderwidth=10,
#             bg="blue"
#         )
#         frame.grid(row=i,column=m,padx=5,pady=5)
#         label=tk.Label(master=frame,text=f"Row {i} \n Column{m}")
#         label.pack(padx=5,pady=5)
# window.mainloop()

window = tk.Tk()

window.columnconfigure([0,1,2,3],weight=1, minsize=50)
window.rowconfigure(0, weight=1,minsize=50)

label1=tk.Label(text="A", bg="purple",fg="white")
label2=tk.Label(text="B", bg="purple",fg="white")
label3=tk.Label(text="C", bg="purple",fg="white")
label4=tk.Label(text="D", bg="purple",fg="white")

label1.grid(row=0,column=0)
label2.grid(row=0,column=1,sticky="ew")
label3.grid(row=0,column=2,sticky="ns")
label4.grid(row=0,column=3,sticky="nsew")

window.mainloop()