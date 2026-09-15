# Kosinüs Teoremi ile Benzerlik Oranı Hesaplama
# Kitapta sayfa 77

cumle1 = "Merhabalar benim adım İrem"
cumle2 = "Selam ben İrem Kılıçer"

def stopWord(kelime):
    stopWords = ["acaba", "ama", "ancak", "artık", "aslında", "az", "gene", "gibi", "da" ,"de","en", "daha", "diğer","diğeri","diye","dolayı"]
    flag = True
    for i in range(len(stopWords)):
        if kelime == stopWords[i]:
            return True
        else:
            flag = False
    return flag
# Fonksiyon kelimemizin stopWords dizisinde olup olmadığını kontrol eder.


def ara(dizi,kelime):
    flag = False
    for eleman in dizi:
        if eleman == kelime:
            flag = True
        else: 
            flag = False
    return flag
#Kelimenin dizide olup olmadığını kontrol eder. Yardımcı fonksiyondur.


def sozlukOku(dizi):
    sozluk = []
    for cumle in dizi:
        kelimeler = cumle.split()
        for kelime in kelimeler:
            if stopWord(kelime):
               continue
            else:
                if len(sozluk) == 0:
                    sozluk.append(kelime)
                else:
                    if ara(sozluk,kelime):
                        continue
                    else:
                        sozluk.append(kelime)
    return sozluk
# Cümleyi parçalara ayırır ve stopWords dizisinde olmayan kelimeleri bir sözlük dizisine ekler.


def cumle2Vec(cumle, sozluk):
    vector = []
    kelimeler = cumle.split(" ")
    for sozcuk in sozluk:
        sozcuksayisi = 0
        for kelime in kelimeler:
            if kelime == sozcuk:
                sozcuksayisi += 1
        vector.append([sozcuk, sozcuksayisi])
    return vector
# Cümleyi sözlükteki kelimelere göre vektörleştirir. Vektörün her bir elemanı sözlükteki kelimenin cümlede kaç defa geçtiğini gösterir.



def noktasalcarpim(vector1,vector2):
    if len(vector1) != len(vector2):
        return -1
    
    toplam = 0
    for i in range(len(vector1)):
        toplam += vector1[i][1] * vector2[i][1]
    return toplam
# Noktasal çarpımı hesaplar. İki vektörün boyutları eşit değilse -1 döndürür.

def vectorboyut(vector):
    toplam = 0
    for i in range(len(vector)):
        toplam += vector[i][1] ** 2
    return toplam ** (1/2)
# Vektörün boyutunu hesaplar. Vektörün her bir elemanının karesini alır, toplar ve karekökünü alır.

def cosinusbenzerliği(vector1,vector2):
        return noktasalcarpim(vector1,vector2) / (vectorboyut(vector1) * vectorboyut(vector2))
# İki vektörün kosinüs benzerliğini hesaplar. Noktasal çarpımı vektörlerin boyutlarının çarpımına böler.



sozluk = sozlukOku([cumle1, cumle2])
cumle1Vector = cumle2Vec(cumle1, sozluk)
cumle2Vector = cumle2Vec(cumle2, sozluk)
print(cumle1Vector)
print(cumle2Vector)
    
benzerlik_orani = cosinusbenzerliği(cumle1Vector, cumle2Vector)
print("iki cümle arasındaki bemzerlik oranı: ", benzerlik_orani)