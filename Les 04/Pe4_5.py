def kwadraten_som(grondgetallen):
    x = 0
    for grondgetal in grondgetallen:
        if grondgetal > 0:
            x += grondgetal*grondgetal
    return x
print(kwadraten_som([2,5,7,4,-9]))