import random
import matplotlib.pyplot as plt

def listcreator():
  mylist = [0]*13
  for x in range(13):
    mylist[x] = random.randint(1,4)
  return mylist

def listmaker(num):
  midlist = []
  while num > 0:
    a = listcreator()
    sumlist = [0]*4
    for x in range(4):
      sumlist[x] = a.count(x+1)
    sumlist.sort(reverse=True)
    midlist.append(sumlist)
    num = num-1

  return midlist

def datamaker(finlist):
  finallist = []
  for elem in finlist:
    y = (1000 * int(elem[0]) + 100 * int(elem[1]) + 10 * int(elem[2]) + int(elem[3]))
    finallist.append(y)
  finallist.sort(reverse=True)
  return finallist

def datasort(data):
  moneylist = [0]*35
  goodlist = [10300,10210,10111,9400,9310,9220,9211,8500,8410,8320,8311,8221,7600,7510,7420,7411,7330,7321,7222,6610,6520,6511,6430,6421,6331,6322,5530,5521,5440,5431,5422,5332,4441,4432,4333]
  for x in range(35):
    moneylist[x] = data.count(goodlist[x])
    print("The amount of " + str(goodlist[x]) + " is " + str(moneylist[x]) + ", and the percent is " + str(float(100*moneylist[x]/numtries)))
  

numtries = 5000
shmu = listmaker(numtries)
pizza = datamaker(shmu)
datasort(pizza)
