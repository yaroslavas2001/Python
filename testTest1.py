from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# from PIL import Image, ImageTk

root = Tk()
root.title("Тест на знание английских слов")
root.geometry("400x500")
root["bg"] = "white"
root.resizable(width=False, height=False)

root.iconbitmap("img/icon.ico")
# не позволяет изменять размер
# 4 варианта , перевод , проверочное слово
var_list = [
    ("apple", "banana", "avocado", "orange", "яблоко", "apple"),
    ("beef", "duck", "veal", "milk", "молоко", "milk"),
    ("Jamie", "Jack", "Heidi", "Lydia", "Джек", "jack"),
    ("answer", "advice", "climb", "edge", "совет", "advice"),
    ("move", "give", "great", "from", "дать", "give"),
    ("night", "sing", "rain", "money", "ночь", "night"),
    ("woman", "write", "talk", "they", "они", "they"),
    ("today", "watch", "like", "group", "нравиться", "like"),
    ("eye", "father", "do", "door", "отец", "father"),
    ("death", "country", "boy", "can", "страна", "country")
]
a_simply = [
    ("apple", "banana", "avocado", "orange", "яблоко", "apple"),
    ("beef", "duck", "veal", "milk", "молоко", "milk"),
    ("Jamie", "Jack", "Heidi", "Lydia", "Джек", "jack"),
    ("answer", "advice", "climb", "edge", "совет", "advice"),
    ("move", "give", "great", "from", "дать", "give"),
    ("night", "sing", "rain", "money", "ночь", "night"),
    ("woman", "write", "talk", "they", "они", "they"),
    ("today", "watch", "like", "group", "нравиться", "like"),
    ("eye", "father", "do", "door", "отец", "father"),
    ("death", "country", "boy", "can", "страна", "country")
]
a_complicated = [
    ("дети", "children"),
    ("цвет", "color"),
    ("Земля", "earth"),
    ("хорошо", "good"),
    ("день", "day"),
    ("любовь", "love"),
    ("только", "only"),
    ("дождь", "rain"),
    ("снег", "snow"),
    ("работать", "work")
]
b_simply = [
    ("valuable", "whistle", "amateur", "quarrel", "любитель", "amateur"),
    ("profit", "mirror", "referee", "humiliate", "выгода", "profit"),
    ("gluttony", "knowledge", "persuade", "interpret", "толковать", "interpret"),
    ("landlord", "mature", "kindness", "prejudice", "доброта", "kindness"),
    ("rapport", "liberty", "squeeze", "remarkable", "значительный", "remarkable"),
    ("petrol", "famine", "hiccup", "courage", "бензин", "petrol"),
    ("boast", "civilian", "addiction", "deliver", "доставлять", "deliver"),
    ("famine", "celebrity", "anger", "deteriorate", "злость", "anger"),
    ("justice", "household", "naughty", "prosecutor", "быт", "household"),
    ("ruthless", "squeeze", "withdraw", "vain", "безжалостный", "ruthless")
]
b_complicated = [
    ("свистеть", "whistle"),
    ("подозревать", "suspect"),
    ("ползать", "crawl"),
    ("глубина", "depth"),
    ("столовая", "canteen"),
    ("щедрость", "generosity"),
    ("репетиция", "rehearsal"),
    ("програмное обеспечение", "rehearsal"),
    ("суеверие", "superstition"),
    ("Спускаться", "descend")
]
c_simply = [
    ("supine", "venerate", "drought", "impugned", "засуха", "drought"),
    ("penchant", "extant", "incise", "philistine", "обыватель", "philistine"),
    ("postulate", "quintessential", "repine", "proprietary", "аксиома", "postulate"),
    ("rarefy", "subliminal", "moralistic", "penchant", "поучающий", "moralistic"),
    ("untoward", "vehemence", "vigilance", "precipitous", "упрямый", "untoward"),
    ("probity", "vestige", "petulant", "inveigle", "частица", "vestige"),
    ("ossified", "ponderous", "visionary", "presumptuous", "мечтательный", "visionary"),
    ("perch", "whittle", "vilify", "venerate", "непостоянный", "volatile"),
    ("subliminal", "prudent", "repine", "plumb", "жаловаться", "repine"),
    ("proximity", "prolific", "pillage", "presumptuous", "близость", "proximity")
]
c_complicated = [
    ("предсказазние", "augury"),
    ("свободный", "glib"),
    ("заманивать", "inveigle"),
    ("заполнять", "pervade"),
    ("чувственный", "voluptuous"),
    ("вниамтельный", "solicitous"),
    ("упрямый", "untoward"),
    ("беспомощный", "feckless"),
    ("грубиян", "boor"),
    ("ловкость", "dexterity")
]
ball = 0
n = 0
k = len(var_list)

style = ttk.Style()
style.map("C.TButton",
          foreground=[('pressed', '#ffafcc'), ('active', '#f3722c')],
          background=[('pressed', '!disabled', 'black'), ('active', '#f94144')]
          )


# при добавлении стиля кнопки необходимо добавить ttk.Buttom
# https://www.englishdom.com/skills/glossary/wordset/top-100-slov-urovnya-advanced/
def clear():
    # list = root.grid_slaves()
    list = root.pack_slaves()
    for l in list:
        l.destroy()


def basic(*event):
    clear()
    clear()
    start()


def rez(ball):
    clear()
    if ball == 10:
        result = Label(root, text="Поздравляю!", bg="white", font=("Play", 20), fg="#303030")
        result.pack(pady=2)
        result1 = Label(root, text="Вы набрали 10 баллов", bg="white", font=("Play", 20), fg="#303030")
        result1.pack(pady=2)
        result2 = Label(root, image=pic_10ball, bg="white")
        result2.pack(pady=20)
        btn1 = Button(root, image=pic_vern, borderwidth=0, bg="white", activebackground="white")
        btn1.pack(pady=2)
        btn1.bind("<Button-1>", basic)
    elif ball == 9:
        result = Label(root, text="Поздравляю!", bg="white", font=("Play", 20), fg="#303030")
        result.pack(pady=2)
        result1 = Label(root, text="Вы набрали 9 баллов", bg="white", font=("Play", 20), fg="#303030")
        result1.pack(pady=2)
        result2 = Label(root, image=pic_9ball, bg="white")
        result2.pack(pady=20)
        btn1 = Button(root, image=pic_vern, borderwidth=0, bg="white", activebackground="white")
        btn1.pack(pady=2)
        btn1.bind("<Button-1>", basic)
    elif ball == 8:
        result = Label(root, text="Поздравляю!", bg="white", font=("Play", 20), fg="#303030")
        result.pack(pady=2)
        result1 = Label(root, text="Вы набрали 8 баллов", bg="white", font=("Play", 20), fg="#303030")
        result1.pack(pady=2)
        result2 = Label(root, image=pic_8ball, bg="white")
        result2.pack(pady=20)
        btn1 = Button(root, image=pic_vern, borderwidth=0, bg="white", activebackground="white")
        btn1.pack(pady=2)
        btn1.bind("<Button-1>", basic)
    elif ball == 7 or ball == 6 or ball == 5 or ball == 4 or ball == 3 or ball == 2:
        result = Label(root, text="Поздравляю! Ваш балл:", bg="white", font=("Play", 20), fg="#303030")
        result.pack(pady=0)
        result1 = Label(root, text=ball, bg="white", font=("Play", 20), fg="#303030")
        result1.pack(pady=0)
        result2 = Label(root, image=pic_dic, bg="white")
        result2.pack()
        btn1 = Button(root, image=pic_vern, borderwidth=0, bg="white", activebackground="white")
        btn1.pack(pady=0)
        btn1.bind("<Button-1>", basic)
    elif ball == 1:
        result = Label(root, text="Поздравляю!", bg="white", font=("Play", 20), fg="#303030")
        result.pack(pady=2)
        result1 = Label(root, text="Вы набрали 1 балл", bg="white", font=("Play", 20), fg="#303030")
        result1.pack(pady=2)
        result2 = Label(root, image=pic_dic, bg="white")
        result2.pack(pady=10)
        btn1 = Button(root, image=pic_vern, borderwidth=0, bg="white", activebackground="white")
        btn1.pack(pady=2)
        btn1.bind("<Button-1>", basic)
    elif ball == 0:
        result = Label(root, text="Вы набрали 0 баллов", bg="white", font=("Play", 20), fg="#303030")
        result.pack(pady=2)
        result = Label(root, image=pic_dic, bg="white")
        result.pack(pady=2)
        btn1 = Button(root, image=pic_vern, borderwidth=0, bg="white", activebackground="white")
        btn1.pack(pady=2)
        btn1.bind("<Button-1>", basic)


# AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
def work_a_simple(n, ball):
    clear()
    question = Label(root, text="Как переводится слово: ", bg="white", font=("Play", 25), fg="#303030")
    question1 = Label(root, text=a_simply[n][4], bg="white", font=("Play", 25), fg="#389CF2")
    question.pack(pady=0)
    question1.pack(pady=0)
    value0 = Label(root, text=a_simply[n][0], bg="white", font=("Play", 25), fg="#303030")
    value1 = Label(root, text=a_simply[n][1], bg="white", font=("Play", 25), fg="#303030")
    value2 = Label(root, text=a_simply[n][2], bg="white", font=("Play", 25), fg="#303030")
    value3 = Label(root, text=a_simply[n][3], bg="white", font=("Play", 25), fg="#303030")
    value0.pack(pady=7)
    value1.pack(pady=7)
    value2.pack(pady=7)
    value3.pack(pady=7)
    answer = Entry(fg="#303030", font=("Play", 20))
    answer.pack(pady=10, ipadx=20, ipady=10)
    btn = Button(root, image=pic_otvet, command=lambda: game1_a_simply(n, ball, answer), borderwidth=0, bg="white",
                 activebackground="white")
    btn.pack(pady=2)


def game1_a_simply(n, ball, answer):
    if answer.get().lower() == a_simply[n][5]:
        print("вроде работает")
        n += 1
        ball = ball + 1
        if n < k:
            clear()
            work_a_simple(n, ball)
        else:
            rez(ball)
    else:
        print("вроде не работает")
        n += 1
        if n < k:
            clear()
            work_a_simple(n, ball)
        else:
            rez(ball)


def work_a_complicated(n, ball):
    clear()
    question = Label(root, text="Как переводится слово: ", bg="white", font=("Play", 25), fg="#303030")
    question1 = Label(root, text=a_complicated[n][0], bg="white", font=("Play", 25), fg="#389CF2")
    question.pack(pady=2)
    question1.pack(pady=2)
    answer = Entry(fg="#303030", font=("Play", 20))
    answer.pack(pady=10, ipadx=20, ipady=10)
    btn = Button(root, image=pic_otvet, command=lambda: game1_a_complicated(n, ball, answer), borderwidth=0, bg="white",
                 activebackground="white")
    btn.pack(pady=2)


def game1_a_complicated(n, ball, answer):
    if answer.get().lower() == a_complicated[n][1]:
        print("вроде работает")
        n += 1
        ball = ball + 1
        if n < k:
            clear()
            work_a_complicated(n, ball)
        else:
            rez(ball)
    else:
        print("вроде не работает")
        n += 1
        if n < k:
            clear()
            work_a_complicated(n, ball)
        else:
            rez(ball)


# BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
def work_b_simply(n, ball):
    clear()
    question = Label(root, text="Как переводится слово: ", bg="white", font=("Play", 25), fg="#303030")
    question1 = Label(root, text=b_simply[n][4], bg="white", font=("Play", 25), fg="#389CF2")
    question.pack(pady=0)
    question1.pack(pady=0)
    value0 = Label(root, text=b_simply[n][0], bg="white", font=("Play", 25), fg="#303030")
    value1 = Label(root, text=b_simply[n][1], bg="white", font=("Play", 25), fg="#303030")
    value2 = Label(root, text=b_simply[n][2], bg="white", font=("Play", 25), fg="#303030")
    value3 = Label(root, text=b_simply[n][3], bg="white", font=("Play", 25), fg="#303030")
    value0.pack(pady=7)
    value1.pack(pady=7)
    value2.pack(pady=7)
    value3.pack(pady=7)
    answer = Entry(fg="#303030", font=("Play", 20))
    answer.pack(pady=10, ipadx=20, ipady=10)
    btn = Button(root, image=pic_otvet, command=lambda: game1_b_simply(n, ball, answer), borderwidth=0, bg="white",
                 activebackground="white")
    btn.pack(pady=2)


def game1_b_simply(n, ball, answer):
    if answer.get().lower() == b_simply[n][5]:
        print("вроде работает")
        n += 1
        ball = ball + 1
        if n < k:
            clear()
            work_b_simply(n, ball)
        else:
            rez(ball)
    else:
        print("вроде не работает")
        n += 1
        if n < k:
            clear()
            work_b_simply(n, ball)
        else:
            rez(ball)


def work_b_complicated(n, ball):
    clear()
    question = Label(root, text="Как переводится слово: ", bg="white", font=("Play", 25), fg="#303030")
    question1 = Label(root, text=b_complicated[n][0], bg="white", font=("Play", 25), fg="#389CF2")
    question.pack(pady=2)
    question1.pack(pady=2)
    answer = Entry(fg="#303030", font=("Play", 20))
    answer.pack(pady=10, ipadx=20, ipady=10)
    btn = Button(root, image=pic_otvet, command=lambda: game1_b_complicated(n, ball, answer), borderwidth=0, bg="white",
                 activebackground="white")
    btn.pack(pady=2)


def game1_b_complicated(n, ball, answer):
    if answer.get().lower() == b_complicated[n][1]:
        print("вроде работает")
        n += 1
        ball = ball + 1
        if n < k:
            clear()
            work_b_complicated(n, ball)
        else:
            rez(ball)
    else:
        print("вроде не работает")
        n += 1
        if n < k:
            clear()
            work_b_complicated(n, ball)
        else:
            rez(ball)


# CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC
def work_c_simply(n, ball):
    clear()
    question = Label(root, text="Как переводится слово: ", bg="white", font=("Play", 25), fg="#303030")
    question1 = Label(root, text=c_simply[n][4], bg="white", font=("Play", 25), fg="#389CF2")
    question.pack(pady=0)
    question1.pack(pady=0)
    value0 = Label(root, text=c_simply[n][0], bg="white", font=("Play", 25), fg="#303030")
    value1 = Label(root, text=c_simply[n][1], bg="white", font=("Play", 25), fg="#303030")
    value2 = Label(root, text=c_simply[n][2], bg="white", font=("Play", 25), fg="#303030")
    value3 = Label(root, text=c_simply[n][3], bg="white", font=("Play", 25), fg="#303030")
    value0.pack(pady=7)
    value1.pack(pady=7)
    value2.pack(pady=7)
    value3.pack(pady=7)
    answer = Entry(fg="#303030", font=("Play", 20))
    answer.pack(pady=10, ipadx=20, ipady=10)
    btn = Button(root, image=pic_otvet, command=lambda: game1_c_simply(n, ball, answer), borderwidth=0, bg="white",
                 activebackground="white")
    btn.pack(pady=2)


def game1_c_simply(n, ball, answer):
    if answer.get().lower() == c_simply[n][5]:
        print("вроде работает")
        n += 1
        ball = ball + 1
        if n < k:
            clear()
            work_c_simply(n, ball)
        else:
            rez(ball)
    else:
        print("вроде не работает")
        n += 1
        if n < k:
            clear()
            work_c_simply(n, ball)
        else:
            rez(ball)


def work_c_complicated(n, ball):
    clear()
    question = Label(root, text="Как переводится слово: ", bg="white", font=("Play", 25), fg="#303030")
    question1 = Label(root, text=c_complicated[n][0], bg="white", font=("Play", 25), fg="#389CF2")
    question.pack(pady=2)
    question1.pack(pady=2)
    answer = Entry(fg="#303030", font=("Play", 20))
    answer.pack(pady=10, ipadx=20, ipady=10)
    btn = Button(root, image=pic_otvet, command=lambda: game1_c_complicated(n, ball, answer), borderwidth=0, bg="white",
                 activebackground="white")
    btn.pack(pady=2)


def game1_c_complicated(n, ball, answer):
    if answer.get().lower() == c_complicated[n][1]:
        print("вроде работает")
        n += 1
        ball = ball + 1
        if n < k:
            clear()
            work_c_complicated(n, ball)
        else:
            rez(ball)
    else:
        print("вроде не работает")
        n += 1
        if n < k:
            clear()
            work_c_complicated(n, ball)
        else:
            rez(ball)


def work(n, ball):
    clear()
    question = Label(root, text="Как переводится слово: ", bg="white")
    question1 = Label(root, text=var_list[n][4], bg="white")
    question.pack(pady=2)
    question1.pack(pady=2)
    value0 = Label(root, text=var_list[n][0], bg="white")
    value1 = Label(root, text=var_list[n][1], bg="white")
    value2 = Label(root, text=var_list[n][2], bg="white")
    value3 = Label(root, text=var_list[n][3], bg="white")
    value0.pack(pady=2)
    value1.pack(pady=2)
    value2.pack(pady=2)
    value3.pack(pady=2)
    answer = Entry()
    answer.pack(pady=2)
    btn = Button(root, image=pic_otvet, command=lambda: game1(n, ball, answer), borderwidth=0, bg="white")
    btn.pack(pady=2)


def game1(n, ball, answer):
    if answer.get().lower() == var_list[n][5]:
        print("вроде работает")
        n += 1
        ball = ball + 1
        if n < k:
            clear()
            work(n, ball)
        else:
            rez(ball)
    else:
        print("вроде не работает")
        n += 1
        if n < k:
            clear()
            work(n, ball)
        else:
            rez(ball)


# Кнопки для показа теста
def a_test(event):
    clear()
    img = Label(root, image=pic_10, bg="white")
    img.pack(pady=5)
    simply = Button(root, image=pic_c_otvet, borderwidth=0, bg="white", command=lambda: work_a_simple(n, ball),
                    activebackground="white")
    simply.pack(pady=20)
    complicated = Button(root, image=pic_bez, borderwidth=0, bg="white",
                         command=lambda: work_a_complicated(n, ball), activebackground="white")
    complicated.pack(pady=0)


def b_test(event):
    clear()
    img = Label(root, image=pic_10, bg="white")
    img.pack(pady=5)
    simply = Button(root, image=pic_c_otvet, borderwidth=0, bg="white", command=lambda: work_b_simply(n, ball),
                    activebackground="white")
    simply.pack(pady=20)
    complicated = Button(root, image=pic_bez, borderwidth=0, bg="white",
                         command=lambda: work_b_complicated(n, ball), activebackground="white")
    complicated.pack(pady=0)


def c_test(event):
    clear()
    img = Label(root, image=pic_10, bg="white")
    img.pack(pady=5)
    simply = Button(root, image=pic_c_otvet, borderwidth=0, bg="white", command=lambda: work_c_simply(n, ball),
                    activebackground="white")
    simply.pack(pady=20)
    complicated = Button(root, image=pic_bez, borderwidth=0, bg="white",
                         command=lambda: work_c_complicated(n, ball), activebackground="white")
    complicated.pack(pady=0)


def test(event):
    clear()
    img = Label(root, image=pic_abc, bg="white")
    img.pack(pady=5)
    a1 = Button(root, image=pic_a, borderwidth=0, bg="white", activebackground="white")
    a1.bind("<Button-1>", a_test)
    a1.pack(pady=5, side=BOTTOM, fill=NONE)
    b1 = Button(root, image=pic_b, borderwidth=0, bg="white", activebackground="white")
    b1.bind("<Button-1>", b_test)
    b1.pack(pady=5, side=BOTTOM, fill=NONE)
    c1 = Button(root, image=pic_c, borderwidth=0, bg="white", activebackground="white")
    c1.bind("<Button-1>", c_test)
    c1.pack(pady=5, side=BOTTOM, fill=NONE)


def show_message():
    messagebox.showinfo("Инструкция", "Вам необходимо ввести варинт, тот который вы считаете"
                                      "правильный, не имеет значения в каком регистре.")


def start():
    clear()
    img = Label(root, image=pic_icon, bg="white")
    img.pack(pady=50)
    b1 = Button(root, image=pic, borderwidth=0, bg="white", activebackground="white")
    b1.bind("<Button-1>", test)
    b1.pack()
    message_button = Button(text="Инструкция", image=pic_instr, command=show_message, borderwidth=0, bg="white",
                            activebackground="white")
    message_button.pack(pady=10)


pic_10ball = PhotoImage(file="img/10ball.png")
pic_9ball = PhotoImage(file="img/9ball.png")
pic_8ball = PhotoImage(file="img/8ball.png")
pic_dic = PhotoImage(file="img/ditionary.png")
pic_10 = PhotoImage(file="img/10.png")
pic_abc = PhotoImage(file="img/abc.png")
pic_icon = PhotoImage(file="img/words.png")
pic = PhotoImage(file="img/start.png")
pic_instr = PhotoImage(file="img/instr.png")
pic_otvet = PhotoImage(file="img/otvet.png")
pic_vern = PhotoImage(file="img/vern.png")
pic_a = PhotoImage(file="img/a.png")
pic_b = PhotoImage(file="img/b.png")
pic_c = PhotoImage(file="img/c.png")
pic_c_otvet = PhotoImage(file="img/c_otvet.png")
pic_bez = PhotoImage(file="img/bez.png")
start()

root.mainloop()
