def sifreleme():        
    import random
    alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm' \
          ,'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'y', 'z']
    kural = random.sample(alfabe,len(alfabe))
    #shuffle modülü sadece ekrana yazdırırken, sample methodu geri dönüş degeri verir.
    or_txt= input("Lütfen sifrelenecek metni giriniz: \n")
    #original_text
   
    new_txt = list()
    for i in range(0,len(or_txt)):
        
        # orijinal metindeki harflerin alfabede kaçıncı sırada oldugunu bulur.
        # bu buldugu degeri de sifreleme kuralının bulundugu kural degiskeninin
        # icinde, ilgili indexde hangi harfin bulundugunu ceker. Sonrasında ise
        # bu degeri new_txt adındaki bos listeye ekler. 
        new_txt.append(kural[alfabe.index(or_txt[i])])

    return new_txt

def cozme():
    import random
    alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm' \
          ,'n', 'o', 'p', 'r', 's', 't', 'u', 'v', 'y', 'z']
    kural = random.sample(alfabe,len(alfabe))

    cry_txt= input("Lütfen sifrelenmis metni giriniz: \n")
    #crypted text

    uncry_txt = list()
    # uncrypted text
    
    for i in range(0,len(cry_txt)):
    ##sifrelenmis metnin harflerinin, sifreleme kuralı olusturan listedeki yeri bulunur.
    ##Orijinal alfabede o yerlere karsılık gelen harfler cekilir ve yeni bos listeye eklenir. 
        uncry_txt.append(alfabe[kural.index(cry_txt[i])])

    return  uncry_txt
    
            


        

        

    
    
    
