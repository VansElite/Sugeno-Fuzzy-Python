
TK = int(input("Masukkan nilai Tingkat Kebersihan: "))
OK = int(input("Masukkan nilai Kadar Oksigen: "))
KA_TK = []
KA_O2 = []
TKU = 0  # TKU 0 = baik, TKU 1 = buruk, TKU 2 = berbahaya
TOK = 0  # TKU 0 = baik, TKU 1 = buruk, TKU 2 = berbahaya
y = [0, 1, 0]

var1 = [[70, 80, 90], [50, 62.25, 75], [30, 42.25, 55]]
var2 = [[7, 8, 9], [5, 6, 7], [3, 4, 5]]


def segitiga(x, a, b, c):
    if(x < a) or (x > c):
        return 0
    if(x < b):
        return (x-a)/(b-a)
    else:
        return (c-x)/(c-b)


for x in var1:
    # print(segitiga(50, var1[x][x], var1[x][x+1], var1[x][x+2]))
    p = segitiga(TK, x[0], x[1], x[2])
    KA_TK.append(p)
print(KA_TK)

for x in var2:
    # print(segitiga(OK, x[0], x[1], x[2]))
    p = segitiga(OK, x[0], x[1], x[2])
    KA_O2.append(p)
print(KA_O2)
# Metode Sugeno
# Jika x ada didalam array 1 = baik, array 2 = buruk, array 3 = berbahaya
# gapaham apasih ini

if (TK >= var1[0][0]) and (TK <= var1[0][2]):
    TKU = 1
    StatusKU = "Baik"
    print(segitiga(TK, var1[0][0], var1[0][1], var1[0][2]))
    NA_KU = segitiga(TK, var1[0][0], var1[0][1], var1[0][2])
if (TK >= var1[1][0]) and (TK <= var1[1][2]):
    TKU = 2
    StatusKU = "Buruk"
    print(segitiga(TK, var1[1][0], var1[1][1], var1[1][2]))
    NA_KU = segitiga(TK, var1[1][0], var1[1][1], var1[1][2])
if(TK >= var1[2][0]) and (TK <= var1[2][2]):
    TKU = 3
    StatusKU = "Berbahaya"
    print(segitiga(TK, var1[2][0], var1[2][1], var1[2][2]))
    NA_KU = segitiga(TK, var1[2][0], var1[2][1], var1[2][2])

# Next Kadar Oksigen
if (OK >= var2[0][0]) and (OK <= var2[0][2]):
    TOK = 1
    StatusO2 = "Banyak"
    print(segitiga(OK, var2[0][0], var2[0][1], var2[0][2]))
    NA_O2 = segitiga(OK, var2[0][0], var2[0][1], var2[0][2])
if (OK >= var2[1][0]) and (OK <= var2[1][2]):
    TOK = 2
    StatusO2 = "Normal"
    print(segitiga(OK, var2[1][0], var2[1][1], var2[1][2]))
    NA_O2 = segitiga(OK, var2[1][0], var2[1][1], var2[1][2])
if (OK >= var2[2][0]) and (OK <= var2[2][2]):
    TOK = 3
    StatusO2 = "Sedikit"
    print(segitiga(OK, var2[2][0], var2[2][1], var2[2][2]))
    NA_O2 = segitiga(OK, var2[2][0], var2[2][1], var2[2][2])
# PR BUAT VARIABEL NA_KU, NA_O2 untuk resolve masalah persilangan

Sugeno = ((NA_KU * TK)+(NA_O2 * OK))/((NA_KU + NA_O2))


# Masuk ke rule
if (TKU == 1) and (TOK == 1):
    print("ZZZ" + " Tingkat Kebersihan Udara " + StatusKU +
          " Kadar Oksigen " + StatusO2 + " dengan Nilai Sugeno ")
elif(TKU == 1) and (TOK == 2):
    print("ZZZ" + " Tingkat Kebersihan Udara " + StatusKU +
          " Kadar Oksigen " + StatusO2 + " dengan Nilai Sugeno ")
elif(TKU == 1) and (TOK == 3):
    print("BEEPPOOP" + " Tingkat Kebersihan Udara " + StatusKU +
          " Kadar Oksigen " + StatusO2 + " dengan Nilai Sugeno ")
elif(TKU == 2) and (TOK == 1):
    print("ZZZ" + " Tingkat Kebersihan Udara " + StatusKU +
          " Kadar Oksigen " + StatusO2 + " dengan Nilai Sugeno ")
elif(TKU == 2) and (TOK == 2):
    print("BEEPPOOP" + " Tingkat Kebersihan Udara " + StatusKU +
          " Kadar Oksigen " + StatusO2 + " dengan Nilai Sugeno ")
elif(TKU == 2) and (TOK == 3):
    print("BEEPPOOP" + " Tingkat Kebersihan Udara " + StatusKU +
          " Kadar Oksigen " + StatusO2 + " dengan Nilai Sugeno ")
elif(TKU == 3) and (TOK == 1):
    print("BEEPPOOP" + " Tingkat Kebersihan Udara " + StatusKU +
          " Kadar Oksigen " + StatusO2 + " dengan Nilai Sugeno ")
elif(TKU == 3) and (TOK == 2):
    print("BEEPPOOP" + " Tingkat Kebersihan Udara " + StatusKU +
          " Kadar Oksigen " + StatusO2 + " dengan Nilai Sugeno ")
elif(TKU == 3) and (TOK == 3):
    print("BEEPPOOP" + " Tingkat Kebersihan Udara " + StatusKU +
          " Kadar Oksigen " + StatusO2 + " dengan Nilai Sugeno ")

print(Sugeno)
