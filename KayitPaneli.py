from tkinter import *
from tkinter import messagebox
from Uye import Uye

def Kaydet():
    kullaniciadi=kullaniciadigiris.get()
    if len(Uye.GetUser(kullaniciadi)) == 0:
        print("Kullanıcı adını kullanabilirsiniz")
        uye = Uye()
        uye.Name = isimgiris.get()
        uye.Surname = soyisimgiris.get()
        uye.Username = kullaniciadigiris.get()
        uye.Password = parolagiris.get()
        uye.SaveUser(uye)
        messagebox.showinfo("BİLGİ", "Kayıt Başarılı")
        pencere.destroy()
        import GirisPaneli
        GirisPaneli.pencere.mainloop()
    else:
        messagebox.showwarning("UYARI","Kullanıcı adı kullanılmaktadır.")
        isimgiris.delete(0, END)
        soyisim.delete(0, END)
        kullaniciadigiris.delete(0, END)
        parola.delete(0, END)

pencere = Tk()
pencere.title("Kayıt Paneli")
pencere.geometry("480x360")

isim = Label(text="Adınız:", font=("Consolas", 12))
isim.place(x=5, y=10)
isimgiris = Entry(text="", width=45, bd=3)
isimgiris.place(x=135, y=10)

soyisim = Label(text="Soyadınız:", font=("Consolas",12))
soyisim.place(x=5, y=40)
soyisimgiris = Entry(text="", width=45, bd=3)
soyisimgiris.place(x=135, y=40)

kullaniciadi = Label(text="Kullanıcı Adı:", font=("Consolas", 12))
kullaniciadi.place(x=5,y=70)
kullaniciadigiris = Entry(text="", width=45, bd=3)
kullaniciadigiris.place(x=135, y=70)

parola=Label(text="Parolanız:", font=("Consolas", 12))
parola.place(x=5, y=100)
parolagiris = Entry(text="", width=45, bd=3)
parolagiris.place(x=135, y=100)

giris=Button(text="KAYIT OL", width=38, bd=3, command=Kaydet)
giris.place(x=135, y=130)
pencere.mainloop()
