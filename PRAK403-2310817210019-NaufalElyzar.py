AngkaPertama, AngkaKedua = input().split()
AngkaPertama = int (AngkaPertama)
AngkaKedua = int (AngkaKedua)
x = AngkaPertama
y = AngkaKedua
print (f"{AngkaPertama} {AngkaKedua}", end= " - ")
if AngkaPertama > AngkaKedua :
    jarak = AngkaPertama - AngkaKedua
    for i in range (jarak - 1) :
        AngkaPertama -=1
        AngkaKedua +=1
        print (f" {AngkaPertama} {AngkaKedua}", end= " - ")
elif AngkaPertama < AngkaKedua :
    jarak = AngkaKedua - AngkaPertama
    for i in range (jarak - 1) :
        AngkaPertama +=1
        AngkaKedua -=1
        print (f"{AngkaPertama} {AngkaKedua}", end= " - ")
print (f"{y} {x}")