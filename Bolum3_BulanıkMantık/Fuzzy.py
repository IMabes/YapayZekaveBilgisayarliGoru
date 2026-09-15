# Bulanık mantık ile Radar Karar Verme Sistemine include edilecek olan bulanık mantık dosyası.


import numpy as np
import Fuzzy as fuzzy
import matplotlib.pyplot as plt

# [(R)] Yolun Yapısı (kötü-normal-iyi)
# [(W)] Hava Şartları (iyi-orta-kötü)
# [(S)] Ortalama Hız (yüksek-orta-düşük)
# [(E)] Kullanıcı Tecrübesi (yüksek-orta-düşük)

#Pythonda belli sınırlarda tanımlı aralıklar oluşturmak için Numpy'nin arrange fonksiyonu kullanılır.



def ucgen(x, abc):
    #İlk parametre değişkenin tanım aralığı, ikinci parametre ise bu tanım aralığı içerisindeki 1.minimum ve 2.minimum noktalarıdır. 
    assert len(abc) == 3, 'Baslangic, tepe ve bitis değerleri verilmelidir.'
    a,b,c = np.r_[abc]
    
    assert a <= b and b <= c, 'Uyelik Fonksiyon değerleri Baslangic <= Tepe <= Bitis' 
    y = np.zeros(len(x))

    #sol
    if a != b:
        idx = np.nonzero(np.logical_and(a < x, x < b))[0]
        y[idx] = (x[idx] - a) / float(b - a)

    #sağ
    if b != c:
        idx = np.nonzero(np.logical_and(b < x, x < c))[0]
        y[idx] = (c - x[idx]) / float(c - b)

    idx = np.nonzero(x == b)
    y[idx] = 1
    return y

def trapez(x , rot, abc):
    y = np.zeros(len(x))
    if(rot=="ORTA"):
        assert len(abc) == 3, 'Baslangic, Tepe ve Bitis Degerleri Verilmelidir!'
        a, b, c = np.r_[abc]
        assert a <= b and b <= c, 'Uyelik Fonksiyon Degerleri Baslangic <= Tepe <= Bitis'
        idx = np.nonzero(np.logical_and(x >= 0, x < a))[0]
        y[idx] = (x[idx]) / float(a)
        idx = np.nonzero(np.logical_and(x >= a, x < b))[0]
        y[idx] = 1
        idx = np.nonzero(np.logical_and(x >= b, x < c))[0]
        y[idx] = (c - x[idx]) / float(c - b)
        return y
    else:
        assert len(abc) == 2, 'Baslangic, Tepe ve Bitis Degerleri Verilmelidir!'
        a, b = np.r_[abc]
        if(rot == "SOL"):
            assert a <= b, 'Uyelik Fonksiyon Degerleri Baslangic <= Tepe <= Bitis'
            idx = np.nonzero(np.logical_and(x >= a, x < b))[0]
            y[idx] = (b - x[idx] - b) / float(a - b)
            return y
        elif(rot == "SAG"):
            assert a <= b, 'Uyelik Fonksiyon Degerleri Baslangic <= Tepe <= Bitis'
            idx = np.nonzero(x > a)[0]
            y[idx] = 1
            idx = np.nonzero(np.logical_and(x > a, x <= b))[0]
            y[idx] = (x[idx] - a) / float(b - a)
            return y



def uyelik(x, xmf, xx, zero_outside_x=True):
    if not zero_outside_x:
        kwargs = {None, None}
    else: 
        kwargs = {0.0, 0.0}

    return np.interp(xx, x, xmf, left=kwargs[0], right=kwargs[1])

