import random
#import matplotlib.pyplot as plt

def init_xy(list,n): #### nの数分、ランダムな座標を取りだす
    i = 0
    while i < n:
       list.append([random.uniform(-5,5),random.random()])
       i += 1

#def plotran():
#    x, y = zip(*xylist)
#    plt.scatter(x, y)
#    plt.show()


def ichi():
    for row in range(len(xylist)):
        for cow in range(len(xylist[row])):
            print(xylist[row][cow])


def san():
    san=0
    for row in range(len(xylist)):
#        print(xylist[row][0])
        xi1 = san*san
        san = xi1 + (xylist[row][0])
#        print(xi)
#        return(xylist[row][0])
    print(san)


def yon():
    yon=0
    for row in range(len(xylist)):
        yon = yon + (xylist[row][0])
        yon = yon * yon / n
    print(yon)



#def yi():
#    for row in range(len(xylist)):
#        print(xylist[row][1])
#        return(xylist[row][1])


#def xiyi():
#    for row in range(len(xylist)):
#        for cow in range(len(xylist[row])):
#            print(xylist[row][cow])
#            return(xylist[row][cow])









if __name__ == "__main__":
    n = 10
    xylist = []
    init_xy(xylist,n)
    print(xylist)
    san()
    yon()
#    yi()
#    xiyi()
