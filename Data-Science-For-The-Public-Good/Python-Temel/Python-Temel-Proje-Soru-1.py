# Samet Arda Erdoğan | sametarda.dev@gmail.com

def donustur(liste):
    yeniListe = []
    for i in liste:
        if type(i) == list:
            yeniListe.extend(donustur(i)) # öz yinemeli fonksiyon
        else:
            yeniListe.append(i)
    return yeniListe


a = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]


print(donustur(a))