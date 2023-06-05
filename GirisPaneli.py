from Uye import Uye
from tkinter import *
from tkinter import messagebox

def kayityap():
    pencere.destroy()
    import KayitPaneli
    KayitPaneli.pencere.mainloop()

def Girisyap():
    kullaniciadi = kullaniciadigiris.get()
    parola = parolagiris.get()
    if (parola != "" and kullaniciadigiris != ""):
        uye = Uye()
        uye = Uye.LoginUser(kullaniciadi, parola)
        if (uye!= -1 and uye.Username != "" and uye.Password != ""):
            messagebox.showinfo("giriş basarili")
        else:
            messagebox.showerror("bilgi", "giris basarisiz")
            messagebox.showerror("hata", "kayıtlı kullanıcı bulunamadı")
            kullaniciadigiris.delete(0, END)
            parola.delete(0, END)
    else:
        messagebox.showwarning("uyarı", "kullanıcı adı veya parola alanları bos olamaz")


pencere = Tk()
pencere.title("GİRİŞ PANELİ")
pencere.geometry("500x140")

kullaniciadi_lbl=Label(text="Kullanıcı Adı: ", font=("Consolas",12))
kullaniciadi_lbl.place(x=5, y=10)
kullaniciadigiris = Entry(text="", width=45, bd=3)
kullaniciadigiris.place(x=135, y=10)

parola_lbl=Label(text="Parola: ", font=("Consolas",12))
parola_lbl.place(x=5,y=40)
parolagiris = Entry(text="", width=45, bd=3)
parolagiris.place(x=135, y=40)

giris=Button(text="Giriş Yap", width=10, bd=3,command=Girisyap)
giris.place(x=135, y=70)

kayit=Button(text="Kayıt ol", width=10, bd=3,command=kayityap)
kayit.place(x=225, y=70)
pencere.mainloop()





























