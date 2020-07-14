import random
import matplotlib.pyplot as plt

def listcreator(): # This creates a list of 13 random cards. 
                   # This list could be one person's hand or the distribution of one suit
                   # 0, 1, 2, 3 can represent Player 1, P2, P3, P4, or Diamonds, Clubs, Hearts, Spades
  mylist = [0]*13
  for x in range(13):
    mylist[x] = random.randint(1,4)
  return mylist

def listmaker(num):
  midlist = []
  while num > 0: #call as many as needed. Default is 5000, edit below
    a = listcreator()
    sumlist = [0]*4
    for x in range(4):
      sumlist[x] = a.count(x+1) # This takes your list of 13 cards and turns it into a 4 number list, made of the number of zeroes, ones, twos, and threes.
    sumlist.sort(reverse=True) # Sorts highest to lowest. This ignores nuances of which suit/player, only looks at the total numbers
    midlist.append(sumlist) # Now we have midlist, a list consisting of num amount of lists. Each list within has four numbers, highest to lowest, summing to 13
    num = num-1

  return midlist

def datamaker(finlist):
  finallist = []
  for elem in finlist:
    y = (1000 * int(elem[0]) + 100 * int(elem[1]) + 10 * int(elem[2]) + int(elem[3])) # For example, [8,2,2,1] becomes 8221, et cetera. Note that [11, 2, 0, 0] becomes 5 digits, 11200. Doesn't matter.
    finallist.append(y)
  finallist.sort(reverse=True)
  return finallist # Finallist consists of midlist turned into a list of num amount of 4 or 5 digits numbers. THe four digiters sum to 13, the five digiters do if we take the first two digits as a two digit number

#autopct_generator and get_new_labels do the same thing. However, the former is for the chart values, the latter for labels
def autopct_generator(limit):
    def inner_autopct(pct):
        return ('%.2f' % pct) if pct > limit else ''
    return inner_autopct

def get_new_labels(sizes, labels):
    i = 0
    new_labels = [0] * 39
    while i < 39:
      if sizes[i] > minpercent:
        new_labels[i] = labels[i]
      else:
        new_labels[i] = ""
      i = i + 1
    return new_labels


def datasort(data):
  moneylist = [0]*39 
  # Moneylist will consist of the amount of times each possibility actually appears in finallist.
  goodlist = [13000, 12100, 11200, 11110, 10300,10210,10111,9400,9310,9220,9211,8500,8410,8320,8311,8221,7600,7510,7420,7411,7330,7321,7222,6610,6520,6511,6430,6421,6331,6322,5530,5521,5440,5431,5422,5332,4441,4432,4333]
  # Goodlist has all of the possibilities
  for x in range(39):
    moneylist[x] = data.count(goodlist[x]) #This line turns Moneylist into a parallel list to Goodlist. Each element in Goodlist appears some quantity of times in Finallist, which can be found by taking the same index in Moneylist 
    print("The amount of " + str(goodlist[x]) + " is " + str(moneylist[x]) + ", and the percent is " + str(float(100*moneylist[x]/numtries)))
  sizes = [(100 * x / numtries) for x in moneylist]
  labels = goodlist
  #Creating variables 'labels' and 'sizes' is unnecessary, as they are the same as moneylist and goodlist, respectively. However, they serve different goals, as labels and sizes are for plotting, moneylist and goodlist are for math. So, I use different variables
  sizes, labels = (list(t) for t in zip(*sorted(zip(sizes, labels)))) 
  #Classic Python parallel list Zip Sort. More info at tinyurl.com/zipsort
  fig1, ax1 = plt.subplots()
  ax1.pie(sizes, labels=get_new_labels(sizes, labels), autopct=autopct_generator(minpercent), shadow=True, startangle=90)
  ax1.axis('equal')  
  plt.show() #normal matplotlib stuff

numtries = 5000 # Number of tried you want. More accurate with more tries
minpercent = 2.5 # Percentage minimum for a label on the graph. If too low, graph becomes disgusting
#Note: Conditionally removing graph labels on a pie chart is surprisingly annoying in matplotlib
shmu = listmaker(numtries)
pizza = datamaker(shmu)
datasort(pizza)
