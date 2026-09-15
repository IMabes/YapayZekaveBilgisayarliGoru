# Ağırlıklı Levenshtein Mesafesi Hesaplama 
#Kitapta sayfa 63 [ödev]

import numpy as np

# QWERTY klavye düzeni - her tuşun koordinatı (satır, sütun)
klavye = {
    'q':(0,0),'w':(0,1),'e':(0,2),'r':(0,3),'t':(0,4),
    'y':(0,5),'u':(0,6),'i':(0,7),'o':(0,8),'p':(0,9),
    'a':(1,0),'s':(1,1),'d':(1,2),'f':(1,3),'g':(1,4),
    'h':(1,5),'j':(1,6),'k':(1,7),'l':(1,8),
    'z':(2,0),'x':(2,1),'c':(2,2),'v':(2,3),'b':(2,4),
    'n':(2,5),'m':(2,6)
}

def tus_mesafesi(c1, c2):
    c1, c2 = c1.lower(), c2.lower()
    if c1 == c2:
        return 0
    if c1 not in klavye or c2 not in klavye:
        return 1  # bilinmeyen karakter → tam puan
    
    r1, k1 = klavye[c1]
    r2, k2 = klavye[c2]
    mesafe = abs(r1 - r2) + abs(k1 - k2)  # Manhattan mesafesi
    
    if mesafe == 1:
        return 0.25   # en yakın tuş
    elif mesafe == 2:
        return 0.50   # 1 tuş ara
    else:
        return 1.00   # 2+ tuş ara

def agirlikli_levenshtein(A, B):
    m, n = len(A), len(B)
    dp = np.zeros((m + 1, n + 1))

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i-1] == B[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                silme        = dp[i-1][j]   + 1
                ekleme       = dp[i][j-1]   + 1
                degistirme   = dp[i-1][j-1] + tus_mesafesi(A[i-1], B[j-1])
                dp[i][j] = min(silme, ekleme, degistirme)

    return dp[m][n]

# --- Ana Program ---
kelime_1 = input("1. kelimeyi girin: ").lower()
kelime_2 = input("2. kelimeyi girin: ").lower()

max_len = max(len(kelime_1), len(kelime_2))
mesafe  = agirlikli_levenshtein(kelime_1, kelime_2)

print(f"\n'{kelime_1}' ve '{kelime_2}' arasındaki Ağırlıklı Levenshtein Mesafesi: {mesafe}")

benzerlik = (max_len - mesafe) / max_len
print(f"Benzerlik Oranı: {benzerlik:.4f}")