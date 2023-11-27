from tkinter import *
from tkinter import filedialog


def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text File","*.txt"),
                                                     ("Log File","*.log"),
                                                     ("All File","*.*")]
                                          )

    if not filepath:
        return
    
    text.delete("1.0",END)

    with open(filepath,mode='r',encoding='utf-8') as f:
        txt = f.read()
        text.insert(END,txt)
        root.title(f"{filepath}")

def save_as():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text File", "*.txt"), ("Custom Files", "*.*")])
    if not filepath:
        return
    with open(filepath, mode='w', encoding='utf-8') as f:
        txt = text.get("1.0", "end")
        f.write(txt)
    root.title(filepath)
    

root = Tk()
root.title("Text Editor")

text = Text(root,fg="black",bg="white",font="Calibri 14")
text.pack()
menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu, tearoff=False)

menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save As", command=save_as)

root.mainloop()

