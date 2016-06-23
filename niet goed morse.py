#heel oud
import random
Morse = ['._','_...','_._.','_..','.','.._.','__.','....','..','.___','_._','._..',"__","_.",'___',".__.","__._",'._.','...','_','.._','..._','.__','_.._','_.__','__..']
Letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
while True:
    woord = []
    z = str(input('')).lower()
    for i in range(0,len(z)):
        if z[i] in Letters:
           d = Letters.index(z[i])
           print("letter ",(i+1)," = ",Morse[d])
           woord.append(Morse[d])
    break


