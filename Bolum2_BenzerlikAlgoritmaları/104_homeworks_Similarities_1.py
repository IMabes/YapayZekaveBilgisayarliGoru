# Toleranslı Benzerlik Algoritması ve Tanimoto Benzerlik Algoritması
#Kitapta sayfa 104 [ödevler]

# Ödev 1 : Toleranslı benzerlik algoritmasını bir önceki konuda gerçekleştirdiğiniz vektör-uzay benzerlik algoritmasını taban alacak şekilde geliştiriniz.

# Ödev 2 : Tanimoto benzerlik algoritmasını araştırın ve tanimoto ile matris benzerliğini hesaplayan bir proje geliştirin. Matris benzerliği ile Tanimoto benzerliği algoritmalarının benzerlik oranı tespitinde ne gibi farkları var, bu farklar sizce neden oluşmuş olabilir açıklayın.

# Toleranslı Benzerlik Algoritması Nedir ? 
# Toleranslı benzerlik algoritması, veriler birebir eşleşmese bile belirli bir hata payı, sapma veya esneklik payı dahilinde benzer olanları bulmayı sağlayan matematiksel yöntemdir. Veri temizleme, ses/görüntü tanıma, biyoinformatik ve arama motorlarında sıkça kullanılır. (DAHA FAZLASINI İNTERNETTE ARAŞTIRIP ÖĞREN)

# Tanimoto Benzerlik Algoritması Nedir ? 
# Tanimoto benzerlik algoritması, iki veri kümesi veya vektör arasındaki benzerlik derecesini hesaplayan matematiksel bir ölçüttür. Temel olarak ortak özelliklerin sayısının, tüm özelliklerin toplamına oranlanmasıyla çalışır ve sonucu 0 ile 1 arasında bir değer verir. Veri madenciliği, kimya ve ilaç gibi alanlarda kullanılır. (DAHA FAZLASINI İNTERNETTE ARAŞTIRIP ÖĞREN)


# Ödev 1 Uygulama:


#     Cümle +
#       ↓
#  Kelimelere ayır +
#       ↓
#  Kelime benzerliği hesapla  ← YENİ
#       ↓
#  Sözlük oluştur +
#       ↓ 
#  Vektör oluştur +
#       ↓
#  Kosinüs benzerliği


cumle1 = "Merhabalar benim adım İrem Kılıçer"
cumle2 = "Selamlar benim ismim İrem Kılıçer"

def ara(dizi, kelime):
    for eleman in dizi:
        if kelimeBenzerlik(eleman, kelime) >= 0.80:
            return True
    return False
# Sözlük dizide var mı kontrolü (yardımcı fonksiyon)

def kelime2Vec(kelime):
    harfler = []
    for harf in kelime:
        harfler.append(ord(harf))
    return harfler
# Kelimeyi vektör hale getirir.


def esitle(A,B):
    if len(A) != len(B):
        if len(A) < len(B):
            for i in range(len(B) - len(A)):
                A.append(A[-1])
        else:
            for i in range(len(A) - len(B)):
                B.append(B[-1])
    return A,B
# Kelimelerin uzunluğunu eşitler.


def noktasalcarpim(vector1, vector2):
    if len(vector1) != len(vector2):
        return -1

    toplam = 0
    for i in range(len(vector1)):
        toplam += vector1[i][1] * vector2[i][1]
    return toplam


def vectorboyut(vector):
    toplam = 0
    for i in range(len(vector)):
        toplam += vector[i][1] ** 2
    return toplam ** 0.5


def cosinusBenzerligi(vector1, vector2):
    return noktasalcarpim(vector1, vector2) / (vectorboyut(vector1) * vectorboyut(vector2))


def asciiBenzerlik(A, B):
    if len(A) != len(B):
        return -1
    total = 0
    for i in range(len(A)):
        total += (B[i] - A[i]) ** 2
    distance = total ** 0.5
    max_deger = max(max(A), max(B))
    max_dist = 0
    for i in range(len(A)):
        max_dist += max_deger ** 2
    max_dist = max_dist ** 0.5

    return 1 - (distance / max_dist)


def kelimeBenzerlik(kelime1, kelime2):
    A = kelime2Vec(kelime1)
    B = kelime2Vec(kelime2)

    A, B = esitle(A, B)
    benzerlik = asciiBenzerlik(A, B)
    return benzerlik
            


def sozlukOku(dizi):
    sozluk = []
    for cumle in dizi:
        kelimeler = cumle.split()
        for kelime in kelimeler:
            if len(sozluk) == 0:
                sozluk.append(kelime)
            else:
                if ara(sozluk,kelime):
                    continue
                else:
                    sozluk.append(kelime)
    return sozluk
# Sözlük Oluştur



def cumle2Vec(cumle, sozluk):
    vector = []
    kelimeler = cumle.split(" ")
    for sozcuk in sozluk:
        sozcuksayisi = 0
        for kelime in kelimeler:
           if kelimeBenzerlik(kelime, sozcuk) >= 0.95:
                sozcuksayisi += 1
        vector.append([sozcuk, sozcuksayisi])
    return vector
# Kelime vektörleştirme

sozluk = sozlukOku([cumle1, cumle2])

cumle1Vector = cumle2Vec(cumle1, sozluk)
cumle2Vector = cumle2Vec(cumle2, sozluk)

print(cumle1Vector)
print(cumle2Vector)

benzerlik = cosinusBenzerligi(cumle1Vector, cumle2Vector)

print("Benzerlik Oranı:", benzerlik)


print(kelimeBenzerlik("Merhabalar", "benim"))
print(kelimeBenzerlik("Merhabalar", "Selamlar"))
print(kelimeBenzerlik("adım", "ismim"))