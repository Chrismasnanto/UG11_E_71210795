print("========Program Manipulasi String=======")
print("Pilihan Menu : ")
print("1. Hitung kata")
print("2. cek kata")
print("3. ubah kata")

opsi = input("Pilihan anda :")
kata = input("Masukkan sebuah kalimat/kata : ")
hasil = (kata.lower()) 

#opsi 1 

if opsi == '1':
    a = input("Masukkan kata  yang inngin dihitung : ")
    z = hasil.count(a)
    print("Terdapat sebanyak", z , "kata" , a , "didalam string")

#opsi 2

if opsi == '2':
    a = input("Masukkan kata yang ingin dicek : ")
    b = a.upper()
    y = hasil.replace(a,b)

    print("Kata" , a , "terdapat didalam string")
    print("stirng diubah menjadi : ")
    print(y)

#opsi 3

if opsi == '3':
    a = input("Masukkan kata yang ingin diubah : ")
    c = input("Masukan kata pengganti : ")

    print("Anda akan mengubah kata" , a , "menjadi" , c , "sebanyak 1x")
    ubah = input("Apakah anda ingin mengubah jumlah  total penggantian kata ? (yes/no) : ")

    if ubah == 'yes' :
        x = int(input("Masukkan jumlah total penggantian : "))
        print("String berhasil diubah menjadi : ")
        y = hasil.replace(a , c , x)
        
    elif ubah == 'no' :
        x = 1
        print("String berhasil diubah menjadi : ")
        y = hasil.replace(a , c , x)
        print(y)
