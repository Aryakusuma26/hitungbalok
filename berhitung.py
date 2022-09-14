print('program menghitung\n1.luas,\n2. volume\n3.luas_kubus')
pilihan = int(input('masukan pilihan')) 

def luas_permukaan (p,l,t):
    L = 2 * ((p*l) + (p*t) + (l*t))
    return L

def volume (p,l,t):
    V = p*l*t
    return V

if pilihan == 1 :
    p = int(input('masukan panjang balok : '))
    l = int(input('masukan lebar balok : '))
    t = int(input('masukan tinggi balok : ' ))
    luas_permukaan (p,l,t)
    print('jika balok dengan ukuran panjang :{}, lebar:{} , tinggi:{}\nmempunyai luas:{}'. format(p,l,t, luas_permukaan(p,l,t)))

elif pilihan == 2 :
    p = int(input('masukan panjang balok : '))
    l = int(input('masukan lebar balok : '))
    t = int(input('masukan tinggi balok : ' ))
    volume (p,l,t)
    print('jika balok dengan ukuran panjang :{}, lebar:{} , tinggi:{}\nmempunyai volume:{}'. format(p,l,t,volume(p,l,t)))

if pilihan == 3 :
        print("program perhitungan kubus")
        sisi =float(input("masukan sisi : "))
        hasil = sisi*sisi*sisi
        print("volume kubus adalah :"+str(hasil)) 



