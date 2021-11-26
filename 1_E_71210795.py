print("Menu program yang Tersedia")
print("1. pangkatkan angka")
print("2. akarkan bilangan")

#penyelesaian
#pil
pil = int(input("Masukkan pilihan yang diinginkan : "))
def pangkat_Angka():
    print("Masukkan angka yang ingin dipangkatkan")
    bil = (float(input("Angka : ")))
    print("Ingin memodifikasi pangkat ? (yes/no) ")
    b = input (": ")
    if b == "yes" :
        pangkat = float(input("Masukkan nilai pangkat : "))
        r = float(bil**pangkat)
        print("Hasil dari (0)^(1) = ".format(bil,pangkat), r)
    else:
        r = (bil**2)
        print("Hasil dari (0)^(1) = ".format(bil), r)
 
def akar_Bilangan():
     bil = (float(input("angka : ")))
     print("ingin memodifikasi pangkat ? (yes/no) ")
     b = input(": ")
     if b == "yes":
         akar = float(input("Masukkan nilai akar : "))
         r = float(bil**(1/akar))
         print("Hasil akar pangkat (0) dari (1) = ".format(akar,bil), r)
     else:
        r = (bil**0.5)
        print("Hasil akar pangkat 2 dari (0) = ".format(bil), round(r, 2))

if pil == 1:
    pangkat_Angka()
elif pil == 2:
    akar_Bilangan()
else: 
    print("-")
