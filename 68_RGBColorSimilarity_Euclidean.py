# İki renk arasındaki benzerlik oranını Öklid Mesafesi (Euclidean Distance) algoritması ile bulma.
# Kitapta Sayfa 68

def arrange(item, dim, min, max):
    item_count,i = len(item), 0

    for i in range(dim):
        if (i <= item_count):
            item[i] = item[i] / ((max - min) / 100) #Persent Value
        else:
            item[i] = 50 / ((max - min) / 100)

    return item

def kokal(x): 
    return x ** (1/2)

def usal(x):
    return x ** 2

kirmizi = [255,0,0]
koyukirmizi = [181,25,25]
kahverengi = [48,34,15]
siyah = [0,0,0]
beyaz = [255,255,255]
gri = [82,82,82]


kirmizi_normalized = arrange(kirmizi, 3, 0, 255)
koyukirmizi_normalized = arrange(koyukirmizi, 3, 0, 255)
kahverengi_normalized = arrange(kahverengi, 3, 0, 255)
siyah_normalized = arrange(siyah, 3, 0, 255)
beyaz_normalized = arrange(beyaz, 3, 0, 255)
gri_normalized = arrange(gri, 3, 0, 255)

def vector_similarity(A, B):
    if len(A) != len(B):
        return -1
    else:
        len_ = len(A)
        total = 0
        for i in range(len_):
            total += usal(B[i] - A[i])
        distance = kokal(total)

        max_dist = 0
        for i in range(len_):
            max_dist += usal(100)
        max_dist = kokal(max_dist)
        return 1 - (distance / max_dist)

        
benzerlik_orani = vector_similarity(koyukirmizi_normalized, kirmizi_normalized)
print(benzerlik_orani)

