import tkinter
import os
from tkinter import filedialog
def file_select():
    filename = filedialog.askopenfilename(initialdir = " / ",title = "Выберите фаил:",
                                          filetypes = (("Текстовый фаил",".txt"),
                                                       ("Все файлы","*")))
    text["text"] = text["text"] +  " " + filename
    os.startfile(filename)

window = tkinter.Tk() # создание окошка
window.title("Проводник")# создание названия окошка
window.geometry("550x550")
window.configure(bg="white")
#window.resizable(False,False)# запрет на изменения размера окошка пользователем
text = tkinter.Label(window, text="Файл:", height=5, width=70, background="silver",foreground="black")
# создание в окошке графы  с названием и с определенными размерами
text.grid(column=1, row=1)#место расположения кнопки в первой строке и первой колонке
button_select=tkinter.Button(window, width=20, height=3, text="Выбрать файл",background="green",foreground="silver",
                             command=file_select)
button_select_1=tkinter.Button(window, width=20, height=3, text="Выбрать файл",background="green",foreground="silver",
                             command=file_select)
# создание кнопки с названием
button_select.grid(column=1, row=2,pady=10)
button_select_1.grid(column=1, row=3,pady=10)
window.mainloop()# запуск окна