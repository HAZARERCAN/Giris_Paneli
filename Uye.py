import sqlite3

class Uye:
    def init(self):
        self.Name = ""
        self.Surname = ""
        self.Username = ""
        self.Password = ""

    @classmethod
    def GetUser(cls, kullaniciadi):
        vt = sqlite3.connect("Uyeler.db")
        cur = vt.cursor()
        komut = "Select * from Uyelik where USERNAME= '" + kullaniciadi + "'"
        cur.execute(komut)
        liste = cur.fetchall()
        vt.close()
        return liste

    def SaveUser(self, uye):
        vt = sqlite3.connect("Uyeler.db")
        cur = vt.cursor()
        try:
            komut = "Insert into Uyelik(NAME, SURNAME, USERNAME, PASSWORD) values (?,?,?,?)"
            cur.execute(komut, (uye.Name, uye.Surname, uye.Username, uye.Password))
            vt.commit()
            print("Kayıt Başarılı")
        except:
            print("Kayıt başarısız")

        vt.close()

    @classmethod
    def LoginUser(cls, kullaniciadi, parola):
        vt = sqlite3.connect("Uyeler.db")
        cur = vt.cursor()
        try:
            komut = "Select NAME,SURNAME,USERNAME,PASSWORD from Uyelik where USERNAME ='"+kullaniciadi+"' and PASSWORD='"+parola+"'"
            cur.execute(komut)
            liste = cur.fetchone()
            uye = Uye()
            uye.Name = liste[0]
            uye.Surname = liste[1]
            uye.Username = liste[2]
            uye.Password = liste[3]
            return uye
        except:
            return -1



























