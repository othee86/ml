
"""
This is Santa Uncertain Gifts Simulator
"""

import os
import numpy as np
import math
import random
import click

class Horse:
    def __init__(self, num):
        self.weight = max(0, np.random.normal(5,2,1)[0])
        self.name = 'horse_' + str(num)

class Ball:
    def __init__(self, num):
        self.weight = max(0, 1 + np.random.normal(1,0.3,1)[0])
        self.name = 'ball_' + str(num)

class Bike:
    def __init__(self, num):
        self.weight = max(0, np.random.normal(20,10,1)[0])
        self.name = 'bike_' + str(num)

class Train:
    def __init__(self, num):
        self.weight = max(0, np.random.normal(10,5,1)[0])
        self.name = 'train_' + str(num)
        
class Coal:
    def __init__(self, num):
        self.weight = 47 * np.random.beta(0.5,0.5,1)[0]
        self.name = 'coal_' + str(num)
        
class Book:
    def __init__(self, num):
        self.weight = np.random.chisquare(2,1)[0]
        self.name = "book_" + str(num)
        
class Doll:
    def __init__(self, num):
        self.weight = np.random.gamma(5,1,1)[0]
        self.name = "doll_" + str(num)

class Blocks:
    def __init__(self, num):
        self.weight = np.random.triangular(5,10,20,1)[0]
        self.name = "blocks_" + str(num)
        
class Gloves:
    def __init__(self, num):
        self.weight = 3.0 + np.random.rand(1)[0] if np.random.rand(1) < 0.3 else np.random.rand(1)[0]
        self.name = "gloves_" + str(num)

def InitGift(gift_id):
    try:
        (gift_type, gift_num) = gift_id.strip().split('_')
    except:
        return None

    if gift_type == "horse": return Horse(gift_num)
    elif gift_type == "book": return Book(gift_num)
    elif gift_type == "bike": return Bike(gift_num)
    elif gift_type == "train": return Train(gift_num)
    elif gift_type == "coal": return Coal(gift_num)
    elif gift_type == "doll": return Doll(gift_num)
    elif gift_type == "ball": return Ball(gift_num)
    elif gift_type == "blocks": return Blocks(gift_num)
    elif gift_type == "gloves": return Gloves(gift_num)
    else:
        assert False, ("Unknown Gift Type Found! (%s)" % gift_type)

class Sim:
    def __init__(self, seed):
        np.random.seed(seed)
        gifts_csv = open("csv/gifts.csv", "r")
        self.all_gifts = [InitGift(gift_id.strip()) for gift_id in gifts_csv]
        self.all_gifts = [gift for gift in self.all_gifts if gift is not None]
        gifts_csv.close()
        self.gifts = list()
        self.overweight_bags = list()
        self.total_weight = 0
        for gift in self.all_gifts:
            self.total_weight = self.total_weight + gift.weight

    def Gift(self, gift_id):
        for idx, gift in enumerate(self.gifts):
            if gift.name == gift_id:
                return self.gifts.pop(idx)
        assert False, ("GiftId (%s) is not found!" % gift_id)

    def Submit(self, submission):
        self.gifts = list(self.all_gifts)
        if "csv" in submission:
            csv = open(submission, "r")
            bags = [line.strip() for line in csv]
            csv.close()
            bags = bags[1:] # remove the line with "Gitfs"
        else:
            bags = submission

        score = 0
        for bag in bags:
	    # RULE:
	    # No gift maybe used more than once
	    # gifts are pop by id hence there will not use the same gift more than once
            gifts_id = bag.split() # gifts are split by space
            gifts = [self.Gift(gift_id) for gift_id in gifts_id]

            # RULE:
	    # Every bag must have 3 or more gifts.
            if len(gifts) < 3:
                continue

            weight = 0
            for gift in gifts:
                weight = weight + gift.weight

            # RULE:
	    # Overfilling a bag above 50lb limit will cause the entire bag to count for nothing 
            if weight <= 50:
                score = score + weight
            else:
                self.overweight_bags.append(bag)

        return score

@click.command()
@click.option('--seed', default=0, help='Seed for Pseudo-Random')
@click.option('--file', default='csv/sample_submission.csv', help='file for submission')
def test_sim(seed, file):
    s = Sim(seed)
    score = s.Submit(file)

    print("SantaGiftBags Simulator:")
    print("  Submission  = %s" % file)
    print("  Seed        = %d" % seed)
    print("  TotalWeight = %lf" % s.total_weight)
    print("  Score       = %lf" % score)
    print("  Drop Bag Count = %d" % len(s.overweight_bags))

if __name__ == '__main__':
    test_sim()

