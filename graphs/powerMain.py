import matplotlib.pyplot as plt
import math as math


def calcolaW(nm, rpm):
    w = (nm * 2 * math.pi * rpm) / 60
    return w

def calcolaKw(nm, rpm):
    kw = calcolaW(nm, rpm) / 1000
    return kw

def calcolaCv(nm, rpm):
    cv = calcolaKw(nm, rpm) * 1.36
    return cv

def calcolaHp(nm, rpm):
    hp = calcolaCv(nm, rpm) * 1.0139
    return hp

def calcolaNm(w, rpm):
    nm = (60 * w) / (2 * math.pi * rpm)
    return nm

def calcolaKgm(w, rpm):
    kgm = calcolaNm(w, rpm) / 9.81
    return kgm



# line 1 points
x1 = [1,2,3]
y1 = [2,4,1]
# plotting the line 1 points 
plt.plot(x1, y1, label = "cv")

# line 2 points
x2 = [1,2,3]
y2 = [4,1,3]
# plotting the line 2 points 
plt.plot(x2, y2, label = "nm")

# naming the x axis
plt.xlabel('rpm')
# naming the y axis
plt.ylabel('cv / nm')
# giving a title to my graph
plt.title('Power Graph')

# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()