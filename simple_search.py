import numpy as np
import copy

TOLERANCE_MAX = 52.0
TOLERANCE_AVR = 32.5
SEED = 2

class Bag:
    def __init__(self, mean, std, items):
        self.mean = mean
        self.std = std
        self.items = items

np.random.seed(SEED)

horse = np.arange(1000)
ball = np.arange(1100)
bike = np.arange(500)
train = np.arange(1000)
coal = np.arange(166)
book = np.arange(1200)
doll = np.arange(1000)
blocks = np.arange(1000)
gloves = np.arange(200)

np.random.shuffle(horse)
np.random.shuffle(ball)
np.random.shuffle(bike)
np.random.shuffle(train)
np.random.shuffle(coal)
np.random.shuffle(book)
np.random.shuffle(doll)
np.random.shuffle(blocks)
np.random.shuffle(gloves)




good_bags = []


with open("combination.txt", 'r') as file:
    lines = file.readlines()
    for items in lines:
        data = items.split()
        if float(data[0])+float(data[1]) < TOLERANCE_MAX and float(data[0]) > TOLERANCE_AVR:
            good_bags.append(Bag(data[0], data[1], data[2:]))
print(len(good_bags))


def get_item(gift_type, num):
    if gift_type == "horse": return "%d" % horse[num]
    elif gift_type == "book": return "%d" % book[num]
    elif gift_type == "bike": return "%d" % bike[num]
    elif gift_type == "train": return "%d" % train[num]
    elif gift_type == "coal": return "%d" % coal[num]
    elif gift_type == "doll": return "%d" % doll[num]
    elif gift_type == "ball": return "%d" % ball[num]
    elif gift_type == "blocks": return "%d" % blocks[num]
    elif gift_type == "gloves": return "%d" % gloves[num]
    else:
        assert False, ("Unknown Gift Type Found! (%s)" % gift_type)

dict = {'horse': 0, 'book': 0, 'bike': 0, 'train': 0, 'coal': 0, 'doll': 0, 'ball': 0, 'blocks': 0, 'gloves': 0}
answer = []
with open("csv/answer.csv", 'w') as output:
    output.write("Gifts\n")
    for i in range(0, 1000):
        while True:
            try:
                str = ""
                temp_dict = copy.deepcopy(dict)
                for item in good_bags[np.random.random_integers(0, len(good_bags)-1)].items:
                    str += item
                    str += "_"
                    str += get_item(item, temp_dict[item])
                    str += " "
                    temp_dict[item] += 1
                str += "\n"
                output.write(str)
                dict = copy.deepcopy(temp_dict)
                break
            except:
                pass


