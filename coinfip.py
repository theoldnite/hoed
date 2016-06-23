import random,time
#spelen met rng vind ik wel leuk
def Coin():
    d = random.randint(1,2)
    if d == 1:
        coin = 'heads'
    else:
        coin = 'tails'
    return coin
longestFlip=[]
rollTimes=0
highestflip=0
#for i in range(0,1000):
print('inside loop')
while True:
    coin = Coin()
    rollTimes+=1
    flipTimes=1
    if rollTimes % 10000000 == 0:
                print('uh ',rollTimes)
    while True:
        if coin == Coin():
            flipTimes+=1
            #print('hazaa ',rollTimes, ' ', flipTimes)
            if flipTimes>highestflip:
                highestflip = flipTimes
                print('ay ay ',flipTimes,'its ',coin, ' and ',rollTimes,' rolls ')
        else:
            #print('nope')
            break
print('outside loop')
