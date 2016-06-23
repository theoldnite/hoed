import random
while True:
    d='ya'
    dot0=0
    try:
        dot0=int(input())
        if dot0>=1000:
            d="ay"
    except ValueError:
        d="ay"
    dot2=[]
    dot1=str(dot0)

    for i in range(0,len(dot1)):
        dot2.append(dot1[i])

    def lengte():
        lng= ['zero','one','two','three','four','five','six','seven','eight','nine']
        lng2=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
        lng3=['zero','ten','twenty','thirty','fourthy','fifthy','sixty','seventy','eighty','ninety']
        if len(dot1) == 1:
            print(lng[int(dot2[0])])
        if len(dot1) == 2:
            if int(dot2[0])==1:
                print(lng2[int(dot2[1])])
            elif int(dot2[1])==0:
                print(lng3[int(dot2[0])])
            else:
                print(lng3[int(dot2[0])]+'-'+lng[int(dot2[1])])
        if len(dot1) == 3:
            if   int(dot2[1])==1:
                print(lng[int(dot2[0])]+'hundred'+'-'+lng2[int(dot2[1])])
            elif int(dot2[2])==0 and int(dot2[1])==0:
                print(lng[int(dot2[0])]+'hundred')
            elif int(dot2[2])==0:
                print(lng[int(dot2[0])]+'hundred'+'-'+lng3[int(dot2[1])])
            else:
                print(lng[int(dot2[0])]+'hundred'+'-'+lng3[int(dot2[1])]+lng[int(dot2[2])])
    
    if d!='ay':
        lengte()
    else:
        print('number must be under 1000')

