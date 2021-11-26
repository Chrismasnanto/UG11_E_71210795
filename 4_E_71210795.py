#import random

print("=======Program test aritmatika dasar=======")
print("Pilihan level yang tersedia : ")
print("1. Easy")
print("2. Medium")
print("3. Hard")

def generate(tingkatan):
    tingkatan=input("Masukan tingkatan yang ingin anda coba : ",)

    if tingkatan == "1":
        ab = "random.randint(20,50)"
        bc = "random.randint(20,50)"
        operasi = ['+','-','/','*']
        x = "random.choice(operasi)"
        pertanyaan = str(ab)+str(x)+str(bc) 
        print("Berapakah hasil dari",pertanyaan,"?")
        jawaban= float(input("Masukan Jawaban Anda : "))
        if jawaban == round(eval(pertanyaan),3):
            print("Jawaban Anda Benar ! ")
        else:
            print("Jawaban Anda Masih Salah")
        return round(eval(pertanyaan),3), pertanyaan

    elif tingkatan == "2":
        ax = "random.randint(20,70)"
        bz = "random.randint(20,70)"
        cy = "random.randint(20,70)"
        operasi = ['+','-','/','*']
        xa = "random.choice(operasi)"
        yz = "random.choice(operasi)"
        
        
        pertanyaan = str(ax)+str(xa)+str(bz)+str(yz)+str(cy) 
        print("Berapakah hasil dari",pertanyaan,"?")
        jawaban= float(input("Masukan Jawaban Anda : "))
        if jawaban == round(eval(pertanyaan),3):
            print("Jawaban Anda Benar ! ")
        else:
            print("Jawaban Anda Masih Salah")
        
        return round(eval(pertanyaan),3), pertanyaan
    

    elif tingkatan == "3":
        ab = "random.randint(20,100)"
        bc = "random.randint(20,100)"
        cd = "random.randint(20,100)"
        db = "random.randint(20,100)"
        operasi = ['+','-','/','*']
        x = "random.choice(operasi)"
        y = "random.choice(operasi)"
        z = "random.choice(operasi)"
        pertanyaan = str(ab) +str(x) +str(bc) +str(y) +str(cd)+str(z)+str(db)
        print("Berapakah hasil dari",pertanyaan,"?")
        jawaban= float(input("Masukan Jawaban Anda : "))
        if jawaban == round(eval(pertanyaan),3):
            print("Jawaban Anda Benar ! ")
        else:
            print("Jawaban Anda Masih Salah")
        
        return round(eval(pertanyaan),3), pertanyaan

def cekHasil():
    x,y =generate(tingkatan=input)
    print("Hasil dari",y,"=",x)
cekHasil()