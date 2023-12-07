from tkinter import *
from tkinter import messagebox

cod = Tk()
cod.geometry("500x450")
cod.title("TO-DO-LIST")
cod.config(bg='#EDE60E')

def add_tsk():
    task = entry.get()
    if task != "":
        lb.insert(END, task)
        entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Enter a task")

def remove_tsk():
    lb.delete(ANCHOR)

fr = Frame(cod)
fr.pack(pady = 10)

lb = Listbox(
     fr, width=25, height=8, font=('Times',20),bd=2,fg="#B70EED",highlightthickness=0, selectbackground="#0EED75",activestyle="none",
)
lb.pack(side = "left", fill= BOTH)

task = [
    'xyz',
    'abc',
]

for item in task:
    lb.insert(END, item)

bar = Scrollbar(fr)
bar.pack(side="right", fill=BOTH)

lb.config(yscrollcommand=bar.set)
bar.config(command=lb.yview)


entry = Entry(
    cod,font=('Times', 24)
)

entry.pack(pady = 20)

button = Frame(cod)
button.pack(pady=20)

newtask_btn = Button(
    button,text = "Add Task", font=("Times",12),bg="#c5f776",padx=20, pady=10, command= add_tsk
)

newtask_btn.pack(fill=BOTH, expand=True, side= LEFT)

deltask_btn = Button(
    button,text = "Delet Task", font=("Times",12),bg="#ff8b61",padx=20, pady=10, command= remove_tsk
)

deltask_btn.pack(fill=BOTH, expand=True, side= LEFT)


cod.mainloop()

