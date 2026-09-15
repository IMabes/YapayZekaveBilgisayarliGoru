# Matris Benzerliği
# Kitapta sayfa 98


# python -m pip install opencv-python 
# python -m pip install pillow
# python -m pip install numpy
# opencv kütüphanesi: Yüz tanıma, nesne tespiti, plaka okuma ve makine öğrenimi gibi bilgisayarlı görü projelerinde yaygın olarak kullanılır.
# pillow kütüphanesi: Python'da resim işleme (image processing) işlemleri yapmak için kullanılan bir kütüphanedir. Resimleri açma, oluşturma, düzenleme, kaydetme ve dönüştürme gibi birçok işlemi kolayca yapmanı sağlar.
# numpy kütüphanesi: Python'da sayısal hesaplamalar yapmak için kullanılan en temel kütüphanelerden biridir. Özellikle diziler, matrisler ve matematiksel işlemleri çok hızlı bir şekilde gerçekleştirmeyi sağlar. Yapay zekâ, veri bilimi, görüntü işleme ve bilimsel hesaplamaların temelini oluşturur.


import math
import warnings
import numpy as np
import cv2
from PIL import Image

warnings.filterwarnings("ignore") #Python'da program çalışırken oluşan uyarı mesajlarını gizlemek için kullanılır.

gorsel1 = cv2.imread('MatrisSimilarityPicture1.png')
gorsel2 = cv2.imread('MatrisSimilarityPicture2.png')
# Görselleri imread() fonksiyonu ile matrise dönüştürdük.


yukseklik = gorsel1.shape[0] 
genislik = gorsel1.shape[1]
# Yatay ve dikeydeki pikselleri shape fonksiyonu ile alıyoruz.

pixelsayi = yukseklik * genislik
# Toplamdaki piksel sayısını bulmak için yükseklik ve genişliği çarpıyoruz
fark = 0

def pixelFark(pixel1, pixel2):
    pixel_fark = 0

    for i in range(3):
        pixel_fark += abs(pixel1[i] - pixel2[i]) / 255
    return pixel_fark
# pixelFark fonksiyonu, iki piksel arasındaki renk farkını hesaplar. range içerisine 3 yazmamızın sebebi ise opencv'de bir pikselin 3 sayıdan oluşmasıdır. - [R,G,B] - Döndürülen değer ne kadar küçükse pikseller birbirine o kadar benzer, ne kadar büyükse renk farkı o kadar fazladır. Bu fonksiyon, iki görüntü arasındaki genel benzerlik oranını hesaplamak için her piksel üzerinde ayrı ayrı uygulanır.


for i in range(yukseklik):
    for j in range(genislik):
        fark += pixelFark(gorsel1[i][j], gorsel2[i][j])
# Buradaki kod bloğunda iki görüntü piksel piksel karşılaştırılır. Her konumdaki piksel çifti pixelFark() fonksiyonuna gönderilerek renk farkı hesaplanır ve bu değer fark değişkenine eklenir.



def farkMatris(matris1, matris2):
    yukseklik,genislik = matris1.shape[0], matris1.shape[1]
    matris = np.zeros(shape=(yukseklik,genislik,3), dtype = np.uint8)
    for i in range(yukseklik):
        for j in range(genislik):
            if pixelFark(matris1[i][j], matris2[i][j]) == 0:
                matris[i,j,0] = 255
                matris[i,j,1] = 255
                matris[i,j,2] = 255
                continue
            else:
                matris[i,j,0] = matris2[i][j][0]
                matris[i,j,1] = matris2[i][j][1]
                matris[i,j,2] = matris2[i][j][2]
    img = Image.fromarray(matris, 'RGB')
    img.save('farkMatris.png')
# farkMatris() fonksiyonu, iki görüntüyü piksel piksel karşılaştırarak yeni bir görüntü oluşturur. Önce orijinal görüntülerle aynı boyda olan siyah-beyaz bir matris oluşturulur. ARdından her piksel için pixelFark() fonksiyonu kullanılarak renklerin farkı hesaplanır. Eğer iki piksel tamamen aynı ise yeni görüntüde o piksel beyaz(255,255,255) olarak işaretlenir. Farklıysa, ikinci görüntüdeki pikselin renk değeri yeni matrise kopyalanır. Böylece benzer bölgeler beyaz, farklı bölgeler ise ikinci görüntünün renkleriyle gösterilerek iki görüntü arasındaki farklılıklar görsel olarak ortaya çıkarılır. Son olarak oluşturulan fark matrisi farkMatris.png adıyla kaydedilir.


farklilik_oran = 100 * fark / (genislik * yukseklik * 3)
print("İki görsel arasındaki farklılık oranı: " , str(farklilik_oran))

benzerlik_oran = 100 - farklilik_oran
print("İki görsel arasındaki benzerlik oranı: " , str(benzerlik_oran))

farkMatris(gorsel1, gorsel2)
print("İki görsel arasındaki farklılıklar, fark.png dosyası olarak kayıt edildi.")
