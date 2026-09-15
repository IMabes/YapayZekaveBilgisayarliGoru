# Soft kosinüs benzerliği ile iki belge arasındaki benzerliği ölçen basit bir proje
# Kitapta sayfa 87

# Kurulması gereken kütüphaneler:
# py -m pip install pyemd
# py -m pip install gensim
# py -m pip install nltk

# Peki bu kütüphaneler kısaca ne işe yarıyor?
# pyemd: Earth Mover's Distance (EMD) hesaplamaları için kullanılır. Bu kütüphane, iki dağılım arasındaki benzerliği ölçmek için kullanılır ve özellikle metin madenciliği ve doğal dil işleme alanında kullanışlıdır.
# gensim: Doğal dil işleme ve metin madenciliği için kullanılan bir kütüphane. Bu kütüphane, metinleri analiz etmek, kelime vektörlerini oluşturmak ve benzerlik ölçümleri yapmak için kullanılır.
# nltk: Doğal dil işleme için kullanılan bir kütüphane. Bu kütüphane, metinleri analiz etmek, kelime köklerini bulmak, cümleleri parçalara ayırmak ve daha fazlası için kullanılır.


import numpy as np
from gensim.models import Word2Vec
from gensim.models import KeyedVectors

# Word2Vec modeli metinleri vektörleştirir.
# KeyedVector ise analiz edilen büyük bir metin kümesinden elde edilen kelime vektörlerini saklamak (depolamak) için kullanılır.

model = KeyedVectors.load_word2vec_format('tr_model', binary=True) # Türkçe Word2Vec modelini yükler



# === Similarity Fonksiyonu === # 

# model.similarity() fonksiyonu, iki kelime arasındaki benzerlik oranını hesaplar. Bu oran 0 ile 1 arasında bir değer alır. 1'e yakın değerler, kelimelerin birbirine daha yakın olduğun gösterir.

print("Similarity Fonksiyonu")

benzerlik = model.similarity("çay", "kahve") # çay ve kahve kelimeleri arasındaki benzerlik oranını hesaplar
print("çay ve kahve arasındaki benzerlik oranı: ", benzerlik)
print("===========================================================")
#  


# === Most Similiar Fonksiyonu === # 

# model.most_similar() fonksiyonu, verilen bir kelimeye en yakın kelimeleri ve benzerlik oranlarını döndürür. Örneğin çay kelimesini kullanırsak fındık, kahve, süt gibi kelimeler dönebilir.

print("Most Similar Fonksiyonu")

benzerlik = model.most_similar(positive=["çay"], topn=5) # çay kelimesine en yakın 5 kelimeyi ve benzerlik oranlarını döndürür
print("çay kelimesine en yakın kelimeler ve benzerlik oranları:", benzerlik)
print("===========================================================")



# === Pozlamalı "Most Similiar" Fonksiyonu === #

# Pozlamalı "Most Similar" (model.most_similar(positive=[])) fonksiyonu, bir kelimeye benzer kelimeleri bulmak için kullanılabilir. Bu fonksiyon, verilen kelimelere pozitif ağırlıklar ekleyerek veya çıkararak, daha anlamlı sonuçlar elde etmeyi sağlar. Örneğin, "dal", "kök" ve "yaprak" kelimelerine en yakın kelimeleri bulmak için kullanılabilir.

print("Pozlamalı 'Most Similiar' Fonksiyonu")

benzerlik = model.most_similar(positive=["dal", "kök", "yaprak"]) # dal, kök ve yaprak kelimelerine en yakın kelimeleri ve benzerlik oranlarını döndürür
print("dal, kök ve yaprak kelimelerine en yakın kelimeler ve benzerlik oranları:", benzerlik)
print("===========================================================")



# === Doesnt Match Fonksiyonu === #

# model.doesnt_match() fonksiyonu, verilen kelimeler arasından en az benzer olan kelimeyi döndürür. Bu fonksiyon, bir kelimeye anlamsal bağlantılar ekleyerek veya çıkararak başka bir kelime vektörüne yakınlığı tespit etmeyi sağlar. Örneğin, çay, kahve, fincan ve insan kelimeleri arasından en az benzer olan kelimeyi bulmak için kullanılabilir.

print("Doesnt Match Fonksiyonu")

benzerlik = model.doesnt_match(["çay", "kahve", "fincan", "insan"]) # çay, kahve, fincan ve insan kelimeleri arasından en az benzer olan kelimeyi döndürür
print("çay, kahve, fincan ve insan kelimeleri arasından en az benzer olan kelime:", benzerlik)
print("============================================================")



# === WM Mesafesi Algoritması ile Cümle Benzerliği Fonksiyonu === #

# WM (Word Mover's Distance) mesafesi fonksiyonu, iki cümle arasındaki benzerliği ölçmek için kullanılır. Bu fonksiyon, cümlelerdeki kelimelerin vektörlerini kullanarak, bir cümlenin diğerine ne kadar "taşınması" gerektiğini hesaplar. Bu mesafe ne kadar küçükse, cümleler o kadar benzerdir.

print("WM Mesafesi Algoritması ile Cümle Benzerliği Fonksiyonu")

cumle1 = 'Galatasaray Fenerbahçe maçı kaç kaç bitti'.lower().split()
cumle2 = 'Bu yıl Beşiktaş şampiyon olur'.lower().split()
distance = model.wmdistance(cumle1,cumle2)
print(cumle1)
print(cumle2)
print("İki cümle arasındaki mesafe: ", distance)
print("============================================================")



# === Cümle Benzerliğini Daha Yüksek Başarı İle Hesaplayalım === #

# Kosinüs benzerliği modeli ile birlikte Word2Vec benzerliği modellerini bir arada kullanırsak doğruluğu daha yüksek model elde edebiliriz.
# Word2Vec modeli hassas (soft) kosinüs benzerliğidir.
# Kosinüs benzerliğinin amacı veriyi vektöre çevirmek değildir.
# Veriyi vektöre çevirmek için birçok algoritma ve hatta kütüphane mevcuttur.
# Kosinüs benzerliğinin amacı; vektörize edilmiş veriler arasındaki benzerlik oranını hesaplamaktır.