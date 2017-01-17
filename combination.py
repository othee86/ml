from itertools import combinations_with_replacement
import numpy as np

AVERAGE_COUNT = 10
COMBINATION_COUNT = 15
SEED = 0

def Horse():
    return max(0, np.random.normal(5,2,1)[0])

def Ball():
    return max(0, 1 + np.random.normal(1,0.3,1)[0])

def Bike():
    return max(0, np.random.normal(20,10,1)[0])

def Train():
    return max(0, np.random.normal(10,5,1)[0])

def Coal():
    return 47 * np.random.beta(0.5,0.5,1)[0]

def Book():
    return np.random.chisquare(2,1)[0]

def Doll():
    return np.random.gamma(5,1,1)[0]

def Blocks():
    return np.random.triangular(5,10,20,1)[0]

def Gloves():
    return 3.0 + np.random.rand(1)[0] if np.random.rand(1) < 0.3 else np.random.rand(1)[0]

def get_weight(gift_type):
    if gift_type == "horse": return Horse()
    elif gift_type == "book": return Book()
    elif gift_type == "bike": return Bike()
    elif gift_type == "train": return Train()
    elif gift_type == "coal": return Coal()
    elif gift_type == "doll": return Doll()
    elif gift_type == "ball": return Ball()
    elif gift_type == "blocks": return Blocks()
    elif gift_type == "gloves": return Gloves()
    else:
        assert False, ("Unknown Gift Type Found! (%s)" % gift_type)

def get_bag_weight(bag):
    weight = []
    for i in range(0, AVERAGE_COUNT):
        total = 0
        for item in bag:
            total += get_weight(item)
        weight.append(total)
    return np.asarray(weight)

np.random.seed(SEED)
presents = ['horse', 'book', 'bike', 'train', 'coal', 'doll', 'ball', 'blocks', 'gloves']
file = open("combination.txt", 'w')

with open("combination.txt", 'w') as file:

    for i in range(3, COMBINATION_COUNT):
        count = 0
        for bag in combinations_with_replacement(presents, i):
            file.write(str(np.mean(get_bag_weight(bag))))
            file.write(" ")
            file.write(str(np.std(get_bag_weight(bag))))
            for item in bag:
                file.write(" " + str(item))
            file.write("\n")
            count += 1

        print("Total Combinations = " + str(count))


