# Toleranslı Benzerlik Algoritması ve Tanimoto Benzerlik Algoritması
#Kitapta sayfa 104 [ödevler]

# Ödev 1 : Toleranslı benzerlik algoritmasını bir önceki konuda gerçekleştirdiğiniz vektör-uzay benzerlik algoritmasını taban alacak şekilde geliştiriniz.

# Ödev 2 : Tanimoto benzerlik algoritmasını araştırın ve tanimoto ile matris benzerliğini hesaplayan bir proje geliştirin. Matris benzerliği ile Tanimoto benzerliği algoritmalarının benzerlik oranı tespitinde ne gibi farkları var, bu farklar sizce neden oluşmuş olabilir açıklayın.

# Toleranslı Benzerlik Algoritması Nedir ? 
# Toleranslı benzerlik algoritması, veriler birebir eşleşmese bile belirli bir hata payı, sapma veya esneklik payı dahilinde benzer olanları bulmayı sağlayan matematiksel yöntemdir. Veri temizleme, ses/görüntü tanıma, biyoinformatik ve arama motorlarında sıkça kullanılır. (DAHA FAZLASINI İNTERNETTE ARAŞTIRIP ÖĞREN)

# Tanimoto Benzerlik Algoritması Nedir ? 
# Tanimoto benzerlik algoritması, iki veri kümesi veya vektör arasındaki benzerlik derecesini hesaplayan matematiksel bir ölçüttür. Temel olarak ortak özelliklerin sayısının, tüm özelliklerin toplamına oranlanmasıyla çalışır ve sonucu 0 ile 1 arasında bir değer verir. Veri madenciliği, kimya ve ilaç gibi alanlarda kullanılır. (DAHA FAZLASINI İNTERNETTE ARAŞTIRIP ÖĞREN)

# Tanimoto= Ortak Eleman Sayısı / Toplam Benzersiz Eleman Sayısı


# Ödev 2 Uygulama:



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
# farkMatris() fonksiyonu, iki görüntüyü piksel piksel karşılaştırarak yeni bir görüntü oluşturur. Önce orijinal görüntülerle aynı boyda olan siyah bir matris oluşturulur. Ardından her piksel için pixelFark() fonksiyonu kullanılarak renklerin farkı hesaplanır. Eğer iki piksel tamamen aynı ise yeni görüntüde o piksel beyaz(255,255,255) olarak işaretlenir. Farklıysa, ikinci görüntüdeki pikselin renk değeri yeni matrise kopyalanır. Böylece benzer bölgeler beyaz, farklı bölgeler ise ikinci görüntünün renkleriyle gösterilerek iki görüntü arasındaki farklılıklar görsel olarak ortaya çıkarılır. Son olarak oluşturulan fark matrisi farkMatris.png adıyla kaydedilir.


def benzerTanimoto(matris1 ,matris2):
    gray1 = cv2.cvtColor(gorsel1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(gorsel2, cv2.COLOR_BGR2GRAY)
    # Resmi griye çeviriyoruz.

    _, binary1 = cv2.threshold(gray1,127,255,cv2.THRESH_BINARY)
    _, binary2 = cv2.threshold(gray2,127,255,cv2.THRESH_BINARY)
    # Resmi siyah beyaz yapıyoruz


    set1 = set(zip(*np.where(binary1==255)))
    set2 = set(zip(*np.where(binary2==255)))
    # Görüntüde beyaz olan bütün piksellerin (satır, sütun) koordinatlarını bul ve bunları bir küme (set) hâline getir.

    # set1 = set(map(tuple, matris1.reshape(-1, 3)))
    # set2 = set(map(tuple, matris2.reshape(-1, 3)))
    ortak = len(set1.intersection(set2))
    toplam = len(set1.union(set2))
    return ortak / toplam

print("Tanimoto benzerliği ile benzerlik oranı: ", benzerTanimoto(gorsel1, gorsel2))


farklilik_oran = 100 * fark / (genislik * yukseklik * 3)
print("İki görsel arasındaki farklılık oranı: " , str(farklilik_oran))

benzerlik_oran = 100 - farklilik_oran
print("İki görsel arasındaki benzerlik oranı: " , str(benzerlik_oran))

farkMatris(gorsel1, gorsel2)
print("İki görsel arasındaki farklılıklar, fark.png dosyası olarak kayıt edildi.")

