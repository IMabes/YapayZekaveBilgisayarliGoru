# Bulanık Mantık ile Radar Karar Verme Sistemi
# Kitapta Sayfa 137

import numpy as np
import Fuzzy as fuzzy
import matplotlib.pyplot as plt

x_R = np.arange(0,91,1) # Yolun Yapısı
x_W = np.arange(0,11,1) # Hava Şartları
x_S = np.arange(0,151,1) # Ortalama Hız
x_E = np.arange(0,21,1) # Kullanıcı Tecrübesi

x_O = np.arange(0,101,1) # Sonuç


R_kotu = fuzzy.trapez(x_R, "SOL", [30, 45])
R_normal = fuzzy.ucgen(x_R, [30, 45, 60])
R_iyi = fuzzy.trapez(x_R, "SAG", [45, 60])

W_kotu = fuzzy.ucgen(x_W, [0, 0, 5])
W_normal = fuzzy.ucgen(x_W, [0, 5, 10])
W_iyi = fuzzy.ucgen(x_W, [5, 10, 10])

S_az = fuzzy.ucgen(x_S, [0, 0, 70])
S_ort = fuzzy.ucgen(x_S, [0, 70, 130])
S_cok = fuzzy.trapez(x_S, "SAG", [70, 130])

E_az = fuzzy.ucgen(x_E, [0, 0, 10])
E_ort = fuzzy.ucgen(x_E, [0, 10, 20])
E_cok = fuzzy.ucgen(x_E, [10, 20, 30])

O_az = fuzzy.trapez(x_O, "SOL", [25, 50])
O_ort = fuzzy.ucgen(x_O, [25, 50, 85])
O_cok = fuzzy.trapez(x_O, "SAG", [50, 85])


#-----------------------------------------------

# Inputları Al
print("Yol viraj düzeyi girin (0-90) ")
input_R = int(input())
print("Hava şartları girin (0-10) ")
input_W = int(input())
print("Ortalama hız girin (30-150) ")
input_S = int(input())
print("Kullanıcı tecrübesi girin (0-20) ")
input_E = int(input())


R_fit_kotu = fuzzy.uyelik(x_R, R_kotu, input_R)
R_fit_normal = fuzzy.uyelik(x_R, R_normal, input_R)
R_fit_iyi = fuzzy.uyelik(x_R, R_iyi, input_R)


w_fit_kotu = fuzzy.uyelik(x_W, W_kotu, input_W)
w_fit_normal = fuzzy.uyelik(x_W, W_normal, input_W)
w_fit_iyi = fuzzy.uyelik(x_W, W_iyi, input_W)

S_fit_az = fuzzy.uyelik(x_S, S_az, input_S)
S_fit_ortalama = fuzzy.uyelik(x_S, S_ort, input_S)
S_fit_cok = fuzzy.uyelik(x_S, S_cok, input_S)

E_fit_az = fuzzy.uyelik(x_E, E_az, input_E)
E_fit_ortalama = fuzzy.uyelik(x_E, E_ort, input_E)
E_fit_cok = fuzzy.uyelik(x_E, E_cok, input_E)


rule1 = np.fmin(np.fmin(R_fit_kotu, w_fit_kotu), O_az)
#Eğer yol çok virajlı ve hava şartları kötü ise hız sınırı düşmelidir.

rule2 = np.fmin(np.fmin(R_fit_normal , w_fit_normal), O_ort)
#Eğer yol normal ve hava şartları normal ise hız sınırı ortalama olmalıdır.

rule3 = np.fmin(np.fmin(R_fit_iyi, w_fit_iyi), O_cok)
#Eğer az virajlı ve hava şartları iyi ise hız sınırı yüksek olmalıdır.

rule4 = np.fmin(np.fmax(S_fit_az, E_fit_az), O_az)
#Eğer ortalama hız az veya kullanıcı tecrübesi az ise hız sınırı düşmelidir.

rule5 = np.fmin(np.fmax(S_fit_ortalama, E_fit_ortalama), O_ort)
#Eğer ortalama hız normal veya kullanıcı tecrübesi normal ise hız sınırı ortalama olmalıdır.

rule6 = np.fmin(np.fmax(S_fit_cok, E_fit_cok), O_cok)
#Eğer ortalama hız yüksek veya kullanıcı tecrübesi yüksek ise hız sınırı yüksek olmalıdır.


out_az = np.fmax(rule1, rule4)
out_ort = np.fmax(rule2, rule5)
out_cok = np.fmax(rule3, rule6)


O_zeros = np.zeros_like(x_O)
fig, grafik_output = plt.subplots(figsize=(7, 4))
grafik_output.fill_between(x_O, O_zeros, out_az, facecolor='r', alpha=0.7)
grafik_output.plot(x_O, O_az, 'r', linewidth=0.5, linestyle='--', label='Kötü')
grafik_output.fill_between(x_O, O_zeros, out_ort, facecolor='g', alpha=0.7)



#------------------------------------------------


fig, (ax0,ax1,ax2,ax3,ax4) = plt.subplots(nrows=5, figsize=(6, 10))

ax0.plot(x_R, R_kotu, 'r', linewidth=2, label='Kötü')
ax0.plot(x_R, R_normal, 'g', linewidth=2, label='Normal')
ax0.plot(x_R, R_iyi, 'b', linewidth=2, label='İyi')
ax0.set_title('Yol viraj ve eğimi')
ax0.legend()

ax1.plot(x_W, W_kotu, 'r', linewidth=2, label='Kötü')
ax1.plot(x_W, W_normal, 'g', linewidth=2, label='Normal')
ax1.plot(x_W, W_iyi, 'b', linewidth=2, label='İyi')
ax1.set_title('Hava Şartları')
ax1.legend()

ax2.plot(x_S, S_az, 'r', linewidth=2, label='Az')
ax2.plot(x_S, S_ort, 'g', linewidth=2, label='Orta')
ax2.plot(x_S, S_cok, 'b', linewidth=2, label='Çok')
ax2.set_title('Ortalama Hız')
ax2.legend()

ax3.plot(x_E, E_az, 'r', linewidth=2, label='Kötü')
ax3.plot(x_E, E_ort, 'g', linewidth=2, label='Normal')
ax3.plot(x_E, E_cok, 'b', linewidth=2, label='İyi')
ax3.set_title('Kullanıcı Tecrübesi')
ax3.legend()

ax4.plot(x_O, O_az, 'r', linewidth=2, label='Kötü')
ax4.plot(x_O, O_ort, 'g', linewidth=2, label='Normal')
ax4.plot(x_O, O_cok, 'b', linewidth=2, label='İyi')
ax4.set_title('Sonuç')
ax4.legend()
plt.tight_layout
plt.savefig('UyelikFonksiyonlari.png')


