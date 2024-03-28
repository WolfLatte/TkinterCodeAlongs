import tkinter as tkin

window = tkin.Tk()
window.title("Widget")
label_ein = tkin.Label(
    window,
    text="Hello, World",
    fg="Medium Purple",
    background="Dark Orchid4",
    width=20,
    height=10,
)
label_ein.pack()


button_ein=tkin.Button(window,text="Click Here!")
button_ein.pack()

user=tkin.Entry(window)
user.pack()
user.insert(0, "World")
user.insert(0, "Hello, ")

some_text=user.get()
print(some_text)
user.delete(0)
user.delete(0,4)
user.delete(0,tkin.END)



window.mainloop()
