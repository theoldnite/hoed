#ik heb dit gemaakt om te kijken wat het volgende was
#g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
#K = M
#O = Q
#E = G
import random,string
Alpha = list(string.ascii_lowercase)
while True:
    ltr1 =int(Alpha.index(str(input('letter 1:')).lower()))
    ltr2 =int(Alpha.index(str(input('letter 1 equals::')).lower()))
    if ltr1!=ltr2 and Alpha[ltr1] and Alpha[ltr1]:
        if ltr1 > ltr2:
            ltr3=int(ltr2-ltr1)
        elif ltr2 > ltr1:
            ltr3=int(ltr2-ltr1)
        break

txt=[]
text=list(str(input("sentence to decode:")).lower())
for i in range(0,len(text)):
    txt.append(text[i])

ant=[]
for i in range(0,len(txt)):
    if txt[i] in Alpha:
        lengte=Alpha.index(txt[i])+ltr3
        if lengte>25:
            lengte=lengte-len(Alpha)
            ant.append(Alpha[lengte])
        elif lengte<=0:
            lengte=lengte+26
            ant.append(Alpha[lengte])
        else:
            ant.append(Alpha[lengte])
    else:
        ant.append(txt[i])
print(''.join(ant))

