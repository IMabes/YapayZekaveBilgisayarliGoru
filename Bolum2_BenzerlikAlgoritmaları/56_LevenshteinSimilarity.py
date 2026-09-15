# Levenshtein Benzerlik Algoritması
# Kitapta Sayfa 56


import numpy

# def minimum(a,b,c):
#     if a<=b and a<=c:
#         return a
#     if b<=a and b<=c:
#         return b
#     if c<=a and c<=b:
#         return c

# def max(a,b):
#     if a>b:
#         return a
#     else:
#         return b
  ### --- MIN VE MAX FONKSIYONLARI PYTHONUN KENDİ FONKSIYONUNU EZIYOR ---
# def normalize(X,size):
#     if len(X) < size:
#         fark = size - len(X)
#         for i in range(fark):
#             X = X + " "
#     return X

def LevenshteinMesafesi(A,B):

    K = numpy.zeros((len(A) + 1, len(B) + 1))

    A_len = len(A)
    B_len = len(B)

    for i in range(A_len + 1):
        K[i][0] = i

    for j in range(B_len + 1):
        K[0][j] = j

    silme = 0
    ekleme = 0
    yerdegistirme = 0

    for i in range(1, A_len + 1):
        for j in range(1, B_len + 1):

            if A[i-1] == B[j-1]:
                K[i][j] = K[i-1][j-1]

            else:
                silme = K[i-1][j] + 1
                ekleme = K[i][j-1] + 1
                yerdegistirme = K[i-1][j-1] + 1

                K[i][j] = min(silme, ekleme, yerdegistirme)

    return K[A_len][B_len]

kelime_1 = input("1.kelimeyi girin: ")
kelime_2 = input("2.kelimeyi girin: ")

max_len = max(len(kelime_1), len(kelime_2))

# kelime_1 = normalize(kelime_1, max_len)
# kelime_2 = normalize(kelime_2, max_len)

mesafe = LevenshteinMesafesi(kelime_1,kelime_2)

print("'" + kelime_1 + "' ve '" + kelime_2 + "' arasındaki Levenshtein Mesafesi: ")
print(mesafe)


benzerlik_oran = (max_len - mesafe)/max_len
print("Benzerlik Oranı: ")
print(benzerlik_oran)

### KOD OPTIMIZE EDILDI GEREKSIZ KISIMLAR ACIKLAMA SATIRINA ALINDI 