from tkinter import *
import math

hesap=0
sonuc=0
s1=0

def yaz(x):
    s=len(giris.get())
    giris.insert(s,str(x))
    # print(x)

def islemler(x):
    global hesap
    hesap=x
    global s1
    s1=float(giris.get())
    print(hesap)
    print(s1)
    giris.delete(0,'end')

    if (hesap == 5 or hesap == 7):
        hesapla()

s2=0

def hesapla():
    global s2
    global hesap
    global sonuc
                                                                                                                   
    if giris.get() != '':                                                     
        s2=float(giris.get())
        print(s2)
        
                                                                                                                                                   
    if(hesap==0):sonuc=s1+s2
    elif(hesap==1):sonuc=s1-s2
    elif(hesap==2):sonuc=s1*s2
    elif(hesap==3):sonuc=s1/s2
    elif(hesap==4):sonuc=int(s1)**int(s2)
    elif(hesap==5):sonuc=math.sqrt(s1)
    elif(hesap==6):sonuc=s1**2
    elif(hesap==7):sonuc=math.factorial(int(s1))
    elif(hesap==8):sonuc=math.log10(s1)
    elif(hesap==9):sonuc=10**s1

    giris.delete(0,'end')
    giris.insert(0,str(sonuc))


def sıfırla():
    global sonuc
    global s1
    global hesap

    sonuc = 0
    s1 = 0
    hesap = 0

    giris.delete(0,'end')

pencere=Tk()
pencere.title('HESAP MAKİNESİ')
pencere.geometry("260x350")
giris=Entry(font="Verdana 14 bold",width=14,justify=RIGHT)
giris.place(x=20,y=20)
b=[]

for i in range(1,10):
    b.append(Button(text=str(i),font="Verdana 14 bold",command=lambda x=i:yaz(x)))

sayac=0

for i in range(0,3):
    for j in range(0,3):
        b[sayac].place(x=20+j*50,y=50+i*50)
        sayac+=1

islem=[]

for i in range(0,10):
    islem.append(Button(font="Verdan 14 bold",width=3 ,command=lambda x=i:islemler(x)))

islem[0]['text']="+"
islem[1]['text']="-"
islem[2]['text']="*"
islem[3]['text']="/"
islem[4]['text']="**"
islem[5]['text']="√"
islem[6]['text']="n**2"
islem[7]['text']="n!"
islem[8]['text']="log"
islem[9]['text']="10**"

islem[0].place(x=170,y=50)
islem[1].place(x=170,y=100)
islem[2].place(x=170,y=150)
islem[3].place(x=170,y=200)
islem[4].place(x=170,y=250)
islem[5].place(x=65,y=250)
islem[6].place(x=120,y=250)
islem[7].place(x=15,y=300)
islem[8].place(x=65,y=300)
islem[9].place(x=170,y=300)


sb=Button(text="0",font="Verdana 14 bold",command=lambda x=0:yaz(x))
sb.place(x=20,y=200)       #sıfır butonu#
pi=Button(text="π",font="calibra 14 bold",width=3,command=lambda x=0:yaz("3.141592653589"))
pi.place(x=115,y=300)       #pi sayısı butonu#
nb=Button(text=".",font="Verdana 14 bold",width=2,command=lambda x=".":yaz(x))
nb.place(x=70,y=200)      #nokta butonu#
eb=Button(text="=",fg="RED",font="Verdana 14 bold",command=hesapla)
eb.place(x=120,y=200)     #eşittir butonu#
cb=Button(text="C",font="Verdana 14 bold",width=2,fg="BLUE",command=sıfırla)
cb.place(x=20,y=250)      #  C butonu = hepsini sil #

pencere.mainloop()

#Hocam hesap makinemiz bu şekildedir. Başlangıç halinden son haline 
#kadar ,sil baştan yaz ,olmadı birdaha yaz, bir sürü hata ,yanlış kodlama
#gibi bir sürü sorunla karşılaştık. Elimizden ekip çalışmasıyla bu kadarı geldi
#Açıkcası daha önce bilgisayar kodlama dersi almadığımızdan dolayı yapılan hatalar
#basit,bu yaptığımız hesap makinesi de kolay olabilir ama bizim için zorlu bir süreçti.
#Yaptığımız hesap makinesi çözemediğimiz başı şeylerden dolayı biraz farklı çalışıyor.
#Köklü sayı, logaritma,üst alma(10 üzeride dahil)işlemleri için ilk önce sayıyı yazıp sonra 
#fonksiyona(kök,log, üst alma ) basmak gerekiyor.Hesap makinesi ikiden fazla
#sayıyla işlem yapamıyor. Sadece iki sayıyla işlem yapıp eşittir dedikten sonra 
#üçüncü bir sayıyla işlem yapabilirsiniz.Bu açıklamaları yapma ihtiyacı hissettik.