from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    sonuc = ""

    if request.method == "POST":
        km = request.form["km"]      #Formdan gelen verileri alıyoruz 
        arac = request.form["arac"]  #Ben bunu değişken oluşturmak diyorum çünkü daha basit olur.

        if km.isdigit():  #Bir digit yani sayı olup olmadığını kontrol ediyoruz.
            km = int(km)  #Girilen sayıyı integer'a yani sayıya ceviriyoruz.

                #Ayak izi hesaplama (Yapay Zeka Kullanıldı)


            if arac == "araba":
                carpan = 21
            elif arac == "otobus":
                carpan = 11
            elif arac == "tren":
                carpan = 4
            elif arac == "ucak":
                carpan = 25
            else:
                carpan = 0

            ayak_izi = km * carpan // 100 # Kilometre'yi çarpan ile çarpıyoruz ve 100'e bolüyoruz. Böylece Sonuç elimize geliyor.
            sonuc = f"Tahmini Karbon Ayak İzi: {ayak_izi} kg CO2"
        else:
            sonuc = "Lütfen sadece sayı girin!" # Sayı değilse girilen yazı ise hata alıyoruz.

    return render_template("index.html", sonuc=sonuc)

if __name__ == "__main__":
    app.run(debug=True)
