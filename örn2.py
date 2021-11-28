def Sezar_sifreleme():
    import math
    unc_txt=input("Lütfen sifrelenecek metni giriniz: \n")
    #uncrypted text
    n = math.ceil(math.sqrt(len(unc_txt)))
    # matrisi belirlerken sifrelenecek metnin uzunluğunun kare kökü alınır. Sonuc
    # tam sayı ise aynı kalır, eğer değilse bir üste yuvarlanır.
    emp = []
    for y in range(n):
        emp.append([])
    #creates empty matrix
   
    i = 0  
    for k in range(len(unc_txt)):
        (emp[i]).append(unc_txt[k])
        i+=1
        if i == n:
            i=0
            continue
    # istenilen matris yapısını elde etmek için bu döngüyü oluşturdum
   
    
    result=list()
    for j in range(n):
        result += emp[j] 
##    emp matrisinin icinde dikey olarak yerlestirilmis harfleri yatay olarak
##    sırayla okur ve result degiskenine atar.       

    result = "".join(result)
##    istedigimiz sifrelenmis metni elde ederiz.

    return result

def Sezar_cozme():
    import math
    cry_txt = input("Lutfen sifrelenmis metni giriniz: \n")
##    crypted text
    n = math.ceil(math.sqrt(len(cry_txt)))
##    sifrelenmis metnin kaca kaclık bir matrise yerlestirildigini ogrenmemizi saglar.
    
    extra = len(cry_txt)%n
##    matriste, belirlenen n degerine gore yerlestirilme yapıldıgında geriye kalan
##    harfleri bulmamızı saglar 
    full = len(cry_txt)//n 
##    n tane satırın tamamının dolu oldugu kolon sayısını gosterir

    emp = []
    for y in range(n):
        emp.append([])
    #creates empty matrix

    cry_txt = list(cry_txt)
##    cry_txt degiskenini liste haline getirdik. Boylece uzerinde degisiklik yapabiliriz.

    values = list()
    idx = list()
    for j in range(extra):
        idx.append( (full)*(j+1)+j )
        values.append( cry_txt[(full)*(j+1)+j] )

##    finds the values to be deleted
##    finds the indexes of the values to be deleted. 
    idx.sort(reverse=True)
##    cry_txt listesinin önce gelen elemanlarını cıkarırsak, o elemanlarn indexeri
##    hep degiseceği icin, once listenin en sonunda bulundan elemanları cıkarmalıyız.
    
    for ele in idx:
        del cry_txt[ele]

    cry_txt = "".join(cry_txt)
##    liste tipinden, tekrardan string tipine ceviririz.
 
    i = 0    
    for k in range(len(cry_txt)):
        (emp[i]).append(cry_txt[k])
        i+=1
        if i == full:
            i = 0
            continue
    
##    bu dongu ile son kolondaki elemanlar haricindeki butun elemanları matrise yerlestirmis olduk    

    count = 0
    for val in range(-extra,0,1) :
        (emp[val]).append(values[count])
        count+=1

    result=list()
    for j in range(n):
        result += emp[j] 
##    listenin icinde yan yana bulunan listeleri tek bir listede toplar.

    result = "".join(result)
##    listedeki elemanları arasına "" ifadesini koyarak tek bir stringe ekler.
##    aradıgımız sonuc budur.

    return result
    
     
