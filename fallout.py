from tkinter import *
from tkinter import ttk
from tkinter import font
import loader

difc = {"легкая":6,"средняя":8,"сложная":10,"1":6,"2":8,"3":10}
root = Tk()
root.title("ахах")
root.geometry("1300x700")
root["bg"]= "#%02x%02x%02x" % (11,35,26)
font_Main = font.Font(family= "systemfixed", size=30)
font_symbs = font.Font(family= "systemfixed", size=20)
global lives
lives = 4
selected_dif = 0

while True:
    print("Выберете сложность:\n1.Легкая\n2.Средняя\n3.Сложная")
    user_input = str(input())
    
    try:
        selected_dif = int(difc[user_input.lower])
    except KeyError:
        try:
            selected_dif = int(difc[user_input])
        except:
            print("Неправильное значение")
            continue
    break
        
final, answer, outline_words = loader.gen(selected_dif)

'''
обработка попытки (активируется при нажатии кнопки ввода)
'''

def clicked():
    global lives
    user_try=entry.get()
    if user_try==answer:
        lab3["text"]+=">Вход в систему"
    elif user_try in outline_words:
        lives-=1
        lab113["text"] = lives
        lab143["text"] = " [] " * lives
        cur = list(answer)
        u_try = list(user_try)
        w_set = []
        for i in range(len(cur)):
            if cur[i] == u_try[i]:
                w_set.append(cur[i])
        lab3["text"] += str(user_try) + "\nОтказ в доступе\n" + str(len(set(w_set)))+'/'+str(len(cur))+" правильно\n"
    else:
        lab3["text"]+="\n>Ошибка"




'''
Первый ряд в сетке символов, задает общий размер столбцов сетки
'''


lab11 = ttk.Label(font=font_Main,  foreground="#%02x%02x%02x" % (29,217,109), background="#%02x%02x%02x" % (11,35,26))
lab11["text"] = "ROBCO  "
lab11.grid(row=0,column=0)

lab12 = ttk.Label(font=font_Main,  foreground="#%02x%02x%02x" % (29,217,109), background="#%02x%02x%02x" % (11,35,26))
lab12["text"] = "INDUSTRIES(TM)"
lab12.grid(row=0,column=1)

lab13 = ttk.Label(font=font_Main,  foreground="#%02x%02x%02x" % (29,217,109), background="#%02x%02x%02x" % (11,35,26))
lab13["text"] = "  TERMLINK"
lab13.grid(row=0,column=2)

lab14 = ttk.Label(font=font_Main,  foreground="#%02x%02x%02x" % (29,217,109), background="#%02x%02x%02x" % (11,35,26))
lab14["text"] = "  PROTOCOL"
lab14.grid(row=0,column=3)

lab15 = ttk.Label(font=font_Main,  foreground="#%02x%02x%02x" % (11,35,26), background="#%02x%02x%02x" % (11,35,26))
lab15["text"] = "=="
lab15.grid(row=0,column=4) 


'''
второй ряд сетки, отображает количество попыток
'''

lab113 = ttk.Label(font=font_Main,  foreground="#%02x%02x%02x" % (29,217,109), background="#%02x%02x%02x" % (11,35,26))
lab113["text"] = lives
lab113.grid(row=1,column=0)

lab123 = ttk.Label(font=font_Main,  foreground="#%02x%02x%02x" % (29,217,109), background="#%02x%02x%02x" % (11,35,26))
lab123["text"] = "  ПОПЫТОК"
lab123.grid(row=1,column=1)

lab133 = ttk.Label(font=font_Main,  foreground="#%02x%02x%02x" % (29,217,109), background="#%02x%02x%02x" % (11,35,26))
lab133["text"] = "  ОСТАЛОСЬ"
lab133.grid(row=1,column=2)

lab143 = ttk.Label(font=font_Main,  foreground="#%02x%02x%02x" % (29,217,109), background="#%02x%02x%02x" % (11,35,26))
lab143["text"] = "[] [] [] []"
lab143.grid(row=1,column=3)

lab153 = ttk.Label(font=font_Main,  foreground="#%02x%02x%02x" % (11,35,26), background="#%02x%02x%02x" % (11,35,26))
lab153["text"] = "=="
lab153.grid(row=1,column=4)


'''
первый косметический столбец, содержит номера рандомных ячеек липовой памяти
'''

pam1 = ttk.Label(font=font_symbs,  foreground="#%02x%02x%02x" % (29,217,109),background="#%02x%02x%02x" % (11,35,26))
pam1["text"] = "0xF680\n0xF68C\n0xF698\n0xF634\n0xF64F\n0xF6C7\n0xF680\n0xF670\n0xF6A7\n0xF689\n0xF6DA\n0xF680\n0xF691\n0xF6A1\n0xF687\n0xF6C6\n0xF6D3\n"
pam1.grid(row=2,column=0,padx=8)

'''
первый столбец слов, хардкод говно кста
'''

lab1 = ttk.Label(font=font_symbs,  foreground="#%02x%02x%02x" % (29,217,109),background="#%02x%02x%02x" % (11,35,26))
lab1["text"] = final[0] + "\n" +final[1] + "\n" +final[2] + "\n" +final[3] + "\n" +final[4] + "\n" +final[5] + "\n" +final[6] + "\n" +final[7] + "\n" +final[8] + "\n" +final[9] + "\n" +final[10] + "\n" +final[11] + "\n" +final[12] + "\n" +final[13] + "\n" +final[14] + "\n" +final[15] + "\n" +final[16]
lab1.grid(row=2,column=1,padx=8)

'''
второй кометический столбец памяти
'''

pam2 = ttk.Label(font=font_symbs,  foreground="#%02x%02x%02x" % (29,217,109),background="#%02x%02x%02x" % (11,35,26))
pam2["text"] = "0xF680\n0xF68C\n0xF698\n0xF634\n0xF64F\n0xF6C7\n0xF680\n0xF670\n0xF6A7\n0xF689\n0xF6DA\n0xF680\n0xF691\n0xF6A1\n0xF687\n0xF6C6\n0xF6D3\n"
pam2.grid(row=2,column=2,padx=10)

'''
второй столбец слов, хардкод все еще говно
'''

lab2 = ttk.Label(font=font_symbs,  foreground="#%02x%02x%02x" % (29,217,109),background="#%02x%02x%02x" % (11,35,26))
lab2["text"] = final[17] + "\n" +final[18] + "\n" +final[19] + "\n" +final[20] + "\n" +final[21] + "\n" +final[22] + "\n" +final[23] + "\n" +final[24] + "\n" +final[25] + "\n" +final[26] + "\n" +final[27] + "\n" +final[28] + "\n" +final[29] + "\n" +final[30] + "\n" +final[31] + "\n" +final[32] + "\n" +final[33]
lab2.grid(row=2,column=3,padx=8)

'''
столбец для отображения прогресса (вводимые слова и их результат)
'''

lab3 = ttk.Label(font=font_symbs,  foreground="#%02x%02x%02x" % (29,217,109),background="#%02x%02x%02x" % (11,35,26))
lab3["text"] = ""
lab3.grid(row=2,column=4,padx=8)

'''
поле ввода слов
'''

entry = ttk.Entry(background="#%02x%02x%02x" % (11,35,26))
entry.grid(row=3, column=0)

'''
кнопка ввода
'''

btn = ttk.Button(text="Enter", command=clicked)
btn.grid(row=3, column=1)
  
root.mainloop()