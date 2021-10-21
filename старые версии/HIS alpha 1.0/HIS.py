#начало создания: 06.11.17
#alpha-версия
import tkinter
from tkinter import *
#3288523
root = Tk()
root.title("HIS")
root.geometry("850x800")
root.resizable(0, 0)

#Создание фрэймов

fr1 = Frame(root,width=850,height=250,bg="peru")
fr2 = Frame(root,width=850,height=510,bg="peru")
fr3 = Frame(root,width=850,height=40,bg="gainsboro")

fr1.pack()
fr2.pack()
fr3.pack()

choice = ""

def vstyplenie():
	global choice
	choice = 0

	citat1 = "Учиться надо всю жизнь,\nдо последнего дыхания!"
	autor1 = "Сюнь-цзы"
	citat2 = "Только самые мудрые и самые глупые \nне поддаются обучению."
	autor2 = "Конфуций"
	citat3 = "Без примера ничему не выучишься."
	autor3 = "Ян Амос Коменский"
	citat4 = "Мы все учились понемногу \nЧему-нибудь и как-нибудь."
	autor4 = "Александр Сергеевич Пушкин"
	citat5 = "Жалок тот ученик, \nкоторый не превосходит \nсвоего учителя."
	autor5 = "Леонардо да Винчи"
	citat6 = "Ни искусство, \nни мудрость не могут быть достигнуты, \nесли им не учиться."
	autor6 = "Демокрид"
	citat7 = "Учение имеет лишь одно назначение — \nотыскание утраченной природы человека."
	autor7 = "Мэн-цзы"
	citat8 = "Великое искусство научиться многому — \nэто браться сразу за немногое."
	autor8 = "Джон Локк"
	citat9 = "Изучай все не из тщеславия, \nа ради практической пользы."
	autor9 = "Георг Кристоф Лихтенберг"

	import random
	 
	citata = random.randint(1, 10)

	if citata==1:

		ci= Label(fr1, text=citat1, bg="peru", fg="black", font="Arial 15")
		ci.place(width=500, height=200, x=100, y=50)
		ci= Label(fr2, text=autor1, bg="peru", fg="black", font="Arial 15")
		ci.place(width=300, height=30, x=350, y=40)
	if citata==2:
		ci= Label(fr1, text=citat2, bg="peru", fg="black", font="Arial 16")
		ci.place(width=500, height=200, x=100, y=50)
		ci= Label(fr2, text=autor2, bg="peru", fg="black", font="Arial 15")
		ci.place(width=300, height=30, x=350, y=40)
	if citata==3:
		ci= Label(fr1, text=citat2, bg="peru", fg="black", font="Arial 16")
		ci.place(width=500, height=200, x=100, y=50)
		ci= Label(fr2, text=autor2, bg="peru", fg="black", font="Arial 15")
		ci.place(width=300, height=30, x=350, y=40)
	if citata==4:
		ci= Label(fr1, text=citat3, bg="peru", fg="black", font="Arial 16")
		ci.place(width=500, height=200, x=100, y=50)
		ci= Label(fr2, text=autor3, bg="peru", fg="black", font="Arial 15")
		ci.place(width=300, height=30, x=350, y=40)
	if citata==5:
		ci= Label(fr1, text=citat4, bg="peru", fg="black", font="Arial 16")
		ci.place(width=500, height=200, x=100, y=50)
		ci= Label(fr2, text=autor4, bg="peru", fg="black", font="Arial 15")
		ci.place(width=300, height=30, x=350, y=40)
	if citata==6:
		ci= Label(fr1, text=citat5, bg="peru", fg="black", font="Arial 16")
		ci.place(width=500, height=200, x=100, y=50)
		ci= Label(fr2, text=autor5, bg="peru", fg="black", font="Arial 15")
		ci.place(width=300, height=30, x=350, y=40)
	if citata==7:
		ci= Label(fr1, text=citat6, bg="peru", fg="black", font="Arial 16")
		ci.place(width=500, height=200, x=100, y=50)
		ci= Label(fr2, text=autor6, bg="peru", fg="black", font="Arial 15")
		ci.place(width=300, height=30, x=350, y=40)
	if citata==8:
		ci= Label(fr1, text=citat7, bg="peru", fg="black", font="Arial 16")
		ci.place(width=500, height=200, x=100, y=50)
		ci= Label(fr2, text=autor7, bg="peru", fg="black", font="Arial 15")
		ci.place(width=300, height=30, x=350, y=40)
	if citata==9:
		ci= Label(fr1, text=citat8, bg="peru", fg="black", font="Arial 16")
		ci.place(width=500, height=200, x=100, y=50)
		ci= Label(fr2, text=autor8, bg="peru", fg="black", font="Arial 15")
		ci.place(width=300, height=30, x=350, y=40)
	if citata==10:
		ci= Label(fr1, text=citat9, bg="peru", fg="black", font="Arial 16")
		ci.place(width=500, height=200, x=100, y=50)
		ci= Label(fr2, text=autor9, bg="peru", fg="black", font="Arial 15")
		ci.place(width=300, height=30, x=350, y=40)

vstyplenie()

def pomosh():
	global choice
	if choice==0:
		L = Label(fr2, text="В данном режими функция «Объяснение решения» не работает", bg="white", fg="black", font="Arial 10")
		L.place(width=850, height=14, x=0, y=490)
	if choice==1:
		h_h = open("files\pomosh\srav.txt", "r").read()
		Lh = Label(fr2, text=h_h, bg="white", font="Arial 14")
		Lh.place(width=850, height=510, x=0, y=0)
	if choice==2:
		h0h = open("files\pomosh\kvad.txt", "r").read()
		Lh1 = Label(fr2, text=h0h, bg="white", font="Arial 14")
		Lh1.place(width=850, height=510, x=0, y=0)
	if choice==3:
		h1 = open("files\pomosh\perkvad.txt", "r").read()
		Lh2 = Label(fr2, text=h1, bg="white", font="Arial 14")
		Lh2.place(width=850, height=510, x=0, y=0)
	if choice==4:
		h2 = open("files\pomosh\plkvad.txt", "r").read()
		L2 = Label(fr2, text=h2, bg="white", font="Arial 14")
		L2.place(width=850, height=510, x=0, y=0)
	if choice==5:
		h3 = open("files\pomosh\perpram.txt", "r").read()
		L3 = Label(fr2, text=h3, bg="white", font="Arial 14")
		L3.place(width=850, height=510, x=0, y=0)
	if choice==6:
		h4 = open("files\pomosh\plpram.txt", "r").read()
		L4 = Label(fr2, text=h4, bg="white", font="Arial 14")
		L4.place(width=850, height=510, x=0, y=0)	
	if choice==7:
		h5 = open("files\pomosh\paralel.txt", "r").read()
		L5 = Label(fr2, text=h5, bg="white", font="Arial 14")
		L5.place(width=850, height=510, x=0, y=0)	
	if choice==8:
		h5 = open("files\pomosh\dva.txt", "r").read()
		L5 = Label(fr2, text=h5, bg="white", font="Arial 14")
		L5.place(width=850, height=510, x=0, y=0)
	if choice==9:
		h5 = open("files\pomosh/vos.txt", "r").read()
		L5 = Label(fr2, text=h5, bg="white", font="Arial 14")
		L5.place(width=850, height=510, x=0, y=0)
	if choice==10:
		h5 = open("files\pomosh\ses.txt", "r").read()
		L5 = Label(fr2, text=h5, bg="white", font="Arial 14")
		L5.place(width=850, height=510, x=0, y=0)
	if choice==11:
		h5 = open("files\pomosh\slog.txt", "r").read()
		L5 = Label(fr2, text=h5, bg="white", font="Arial 14")
		L5.place(width=850, height=510, x=0, y=0)
	if choice==12:
		h5 = open("files\pomosh/vich.txt", "r").read()
		L5 = Label(fr2, text=h5, bg="white", font="Arial 14")
		L5.place(width=850, height=510, x=0, y=0)
	if choice==13:
		h5 = open("files\pomosh\ymn.txt", "r").read()
		L5 = Label(fr2, text=h5, bg="white", font="Arial 14")
		L5.place(width=850, height=510, x=0, y=0)
	if choice==14:
		h5 = open("files\pomosh\del.txt", "r").read()
		L5 = Label(fr2, text=h5, bg="white", font="Arial 14")
		L5.place(width=850, height=510, x=0, y=0)
	if choice==15:
		h5 = open("files\pomosh\cor.txt", "r").read()
		L5 = Label(fr2, text=h5, bg="white", font="Arial 14")
		L5.place(width=850, height=510, x=0, y=0)
	if choice==16:
		h5 = open("files\pomosh\step.txt", "r").read()
		L5 = Label(fr2, text=h5, bg="white", font="Arial 14")
		L5.place(width=850, height=510, x=0, y=0)


pomos = Button(fr3, text="Объяснение решения", bg="gainsboro", fg="MediumBluE", font="Arial 14", relief=RIDGE, bd=5, command=pomosh)
pomos.place(width=300, height=40, x=275, y=0)

ckv1 = 0
ckv2 = 0
ckv3 = 0
# НЕ ИСПОЛЬЗОВАТЬ ОДНОБУКВЕННЫЕ ПЕРЕМЕННЫЕ

#  .place_forget()

#•

# М А Т Е М А Т И К А - удалено, перенесенно в алгебру и геометрию
# Сравнение
def srav():
	global j
	global jj
	jjj = j.get()
	jjjj = jj.get()
	if jjj>jjjj:
		y1 = len(jjj)
		y2 = len(jjjj)
		otstyp1 = y1*9
		otstyp2 = y2*9
		otstyp3 = otstyp1+100
		l1d = Label(fr2, text=jjj, bg="white", fg="black", font="Arial 12")
		l1d.place(width=otstyp1, height=25, x=0, y=80)
		l2d = Label(fr2, text="больше, чем", bg="white", fg="black", font="Arial 12")
		l2d.place(width=100, height=25, x=otstyp1, y=80)
		l3d = Label(fr2, text=jjjj, bg="white", fg="black", font="Arial 12")
		l3d.place(width=otstyp2, height=25, x=otstyp3, y=80)
	if jjj<jjjj:
		y1 = len(jjj)
		y2 = len(jjjj)
		otstyp1 = y1*9
		otstyp2 = y2*9
		otstyp3 = otstyp1+100
		l1d = Label(fr2, text=jjj, bg="white", fg="black", font="Arial 12")
		l1d.place(width=otstyp1, height=25, x=0, y=80)
		l2d = Label(fr2, text="меньше, чем", bg="white", fg="black", font="Arial 12")
		l2d.place(width=100, height=25, x=otstyp1, y=80)
		l3d = Label(fr2, text=jjjj, bg="white", fg="black", font="Arial 12")
		l3d.place(width=otstyp2, height=25, x=otstyp3, y=80)
	if jjj==jjjj:
		l1d = Label(fr2, text="Числа равны", bg="white", fg="black", font="Arial 12")
		l1d.place(width=850, height=25, x=0, y=80)
def sravnenie():
	global choice
	choice = 1

	clean_fr1 = Label(fr1, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr1.place(width=850, height=250, x=0, y=0)
	clean_fr2 = Label(fr2, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr2.place(width=850, height=510, x=0, y=0)

	lb = Label(fr1, text="Первое число:", bg="white", fg="black", font="Arial 12")
	lb.place(width=300, height=20, x=50, y=60)
	lb = Label(fr1, text="Второе число:", bg="white", fg="black", font="Arial 12")
	lb.place(width=300, height=20, x=500, y=60)

	lab = Label(fr1, text="Введите данные:", bg="white", fg="MediumBluE", font="Arial 22")
	lab.place(width=850, height=40, x=0, y=5)
	global j
	j = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	j.place(width=300, height=16, x=50, y=90)
	global jj
	jj = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	jj.place(width=300, height=16, x=500, y=90)

	ld = Label(fr2, text="В данном разделе можно сравнивать только числа, если вы хотите сравнить корни и т. п., воспользуйтесь нашим разделом - 'Простые вычисления'", bg="white", fg="black", font="Arial 8")
	ld.place(width=850, height=25, x=0, y=0)

	kresh = Button(fr1, text="Сравнить", background="white", foreground="MediumBluE", font="Arial 16", command=srav)
	kresh.place(width=120, height=30, x=362, y=220)

# периметр квадрата
def per_kvad():
	clean_fr1 = Label(fr1, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr1.place(width=850, height=250, x=0, y=0)
	clean_fr2 = Label(fr2, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr2.place(width=850, height=510, x=0, y=0)

	global choice
	choice = 3
	lab = Label(fr1, text="Введите длину стороны:", bg="white", fg="MediumBluE", font="Arial 22")
	lab.place(width=850, height=40, x=0, y=5)
	global mmmmm
	ov = Label(fr1, text="Введите сторону:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	ov.place(width=120, height=20, x=0, y=40)
	mmmmm = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	mmmmm.place(width=100, height=16, x=120, y=44)

	kresh = Button(fr1, text="Решить", background="white", foreground="MediumBluE", font="Arial 16", command=r_pr_kvad)
	kresh.place(width=120, height=30, x=362, y=170)
	
	lb = Label(fr2, text="Решение:", bg="white", fg="MediumBluE", font="Arial 22")
	lb.place(width=850, height=40, x=0, y=5)
def r_pr_kvad():
	global mmmmm
	nn = mmmmm.get()
	resh = int(nn)*4
	y1 = len(nn)
	y2 = len(str(resh))
	otstyp1 = y1*9
	otstyp3 = y2*9
	otstyp5 = otstyp1+15
	otstyp6 = otstyp5+10
	otstyp7 = otstyp6+otstyp3
	otstyp8 = otstyp7+10
	l1d = Label(fr2, text="По формуле:P=a•4", bg="white", fg="black", font="Arial 12")
	l1d.place(width=150, height=25, x=0, y=50)
	l2d = Label(fr2, text="P=", bg="white", fg="black", font="Arial 12")
	l2d.place(width=15, height=25, x=0, y=75)
	l6d = Label(fr2, text=resh, bg="white", fg="black", font="Arial 12")
	l6d.place(width=otstyp3, height=25, x=15, y=75)
	l7d = Label(fr2, text="Ответ: P=", bg="white", fg="black", font="Arial 12")
	l7d.place(width=70, height=25, x=2, y=100)
	l8d = Label(fr2, text=resh, bg="white", fg="black", font="Arial 12")
	l8d.place(width=otstyp3, height=25, x=75, y=100)

# площадь квадрата
def pl_kvad():
	clean_fr1 = Label(fr1, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr1.place(width=850, height=250, x=0, y=0)
	clean_fr2 = Label(fr2, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr2.place(width=850, height=510, x=0, y=0)

	global choice
	choice = 4

	lab = Label(fr1, text="Введите длину стороны:", bg="white", fg="MediumBluE", font="Arial 22")
	lab.place(width=850, height=40, x=0, y=5)
	global mmmm
	ov = Label(fr1, text="Введите сторону:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	ov.place(width=120, height=20, x=0, y=40)
	mmmm = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	mmmm.place(width=100, height=16, x=120, y=44)

	kresh = Button(fr1, text="Решить", background="white", foreground="MediumBluE", font="Arial 16", command=r_pl_kvad)
	kresh.place(width=120, height=30, x=362, y=170)
	
	lb = Label(fr2, text="Решение:", bg="white", fg="MediumBluE", font="Arial 22")
	lb.place(width=850, height=40, x=0, y=5)
def r_pl_kvad():
	global mmmm
	nn = mmmm.get()
	resh = int(nn)**2
	y1 = len(nn)
	y2 = len(str(resh))
	otstyp1 = y1*9
	otstyp3 = y2*9
	otstyp5 = otstyp1+15
	otstyp6 = otstyp5+10
	otstyp7 = otstyp6+otstyp3
	otstyp8 = otstyp7+10
	l1d = Label(fr2, text="По формуле:S=a^2", bg="white", fg="black", font="Arial 12")
	l1d.place(width=150, height=25, x=0, y=50)
	l2d = Label(fr2, text="S=", bg="white", fg="black", font="Arial 12")
	l2d.place(width=15, height=25, x=0, y=75)
	l6d = Label(fr2, text=resh, bg="white", fg="black", font="Arial 12")
	l6d.place(width=otstyp3, height=25, x=15, y=75)
	l7d = Label(fr2, text="Ответ: P=", bg="white", fg="black", font="Arial 12")
	l7d.place(width=70, height=25, x=2, y=100)
	l8d = Label(fr2, text=resh, bg="white", fg="black", font="Arial 12")
	l8d.place(width=otstyp3, height=25, x=75, y=100)

# периметр прямоугольника
def per_pram():
	clean_fr1 = Label(fr1, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr1.place(width=850, height=250, x=0, y=0)
	clean_fr2 = Label(fr2, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr2.place(width=850, height=510, x=0, y=0)

	global choice
	choice = 5

	lab = Label(fr1, text="Введите длину сторон:", bg="white", fg="MediumBluE", font="Arial 22")
	lab.place(width=850, height=40, x=0, y=5)
	global bb
	ov = Label(fr1, text="Введите сторону a:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	ov.place(width=120, height=20, x=0, y=40)
	bb = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	bb.place(width=100, height=16, x=120, y=44)
	global bbb
	vo = Label(fr1, text="Введите сторону b:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	vo.place(width=120, height=20, x=0, y=60)
	bbb = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	bbb.place(width=100, height=16, x=120, y=64)

	kresh = Button(fr1, text="Решить", background="white", foreground="MediumBluE", font="Arial 16", command=r_per_pram)
	kresh.place(width=120, height=30, x=362, y=170)
	
	lb = Label(fr2, text="Решение:", bg="white", fg="MediumBluE", font="Arial 22")
	lb.place(width=850, height=40, x=0, y=5)
def r_per_pram():
	global bb
	nn = bb.get()
	global bbb
	nnn = bbb.get()
	resh = (int(nn)+int(nnn))*2
	rash = int(nn)+int(nnn)
	y1 = len(nn)
	y2 = len(nnn)
	y3 = len(str(resh))
	otstyp1 = y1*9
	otstyp2 = y2*9
	otstyp3 = y3*9
	otstyp5 = otstyp1+15
	otstyp6 = otstyp5+10
	otstyp7 = otstyp6+otstyp2
	otstyp8 = otstyp7+10
	otstyp9 = otstyp1+35
	otstyp0 = otstyp1+25
	l1d = Label(fr2, text="По формуле:S=2(a•b)", bg="white", fg="black", font="Arial 12")
	l1d.place(width=155, height=25, x=0, y=50)

	l2d = Label(fr2, text="S=", bg="white", fg="black", font="Arial 12")
	l2d.place(width=15, height=25, x=1, y=75)
	l3d = Label(fr2, text=nn, bg="white", fg="black", font="Arial 12")
	l3d.place(width=otstyp1, height=25, x=15, y=75)
	l4d = Label(fr2, text="+", bg="white", fg="black", font="Arial 12")
	l4d.place(width=10, height=25, x=otstyp5, y=75)
	l4d = Label(fr2, text=nnn, bg="white", fg="black", font="Arial 12")
	l4d.place(width=otstyp2, height=25, x=otstyp6, y=75)
	l5d = Label(fr2, text="=", bg="white", fg="black", font="Arial 12")
	l5d.place(width=10, height=25, x=otstyp7, y=75)
	l6d = Label(fr2, text=rash, bg="white", fg="black", font="Arial 12")
	l6d.place(width=otstyp3, height=25, x=otstyp8, y=75)

	l2d = Label(fr2, text="S=", bg="white", fg="black", font="Arial 12")
	l2d.place(width=15, height=25, x=1, y=100)
	l3d = Label(fr2, text=rash, bg="white", fg="black", font="Arial 12")
	l3d.place(width=otstyp1, height=25, x=15, y=100)
	l4d = Label(fr2, text="•", bg="white", fg="black", font="Arial 12")
	l4d.place(width=10, height=25, x=otstyp5, y=100)
	l4d = Label(fr2, text="2", bg="white", fg="black", font="Arial 12")
	l4d.place(width=10, height=25, x=otstyp6, y=100)
	l5d = Label(fr2, text="=", bg="white", fg="black", font="Arial 12")
	l5d.place(width=20, height=25, x=otstyp9, y=100)
	l6d = Label(fr2, text=resh, bg="white", fg="black", font="Arial 12")
	l6d.place(width=otstyp9, height=25, x=otstyp9, y=100)

	l7d = Label(fr2, text="Ответ: S=", bg="white", fg="black", font="Arial 12")
	l7d.place(width=70, height=25, x=2, y=125)
	l8d = Label(fr2, text=resh, bg="white", fg="black", font="Arial 12")
	l8d.place(width=otstyp3, height=25, x=75, y=125)

# площадь прямоугольника
def pl_pram():
	clean_fr1 = Label(fr1, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr1.place(width=850, height=250, x=0, y=0)
	clean_fr2 = Label(fr2, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr2.place(width=850, height=510, x=0, y=0)

	global choice
	choice = 6
	lab = Label(fr1, text="Введите длину сторон:", bg="white", fg="MediumBluE", font="Arial 22")
	lab.place(width=850, height=40, x=0, y=5)
	global mm
	ov = Label(fr1, text="Введите сторону a:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	ov.place(width=120, height=20, x=0, y=40)
	mm = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	mm.place(width=100, height=16, x=120, y=44)
	global mmm
	vo = Label(fr1, text="Введите сторону b:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	vo.place(width=120, height=20, x=0, y=60)
	mmm = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	mmm.place(width=100, height=16, x=120, y=64)

	kresh = Button(fr1, text="Решить", background="white", foreground="MediumBluE", font="Arial 16", command=r_pl_pram)
	kresh.place(width=120, height=30, x=362, y=170)
	
	lb = Label(fr2, text="Решение:", bg="white", fg="MediumBluE", font="Arial 22")
	lb.place(width=850, height=40, x=0, y=5)
def r_pl_pram():
	global mm
	nn = mm.get()
	global mmm
	nnn = mmm.get()
	resh = int(nn)*int(nnn)
	y1 = len(nn)
	y2 = len(nnn)
	y3 = len(str(resh))
	otstyp1 = y1*9
	otstyp2 = y2*9
	otstyp3 = y3*9
	otstyp5 = otstyp1+15
	otstyp6 = otstyp5+10
	otstyp7 = otstyp6+otstyp2
	otstyp8 = otstyp7+10
	l1d = Label(fr2, text="По формуле:S=a•b", bg="white", fg="black", font="Arial 12")
	l1d.place(width=150, height=25, x=0, y=50)
	l2d = Label(fr2, text="S=", bg="white", fg="black", font="Arial 12")
	l2d.place(width=15, height=25, x=0, y=75)
	l3d = Label(fr2, text=nn, bg="white", fg="black", font="Arial 12")
	l3d.place(width=otstyp1, height=25, x=15, y=75)
	l4d = Label(fr2, text="•", bg="white", fg="black", font="Arial 12")
	l4d.place(width=10, height=25, x=otstyp5, y=75)
	l4d = Label(fr2, text=nnn, bg="white", fg="black", font="Arial 12")
	l4d.place(width=otstyp2, height=25, x=otstyp6, y=75)
	l5d = Label(fr2, text="=", bg="white", fg="black", font="Arial 12")
	l5d.place(width=10, height=25, x=otstyp7, y=75)
	l6d = Label(fr2, text=resh, bg="white", fg="black", font="Arial 12")
	l6d.place(width=otstyp3, height=25, x=otstyp8, y=75)
	l7d = Label(fr2, text="Ответ: S=", bg="white", fg="black", font="Arial 12")
	l7d.place(width=70, height=25, x=2, y=100)
	l8d = Label(fr2, text=resh, bg="white", fg="black", font="Arial 12")
	l8d.place(width=otstyp3, height=25, x=75, y=100)

# объём параллелепипеда
def ob_p():
	clean_fr1 = Label(fr1, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr1.place(width=850, height=250, x=0, y=0)
	clean_fr2 = Label(fr2, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr2.place(width=850, height=510, x=0, y=0)

	global choice
	choice = 7

	lab = Label(fr1, text="Введите длину сторон:", bg="white", fg="MediumBluE", font="Arial 22")
	lab.place(width=850, height=40, x=0, y=5)
	global cc
	ov = Label(fr1, text="Введите сторону a:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	ov.place(width=120, height=20, x=0, y=40)
	cc = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	cc.place(width=100, height=16, x=120, y=44)
	global ccc
	vo = Label(fr1, text="Введите сторону b:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	vo.place(width=120, height=20, x=0, y=60)
	ccc = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	ccc.place(width=100, height=16, x=120, y=64)

	global c
	ov = Label(fr1, text="Введите сторону c:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	ov.place(width=120, height=20, x=0, y=80)
	c = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	c.place(width=100, height=16, x=120, y=84)

	kresh = Button(fr1, text="Решить", background="white", foreground="MediumBluE", font="Arial 16", command=r_ob_p)
	kresh.place(width=120, height=30, x=362, y=170)
	
	lb = Label(fr2, text="Решение:", bg="white", fg="MediumBluE", font="Arial 22")
	lb.place(width=850, height=40, x=0, y=5)
def r_ob_p():
	global cc
	nn = cc.get()
	global ccc
	nnn = ccc.get()
	global c
	n = c.get()
	resh = int(nn)*int(nnn)*int(n)
	y1 = len(nn)
	y2 = len(nnn)
	y0 = len(n)
	y3 = len(str(resh))
	otstyp1 = y1*9
	otstyp2 = y2*9
	otstyp3 = y3*9
	otstyp4 = y0*9
	otstyp5 = otstyp1+15
	otstyp6 = otstyp5+10
	otstyp9 = otstyp6+otstyp2
	otstyp7 = otstyp9+otstyp4
	otstyp8 = otstyp7+otstyp4
	otstyp0 = otstyp8+otstyp3
	l1d = Label(fr2, text="По формуле:V=a•b•c", bg="white", fg="black", font="Arial 12")
	l1d.place(width=155, height=25, x=0, y=50)
	l2d = Label(fr2, text="V=", bg="white", fg="black", font="Arial 12")
	l2d.place(width=15, height=25, x=0, y=75)
	l3d = Label(fr2, text=nn, bg="white", fg="black", font="Arial 12")
	l3d.place(width=otstyp1, height=25, x=15, y=75)
	l4d = Label(fr2, text="•", bg="white", fg="black", font="Arial 12")
	l4d.place(width=10, height=25, x=otstyp5, y=75)
	l4d = Label(fr2, text=nnn, bg="white", fg="black", font="Arial 12")
	l4d.place(width=otstyp2, height=25, x=otstyp6, y=75)
	l4d = Label(fr2, text="•", bg="white", fg="black", font="Arial 12")
	l4d.place(width=10, height=25, x=otstyp9, y=75)
	l4d = Label(fr2, text=n, bg="white", fg="black", font="Arial 12")
	l4d.place(width=otstyp4, height=25, x=otstyp7, y=75)

	l5d = Label(fr2, text="=", bg="white", fg="black", font="Arial 12")
	l5d.place(width=10, height=25, x=otstyp8, y=75)
	l6d = Label(fr2, text=resh, bg="white", fg="black", font="Arial 12")
	l6d.place(width=otstyp3, height=25, x=otstyp0, y=75)

	l7d = Label(fr2, text="Ответ: V=", bg="white", fg="black", font="Arial 12")
	l7d.place(width=70, height=25, x=2, y=100)
	l8d = Label(fr2, text=resh, bg="white", fg="black", font="Arial 12")
	l8d.place(width=otstyp3, height=25, x=75, y=100)

# А Л Г Е Б Р А
# А Л Г Е Б Р А
# А Л Г Е Б Р А
# А Л Г Е Б Р А
# А Л Г Е Б Р А

#квадратное уравнение
def clk():
	lb = Label(fr2, text="Решение:", bg="white", fg="MediumBluE", font="Arial 22")
	lb.place(width=850, height=40, x=0, y=5)

	lb = Label(fr1, text="Уравнение:", bg="white", fg="black", font="Arial 16")
	lb.place(width=150, height=40, x=350, y=80)

	#вычисление методов решения
	global ckv1
	global ckv2

	chvv = ""

#установление возмоджностей решения

	if ckv1==1 and ckv2==1:
		chvv = 1
	elif ckv1==1 and ckv2==0:
		chvv = 2
	elif ckv1==0 and ckv2==1:
		chvv = 3
	elif ckv1==0 and ckv2==0:
		chvv = 0

	global z
	vda = z.get()
	global zz
	vdb = zz.get()
	global zzz
	vdc = zzz.get()

	#вычисление вариантов прописания
	#a
	ka = ""
	if int(vda)==1:
		ka=1
	elif int(vda)>1:
		ka=2
	elif int(vda)<-1:
		ka=3
	elif int(vda)==0:
		ka=0
	elif int(vda)==-1:
		ka=4
	#b
	kb = ""
	if int(vdb)==1:
		kb=1
	elif int(vdb)>1:
		kb=2
	elif int(vdb)<-1:
		kb=3
	elif int(vdb)==0:
		kb=0
	elif int(vdb)==-1:
		kb=4
	#c
	kc = ""
	if int(vda)>0:
		kc=1
	elif int(vda)<0:
		kc=2
	elif int(vda)==0:
		kc=0

	#НАПИСАНИЕ УРАВНЕНИЯ
	#НАПИСАНИЕ УРАВНЕНИЯ
	#НАПИСАНИЕ УРАВНЕНИЯ
	y1 = len(vda)
	y2 = len(vdb)
	y3 = len(vdc)

	#отступ для b
	aa = 0

	#a
	#ширина объекта "x^2"
	otstyp1 = 30
	#ширина числа
	otstyp2 = y1*9
	#b
	#отступ при 0 значении
	otstyp3  = aa+10
	#ширина числа
	otstyp4 = y2*9
	#отступ для х
	otstyp5 = otstyp3+otstyp4
	#ширина числа
	otstyp10 = y3*9

	#печать коэффециента a
	if ka==0:
		lу = Label(fr1, text="Вы ввели не квадратное уравнение!", bg="white", fg="black", font="Arial 12")
		lу.place(width=850, height=40, x=0, y=120)
	elif ka==1:
		otstyp1 = 30
		l1d = Label(fr1, text="X^2", bg="white", fg="black", font="Arial 12")
		l1d.place(width=30, height=25, x=0, y=120)
		aa=30
	elif ka==2:
		l1d = Label(fr1, text=vda, bg="white", fg="black", font="Arial 12")
		l1d.place(width=otstyp2, height=25, x=0, y=120)
		l1d = Label(fr1, text="X^2", bg="white", fg="black", font="Arial 12")
		l1d.place(width=30, height=25, x=otstyp2, y=120)
		aa=otstyp2+30
	elif ka==3:
		l1d = Label(fr1, text=vda, bg="white", fg="black", font="Arial 12")
		l1d.place(width=otstyp2, height=25, x=0, y=120)
		l1000d = Label(fr1, text="X^2", bg="white", fg="black", font="Arial 12")
		l1000d.place(width=30, height=25, x=otstyp2, y=120)
		aa=otstyp2+30
	elif ka==4:
		otstyp1 = 30
		l1d = Label(fr1, text="-X^2", bg="white", fg="black", font="Arial 12")
		l1d.place(width=30, height=25, x=0, y=120)
		aa=30

	#печать коэффециента b

	otstyp6=aa+10
	otstyp7=otstyp6+otstyp4
	otstyp8=aa+otstyp4
	#отступ для c
	bb=0

	if kb==0:
		lу = Label(fr1, text="Вы ввели не квадратное уравнение!", bg="white", fg="black", font="Arial 12")
		lу.place(width=850, height=40, x=otstyp2, y=120)
	elif kb==1:
		l2d = Label(fr1, text="+", bg="white", fg="black", font="Arial 12")
		l2d.place(width=10, height=25, x=aa, y=120)
		l3d = Label(fr1, text="X", bg="white", fg="black", font="Arial 12")
		l3d.place(width=10, height=25, x=otstyp6, y=120)
		bb=otstyp6+10
	elif kb==2:
		l2d = Label(fr1, text="+", bg="white", fg="black", font="Arial 12")
		l2d.place(width=10, height=25, x=aa, y=120)
		l3d = Label(fr1, text=vdb, bg="white", fg="black", font="Arial 12")
		l3d.place(width=otstyp4, height=25, x=otstyp6, y=120)
		l4d = Label(fr1, text="X", bg="white", fg="black", font="Arial 12")
		l4d.place(width=10, height=25, x=otstyp7, y=120)
		bb=otstyp7+10
	elif kb==3:
		l3d = Label(fr1, text=vdb, bg="white", fg="black", font="Arial 12")
		l3d.place(width=otstyp4, height=25, x=aa, y=120)
		l4d = Label(fr1, text="X", bg="white", fg="black", font="Arial 12")
		l4d.place(width=10, height=25, x=otstyp8, y=120)
		bb=otstyp8+10
	elif kb==4:
		l2d = Label(fr1, text="-", bg="white", fg="black", font="Arial 12")
		l2d.place(width=10, height=25, x=aa, y=120)
		l3d = Label(fr1, text="X", bg="white", fg="black", font="Arial 12")
		l3d.place(width=10, height=25, x=otstyp6, y=120)
		bb=otstyp6+10

	otstyp9=bb+10
	otstyp11=otstyp9+otstyp10
	otstyp12=otstyp11+10
	#печать коэффециента c
	if kc==0:
		lу = Label(fr1, text="Вы ввели не квадратное уравнение!", bg="white", fg="black", font="Arial 12")
		lу.place(width=850, height=40, x=0, y=120)
	elif kc==1:
		l5d = Label(fr1, text="+", bg="white", fg="black", font="Arial 12")
		l5d.place(width=10, height=25, x=bb, y=120)
		l6d = Label(fr1, text=vdc, bg="white", fg="black", font="Arial 12")
		l6d.place(width=otstyp10, height=25, x=otstyp9, y=120)
		l7d = Label(fr1, text="=", bg="white", fg="black", font="Arial 12")
		l7d.place(width=10, height=25, x=otstyp11, y=120)
		l8d = Label(fr1, text="0", bg="white", fg="black", font="Arial 12")
		l8d.place(width=10, height=25, x=otstyp12, y=120)
	elif kc==2:
		l6d = Label(fr1, text=vdc, bg="white", fg="black", font="Arial 12")
		l6d.place(width=otstyp10, height=25, x=bb, y=120)
		l7d = Label(fr1, text="=", bg="white", fg="black", font="Arial 12")
		l7d.place(width=10, height=25, x=otstyp11, y=120)
		l8d = Label(fr1, text="0", bg="white", fg="black", font="Arial 12")
		l8d.place(width=10, height=25, x=otstyp12, y=120)

	#Решение
	#Решение
	#Решение
	#Решение
	#Решение
	
	if ka==0:
		lу = Label(fr2, text="Вы ввели не квадратное уравнение!", bg="white", fg="black", font="Arial 12")
		lу.place(width=850, height=40, x=0, y=50)
	elif ka==1:
		otstyp1 = 30
		l1d = Label(fr2, text="X^2", bg="white", fg="black", font="Arial 12")
		l1d.place(width=30, height=25, x=0, y=50)
		aa=30
	elif ka==2:
		l1d = Label(fr2, text=vda, bg="white", fg="black", font="Arial 12")
		l1d.place(width=otstyp2, height=25, x=0, y=50)
		l1d = Label(fr2, text="X^2", bg="white", fg="black", font="Arial 12")
		l1d.place(width=30, height=25, x=otstyp2, y=50)
		aa=otstyp2+30
	elif ka==3:
		l1d = Label(fr2, text=vda, bg="white", fg="black", font="Arial 12")
		l1d.place(width=otstyp2, height=25, x=0, y=50)
		l1000d = Label(fr2, text="X^2", bg="white", fg="black", font="Arial 12")
		l1000d.place(width=30, height=25, x=otstyp2, y=50)
		aa=otstyp2+30
	elif ka==4:
		otstyp1 = 30
		l1d = Label(fr2, text="-X^2", bg="white", fg="black", font="Arial 12")
		l1d.place(width=30, height=25, x=0, y=50)
		aa=30

	if kb==0:
		lу = Label(fr2, text="Вы ввели не квадратное уравнение!", bg="white", fg="black", font="Arial 12")
		lу.place(width=850, height=40, x=otstyp2, y=50)
	elif kb==1:
		l2d = Label(fr2, text="+", bg="white", fg="black", font="Arial 12")
		l2d.place(width=10, height=25, x=aa, y=50)
		l3d = Label(fr1, text="X", bg="white", fg="black", font="Arial 12")
		l3d.place(width=10, height=25, x=otstyp6, y=50)
		bb=otstyp6+10
	elif kb==2:
		l2d = Label(fr2, text="+", bg="white", fg="black", font="Arial 12")
		l2d.place(width=10, height=25, x=aa, y=50)
		l3d = Label(fr2, text=vdb, bg="white", fg="black", font="Arial 12")
		l3d.place(width=otstyp4, height=25, x=otstyp6, y=50)
		l4d = Label(fr2, text="X", bg="white", fg="black", font="Arial 12")
		l4d.place(width=10, height=25, x=otstyp7, y=50)
		bb=otstyp7+10
	elif kb==3:
		l3d = Label(fr2, text=vdb, bg="white", fg="black", font="Arial 12")
		l3d.place(width=otstyp4, height=25, x=aa, y=50)
		l4d = Label(fr2, text="X", bg="white", fg="black", font="Arial 12")
		l4d.place(width=10, height=25, x=otstyp8, y=50)
		bb=otstyp8+10
	elif kb==4:
		l2d = Label(fr2, text="-", bg="white", fg="black", font="Arial 12")
		l2d.place(width=10, height=25, x=aa, y=50)
		l3d = Label(fr2, text="X", bg="white", fg="black", font="Arial 12")
		l3d.place(width=10, height=25, x=otstyp6, y=50)
		bb=otstyp6+10

	if kc==0:
		lу = Label(fr2, text="Вы ввели не квадратное уравнение!", bg="white", fg="black", font="Arial 12")
		lу.place(width=850, height=40, x=0, y=50)
	elif kc==1:
		l5d = Label(fr2, text="+", bg="white", fg="black", font="Arial 12")
		l5d.place(width=10, height=25, x=bb, y=50)
		l6d = Label(fr2, text=vdc, bg="white", fg="black", font="Arial 12")
		l6d.place(width=otstyp10, height=25, x=otstyp9, y=50)
		l7d = Label(fr2, text="=", bg="white", fg="black", font="Arial 12")
		l7d.place(width=10, height=25, x=otstyp11, y=50)
		l8d = Label(fr2, text="0", bg="white", fg="black", font="Arial 12")
		l8d.place(width=10, height=25, x=otstyp12, y=50)
	elif kc==2:
		l6d = Label(fr2, text=vdc, bg="white", fg="black", font="Arial 12")
		l6d.place(width=otstyp10, height=25, x=bb, y=50)
		l7d = Label(fr2, text="=", bg="white", fg="black", font="Arial 12")
		l7d.place(width=10, height=25, x=otstyp11, y=50)
		l8d = Label(fr2, text="0", bg="white", fg="black", font="Arial 12")
		l8d.place(width=10, height=25, x=otstyp12, y=50)

	if chvv == 0:
		lу = Label(fr1, text="Выберите хотя бы один метод решения уравнения!", bg="white", fg="black", font="Arial 16")
		lу.place(width=850, height=40, x=0, y=120)
		lу0 = Label(fr2, text="Выберите хотя бы один метод решения уравнения!", bg="white", fg="black", font="Arial 16")
		lу0.place(width=850, height=40, x=0, y=50)

	#проверка метода коэффециентов
	ysl1 = ""
	mt1 = vda+vdb+vdc
	if mt1 == 0:
		ysl1 = 1
	else:
		ysl1 = 0

	ysl2 = ""
	mt2 = vda+vdc

	if vdb == mt2:
		ysl2 = 1
	else:
		ysl2 = 0

	if chvv == 3:
		if ysl1==0 and ysl2==0:
			lу = Label(fr1, text="Методом коэффециентов данное уравнение решить нельзя!", bg="white", fg="black", font="Arial 16")
			lу.place(width=850, height=40, x=0, y=120)
			lу0 = Label(fr2, text="Методом коэффециентов данное уравнение решить нельзя!", bg="white", fg="black", font="Arial 16")
			lу0.place(width=850, height=40, x=0, y=50)
		else:
			if ysl1==1:
				lу0 = Label(fr2, text="По свойству коэффециентов квадратногного уравнения:", bg="white", fg="black", font="Arial 12")
				lу0.place(width=410, height=25, x=0, y=75)
				l1d = Label(fr2, text="X1=1", bg="white", fg="black", font="Arial 12")
				l1d.place(width=40, height=25, x=0, y=100)
				l2d = Label(fr2, text="X2=C/A", bg="white", fg="black", font="Arial 12")
				l2d.place(width=55, height=25, x=0, y=125)
				re = int(vdc)/int(vda)
				y1 = len(str(re))
				ost = y1*9
				l2d = Label(fr2, text="X2=", bg="white", fg="black", font="Arial 12")
				l2d.place(width=30, height=25, x=0, y=150)
				l3d = Label(fr2, text=re, bg="white", fg="black", font="Arial 12")
				l3d.place(width=ost, height=25, x=30, y=150)
			if ysl2==1:
				lу0 = Label(fr2, text="По свойству коэффециентов квадратногного уравнения:", bg="white", fg="black", font="Arial 12")
				lу0.place(width=410, height=25, x=0, y=75)
				l1d = Label(fr2, text="X1=-1", bg="white", fg="black", font="Arial 12")
				l1d.place(width=46, height=25, x=0, y=100)
				l2d = Label(fr2, text="X2=-C/A", bg="white", fg="black", font="Arial 12")
				l2d.place(width=60, height=25, x=0, y=125)
				rem = int(vdc)* -1
				re = int(rem)/int(vda)
				y1 = len(str(re))
				ost = y1*9
				l2d = Label(fr2, text="X2=", bg="white", fg="black", font="Arial 12")
				l2d.place(width=30, height=25, x=0, y=150)
				l3d = Label(fr2, text=re, bg="white", fg="black", font="Arial 12")
				l3d.place(width=ost, height=25, x=30, y=150)
	
	if chvv == 2:
		b2 = int(vdb)**2
		ac = int(vda)*int(vdc)
		ac4 = 4*int(ac)
		diskr = int(b2)-int(ac4)
		ovdb = int(vdb) * -1 

		import math
		kor = math.sqrt(diskr)

		xp1 = int(ovdb) + int(kor)
		a21 = int(vda) * 2
		x1 = int(xp1)/int(a21)
		xp2 = int(ovdb) - int(kor)
		x2 = int(xp2)/int(a21)

		px = int(b2)/int(ac4)

		do = len(str(diskr))
		otstyp0 = do*9

		po = len(str(px))
		otstyp1 = po*9

		lу0 = Label(fr2, text="D=b^2-4ac", bg="white", fg="black", font="Arial 12")
		lу0.place(width=80, height=25, x=0, y=75)
		lу1 = Label(fr2, text="D=", bg="white", fg="black", font="Arial 12")
		lу1.place(width=20, height=25, x=0, y=100)
		lу2 = Label(fr2, text=diskr, bg="white", fg="black", font="Arial 12")
		lу2.place(width=otstyp0, height=25, x=20, y=100)


		#if int(diskr)<0:
		
		#elif diskr==0:
		#	lу3 = Label(fr2, text="x=", bg="white", fg="black", font="Arial 12")
		#	lу3.place(width=20, height=25, x=0, y=125)
		#	lу4 = Label(fr2, text=px, bg="white", fg="black", font="Arial 12")
		#	lу4.place(width=otstyp1, height=25, x=20, y=125)



def vvod_kvad_yrav():
	global choice
	choice = 2
	clean_fr1 = Label(fr1, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr1.place(width=850, height=250, x=0, y=0)
	clean_fr2 = Label(fr2, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr2.place(width=850, height=510, x=0, y=0)

	lab = Label(fr1, text="Решение квадратных уравнений", bg="white", fg="MediumBluE", font="Arial 22")
	lab.place(width=850, height=40, x=0, y=5)
	global z
	za = Label(fr1, text="Введите коэффициент a:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	za.place(width=150, height=20, x=0, y=40)
	z = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	z.place(width=100, height=16, x=150, y=44)
	global zz
	zo = Label(fr1, text="Введите коэффициент b:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	zo.place(width=150, height=20, x=0, y=60)
	zz = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	zz.place(width=100, height=16, x=150, y=64)
	global zzz
	zu = Label(fr1, text="Введите коэффициент c:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	zu.place(width=150, height=20, x=0, y=80)
	zzz = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	zzz.place(width=100, height=16, x=150, y=84)

	lb = Label(fr1, text="Выберите способы, с помощью которых нужно решить уравнение:", bg="white", fg="black", font="Arial 10")
	lb.place(width=850, height=20, x=0, y=170)

	sp1 = Checkbutton(fr1, text="Дискриминант", bg="white", font="Arial 12", justify=LEFT, command=kvad_yr1,
		activebackground="MediumBluE", activeforeground="white")
	sp1.place(width=130, height=25, x=275, y=190)

	sp2 = Checkbutton(fr1, text="Метод коэффициентов", bg="white", font="Arial 12", justify=LEFT, command=kvad_yr2,
		activebackground="MediumBluE", activeforeground="white")
	sp2.place(width=190, height=25, x=405, y=190)

	kresh = Button(fr1, text="Решить", background="white", foreground="MediumBluE", font="Arial 16", command=clk)
	kresh.place(width=120, height=30, x=362, y=220)

	L = Label(fr2, text="Решение уравниения с помощью дискриминанта находиться в стадии разработки, поэтому будет работать некоректно", bg="white", fg="black", font="Arial 10")
	L.place(width=850, height=14, x=0, y=490)


def kvad_yr1():
	global ckv1
	ckv1 = 1
def kvad_yr2():
	global ckv2
	ckv2 = 1 

# И Н Ф О Р М А Т И К А
# И Н Ф О Р М А Т И К А
# И Н Ф О Р М А Т И К А
# И Н Ф О Р М А Т И К А
# И Н Ф О Р М А Т И К А

def dvy_res():
	global dva
	dv = dva.get()
	rr = bin(int(dv))
	ld = Label(fr2, text=rr, bg="white", fg="black", font="Arial 12")
	ld.place(width=850, height=25, x=0, y=50)
def dvy_vv():
	clean_fr1 = Label(fr1, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr1.place(width=850, height=250, x=0, y=0)
	clean_fr2 = Label(fr2, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr2.place(width=850, height=510, x=0, y=0)

	global choice
	choice = 8
	#Первый фрэйм, ввод чисел
	lab = Label(fr1, text="Введите число для перевода:", bg="white", fg="MediumBluE", font="Arial 22")
	lab.place(width=850, height=40, x=0, y=5)

	global dva
	dva = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	dva.place(width=500, height=16, x=175, y=70)

	kresh = Button(fr1, text="Перевести", background="white", foreground="MediumBluE", font="Arial 16", command=dvy_res)
	kresh.place(width=120, height=30, x=362, y=170)
	
	lb = Label(fr2, text="Переведённое число:", bg="white", fg="MediumBluE", font="Arial 22")
	lb.place(width=850, height=40, x=0, y=5)

def voc_res():
	global vos
	dv = vos.get()
	rr = oct(int(dv))
	ld = Label(fr2, text=rr, bg="white", fg="black", font="Arial 12")
	ld.place(width=850, height=25, x=0, y=50)
def vos_vv():
	clean_fr1 = Label(fr1, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr1.place(width=850, height=250, x=0, y=0)
	clean_fr2 = Label(fr2, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr2.place(width=850, height=510, x=0, y=0)

	global choice
	choice = 9
	#Первый фрэйм, ввод чисел
	lab = Label(fr1, text="Введите число для перевода:", bg="white", fg="MediumBluE", font="Arial 22")
	lab.place(width=850, height=40, x=0, y=5)

	global vos
	vos = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	vos.place(width=500, height=16, x=175, y=70)

	kresh = Button(fr1, text="Перевести", background="white", foreground="MediumBluE", font="Arial 16", command=voc_res)
	kresh.place(width=120, height=30, x=362, y=170)
	
	lb = Label(fr2, text="Переведённое число:", bg="white", fg="MediumBluE", font="Arial 22")
	lb.place(width=850, height=40, x=0, y=5)

def shest_res():
	global shest
	dv = shest.get()
	rr = hex(int(dv))
	ld = Label(fr2, text=rr, bg="white", fg="black", font="Arial 12")
	ld.place(width=850, height=25, x=0, y=50)
def shest_vv():
	clean_fr1 = Label(fr1, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr1.place(width=850, height=250, x=0, y=0)
	clean_fr2 = Label(fr2, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr2.place(width=850, height=510, x=0, y=0)

	global choice
	choice = 10
	#Первый фрэйм, ввод чисел
	lab = Label(fr1, text="Введите число для перевода:", bg="white", fg="MediumBluE", font="Arial 22")
	lab.place(width=850, height=40, x=0, y=5)

	global shest
	shest = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	shest.place(width=500, height=16, x=175, y=70)

	kresh = Button(fr1, text="Перевести", background="white", foreground="MediumBluE", font="Arial 16", command=shest_res)
	kresh.place(width=120, height=30, x=362, y=170)
	
	lb = Label(fr2, text="Переведённое число:", bg="white", fg="MediumBluE", font="Arial 22")
	lb.place(width=850, height=40, x=0, y=5)

# П Р О С Т Ы Е   В Ы Ч И С Л Е Н И Я
# П Р О С Т Ы Е   В Ы Ч И С Л Е Н И Я
# П Р О С Т Ы Е   В Ы Ч И С Л Е Н И Я
# П Р О С Т Ы Е   В Ы Ч И С Л Е Н И Я
# П Р О С Т Ы Е   В Ы Ч И С Л Е Н И Я
#СЛОЖЕНИЕ
def click(): 
	global vv
	rr = vv.get()
	global vvv
	ff = vvv.get()
	resh = int(rr)+int(ff)
	y1 = len(rr)
	y2 = len(ff)
	y3 = len(str(resh))
	otstyp1 = y1*9
	otstyp2 = y2*9
	otstyp3 = otstyp1+20
	otstyp4 = otstyp3+10
	otstyp5 = otstyp4+otstyp2
	otstyp6 = otstyp5+10
	otstyp7 = y3*9
	l1d = Label(fr2, text="1)", bg="white", fg="black", font="Arial 12")
	l1d.place(width=20, height=25, x=0, y=50)
	l2d = Label(fr2, text=rr, bg="white", fg="black", font="Arial 12")
	l2d.place(width=otstyp1, height=25, x=20, y=50)
	l3d = Label(fr2, text="+", bg="white", fg="black", font="Arial 12")
	l3d.place(width=10, height=25, x=otstyp3, y=50)
	l4d = Label(fr2, text=ff, bg="white", fg="black", font="Arial 12")
	l4d.place(width=otstyp2, height=25, x=otstyp4, y=50)
	l5d = Label(fr2, text="=", bg="white", fg="black", font="Arial 12")
	l5d.place(width=10, height=25, x=otstyp5, y=50)
	l6d = Label(fr2, text=resh, bg="white", fg="black", font="Arial 12")
	l6d.place(width=otstyp7, height=25, x=otstyp6, y=50)
def prost_slog():
	clean_fr1 = Label(fr1, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr1.place(width=850, height=250, x=0, y=0)
	clean_fr2 = Label(fr2, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr2.place(width=850, height=510, x=0, y=0)

	global choice
	choice = 11
	#Первый фрэйм, ввод чисел
	lab = Label(fr1, text="Введите числа:", bg="white", fg="MediumBluE", font="Arial 22")
	lab.place(width=850, height=40, x=0, y=5)
	global vv
	ov = Label(fr1, text="Введите 1-ое слагаемое:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	ov.place(width=160, height=20, x=0, y=40)
	vv = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	vv.place(width=100, height=16, x=160, y=44)
	global vvv
	vo = Label(fr1, text="Введите 2-ое слагаемое:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	vo.place(width=160, height=20, x=0, y=60)
	vvv = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	vvv.place(width=100, height=16, x=160, y=64)
	
	#установка первоначальных значений
	
	kresh = Button(fr1, text="Решить", background="white", foreground="MediumBluE", font="Arial 16", command=click)
	kresh.place(width=120, height=30, x=362, y=170)
	
	lb = Label(fr2, text="Решение:", bg="white", fg="MediumBluE", font="Arial 22")
	lb.place(width=850, height=40, x=0, y=5)
#УМНОЖЕНИЕ
def clack(): 
	global qq
	rr = qq.get()
	global qqq
	ff = qqq.get()
	resh = int(rr)*int(ff)
	y1 = len(rr)
	y2 = len(ff)
	y3 = len(str(resh))
	otstyp1 = y1*9
	otstyp2 = y2*9
	otstyp3 = otstyp1+20
	otstyp4 = otstyp3+10
	otstyp5 = otstyp4+otstyp2
	otstyp6 = otstyp5+10
	otstyp7 = y3*9
	l1d = Label(fr2, text="1)", bg="white", fg="black", font="Arial 12")
	l1d.place(width=20, height=25, x=0, y=50)
	l2d = Label(fr2, text=rr, bg="white", fg="black", font="Arial 12")
	l2d.place(width=otstyp1, height=25, x=20, y=50)
	l3d = Label(fr2, text="•", bg="white", fg="black", font="Arial 12")
	l3d.place(width=10, height=25, x=otstyp3, y=50)
	l4d = Label(fr2, text=ff, bg="white", fg="black", font="Arial 12")
	l4d.place(width=otstyp2, height=25, x=otstyp4, y=50)
	l5d = Label(fr2, text="=", bg="white", fg="black", font="Arial 12")
	l5d.place(width=10, height=25, x=otstyp5, y=50)
	l6d = Label(fr2, text=resh, bg="white", fg="black", font="Arial 12")
	l6d.place(width=otstyp7, height=25, x=otstyp6, y=50)
def prost_ymnog():
	clean_fr1 = Label(fr1, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr1.place(width=850, height=250, x=0, y=0)
	clean_fr2 = Label(fr2, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr2.place(width=850, height=510, x=0, y=0)

	global choice
	choice = 13
	#Первый фрэйм, ввод чисел
	lab = Label(fr1, text="Введите числа:", bg="white", fg="MediumBluE", font="Arial 22")
	lab.place(width=850, height=40, x=0, y=5)
	global qq
	ov = Label(fr1, text="Введите 1-ый множитель:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	ov.place(width=160, height=20, x=0, y=40)
	qq = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	qq.place(width=100, height=16, x=160, y=44)
	global qqq
	vo = Label(fr1, text="Введите 2-ой множитель:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	vo.place(width=160, height=20, x=0, y=60)
	qqq = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	qqq.place(width=100, height=16, x=160, y=64)
	
	kresh = Button(fr1, text="Решить", background="white", foreground="MediumBluE", font="Arial 16", command=clack)
	kresh.place(width=120, height=30, x=362, y=170)
	
	#Второй фрэйм, вывод результата 
	
	lb = Label(fr2, text="Решение:", bg="white", fg="MediumBluE", font="Arial 22")
	lb.place(width=850, height=40, x=0, y=5)
	strl="0123456789"
#ДЕЛЕНИЕ
def cleck(): 
	global ww
	rr = ww.get()
	global www
	ff = www.get()
	resh = int(rr)/int(ff)
	y1 = len(rr)
	y2 = len(ff)
	y3 = len(str(resh))
	otstyp1 = y1*9
	otstyp2 = y2*9
	otstyp3 = otstyp1+20
	otstyp4 = otstyp3+10
	otstyp5 = otstyp4+otstyp2
	otstyp6 = otstyp5+10
	otstyp7 = y3*9
	l1d = Label(fr2, text="1)", bg="white", fg="black", font="Arial 12")
	l1d.place(width=20, height=25, x=0, y=50)
	l2d = Label(fr2, text=rr, bg="white", fg="black", font="Arial 12")
	l2d.place(width=otstyp1, height=25, x=20, y=50)
	l3d = Label(fr2, text=":", bg="white", fg="black", font="Arial 12")
	l3d.place(width=10, height=25, x=otstyp3, y=50)
	l4d = Label(fr2, text=ff, bg="white", fg="black", font="Arial 12")
	l4d.place(width=otstyp2, height=25, x=otstyp4, y=50)
	l5d = Label(fr2, text="=", bg="white", fg="black", font="Arial 12")
	l5d.place(width=10, height=25, x=otstyp5, y=50)
	l6d = Label(fr2, text=resh, bg="white", fg="black", font="Arial 12")
	l6d.place(width=otstyp7, height=25, x=otstyp6, y=50)
def prost_del():
	clean_fr1 = Label(fr1, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr1.place(width=850, height=250, x=0, y=0)
	clean_fr2 = Label(fr2, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr2.place(width=850, height=510, x=0, y=0)

	global choice
	choice = 14
	#Первый фрэйм, ввод чисел
	lab = Label(fr1, text="Введите числа:", bg="white", fg="MediumBluE", font="Arial 22")
	lab.place(width=850, height=40, x=0, y=5)
	global ww
	ov = Label(fr1, text="Введите делимое:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	ov.place(width=160, height=20, x=0, y=40)
	ww = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	ww.place(width=100, height=16, x=160, y=44)
	global www
	vo = Label(fr1, text="Введите делитель:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	vo.place(width=160, height=20, x=0, y=60)
	www = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	www.place(width=100, height=16, x=160, y=64)
	
	kresh = Button(fr1, text="Решить", background="white", foreground="MediumBluE", font="Arial 16", command=cleck)
	kresh.place(width=120, height=30, x=362, y=170)
	
	#Второй фрэйм, вывод результата 
	
	lb = Label(fr2, text="Решение:", bg="white", fg="MediumBluE", font="Arial 22")
	lb.place(width=850, height=40, x=0, y=5)
#ВЫЧИТАНИЕ
def clock(): 
	global ee
	rr = ee.get()
	global eee
	ff = eee.get()
	resh = int(rr)-int(ff)
	y1 = len(rr)
	y2 = len(ff)
	y3 = len(str(resh))
	otstyp1 = y1*9
	otstyp2 = y2*9
	otstyp3 = otstyp1+20
	otstyp4 = otstyp3+10
	otstyp5 = otstyp4+otstyp2
	otstyp6 = otstyp5+10
	otstyp7 = y3*9
	l1d = Label(fr2, text="1)", bg="white", fg="black", font="Arial 12")
	l1d.place(width=20, height=25, x=0, y=50)
	l2d = Label(fr2, text=rr, bg="white", fg="black", font="Arial 12")
	l2d.place(width=otstyp1, height=25, x=20, y=50)
	l3d = Label(fr2, text="-", bg="white", fg="black", font="Arial 12")
	l3d.place(width=10, height=25, x=otstyp3, y=50)
	l4d = Label(fr2, text=ff, bg="white", fg="black", font="Arial 12")
	l4d.place(width=otstyp2, height=25, x=otstyp4, y=50)
	l5d = Label(fr2, text="=", bg="white", fg="black", font="Arial 12")
	l5d.place(width=10, height=25, x=otstyp5, y=50)
	l6d = Label(fr2, text=resh, bg="white", fg="black", font="Arial 12")
	l6d.place(width=otstyp7, height=25, x=otstyp6, y=50)
def prost_vichit():
	clean_fr1 = Label(fr1, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr1.place(width=850, height=250, x=0, y=0)
	clean_fr2 = Label(fr2, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr2.place(width=850, height=510, x=0, y=0)

	global choice
	choice = 12
	#Первый фрэйм, ввод чисел
	lab = Label(fr1, text="Введите числа:", bg="white", fg="MediumBluE", font="Arial 22")
	lab.place(width=850, height=40, x=0, y=5)
	global ee
	ov = Label(fr1, text="Введите 1-ое число:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	ov.place(width=160, height=20, x=0, y=40)
	ee = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	ee.place(width=100, height=16, x=160, y=44)
	global eee
	vo = Label(fr1, text="Введите 2-ое число:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	vo.place(width=160, height=20, x=0, y=60)
	eee = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	eee.place(width=100, height=16, x=160, y=64)
	
	kresh = Button(fr1, text="Решить", background="white", foreground="MediumBluE", font="Arial 16", command=clock)
	kresh.place(width=120, height=30, x=362, y=170)
	
	#Второй фрэйм, вывод результата 
	
	lb = Label(fr2, text="Решение:", bg="white", fg="MediumBluE", font="Arial 22")
	lb.place(width=850, height=40, x=0, y=5)
#ВОЗВЕДЕНИЕ В СТЕПЕНЬ
def clyck(): 
	global tt
	rr = tt.get()
	global ttt
	ff = ttt.get()
	resh = int(rr)**int(ff)
	l1d = Label(fr2, text=resh, bg="white", fg="black", font="Arial 16")
	l1d.place(width=850, height=25, x=0, y=50)
def prost_stepen():
	clean_fr1 = Label(fr1, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr1.place(width=850, height=250, x=0, y=0)
	clean_fr2 = Label(fr2, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr2.place(width=850, height=510, x=0, y=0)

	global choice
	choice = 16
	#Первый фрэйм, ввод чисел
	lab = Label(fr1, text="Возведение в степень:", bg="white", fg="MediumBluE", font="Arial 22")
	lab.place(width=850, height=40, x=0, y=5)
	global tt
	ov = Label(fr1, text="Введите число:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	ov.place(width=97, height=20, x=0, y=40)
	tt = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	tt.place(width=100, height=16, x=110, y=44)
	global ttt
	vo = Label(fr1, text="Введите степень:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	vo.place(width=110, height=20, x=0, y=60)
	ttt = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	ttt.place(width=100, height=16, x=110, y=64)
	
	kresh = Button(fr1, text="Возвести", background="white", foreground="MediumBluE", font="Arial 16", command=clyck)
	kresh.place(width=200, height=30, x=325, y=170)
	
	#Второй фрэйм, вывод результата 
	
	lb = Label(fr2, text="Возведенное число:", bg="white", fg="MediumBluE", font="Arial 22")
	lb.place(width=850, height=40, x=0, y=5)
#ИЗВЛЕЧЕНИЕ КОРНЯ
def cluck(): 
	global yy
	rr = yy.get()

	import math
	resh = math.sqrt(int(rr))

	l1d = Label(fr2, text=resh, bg="white", fg="black", font="Arial 16")
	l1d.place(width=850, height=25, x=0, y=50)
def prost_koren():
	clean_fr1 = Label(fr1, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr1.place(width=850, height=250, x=0, y=0)
	clean_fr2 = Label(fr2, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr2.place(width=850, height=510, x=0, y=0)

	global choice
	choice = 15
	#Первый фрэйм, ввод чисел
	lab = Label(fr1, text="Извлечение корня", bg="white", fg="MediumBluE", font="Arial 22")
	lab.place(width=850, height=40, x=0, y=5)
	global yy
	ov = Label(fr1, text="Введите число:", bg="white", fg="black", font="Arial 10", justify=LEFT)
	ov.place(width=97, height=20, x=0, y=40)
	yy = Entry(fr1, bg="whitesmoke", bd=1, fg="MediumBluE", font="Arial 12", width=20)
	yy.place(width=100, height=16, x=110, y=44)
	
	kresh = Button(fr1, text="Извлечь", background="white", foreground="MediumBluE", font="Arial 16", command=cluck)
	kresh.place(width=200, height=30, x=325, y=170)

	lb = Label(fr2, text="Корень числа", bg="white", fg="MediumBluE", font="Arial 22")
	lb.place(width=850, height=40, x=0, y=5)


# Х И М И Я
# Х И М И Я
# Х И М И Я
# Х И М И Я
# Х И М И Я

#Характеристика хим элементов
#Характеристика хим элементов
#Характеристика хим элементов

def harakter():
	clean_fr1 = Label(fr1, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr1.place(width=850, height=250, x=0, y=0)
	clean_fr2 = Label(fr2, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr2.place(width=850, height=510, x=0, y=0)

	global choice
	choice = 0

	lab = Label(fr1, text="Выберите элемент:", bg="white", fg="MediumBluE", font="Arial 20")
	lab.place(width=850, height=30, x=0, y=0)
	#ряд
	l1b = Label(fr1, text="1", bg="white", fg="black", font="Arial 12")
	l1b.place(width=15, height=20, x=0, y=50)
	l2b = Label(fr1, text="2", bg="white", fg="black", font="Arial 12")
	l2b.place(width=15, height=20, x=0, y=70)
	l3b = Label(fr1, text="3", bg="white", fg="black", font="Arial 12")
	l3b.place(width=15, height=20, x=0, y=90)
	l4b = Label(fr1, text="4", bg="white", fg="black", font="Arial 12")
	l4b.place(width=15, height=20, x=0, y=110)
	l5b = Label(fr1, text="5", bg="white", fg="black", font="Arial 12")
	l5b.place(width=15, height=20, x=0, y=130)
	l6b = Label(fr1, text="6", bg="white", fg="black", font="Arial 12")
	l6b.place(width=15, height=20, x=0, y=150)
	l7b = Label(fr1, text="7", bg="white", fg="black", font="Arial 12")
	l7b.place(width=15, height=20, x=0, y=170)
	l0b = Label(fr1, text="8", bg="white", fg="black", font="Arial 12")
	l0b.place(width=15, height=20, x=0, y=190)
	lob = Label(fr1, text="9", bg="white", fg="black", font="Arial 12")
	lob.place(width=15, height=20, x=0, y=210)
	lcb = Label(fr1, text="10", bg="white", fg="black", font="Arial 10")
	lcb.place(width=20, height=20, x=0, y=230)
	#группы
	l8b = Label(fr1, text="I", bg="white", fg="black", font="Arial 12")
	l8b.place(width=40, height=20, x=15, y=30)
	l9b = Label(fr1, text="II", bg="white", fg="black", font="Arial 12")
	l9b.place(width=40, height=20, x=55, y=30)
	l10b = Label(fr1, text="III", bg="white", fg="black", font="Arial 12")
	l10b.place(width=40, height=20, x=95, y=30)
	l11b = Label(fr1, text="IV", bg="white", fg="black", font="Arial 12")
	l11b.place(width=40, height=20, x=135, y=30)
	l12b = Label(fr1, text="V", bg="white", fg="black", font="Arial 12")
	l12b.place(width=40, height=20, x=175, y=30)
	l13b = Label(fr1, text="VI", bg="white", fg="black", font="Arial 12")
	l13b.place(width=40, height=20, x=215, y=30)
	l14b = Label(fr1, text="VII", bg="white", fg="black", font="Arial 12")
	l14b.place(width=40, height=20, x=255, y=30)
	l15b = Label(fr1, text="VIII", bg="white", fg="black", font="Arial 12")
	l15b.place(width=40, height=20, x=295, y=30)

	lang = IntVar()
	# 1 ряд
	H_checkbutton = Radiobutton(fr1, text="H", bg="LimeGreen", font="Arial 12", value=1, justify=LEFT, command=H_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	H_checkbutton.place(width=40, height=20, x=15, y=50)

	Hh_checkbutton = Radiobutton(fr1, text="H", bg="Yellow", font="Arial 12", value=1, justify=LEFT, command=Hh_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Hh_checkbutton.place(width=40, height=20, x=255, y=50)

	He_checkbutton = Radiobutton(fr1, text="He", bg="DarkOrchid", font="Arial 12", value=2, justify=LEFT, command=He_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	He_checkbutton.place(width=40, height=20, x=295, y=50)
	# 2 ряд
	Li_checkbutton = Radiobutton(fr1, text="Li", bg="LimeGreen", font="Arial 12", value=3, justify=LEFT, command=Li_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Li_checkbutton.place(width=40, height=20, x=15, y=70)

	Be_checkbutton = Radiobutton(fr1, text="Be", bg="LimeGreen", font="Arial 12", value=4, justify=LEFT, command=Be_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Be_checkbutton.place(width=40, height=20, x=55, y=70)

	B_checkbutton = Radiobutton(fr1, text="B", bg="Yellow", font="Arial 12", value=5, justify=LEFT, command=B_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	B_checkbutton.place(width=40, height=20, x=95, y=70)

	C_checkbutton = Radiobutton(fr1, text="C", bg="Yellow", font="Arial 12", value=6, justify=LEFT, command=C_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	C_checkbutton.place(width=40, height=20, x=135, y=70)

	N_checkbutton = Radiobutton(fr1, text="N", bg="Yellow", font="Arial 12", value=7, justify=LEFT, command=N_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	N_checkbutton.place(width=40, height=20, x=175, y=70)

	O_checkbutton = Radiobutton(fr1, text="O", bg="Yellow", font="Arial 12", value=8, justify=LEFT, command=O_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	O_checkbutton.place(width=40, height=20, x=215, y=70)

	F_checkbutton = Radiobutton(fr1, text="N", bg="Yellow", font="Arial 12", value=9, justify=LEFT, command=F_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	F_checkbutton.place(width=40, height=20, x=255, y=70)

	Ne_checkbutton = Radiobutton(fr1, text="Ne", bg="DarkOrchid", font="Arial 12", value=10, justify=LEFT,command=Ne_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Ne_checkbutton.place(width=40, height=20, x=295, y=70)
	# 3 ряд
	Na_checkbutton = Radiobutton(fr1, text="Na", bg="LimeGreen", font="Arial 12", value=11, justify=LEFT, command=Na_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Na_checkbutton.place(width=40, height=20, x=15, y=90)

	Mg_checkbutton = Radiobutton(fr1, text="Mg", bg="LimeGreen", font="Arial 12", value=12, justify=LEFT, command=Mg_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Mg_checkbutton.place(width=40, height=20, x=55, y=90)

	Al_checkbutton = Radiobutton(fr1, text="Al", bg="DeepPink", font="Arial 12", value=13, justify=LEFT, command=Al_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Al_checkbutton.place(width=40, height=20, x=95, y=90)

	Si_checkbutton = Radiobutton(fr1, text="Si", bg="Yellow", font="Arial 12", value=14, justify=LEFT, command=Si_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Si_checkbutton.place(width=40, height=20, x=135, y=90)

	P_checkbutton = Radiobutton(fr1, text="P", bg="Yellow", font="Arial 12", value=15, justify=LEFT, command=P_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	P_checkbutton.place(width=40, height=20, x=175, y=90)

	S_checkbutton = Radiobutton(fr1, text="S", bg="Yellow", font="Arial 12", value=16, justify=LEFT, command=S_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	S_checkbutton.place(width=40, height=20, x=215, y=90)

	Cl_checkbutton = Radiobutton(fr1, text="Cl", bg="Yellow", font="Arial 12", value=17, justify=LEFT, command=Cl_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Cl_checkbutton.place(width=40, height=20, x=255, y=90)

	Ar_checkbutton = Radiobutton(fr1, text="Ar", bg="DarkOrchid", font="Arial 12", value=18, justify=LEFT, command=Ar_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Ar_checkbutton.place(width=40, height=20, x=295, y=90)
	# 4 ряд
	K_checkbutton = Radiobutton(fr1, text="K", bg="LimeGreen", font="Arial 12", value=19, justify=LEFT, command=K_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	K_checkbutton.place(width=40, height=20, x=15, y=110)

	Ca_checkbutton = Radiobutton(fr1, text="Ca", bg="LimeGreen", font="Arial 12", value=20, justify=LEFT, command=Ca_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Ca_checkbutton.place(width=40, height=20, x=55, y=110)

	Sc_checkbutton = Radiobutton(fr1, text="Sc", bg="LimeGreen", font="Arial 12", value=21, justify=LEFT, command=Sc_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Sc_checkbutton.place(width=40, height=20, x=95, y=110)

	Ti_checkbutton = Radiobutton(fr1, text="Ti", bg="LimeGreen", font="Arial 12", value=22, justify=LEFT, command=Ti_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Ti_checkbutton.place(width=40, height=20, x=135, y=110)

	V_checkbutton = Radiobutton(fr1, text="V", bg="LimeGreen", font="Arial 12", value=23, justify=LEFT, command=V_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	V_checkbutton.place(width=40, height=20, x=175, y=110)

	Cr_checkbutton = Radiobutton(fr1, text="Cr", bg="LimeGreen", font="Arial 12", value=24, justify=LEFT, command=Cr_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Cr_checkbutton.place(width=40, height=20, x=215, y=110)

	Mn_checkbutton = Radiobutton(fr1, text="Mn", bg="LimeGreen", font="Arial 12", value=25, justify=LEFT, command=Mn_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Mn_checkbutton.place(width=40, height=20, x=255, y=110)

	Fe_checkbutton = Radiobutton(fr1, text="Fe", bg="LimeGreen", font="Arial 12", value=26, justify=LEFT, command=Fe_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Fe_checkbutton.place(width=40, height=20, x=295, y=110)

	Co_checkbutton = Radiobutton(fr1, text="Co", bg="LimeGreen", font="Arial 12", value=27, justify=LEFT, command=Co_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Co_checkbutton.place(width=40, height=20, x=335, y=110)

	Ni_checkbutton = Radiobutton(fr1, text="Ni", bg="LimeGreen", font="Arial 12", value=28, justify=LEFT, command=Ni_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Ni_checkbutton.place(width=40, height=20, x=375, y=110)
	# 5 ряд
	Cu_checkbutton = Radiobutton(fr1, text="Cu", bg="LimeGreen", font="Arial 12", value=29, justify=LEFT, command=Cu_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Cu_checkbutton.place(width=40, height=20, x=15, y=130)

	Zn_checkbutton = Radiobutton(fr1, text="Zn", bg="LimeGreen", font="Arial 12", value=30, justify=LEFT, command=Zn_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Zn_checkbutton.place(width=40, height=20, x=55, y=130)

	Ga_checkbutton = Radiobutton(fr1, text="Ga", bg="LimeGreen", font="Arial 12", value=31, justify=LEFT, command=Ga_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Ga_checkbutton.place(width=40, height=20, x=95, y=130)

	Ge_checkbutton = Radiobutton(fr1, text="Ge", bg="DeepPink", font="Arial 12", value=32, justify=LEFT, command=Ge_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Ge_checkbutton.place(width=40, height=20, x=135, y=130)

	As_checkbutton = Radiobutton(fr1, text="As", bg="Yellow", font="Arial 12", value=33, justify=LEFT, command=As_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	As_checkbutton.place(width=40, height=20, x=175, y=130)

	Se_checkbutton = Radiobutton(fr1, text="Se", bg="Yellow", font="Arial 12", value=34, justify=LEFT, command=Se_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Se_checkbutton.place(width=40, height=20, x=215, y=130)

	Br_checkbutton = Radiobutton(fr1, text="Br", bg="Yellow", font="Arial 12", value=35, justify=LEFT, command=Br_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Br_checkbutton.place(width=40, height=20, x=255, y=130)

	Kr_checkbutton = Radiobutton(fr1, text="Kr", bg="DarkOrchid", font="Arial 12", value=36, justify=LEFT, command=Kr_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Kr_checkbutton.place(width=40, height=20, x=295, y=130)
	# 6 ряд
	Rb_checkbutton = Radiobutton(fr1, text="Rb", bg="LimeGreen", font="Arial 12", value=37, justify=LEFT, command=Rb_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Rb_checkbutton.place(width=40, height=20, x=15, y=150)

	Sr_checkbutton = Radiobutton(fr1, text="Sr", bg="LimeGreen", font="Arial 12", value=38, justify=LEFT, command=Sr_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Sr_checkbutton.place(width=40, height=20, x=55, y=150)

	Y_checkbutton = Radiobutton(fr1, text="Y", bg="LimeGreen", font="Arial 12", value=39, justify=LEFT, command=Y_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Y_checkbutton.place(width=40, height=20, x=95, y=150)

	Zr_checkbutton = Radiobutton(fr1, text="Zr", bg="LimeGreen", font="Arial 12", value=40, justify=LEFT, command=Zr_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Zr_checkbutton.place(width=40, height=20, x=135, y=150)

	Nb_checkbutton = Radiobutton(fr1, text="Nb", bg="LimeGreen", font="Arial 12", value=41, justify=LEFT, command=Nb_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Nb_checkbutton.place(width=40, height=20, x=175, y=150)

	Mo_checkbutton = Radiobutton(fr1, text="Mo", bg="LimeGreen", font="Arial 12", value=42, justify=LEFT, command=Mo_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Mo_checkbutton.place(width=40, height=20, x=215, y=150)

	Tc_checkbutton = Radiobutton(fr1, text="Tc", bg="LimeGreen", font="Arial 12", value=43, justify=LEFT, command=Tc_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Tc_checkbutton.place(width=40, height=20, x=255, y=150)

	Ru_checkbutton = Radiobutton(fr1, text="Ru", bg="LimeGreen", font="Arial 12", value=44, justify=LEFT, command=Ru_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Ru_checkbutton.place(width=40, height=20, x=295, y=150)

	Rh_checkbutton = Radiobutton(fr1, text="Rh", bg="LimeGreen", font="Arial 12", value=45, justify=LEFT, command=Rh_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Rh_checkbutton.place(width=40, height=20, x=335, y=150)

	Pd_checkbutton = Radiobutton(fr1, text="Pd", bg="LimeGreen", font="Arial 12", value=46, justify=LEFT, command=Pd_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Pd_checkbutton.place(width=40, height=20, x=375, y=150)
	# 7 ряд
	Ag_checkbutton = Radiobutton(fr1, text="Ag", bg="LimeGreen", font="Arial 12", value=47, justify=LEFT, command=Ag_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Ag_checkbutton.place(width=40, height=20, x=15, y=170)

	Cd_checkbutton = Radiobutton(fr1, text="Cd", bg="LimeGreen", font="Arial 12", value=48, justify=LEFT, command=Cd_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Cd_checkbutton.place(width=40, height=20, x=55, y=170)

	In_checkbutton = Radiobutton(fr1, text="In", bg="DeepPink", font="Arial 12", value=49, justify=LEFT, command=In_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	In_checkbutton.place(width=40, height=20, x=95, y=170)

	Sn_checkbutton = Radiobutton(fr1, text="Sn", bg="DeepPink", font="Arial 12", value=50, justify=LEFT, command=Sn_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Sn_checkbutton.place(width=40, height=20, x=135, y=170)

	Sb_checkbutton = Radiobutton(fr1, text="In", bg="DeepPink", font="Arial 12", value=51, justify=LEFT, command=Sb_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Sb_checkbutton.place(width=40, height=20, x=175, y=170)

	Te_checkbutton = Radiobutton(fr1, text="Te", bg="Yellow", font="Arial 12", value=52, justify=LEFT, command=Te_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Te_checkbutton.place(width=40, height=20, x=215, y=170)

	I_checkbutton = Radiobutton(fr1, text="I", bg="Yellow", font="Arial 12", value=53, justify=LEFT, command=I_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	I_checkbutton.place(width=40, height=20, x=255, y=170)

	Kr_checkbutton = Radiobutton(fr1, text="Kr", bg="DarkOrchid", font="Arial 12", value=54, justify=LEFT, command=Kr_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Kr_checkbutton.place(width=40, height=20, x=295, y=170)
	# 8 ряд
	Cs_checkbutton = Radiobutton(fr1, text="Cs", bg="LimeGreen", font="Arial 12", value=55, justify=LEFT, command=Cs_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Cs_checkbutton.place(width=40, height=20, x=15, y=190)

	Ba_checkbutton = Radiobutton(fr1, text="Ba", bg="LimeGreen", font="Arial 12", value=56, justify=LEFT, command=Ba_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Ba_checkbutton.place(width=40, height=20, x=55, y=190)
		# Лантан
	La_checkbutton = Radiobutton(fr1, text="La'", bg="LimeGreen", font="Arial 12", value=57, justify=LEFT, command=La_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	La_checkbutton.place(width=40, height=20, x=95, y=190)

	Hf_checkbutton = Radiobutton(fr1, text="Hf", bg="LimeGreen", font="Arial 12", value=72, justify=LEFT, command=Hf_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Hf_checkbutton.place(width=40, height=20, x=135, y=190)

	Ta_checkbutton = Radiobutton(fr1, text="Ta", bg="LimeGreen", font="Arial 12", value=73, justify=LEFT, command=Ta_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Ta_checkbutton.place(width=40, height=20, x=175, y=190)

	W_checkbutton = Radiobutton(fr1, text="W", bg="LimeGreen", font="Arial 12", value=74, justify=LEFT, command=W_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	W_checkbutton.place(width=40, height=20, x=215, y=190)

	Re_checkbutton = Radiobutton(fr1, text="Re", bg="LimeGreen", font="Arial 12", value=75, justify=LEFT, command=Re_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Re_checkbutton.place(width=40, height=20, x=255, y=190)

	Os_checkbutton = Radiobutton(fr1, text="Os", bg="LimeGreen", font="Arial 12", value=76, justify=LEFT, command=Os_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Os_checkbutton.place(width=40, height=20, x=295, y=190)

	Ir_checkbutton = Radiobutton(fr1, text="Ir", bg="LimeGreen", font="Arial 12", value=77, justify=LEFT, command=Ir_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Ir_checkbutton.place(width=40, height=20, x=335, y=190)

	Pt_checkbutton = Radiobutton(fr1, text="Pt", bg="LimeGreen", font="Arial 12", value=78, justify=LEFT, command=Pt_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Pt_checkbutton.place(width=40, height=20, x=375, y=190)
	# 9 ряд
	Au_checkbutton = Radiobutton(fr1, text="Au", bg="LimeGreen", font="Arial 12", value=79, justify=LEFT, command=Au_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Au_checkbutton.place(width=40, height=20, x=15, y=210)

	Hg_checkbutton = Radiobutton(fr1, text="Hg", bg="LimeGreen", font="Arial 12", value=80, justify=LEFT, command=Hg_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Hg_checkbutton.place(width=40, height=20, x=55, y=210)

	Ti_checkbutton = Radiobutton(fr1, text="Ti", bg="LimeGreen", font="Arial 12", value=81, justify=LEFT, command=Ti_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Ti_checkbutton.place(width=40, height=20, x=95, y=210)

	Pb_checkbutton = Radiobutton(fr1, text="Pb", bg="LimeGreen", font="Arial 12", value=82, justify=LEFT, command=Pb_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Pb_checkbutton.place(width=40, height=20, x=135, y=210)

	Bi_checkbutton = Radiobutton(fr1, text="Bi", bg="DeepPink", font="Arial 12", value=83, justify=LEFT, command=Bi_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Bi_checkbutton.place(width=40, height=20, x=175, y=210)

	Po_checkbutton = Radiobutton(fr1, text="Po", bg="DeepPink", font="Arial 12", value=84, justify=LEFT, command=Po_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Po_checkbutton.place(width=40, height=20, x=215, y=210)

	At_checkbutton = Radiobutton(fr1, text="At", bg="DeepPink", font="Arial 12", value=85, justify=LEFT, command=At_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	At_checkbutton.place(width=40, height=20, x=255, y=210)

	Rn_checkbutton = Radiobutton(fr1, text="Rn", bg="DarkOrchid", font="Arial 12", value=86, justify=LEFT, command=Rn_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Rn_checkbutton.place(width=40, height=20, x=295, y=210)

	Fr_checkbutton = Radiobutton(fr1, text="Fr", bg="LimeGreen", font="Arial 12", value=87, justify=LEFT, command=Fr_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Fr_checkbutton.place(width=40, height=20, x=15, y=230)

	Ra_checkbutton = Radiobutton(fr1, text="Ra", bg="LimeGreen", font="Arial 12", value=88, justify=LEFT, command=Ra_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Ra_checkbutton.place(width=40, height=20, x=55, y=230)
		# Актиний
	Ac_checkbutton = Radiobutton(fr1, text="Ac'", bg="LimeGreen", font="Arial 12", value=89, justify=LEFT, command=Ac_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Ac_checkbutton.place(width=40, height=20, x=95, y=230)

	Rf_checkbutton = Radiobutton(fr1, text="Rf", bg="LimeGreen", font="Arial 12", value=104, justify=LEFT, command=Rf_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Rf_checkbutton.place(width=40, height=20, x=135, y=230)

	Db_checkbutton = Radiobutton(fr1, text="Db", bg="LimeGreen", font="Arial 12", value=105, justify=LEFT, command=Db_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Db_checkbutton.place(width=40, height=20, x=175, y=230)

	Sg_checkbutton = Radiobutton(fr1, text="Sg", bg="LimeGreen", font="Arial 12", value=106, justify=LEFT, command=Sg_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Sg_checkbutton.place(width=40, height=20, x=215, y=230)

	Bh_checkbutton = Radiobutton(fr1, text="Bh", bg="LimeGreen", font="Arial 12", value=107, justify=LEFT, command=Bh_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Bh_checkbutton.place(width=40, height=20, x=255, y=230)

	Hs_checkbutton = Radiobutton(fr1, text="Hs", bg="LimeGreen", font="Arial 12", value=108, justify=LEFT, command=Hs_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Hs_checkbutton.place(width=40, height=20, x=295, y=230)

	Mt_checkbutton = Radiobutton(fr1, text="Mt", bg="LimeGreen", font="Arial 12", value=109, justify=LEFT, command=Mt_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Mt_checkbutton.place(width=40, height=20, x=335, y=230)

	Ds_checkbutton = Radiobutton(fr1, text="Ds", bg="LimeGreen", font="Arial 12", value=110, justify=LEFT, command=Ds_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Ds_checkbutton.place(width=40, height=20, x=375, y=230)

	#Лантаноиды
	lcd = Label(fr1, text="Лантаноиды:", bg="white", fg="black", font="Arial 14")
	lcd.place(width=150, height=20, x=632, y=30)

	Ce_checkbutton = Radiobutton(fr1, text="Ce", bg="DarkOrange", font="Arial 12", value=58, justify=CENTER, command=Ce_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Ce_checkbutton.place(width=40, height=20, x=560, y=50)

	Pr_checkbutton = Radiobutton(fr1, text="Pr", bg="DarkOrange", font="Arial 12", value=59, justify=CENTER, command=Pr_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Pr_checkbutton.place(width=40, height=20, x=600, y=50)

	Nd_checkbutton = Radiobutton(fr1, text="Nd", bg="DarkOrange", font="Arial 12", value=60, justify=CENTER, command=Nd_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Nd_checkbutton.place(width=40, height=20, x=640, y=50)

	Pm_checkbutton = Radiobutton(fr1, text="Pm", bg="DarkOrange", font="Arial 12", value=61, justify=CENTER, command=Pm_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Pm_checkbutton.place(width=40, height=20, x=680, y=50)

	Sm_checkbutton = Radiobutton(fr1, text="Sm", bg="DarkOrange", font="Arial 12", value=62, justify=CENTER, command=Sm_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Sm_checkbutton.place(width=40, height=20, x=720, y=50)

	Eu_checkbutton = Radiobutton(fr1, text="Eu", bg="DarkOrange", font="Arial 12", value=63, justify=CENTER, command=Eu_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Eu_checkbutton.place(width=40, height=20, x=760, y=50)

	Gd_checkbutton = Radiobutton(fr1, text="Gd", bg="DarkOrange", font="Arial 12", value=64, justify=CENTER, command=Gd_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Gd_checkbutton.place(width=40, height=20, x=800, y=50)

	Tb_checkbutton = Radiobutton(fr1, text="Tb", bg="DarkOrange", font="Arial 12", value=65, justify=CENTER, command=Tb_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Tb_checkbutton.place(width=40, height=20, x=560, y=70)

	Dy_checkbutton = Radiobutton(fr1, text="Dy", bg="DarkOrange", font="Arial 12", value=66, justify=CENTER, command=Dy_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Dy_checkbutton.place(width=40, height=20, x=600, y=70)

	Ho_checkbutton = Radiobutton(fr1, text="Ho", bg="DarkOrange", font="Arial 12", value=67, justify=CENTER, command=Ho_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Ho_checkbutton.place(width=40, height=20, x=640, y=70)

	Er_checkbutton = Radiobutton(fr1, text="Er", bg="DarkOrange", font="Arial 12", value=68, justify=CENTER, command=Er_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Er_checkbutton.place(width=40, height=20, x=680, y=70)

	Tm_checkbutton = Radiobutton(fr1, text="Tm", bg="DarkOrange", font="Arial 12", value=69, justify=CENTER, command=Tm_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Tm_checkbutton.place(width=40, height=20, x=720, y=70)

	Yb_checkbutton = Radiobutton(fr1, text="Yb", bg="DarkOrange", font="Arial 12", value=70, justify=CENTER, command=Yb_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Yb_checkbutton.place(width=40, height=20, x=760, y=70)

	Lu_checkbutton = Radiobutton(fr1, text="Lu", bg="DarkOrange", font="Arial 12", value=71, justify=CENTER, command=Lu_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Lu_checkbutton.place(width=40, height=20, x=800, y=70)

	#Актиноиды

	Icd = Label(fr1, text="Актиноиды:", bg="white", fg="black", font="Arial 14")
	Icd.place(width=150, height=20, x=632, y=90)

	Th_checkbutton = Radiobutton(fr1, text="Th", bg="DarkOrange", font="Arial 12", value=90, justify=CENTER, command=Th_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Th_checkbutton.place(width=40, height=20, x=560, y=110)

	Pa_checkbutton = Radiobutton(fr1, text="Pa", bg="DarkOrange", font="Arial 12", value=91, justify=CENTER, command=Pa_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Pa_checkbutton.place(width=40, height=20, x=600, y=110)

	U_checkbutton = Radiobutton(fr1, text="U", bg="DarkOrange", font="Arial 12", value=92, justify=CENTER, command=U_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	U_checkbutton.place(width=40, height=20, x=640, y=110)

	Np_checkbutton = Radiobutton(fr1, text="Np", bg="DarkOrange", font="Arial 12", value=93, justify=CENTER, command=Np_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Np_checkbutton.place(width=40, height=20, x=680, y=110)

	Pu_checkbutton = Radiobutton(fr1, text="Pu", bg="DarkOrange", font="Arial 12", value=94, justify=CENTER, command=Pu_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Pu_checkbutton.place(width=40, height=20, x=720, y=110)

	Am_checkbutton = Radiobutton(fr1, text="Am", bg="DarkOrange", font="Arial 12", value=95, justify=CENTER, command=Am_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Am_checkbutton.place(width=40, height=20, x=760, y=110)

	Cm_checkbutton = Radiobutton(fr1, text="Cm", bg="DarkOrange", font="Arial 12", value=96, justify=CENTER, command=Cm_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Cm_checkbutton.place(width=40, height=20, x=800, y=110)

	Bk_checkbutton = Radiobutton(fr1, text="Bk", bg="DarkOrange", font="Arial 12", value=97, justify=CENTER, command=Bk_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Bk_checkbutton.place(width=40, height=20, x=560, y=130)

	Cf_checkbutton = Radiobutton(fr1, text="Cf", bg="DarkOrange", font="Arial 12", value=98, justify=CENTER, command=Cf_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Cf_checkbutton.place(width=40, height=20, x=600, y=130)

	Es_checkbutton = Radiobutton(fr1, text="Es", bg="DarkOrange", font="Arial 12", value=99, justify=CENTER, command=Es_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Es_checkbutton.place(width=40, height=20, x=640, y=130)

	Fm_checkbutton = Radiobutton(fr1, text="Fm", bg="DarkOrange", font="Arial 12", value=100, justify=CENTER, command=Fm_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Fm_checkbutton.place(width=40, height=20, x=680, y=130)

	Md_checkbutton = Radiobutton(fr1, text="Md", bg="DarkOrange", font="Arial 12", value=101, justify=CENTER, command=Md_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Md_checkbutton.place(width=40, height=20, x=720, y=130)

	No_checkbutton = Radiobutton(fr1, text="No", bg="DarkOrange", font="Arial 12", value=102, justify=CENTER, command=No_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	No_checkbutton.place(width=40, height=20, x=760, y=130)

	Lr_checkbutton = Radiobutton(fr1, text="Lr", bg="DarkOrange", font="Arial 12", value=103, justify=CENTER, command=Lr_check,
		activebackground="MediumBluE", activeforeground="white", variable=lang)
	Lr_checkbutton.place(width=40, height=20, x=800, y=130)


def H_check():
	h_h = open("files\harakter\H.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Hh_check():
	h_h = open("files\harakter\H.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def He_check():
	h_h = open("files\harakter\He.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Li_check():
	h_h = open("files\harakter\Li.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Be_check():
	h_h = open("files\harakter\Be.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def B_check():
	h_h = open("files\harakter\B.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def C_check():
	h_h = open("files\harakter\C.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def N_check():
	h_h = open ("files\harakter/N.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def O_check():
	h_h = open("files\harakter\O.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def F_check():
	h_h = open("files\harakter\F.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Ne_check():
	h_h = open("files\harakter/Ne.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Na_check():
	h_h = open("files\harakter/Na.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Mg_check():
	h_h = open("files\harakter/Mg.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Al_check():
	h_h = open("files\harakter/Al.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Si_check():
	h_h = open("files\harakter/Si.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def P_check():
	h_h = open("files\harakter/P.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def S_check():
	h_h = open("files\harakter/S.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Cl_check():
	h_h = open("files\harakter/Cl.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Ar_check():
	h_h = open("files\harakter/Ar.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def K_check():
	h_h = open("files\harakter/K.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Ca_check():
	h_h = open("files\harakter/Ca.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Sc_check():
	h_h = open("files\harakter/Sc.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Ti_check():
	h_h = open("files\harakter/Ti.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def V_check():
	h_h = open("files\harakter/V.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Cr_check():
	h_h = open("files\harakter/Cr.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Mn_check():
	h_h = open("files\harakter/Mn.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Fe_check():
	h_h = open("files\harakter/Fe.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Co_check():
	h_h = open("files\harakter/Co.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Ni_check():
	h_h = open("files\harakter/Ni.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Cu_check():
	h_h = open("files\harakter/Cu.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Zn_check():
	h_h = open("files\harakter/Zn.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Ga_check():
	h_h = open("files\harakter/Ga.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Ge_check():
	h_h = open("files\harakter/Ge.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def As_check():
	h_h = open("files\harakter/As.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Se_check():
	h_h = open("files\harakter/Se.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Br_check():
	h_h = open("files\harakter/Br.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Kr_check():
	h_h = open("files\harakter/Kr.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Rb_check():
	h_h = open("files\harakter/Rb.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Sr_check():
	h_h = open("files\harakter/Sr.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Y_check():
	h_h = open("files\harakter/Y.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Zr_check():
	h_h = open("files\harakter/Zr.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Nb_check():
	h_h = open("files\harakter/Nb.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Mo_check():
	h_h = open("files\harakter/Mo.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Tc_check():
	h_h = open("files\harakter/Tc.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Ru_check():
	h_h = open("files\harakter/Ru.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Rh_check():
	h_h = open("files\harakter/Rh.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Pd_check():
	h_h = open("files\harakter/Pd.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Ag_check():
	h_h = open("files\harakter/Ag.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Cd_check():
	h_h = open("files\harakter/Cd.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def In_check():
	h_h = open("files\harakter/In.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Sn_check():
	h_h = open("files\harakter/Sn.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Sb_check():
	h_h = open("files\harakter/Sb.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Te_check():
	h_h = open("files\harakter/Te.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def I_check():
	h_h = open("files\harakter/I.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Xe_check():
	h_h = open("files\harakter/Xe.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Cs_check():
	h_h = open("files\harakter/Cs.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Ba_check():
	h_h = open("files\harakter/Ba.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def La_check():
	h_h = open("files\harakter/La.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Hf_check():
	h_h = open("files\harakter/Hf.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Ta_check():
	h_h = open("files\harakter/Ta.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def W_check():
	h_h = open("files\harakter/W.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Re_check():
	h_h = open("files\harakter/Re.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Os_check():
	h_h = open("files\harakter/Os.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Ir_check():
	h_h = open("files\harakter/Ir.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Pt_check():
	h_h = open("files\harakter/Pt.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Au_check():
	h_h = open("files\harakter/Au.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Hg_check():
	h_h = open("files\harakter/Hg.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Tl_check():
	h_h = open("files\harakter/Tl.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Pb_check():
	h_h = open("files\harakter/Pb.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Bi_check():
	h_h = open("files\harakter/Bi.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Po_check():
	h_h = open("files\harakter/Po.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def At_check():
	h_h = open("files\harakter/At.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Fr_check():
	h_h = open("files\harakter/Fr.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Ra_check():
	h_h = open("files\harakter/Ra.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Ac_check():
	h_h = open("files\harakter/Ac.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Rf_check():
	h_h = open("files\harakter/Rf.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Db_check():
	h_h = open("files\harakter/Db.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Sg_check():
	h_h = open("files\harakter/Sg.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Bh_check():
	h_h = open("files\harakter/Bh.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Hs_check():
	h_h = open("files\harakter/Hs.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Mt_check():
	h_h = open("files\harakter/Mt.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Ds_check():
	h_h = open("files\harakter/Ds.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Rn_check():
	h_h = open("files\harakter/Rn.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Ce_check():
	h_h = open("files\harakter/Ce.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Pr_check():
	h_h = open("files\harakter/Pr.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Nd_check():
	h_h = open("files\harakter/Nd.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Pm_check():
	h_h = open("files\harakter/Pm.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Sm_check():
	h_h = open("files\harakter/Sm.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Eu_check():
	h_h = open("files\harakter/Eu.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Gd_check():
	h_h = open("files\harakter/Gd.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Tb_check():
	h_h = open("files\harakter/Tb.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Dy_check():
	h_h = open("files\harakter/Dy.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Ho_check():
	h_h = open("files\harakter/Ho.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Er_check():
	h_h = open("files\harakter/Er.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Tm_check():
	h_h = open("files\harakter/Tm.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Yb_check():
	h_h = open("files\harakter/Yb.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Lu_check():
	h_h = open("files\harakter/Lu.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Th_check():
	h_h = open("files\harakter/Th.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Pa_check():
	h_h = open("files\harakter/Pa.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def U_check():
	h_h = open("files\harakter/U.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Np_check():
	h_h = open("files\harakter/Np.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Pu_check():
	h_h = open("files\harakter/Pu.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Am_check():
	h_h = open("files\harakter/Am.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Cm_check():
	h_h = open("files\harakter/Cm.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Bk_check():
	h_h = open("files\harakter/Bk.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Cf_check():
	h_h = open("files\harakter/Cf.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Es_check():
	h_h = open("files\harakter/Es.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Fm_check():
	h_h = open("files\harakter/Fm.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Md_check():
	h_h = open("files\harakter/Md.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def No_check():
	h_h = open("files\harakter/No.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)
def Lr_check():
	h_h = open("files\harakter/Lr.txt", "r").read()
	Lh = Label(fr2, text=h_h, bg="white", font="Arial 16")
	Lh.place(width=850, height=510, x=0, y=0)

# Ф О Р М У Л Ы
# Ф О Р М У Л Ы
# Ф О Р М У Л Ы
# Ф О Р М У Л Ы
# Ф О Р М У Л Ы

def ff_him():
	clean_fr1 = Label(fr1, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr1.place(width=850, height=250, x=0, y=0)
	clean_fr2 = Label(fr2, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr2.place(width=850, height=510, x=0, y=0)

	global choice
	choice = 0
	nac= Label(fr1, text="Выберите тему:", bg="white", fg="MediumBluE", font="Arial 24")
	nac.place(width=850, height=40, x=0, y=0)
	him = IntVar()
	ch1 = Radiobutton(fr1, text="Моль", bg="white", font="Arial 12", value=1, justify=LEFT, command=him1,
		activebackground="MediumBluE", activeforeground="white", variable=him)
	ch1.place(width=60, height=20, x=0, y=70)

	ch2 = Radiobutton(fr1, text="Молярная масса вещества", bg="white", font="Arial 12", value=2, justify=LEFT, command=him2,
		activebackground="MediumBluE", activeforeground="white", variable=him)
	ch2.place(width=225, height=20, x=0, y=90)

	ch3 = Radiobutton(fr1, text="Объём вещества", bg="white", font="Arial 12", value=3, justify=LEFT, command=him3,
		activebackground="MediumBluE", activeforeground="white", variable=him)
	ch3.place(width=150, height=20, x=0, y=110)

	ch4 = Radiobutton(fr1, text="Число Авогадро", bg="white", font="Arial 12", value=4, justify=LEFT, command=him4,
		activebackground="MediumBluE", activeforeground="white", variable=him)
	ch4.place(width=150, height=20, x=0, y=130)

def him1():
	f1 = Label(fr2, text="n=m\Mr", bg="white", font="Arial 14")
	f1.place(width=850, height=100, x=0, y=50)
def him2():
	f2 = Label(fr2, text="m=n•Mr", bg="white", font="Arial 14")
	f2.place(width=850, height=100, x=0, y=50)
def him3():
	f3 = Label(fr2, text="V=n•22.4 (л\моль)", bg="white", font="Arial 14")
	f3.place(width=850, height=100, x=0, y=50)
def him4():
	f4 = Label(fr2, text="6,02 · 1023 частиц", bg="white", font="Arial 14")
	f4.place(width=850, height=100, x=0, y=50)

def ff_geo():
	clean_fr1 = Label(fr1, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr1.place(width=850, height=250, x=0, y=0)
	clean_fr2 = Label(fr2, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr2.place(width=850, height=510, x=0, y=0)

	global choice
	choice = 0
	nac= Label(fr1, text="Выберите тему:", bg="white", fg="MediumBluE", font="Arial 24")
	nac.place(width=850, height=40, x=0, y=0)
	geo = IntVar()
	ch1 = Radiobutton(fr1, text="Площадь треугольника через две стороны и угол между ними", bg="white", font="Arial 12", value=1, justify=LEFT, command=geo1,
		activebackground="MediumBluE", activeforeground="white", variable=geo)
	ch1.place(width=470, height=20, x=0, y=70)

	ch2 = Radiobutton(fr1, text="Площадь треугольника через основание и высоту", bg="white", font="Arial 12", value=2, justify=LEFT, command=geo2,
		activebackground="MediumBluE", activeforeground="white", variable=geo)
	ch2.place(width=380, height=20, x=0, y=90)

	ch3 = Radiobutton(fr1, text="Теорема Пифагора", bg="white", font="Arial 12", value=3, justify=LEFT, command=geo3,
		activebackground="MediumBluE", activeforeground="white", variable=geo)
	ch3.place(width=170, height=20, x=0, y=110)

	ch4 = Radiobutton(fr1, text="Теорема косинусов", bg="white", font="Arial 12", value=4, justify=LEFT, command=geo4,
		activebackground="MediumBluE", activeforeground="white", variable=geo)
	ch4.place(width=170, height=20, x=0, y=130)

def geo1():
	f1 = Label(fr2, text="S = 0,5ab∙sin γ", bg="white", font="Arial 14")
	f1.place(width=850, height=100, x=0, y=50)
def geo2():
	f2 = Label(fr2, text="S = 0,5bh", bg="white", font="Arial 14")
	f2.place(width=850, height=100, x=0, y=50)
def geo3():
	f3 = Label(fr2, text="a² = b² +c²", bg="white", font="Arial 14")
	f3.place(width=850, height=100, x=0, y=50)
def geo4():
	f4 = Label(fr2, text="a² = b² + c² – 2bc∙cos α", bg="white", font="Arial 14")
	f4.place(width=850, height=100, x=0, y=50)

def ff_fiz():
	clean_fr1 = Label(fr1, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr1.place(width=850, height=250, x=0, y=0)
	clean_fr2 = Label(fr2, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr2.place(width=850, height=510, x=0, y=0)

	global choice
	choice = 0
	nac= Label(fr1, text="Выберите тему:", bg="white", fg="MediumBluE", font="Arial 24")
	nac.place(width=850, height=40, x=0, y=0)
	fiz = IntVar()
	ch1 = Radiobutton(fr1, text="Давление", bg="white", font="Arial 12", value=1, justify=LEFT, command=fiz1,
		activebackground="MediumBluE", activeforeground="white", variable=fiz)
	ch1.place(width=90, height=20, x=0, y=70)

	ch2 = Radiobutton(fr1, text="Плотность", bg="white", font="Arial 12", value=2, justify=LEFT, command=fiz2,
		activebackground="MediumBluE", activeforeground="white", variable=fiz)
	ch2.place(width=97, height=20, x=0, y=90)

	ch3 = Radiobutton(fr1, text="Сила тяжести", bg="white", font="Arial 12", value=3, justify=LEFT, command=fiz3,
		activebackground="MediumBluE", activeforeground="white", variable=fiz)
	ch3.place(width=120, height=20, x=0, y=110)
	
	ch4 = Radiobutton(fr1, text="Сила Архимеда", bg="white", font="Arial 12", value=4, justify=LEFT, command=fiz4,
		activebackground="MediumBluE", activeforeground="white", variable=fiz)
	ch4.place(width=135, height=20, x=0, y=130)

	ch5 = Radiobutton(fr1, text="Ускорение", bg="white", font="Arial 12", value=5, justify=LEFT, command=fiz5,
		activebackground="MediumBluE", activeforeground="white", variable=fiz)
	ch5.place(width=100, height=20, x=0, y=150)

	ch6 = Radiobutton(fr1, text="II закон Ньютона", bg="white", font="Arial 12", value=6, justify=LEFT, command=fiz6,
		activebackground="MediumBluE", activeforeground="white", variable=fiz)
	ch6.place(width=145, height=20, x=0, y=170)

	ch7 = Radiobutton(fr1, text="Закон Гука", bg="white", font="Arial 12", value=7, justify=LEFT, command=fiz7,
		activebackground="MediumBluE", activeforeground="white", variable=fiz)
	ch7.place(width=100, height=20, x=0, y=190)

	ch8 = Radiobutton(fr1, text="Закон Всемирного тяготения", bg="white", font="Arial 12", value=8, justify=LEFT, command=fiz8,
		activebackground="MediumBluE", activeforeground="white", variable=fiz)
	ch8.place(width=230, height=20, x=0, y=210)

	ch9 = Radiobutton(fr1, text="Сила трения", bg="white", font="Arial 12", value=9, justify=LEFT, command=fiz9,
		activebackground="MediumBluE", activeforeground="white", variable=fiz)
	ch9.place(width=110, height=20, x=0, y=230)

	ch10 = Radiobutton(fr1, text="Импульс тела ", bg="white", font="Arial 12", value=10, justify=LEFT, command=fiz10,
		activebackground="MediumBluE", activeforeground="white", variable=fiz)
	ch10.place(width=122, height=20, x=728, y=70)

	ch11 = Radiobutton(fr1, text="Импульс силы", bg="white", font="Arial 12", value=11, justify=LEFT, command=fiz11,
		activebackground="MediumBluE", activeforeground="white", variable=fiz)
	ch11.place(width=122, height=20, x=728, y=90)

	ch12 = Radiobutton(fr1, text="Момент силы", bg="white", font="Arial 12", value=12, justify=LEFT, command=fiz12,
		activebackground="MediumBluE", activeforeground="white", variable=fiz)
	ch12.place(width=118, height=20, x=732, y=110)

	ch13 = Radiobutton(fr1, text="Работа", bg="white", font="Arial 12", value=13, justify=LEFT, command=fiz13,
		activebackground="MediumBluE", activeforeground="white", variable=fiz)
	ch13.place(width=80, height=20, x=770, y=130)

	ch14 = Radiobutton(fr1, text="Мощность", bg="white", font="Arial 12", value=14, justify=LEFT, command=fiz14,
		activebackground="MediumBluE", activeforeground="white", variable=fiz)
	ch14.place(width=95, height=20, x=755, y=150)

	ch15 = Radiobutton(fr1, text="Закон преломления света", bg="white", font="Arial 12", value=15, justify=LEFT, command=fiz15,
		activebackground="MediumBluE", activeforeground="white", variable=fiz)
	ch15.place(width=215, height=20, x=635, y=170)

	ch16 = Radiobutton(fr1, text="Напряжение", bg="white", font="Arial 12", value=16, justify=LEFT, command=fiz16,
		activebackground="MediumBluE", activeforeground="white", variable=fiz)
	ch16.place(width=110, height=20, x=740, y=190)

	ch17 = Radiobutton(fr1, text="Сила тока", bg="white", font="Arial 12", value=17, justify=LEFT, command=fiz17,
		activebackground="MediumBluE", activeforeground="white", variable=fiz)
	ch17.place(width=95, height=20, x=755, y=210)

	ch18 = Radiobutton(fr1, text="Закон радиоактивного распада", bg="white", font="Arial 12", value=18, justify=LEFT, command=fiz18,
		activebackground="MediumBluE", activeforeground="white", variable=fiz)
	ch18.place(width=250, height=20, x=600, y=230)

def fiz1():
	f1 = Label(fr2, text="Р=F:S", bg="white", font="Arial 14")
	f1.place(width=850, height=100, x=0, y=50)
def fiz2():
	f2 = Label(fr2, text="ρ=m:V", bg="white", font="Arial 14")
	f2.place(width=850, height=100, x=0, y=50)
def fiz3():
	f3 = Label(fr2, text="Fт=m•g", bg="white", font="Arial 14")
	f3.place(width=850, height=100, x=0, y=50)
def fiz4():
	f4 = Label(fr2, text="Fa=ρж•g•Vт", bg="white", font="Arial 14")
	f4.place(width=850, height=100, x=0, y=50)
def fiz5():
	f5 = Label(fr2, text="a=(υ-υ 0):t", bg="white", font="Arial 14")
	f5.place(width=850, height=100, x=0, y=50)
def fiz6():
	f5 = Label(fr2, text="F=ma", bg="white", font="Arial 14")
	f5.place(width=850, height=100, x=0, y=50)
def fiz7():
	f5 = Label(fr2, text="Fy=-kx", bg="white", font="Arial 14")
	f5.place(width=850, height=100, x=0, y=50)
def fiz8():
	f5 = Label(fr2, text="F=G∙M∙m/R^2", bg="white", font="Arial 14")
	f5.place(width=850, height=100, x=0, y=50)
def fiz9():
	f5 = Label(fr2, text="Fтр=µN", bg="white", font="Arial 14")
	f5.place(width=850, height=100, x=0, y=50)
def fiz10():
	f5 = Label(fr2, text="p=mυ", bg="white", font="Arial 14")
	f5.place(width=850, height=100, x=0, y=50)
def fiz11():
	f5 = Label(fr2, text="Ft=∆p", bg="white", font="Arial 14")
	f5.place(width=850, height=100, x=0, y=50)
def fiz12():
	f5 = Label(fr2, text="M=F∙ℓ", bg="white", font="Arial 14")
	f5.place(width=850, height=100, x=0, y=50)
def fiz13():
	f5 = Label(fr2, text="A=F∙S∙cosα", bg="white", font="Arial 14")
	f5.place(width=850, height=100, x=0, y=50)
def fiz14():
	f5 = Label(fr2, text="N=A/t=F∙υ", bg="white", font="Arial 14")
	f5.place(width=850, height=100, x=0, y=50)
def fiz15():
	f5 = Label(fr2, text="n21=n2/n1= υ 1/ υ 2", bg="white", font="Arial 14")
	f5.place(width=850, height=100, x=0, y=50)
def fiz16():
	f5 = Label(fr2, text="U=A/q", bg="white", font="Arial 14")
	f5.place(width=850, height=100, x=0, y=50)
def fiz17():
	f5 = Label(fr2, text="I=q/t", bg="white", font="Arial 14")
	f5.place(width=850, height=100, x=0, y=50)
def fiz18():
	f5 = Label(fr2, text="N=N0∙2-t/T", bg="white", font="Arial 14")
	f5.place(width=850, height=100, x=0, y=50)

def ff_mat():
	clean_fr1 = Label(fr1, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr1.place(width=850, height=250, x=0, y=0)
	clean_fr2 = Label(fr2, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr2.place(width=850, height=510, x=0, y=0)

	global choice
	choice = 0
	nac= Label(fr1, text="Выберите тему:", bg="white", fg="MediumBluE", font="Arial 24")
	nac.place(width=850, height=40, x=0, y=0)
	mat = IntVar()
	ch1 = Radiobutton(fr1, text="Нахождение площади прямоугольника", bg="white", font="Arial 12", value=1, justify=LEFT, command=mat1,
		activebackground="MediumBluE", activeforeground="white", variable=mat)
	ch1.place(width=300, height=20, x=0, y=40)

	ch2 = Radiobutton(fr1, text="Нахождение периметра прямоугольника", bg="white", font="Arial 12", value=2, justify=LEFT, command=mat2,
		activebackground="MediumBluE", activeforeground="white", variable=mat)
	ch2.place(width=317, height=20, x=0, y=60)

	ch3 = Radiobutton(fr1, text="Нахождение периметра квадрата", bg="white", font="Arial 12", value=3, justify=LEFT, command=mat3,
		activebackground="MediumBluE", activeforeground="white", variable=mat)
	ch3.place(width=268, height=20, x=0, y=80)
	ch4 = Radiobutton(fr1, text="Деление с остатком", bg="white", font="Arial 12", value=4, justify=LEFT, command=mat4,
		activebackground="MediumBluE", activeforeground="white", variable=mat)
	ch4.place(width=167, height=20, x=0, y=100)

	ch5 = Radiobutton(fr1, text="Формула пути", bg="white", font="Arial 12", value=5, justify=LEFT, command=mat5,
		activebackground="MediumBluE", activeforeground="white", variable=mat)
	ch5.place(width=120, height=20, x=0, y=120)

	ch6 = Radiobutton(fr1, text="Формула стоимости", bg="white", font="Arial 12", value=6, justify=LEFT, command=mat6,
		activebackground="MediumBluE", activeforeground="white", variable=mat)
	ch6.place(width=165, height=20, x=0, y=140)

	ch7 = Radiobutton(fr1, text="Движение", bg="white", font="Arial 12", value=7, justify=LEFT, command=mat7,
		activebackground="MediumBluE", activeforeground="white", variable=mat)
	ch7.place(width=93, height=20, x=0, y=160)
	ch8 = Radiobutton(fr1, text="Переместительное свойство", bg="white", font="Arial 12", value=8, justify=LEFT, command=mat8,
		activebackground="MediumBluE", activeforeground="white", variable=mat)
	ch8.place(width=233, height=20, x=0, y=180)

	ch9 = Radiobutton(fr1, text="Сочетательное свойство", bg="white", font="Arial 12", value=9, justify=LEFT, command=mat9,
		activebackground="MediumBluE", activeforeground="white", variable=mat)
	ch9.place(width=205, height=20, x=0, y=200)

	ch10 = Radiobutton(fr1, text="Формула работы", bg="white", font="Arial 12", value=10, justify=LEFT, command=mat10,
		activebackground="MediumBluE", activeforeground="white", variable=mat)
	ch10.place(width=145, height=20, x=0, y=220)

def mat1():
	m = open("files\ormuls\matem\Find_area_of_rectangle.txt", "r").read()
	mr1 = Label(fr2, text=m, bg="white", font="Arial 14")
	mr1.place(width=850, height=100, x=0, y=50)
def mat2():
	m = open("files\ormuls\matem\Finding_the_perimeter_of_a_rectangle.txt", "r").read()
	mr2 = Label(fr2, text=m, bg="white", font="Arial 14")
	mr2.place(width=850, height=100, x=0, y=50)
def mat3():
	m = open("files\ormuls\matem\Finding_the_perimeter_of_a_square.txt", "r").read()
	mr3 = Label(fr2, text=m, bg="white", font="Arial 14")
	mr3.place(width=850, height=100, x=0, y=50)
def mat4():
	m = open("files\ormuls\matem\Find_area_of_rectangle.txt", "r").read()
	mr4 = Label(fr2, text=m, bg="white", font="Arial 14")
	mr4.place(width=850, height=100, x=0, y=50)
def mat5():
	m = open("files\ormuls\matem\Formula_is_the_way.txt", "r").read()
	mr5 = Label(fr2, text=m, bg="white", font="Arial 14")
	mr5.place(width=850, height=100, x=0, y=50)
def mat6():
	m = open("files\ormuls\matem\Formula_cost.txt", "r").read()
	mr6 = Label(fr2, text=m, bg="white", font="Arial 14")
	mr6.place(width=850, height=100, x=0, y=50)
def mat7():
	m = open("files\ormuls\matem\Movement.txt", "r").read()
	mr7 = Label(fr2, text=m, bg="white", font="Arial 14")
	mr7.place(width=850, height=100, x=0, y=50)
def mat8():
	m = open("files\ormuls\matem\Commutative_property.txt", "r").read()
	mr8 = Label(fr2, text=m, bg="white", font="Arial 14")
	mr8.place(width=850, height=100, x=0, y=50)
def mat9():
	m = open("files\ormuls\matem\Associative_property.txt", "r").read()
	mr9 = Label(fr2, text=m, bg="white", font="Arial 14")
	mr9.place(width=850, height=100, x=0, y=50)
def mat10():
	m = open("files\ormuls\matem\The_formula_works.txt", "r").read()
	mr10 = Label(fr2, text=m, bg="white", font="Arial 14")
	mr10.place(width=850, height=100, x=0, y=50)

def ff_alg():
	clean_fr1 = Label(fr1, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr1.place(width=850, height=250, x=0, y=0)
	clean_fr2 = Label(fr2, text="пасхалка", bg="white", fg="white", font="Arial 25")
	clean_fr2.place(width=850, height=510, x=0, y=0)

	global choice
	choice = 1
	nac= Label(fr1, text="Выберите тему:", bg="white", fg="MediumBluE", font="Arial 24")
	nac.place(width=850, height=40, x=0, y=0)
	alg = IntVar()

	ch1 = Radiobutton(fr1, text="Формулы сокращенного умножения", bg="white", font="Arial 12", value=1, justify=LEFT, command=alg1,
		activebackground="MediumBluE", activeforeground="white", variable=alg)
	ch1.place(width=280, height=20, x=0, y=70)

	ch2 = Radiobutton(fr1, text="Квадратное уравнение ax^2+bx+c=0", bg="white", font="Arial 12", value=2, justify=LEFT, command=alg2,
		activebackground="MediumBluE", activeforeground="white", variable=alg)
	ch2.place(width=290, height=20, x=0, y=90)

	ch3 = Radiobutton(fr1, text="Арифметическая прогрессия", bg="white", font="Arial 12", value=3, justify=LEFT, command=alg3,
		activebackground="MediumBluE", activeforeground="white", variable=alg)
	ch3.place(width=235, height=20, x=0, y=110)
	
	ch4 = Radiobutton(fr1, text="Геометрическая прогрессия", bg="white", font="Arial 12", value=4, justify=LEFT, command=alg4,
		activebackground="MediumBluE", activeforeground="white", variable=alg)
	ch4.place(width=230, height=20, x=0, y=130)

	ch5 = Radiobutton(fr1, text="Определение модуля", bg="white", font="Arial 12", value=5, justify=LEFT, command=alg5,
		activebackground="MediumBluE", activeforeground="white", variable=alg)
	ch5.place(width=180, height=20, x=0, y=150)

	ch6 = Radiobutton(fr1, text="Простейшие суммы", bg="white", font="Arial 12", value=6, justify=LEFT, command=alg6,
		activebackground="MediumBluE", activeforeground="white", variable=alg)
	ch6.place(width=170, height=20, x=0, y=170)

def alg1():
	a1 = Label(fr2, text="""
(a+b)2=a2+2ab+b2
a2-b2=(a-b)(a+b)
(a+b)3=a3+3a2b+3ab2+b3
a3+b3=(a+b)(a2-ab+b2)
a3-b3=(a-b)(a2+ab+b2)
(a+b+c)2=a2+b2+c2+2ab+2ac+2bc
(a+b)2=(b+a)2
		""", bg="white", font="Arial 14")
	a1.place(width=850, height=460, x=0, y=50)
def alg2():
	a1 = Label(fr2, text="""
Квадратное уравнение ax2+bx+c=0
D=b2-4ac  
-Если D>0, два различных корня x=(-b+√D)/(2a)
-Если D=0, два одинаковых корня x1=x2=-b/2a
-Если D<0, действительных корней нет
 
Квадратное уравнение ax2+bx+c=0, если b-четное число
D=b/2-ac
 x=(-b/2+√D)/a
 
Теорема Виета
х1+х2=-b
x1·x2=c
 
Метод коэффициентов
Если a+b+c=0, то х1=1, х2=с/а
Если а-b+c=0 или a+c=b, то х1=-1, х2=-с/а

Разложение квадратного трехчлена на множители
ax2+bx+c=а(х-х1)(х-х2)
		""", bg="white", font="Arial 14")
	a1.place(width=850, height=460, x=0, y=50)
def alg3():
	a1 = Label(fr2, text="""
аn=a1+d(n-1)
d=an+1-an
(an+1+an-1))/2=an
Sn=((a1+an)/2)·n
Sn=(((2a1+d(n-1))/2)·n
		""", bg="white", font="Arial 14")
	a1.place(width=850, height=460, x=0, y=50)
def alg4():
	a1 = Label(fr2, text="""
bn=b1·qn-1
bn+1=bn·q
 bn+1·bn-1=bn2,b‡0 
Sn=(b1(qn-1))/(q-1), q‡1
Sn=b1/(1-q), q‡1
		""", bg="white", font="Arial 14")
	a1.place(width=850, height=460, x=0, y=50)
def alg5():
	a1 = Label(fr2, text="""
       [f(x),    f(x)>0
|f(x)|= [0,       f(x)=0
         [-f(x),   f(x)<0
        
|a-b|=|b-a|
√a2=|a|
|a·b|=|a|·|b|
|a|2=a2
		""", bg="white", font="Arial 14")
	a1.place(width=850, height=460, x=0, y=50)
def alg6():
	a1 = Label(fr2, text="""
1+2+3+....+n=(n(n+1))/2
1+3+5+....+(2n-1)=n2
2+4+6+....+2n=n(n+1)
		""", bg="white", font="Arial 14")
	a1.place(width=850, height=460, x=0, y=50)

# Г Р А Ф И Ч Е С К А Я   Ч А С Т Ь
# Г Р А Ф И Ч Е С К А Я   Ч А С Т Ь
# Г Р А Ф И Ч Е С К А Я   Ч А С Т Ь
# Г Р А Ф И Ч Е С К А Я   Ч А С Т Ь
# Г Р А Ф И Ч Е С К А Я   Ч А С Т Ь
# Г Р А Ф И Ч Е С К А Я   Ч А С Т Ь
# Г Р А Ф И Ч Е С К А Я   Ч А С Т Ь
# Г Р А Ф И Ч Е С К А Я   Ч А С Т Ь
# Г Р А Ф И Ч Е С К А Я   Ч А С Т Ь
# Г Р А Ф И Ч Е С К А Я   Ч А С Т Ь
# Г Р А Ф И Ч Е С К А Я   Ч А С Т Ь
# Г Р А Ф И Ч Е С К А Я   Ч А С Т Ь
# Г Р А Ф И Ч Е С К А Я   Ч А С Т Ь


#    menu.add_separator()  -  добавление черты в меню

main_menu = Menu()

#АЛГЕБРА

menu = Menu(font=("Arial", 8, "bold"), tearoff=0, bg="white", fg=("MediumBlue"), activebackground=("MediumBlue"), activeforeground=("Snow"))

menu.add_command(label="Задачи на сравнение чисел", command=sravnenie)
menu.add_command(label="Задачи на решение квадратных уравнений", command=vvod_kvad_yrav)


#ГЕОМЕТРИЯ
menumenu = Menu()

menumenu = Menu(font=("Arial", 8, "bold"), tearoff=0, bg="white", fg=("MediumBlue"), activebackground=("MediumBlue"), activeforeground=("Snow"))
menumenu.add_command(label="Задачи на поиск периметра квадрата", command=per_kvad)
menumenu.add_command(label="Задачи на поиск площади квадрата", command=pl_kvad)
menumenu.add_command(label="Задачи на поиск периметра прямоугольника", command=per_pram)
menumenu.add_command(label="Задачи на поиск площади прямоугольника", command=pl_pram)
menumenu.add_command(label="Задачи на поиск объёма параллелепипеда", command=ob_p)

#ХИМИЯ
numenu = Menu()

numenu = Menu(font=("Arial", 8, "bold"), tearoff=0, bg="white", fg=("MediumBlue"), activebackground=("MediumBlue"), activeforeground=("Snow"))

numenu.add_command(label="Характеристика химических элементов", command=harakter)

#ИНФОРМАТИКА
umenu = Menu()
umenu = Menu(font=("Arial", 8, "bold"), tearoff=0, bg="Snow", fg=("DarkBlue"), activebackground=("Snow"), activeforeground=("Maroon"))

umenu.add_command(label="Переведение чисел в двуичную систему счисления", command=dvy_vv)
umenu.add_command(label="Переведение чисел в восьмеричную систему счисления", command=vos_vv)
umenu.add_command(label="Переведение чисел в шестнадцатеричную систему счисления", command=shest_vv)

#ПРОСТЫЕ ВЫЧИСЛЕНИЯ
menumenumenu = Menu()

menumenumenu = Menu(font=("Arial", 8, "bold"), tearoff=0, bg="white", fg=("MediumBlue"), activebackground=("MediumBlue"), activeforeground=("Snow"))

menumenumenu.add_command(label="Сложение", command=prost_slog)
menumenumenu.add_command(label="Вычитание", command=prost_vichit)
menumenumenu.add_command(label="Умножение", command=prost_ymnog)
menumenumenu.add_command(label="Деление", command=prost_del)
menumenumenu.add_command(label="Возведение в степень", command=prost_stepen)
menumenumenu.add_command(label="Извлечение корня", command=prost_koren)

#ФОРМУЛЫ

enu = Menu()

enu = Menu(font=("Arial", 8, "bold"), tearoff=0, bg="white", fg=("MediumBlue"), activebackground=("MediumBlue"), activeforeground=("Snow"))

enu.add_command(label="Математика", command=ff_mat)
enu.add_separator()
enu.add_command(label="Алгебра", command=ff_alg)
enu.add_command(label="Геометрия", command=ff_geo)
enu.add_command(label="Физика", command=ff_fiz)
enu.add_separator()
enu.add_command(label="Химия", command=ff_him)

#пункты меню:
main_menu.add_cascade(label="|")
main_menu.add_cascade(label="Алгебра", menu=menu)
main_menu.add_cascade(label="Геометрия", menu=menumenu)
main_menu.add_cascade(label="Химия", menu=numenu)
main_menu.add_cascade(label="Информатика", menu=umenu)
main_menu.add_cascade(label="|")
main_menu.add_cascade(label="Простые вычисления", menu=menumenumenu)
main_menu.add_cascade(label="|")
main_menu.add_cascade(label="Формулы", menu=enu)
main_menu.add_cascade(label="|")

root.config(menu=main_menu)


root.mainloop()
