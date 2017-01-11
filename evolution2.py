import os
import numpy as np
import math
import random
import pandas
import copy

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)


print("Start")



def get_weight(item_number):
    if 2 <= item_number <= 1001 :  # house 1000
        return max(0, np.random.normal(5, 2, 10)[0])
    elif 1002 <= item_number <= 2101:  # ball 1100
        return max(0, 1 + np.random.normal(1, 0.3, 1)[0])
    elif 2102 <= item_number <= 2601:  # bike 500
        return max(0, np.random.normal(20, 10, 1)[0])
    elif 2602 <= item_number <= 3601:  # train 1000
        return max(0, np.random.normal(10, 5, 1)[0])
    elif 3602 <= item_number <= 3767:  # coal 163
        return 47 * np.random.beta(0.5, 0.5, 1)[0]
    elif 3768<= item_number <= 4967:  # book 1200
        return np.random.chisquare(2, 1)[0]
    elif 4968 <= item_number <= 5967:  # doll 1000
        return np.random.gamma(5, 1, 1)[0]
    elif 5968 <= item_number <= 6967:  # block 1000
        return np.random.triangular(5, 10, 20, 1)[0]
    elif 6968 <= item_number <= 7167:  # gloves 200
        return 3.0 + np.random.rand(1)[0] if np.random.rand(1) < 0.3 else np.random.rand(1)[0]
    else:
        print("ERROR ITEM NUMBER %d!!" % item_number)
        return 0


def convert_gift_name_to_number(gift_name):
    [name, number] = gift_name.split("_")
    number = int(number)
    if (name == "horse"):   # house 1000
        return number + 2
    elif (name == "ball"):   # ball 1100
        return number + 1002
    elif (name == "bike"):   # bike 500
        return number + 2102
    elif (name == "train"):   # train 1000
        return number + 2602
    elif (name == "coal"):   # coal 163
        return number + 3602
    elif (name == "book"):   # book 1200
        return number + 3768
    elif (name == "doll"):   # doll 1000
        return number + 4968
    elif (name == "blocks"):   # block 1000
        return number + 5968
    elif (name == "gloves"):   # gloves 200
        return number + 6968
    else:
        print("ERROR INPUT: %s !!" % name)
        return 0
        
        
        
def string_graph(input_in_percent, number_of_character=40, got_negative = True, white_symbol = "#", black_symbol = "_"):
    
    if got_negative == True:
        number_of_character /= 2
        length = min(100.0,max(-100.0,input_in_percent)) / 100
        if (input_in_percent < 0):
            length = -length
            black = black_symbol * int(round((1-length)*number_of_character))
            white = white_symbol * int(round(length*number_of_character))
            fill = black_symbol * int(number_of_character)
            return (black + white + "|" + fill)
        else:
            black = black_symbol * int(round((1-length)*number_of_character))
            white = white_symbol * int(round(length*number_of_character))
            fill = black_symbol * int(number_of_character)
            return (fill + "|" + white + black)
            
        
#GLOBAL
best_individual_fitness = 0 
        
item_weight = []

for i in range(2, 7168):
    item_weight.append(get_weight(i))
 
    

class Box:
    def __init__(self):
        self.weight = 0
        self.score = 0
        self.overweight = 0
        self.item = []
        self.debug = 0
    def add_item(self, gift_type):
        self.item.append(gift_type)
    def remove_random_item(self):
        if len(self.item) == 0: return 9999
        index = math.floor(random.random() * len(self.item))
        return self.item.pop(index)
    def calculate_total_weight(self, d=False):
        iteration = 1 
        w = 0.0
        self.overweight = 0
        for i in self.item:
            for j in range(iteration):
                # t = self.check_weight(i) 
                w += self.check_weight(i)
                # if d: (print("*******", t, self.item)) 
        self.weight = w / iteration
        if (self.weight <= 50) :  self.score = self.weight
        else :                    self.score = 0; self.overweight += 1
    '''# def calculate_total_weight(self):
        # iteration = 1
        # w = 0
        # self.score = 0
        # self.overweight = 0
        # for j in range(iteration):
            # for i in self.item:
                # w += self.check_weight(i)
            # self.weight = w
            # if (self.weight <= 50) :  self.score += self.weight
            # else: self.overweight += 1
        # self.score /= iteration
        '''
    def check_weight(self, item_number): 
        global item_weight
        # if (item_number == 4):  
            # print("=========", item_weight[item_number - 2])
        return item_weight[item_number - 2]
    def get_random_weight(self, item_number): # TODO: Need to fix these value for each generation
        if 2 <= item_number <= 1001 :  # house 1000
            return max(0, np.random.normal(5, 2, 10)[0])
        elif 1002 <= item_number <= 2101:  # ball 1100
            return max(0, 1 + np.random.normal(1, 0.3, 1)[0])
        elif 2102 <= item_number <= 2601:  # bike 500
            return max(0, np.random.normal(20, 10, 1)[0])
        elif 2602 <= item_number <= 3601:  # train 1000
            return max(0, np.random.normal(10, 5, 1)[0])
        elif 3602 <= item_number <= 3767:  # coal 163
            return 47 * np.random.beta(0.5, 0.5, 1)[0]
        elif 3768<= item_number <= 4967:  # book 1200
            return np.random.chisquare(2, 1)[0]
        elif 4968 <= item_number <= 5967:  # doll 1000
            return np.random.gamma(5, 1, 1)[0]
        elif 5968 <= item_number <= 6967:  # block 1000
            return np.random.triangular(5, 10, 20, 1)[0]
        elif 6968 <= item_number <= 7167:  # gloves 200
            return 3.0 + np.random.rand(1)[0] if np.random.rand(1) < 0.3 else np.random.rand(1)[0]
        else:
            print("ERROR !!")
            return 0
    def print(self):
        output = ""
        for i in self.item:
            output += self.get_name(i)
        output += "\n"
        return output
    def get_name(self, item_number):
        if 2 <= item_number <= 1001 :  # house 1000
            return "horse_%d " % (item_number - 2)
        elif 1002 <= item_number <= 2101:  # ball 1100
            return "ball_%d " % (item_number - 1002)
        elif 2102 <= item_number <= 2601:  # bike 500
            return "bike_%d " % (item_number - 2102)
        elif 2602 <= item_number <= 3601:  # train 1000
            return "train_%d " % (item_number - 2602)
        elif 3602 <= item_number <= 3767:  # coal 163
            return "coal_%d " % (item_number - 3602)
        elif 3768<= item_number <= 4967:  # book 1200
            return "book_%d " % (item_number - 3768)
        elif 4968 <= item_number <= 5967:  # doll 1000
            return "doll_%d " % (item_number - 4968)
        elif 5968 <= item_number <= 6967:  # block 1000
            return "blocks_%d " % (item_number - 5968)
        elif 6968 <= item_number <= 7167:  # gloves 200
            return "gloves_%d " % (item_number - 6968)
        else:
            print("ERROR !!")
            return "ERROR !!"

class Individual2():  
    def __init__(self):
        self.id = 0
        self.mutate_rate = 0.0
        self.generation = 0
        self.actual_fitness = 0
        self.fitness = 0
        self.best_fitness = 0
        self.number_of_overweight_before = 0
        self.number_of_overweight_after = 0
        self.box = []
        self.available_present_number = list(range(2, 7168))
        for i in range(1000):
            self.box.append(Box())
    def calculate_fitness(self, display = True):
        last_fitness = self.fitness
        self.fitness = 0
        self.number_of_overweight_after = 0
        for i in range(1000):
            self.box[i].calculate_total_weight()
            if (i == 3):  
                self.box[i].calculate_total_weight(True) 
                # print("")
                self.box[i].calculate_total_weight(True)
            if len(self.box[i].item) > 0 and self.box[i].score == 0:  # OVERWEIGHT !
                    self.number_of_overweight_after += 1
            self.fitness += self.box[i].score
            
            # if(i == 3):      
                # print("---------------: ", self.box[i].item) 
            
        # for i in self.box[3].item:
            # print("++++++++", i) 
        # print(">>>>>>>",self.box[4].score) 
        improvement = self.fitness - last_fitness
        global best_individual_fitness
        if (best_individual_fitness < self.fitness): best_individual_fitness = self.fitness
        if self.generation % 1 == 0 and display == True: 
            print("id: %2d gen: %5d  fit: %5d_%5d  imprvd: %5d  OW_b4: %2d  OW_aftr: %2d  gift_left: %4d" % (self.id, self.generation, best_individual_fitness, self.fitness, improvement, self.number_of_overweight_before, self.number_of_overweight_after, len(self.available_present_number)))
        return improvement
    def mutate(self,mutate_rate = 5):
        for j in range(int(self.mutate_rate)):
            add_or_remove = round(random.random())
            which_box = math.floor(random.random()*1000)
            if add_or_remove == 0 and len(self.available_present_number) > 0:
                self.box[which_box].add_item(self.get_gift())
            else:
                removed_item_number = self.box[which_box].remove_random_item()
                if removed_item_number != 9999:
                    self.return_gift(removed_item_number)
    def update(self):
        algorithm = 1
        self.generation += 1
        
        self.number_of_overweight_before = 0
        

        # CHOICE
        for i in range(1000):
            if len(self.box[i].item) > 0 and self.box[i].overweight >= 1:  # OVERWEIGHT !
                self.number_of_overweight_before += 1
                self.handle_overweight(i)
            elif self.box[i].score < 49.99 and len(self.available_present_number) > 0: # UNDERWEIGHT #(2000-self.generation)/50
                self.box[i].add_item(self.get_gift())

            if len(self.box[i].item) < 3: # UNDERCOUNT < 3
                for j in range(3 - len(self.box[i].item)):
                    if len(self.available_present_number) > 0:
                        self.box[i].add_item(self.get_gift())
    def remove_gift(self,gift_number):
        self.available_present_number.remove(gift_number)
    def get_gift(self):
        gift_index = math.floor(random.random()*len(self.available_present_number))
        # Swap with last one
        choosen_number = self.available_present_number[gift_index]
        self.available_present_number.pop(gift_index)
        return choosen_number
    def return_gift(self,removed_item_number):
        self.available_present_number.append(removed_item_number)
    def handle_overweight(self,which_box):
        # remove 1 item
        while (len(self.box[which_box].item) > 0 and self.box[which_box].overweight >= 1):
            removed_item_number = self.box[which_box].remove_random_item()
            if removed_item_number != 9999:
                self.return_gift(removed_item_number)
                #print(removed_item_number)
            else: print("ERROR #1 !")
            # if (self.generation >= 590): print(removed_item_number)
    '''# def #self.box[which_box].calculate_total_weight()
        #if len(self.box[which_box].item) > 0 and self.box[which_box].score == 0:
            #self.number_of_overweight_after += 1 
        '''
    def next_generation(self): 
        old_box = copy.deepcopy(self.box)
        # old_box = list(self.box)
        
        self.mutate_rate += 0.1
        if (self.generation % 20 == 0):
            self.mutate(10)
        self.update()
         
        improvement = self.calculate_fitness()
        
        if (self.best_fitness < self.fitness): 
            self.best_fitness = self.fitness
            self.mutate_rate = 0

        if improvement < 0:
            self.box = copy.deepcopy(old_box)
            
    def get_estimation_error(self):
        self.calculate_fitness(False)
        estimation_error = self.actual_fitness - self.fitness
        # print("-"*40, self.id, self.actual_fitness, self.fitness, estimation_error)
        return estimation_error 
        

class Individual(): 
    def __init__(self):
        self.generation = 0
        self.fitness = 0
        self.number_of_overweight_before = 0
        self.number_of_overweight_after = 0
        self.box = []
        self.available_present_number = list(range(2, 7168))
        for i in range(1000):
            self.box.append(Box())
    def calculate_fitness(self, display = True):
        last_fitness = self.fitness
        self.fitness = 0
        self.number_of_overweight_after = 0
        for i in range(1000):
            self.box[i].calculate_total_weight()
            if len(self.box[i].item) > 0 and self.box[i].score == 0:  # OVERWEIGHT !
                    self.number_of_overweight_after += 1
            self.fitness += self.box[i].score
        improvement = self.fitness - last_fitness
        global best_individual_fitness
        if (best_individual_fitness < self.fitness): best_individual_fitness = self.fitness
        if self.generation % 1 == 0 and display == True: 
            print("gen: %5d  fit: %5d_%5d  imprvd: %5d  OW_b4: %2d  OW_aftr: %2d  gift_left: %4d" % (self.generation, best_individual_fitness, self.fitness, improvement, self.number_of_overweight_before, self.number_of_overweight_after, len(self.available_present_number)))
        return improvement
    def update(self):
        mutate_rate = 5
        algorithm = 1
        self.generation += 1
        
        self.number_of_overweight_before = 0
        
        # MUTATION
        if (self.generation % 20 == 0):
            for i in range(mutate_rate):
                add_or_remove = round(random.random())
                which_box = math.floor(random.random()*1000)
                if add_or_remove == 0 and len(self.available_present_number) > 0:
                    self.box[which_box].add_item(self.get_gift())
                else:
                    removed_item_number = self.box[which_box].remove_random_item()
                    if removed_item_number != 9999:
                        self.return_gift(removed_item_number)
            
        # CHOICE
        for i in range(1000):
            if len(self.box[i].item) > 0 and self.box[i].overweight >= 1:  # OVERWEIGHT !
                self.number_of_overweight_before += 1
                self.handle_overweight(i)
            elif self.box[i].score < 49.9 and len(self.available_present_number) > 0: # UNDERWEIGHT #(2000-self.generation)/50
                self.box[i].add_item(self.get_gift())

            if len(self.box[i].item) < 3: # UNDERCOUNT < 3
                for j in range(3 - len(self.box[i].item)):
                    if len(self.available_present_number) > 0:
                        self.box[i].add_item(self.get_gift())
    def remove_gift(self,gift_number):
        self.available_present_number.remove(gift_number)
    def get_gift(self):
        gift_index = math.floor(random.random()*len(self.available_present_number))
        # Swap with last one
        choosen_number = self.available_present_number[gift_index]
        self.available_present_number.pop(gift_index)
        return choosen_number
    def return_gift(self,removed_item_number):
        self.available_present_number.append(removed_item_number)
    def handle_overweight(self,which_box):
        # remove 1 item
        #while (len(self.box[which_box].item) > 0 and self.box[which_box].score == 0):
        removed_item_number = self.box[which_box].remove_random_item()
        if removed_item_number != 9999:
            self.return_gift(removed_item_number)
            #print(removed_item_number)
        else: print("ERROR #1 !")
    '''# def #self.box[which_box].calculate_total_weight()
        #if len(self.box[which_box].item) > 0 and self.box[which_box].score == 0:
            #self.number_of_overweight_after += 1 
        '''
    def next_generation(self):
        old_box = self.box
        self.update()
        if self.calculate_fitness() < 0:
            self.box = old_box

    def get_estimation_error(self):
        self.calculate_fitness(False)
        estimation_error = self.actual_fitness - self.fitness
        # print("-"*40, self.id, self.actual_fitness, self.fitness, estimation_error)
        return estimation_error 
        
        
        
class world():
    def __init__(self):
        self.population = []
        self.generation = 0
        self.average_error = 0
        self.weight_estimation_difference = 0
        self.best_estimation_error = 99999
    def read_submission(self, path):
        print("Loading Submission....")
        files = os.listdir(path)
        for i in range(len(files)):
            filename = files[i]
            print("Loading %s  at  %s" % (filename, path))
            self.population.append(Individual())
            self.population[i].actual_fitness = float(filename[:-4])
            self.population[i].id = i
            
            csv = pandas.read_csv(path + "\\" + filename," ",names=["a","b","c","d","e","f","g","h","i","j","k","l"]).values.tolist()
            
            for g in range(1,1001):
                # if g in [1,121,558,988,1000]: print(" ")
                for item in csv[g]: 
                    if isinstance(item, str):
                        gift_number = convert_gift_name_to_number(item)
                        # if g in [1,121,558,988,1000]: print(item,gift_number)
                        self.population[i].box[g-1].add_item(gift_number) 
                        self.population[i].remove_gift(gift_number)
    def get_estimation_difference(self):
        self.average_error = 0
        for p in self.population:
            self.average_error += p.get_estimation_error()
        self.average_error /= len(self.population)
        graph_length = self.average_error / 5 
        if (self.best_estimation_error == 99999):
            if self.best_estimation_error > abs(self.average_error):
                self.best_estimation_error = abs(self.average_error)
        print(" Gen: %3d  Best: %11.5f  Error: %11.5f   %s" % (self.generation, self.best_estimation_error, self.average_error, string_graph(graph_length)))
    def re_estimation_item_weight(self):
        self.generation += 1
        mutate_rate = 10
        global item_weight
        # print("BEFORE: ", item_weight[1])
        previous_item_weight = copy.deepcopy(item_weight)
        previous_error = self.average_error
        # EVOLVE
        for i in range(2, 7168):    
            if 2 <= i <= 1001 :  # house 1000
                item_weight[i-2] = min(max(item_weight[i-2] + np.random.normal(0, 0.019, 1)[0],-3),13)
            elif 1002 <= i <= 2101:  # ball 1100
                item_weight[i-2] = min(max(item_weight[i-2] + np.random.normal(0, 0.003, 1)[0],-0.5),3.5)
            elif 2102 <= i <= 2601:  # bike 500
                item_weight[i-2] = min(max(item_weight[i-2] + np.random.normal(0, 0.098, 1)[0],-20),60)
            elif 2602 <= i <= 3601:  # train 1000
                item_weight[i-2] = min(max(item_weight[i-2] + np.random.normal(0, 0.048, 1)[0],-10),30)
            elif 3602 <= i <= 3767:  # coal 163
                item_weight[i-2] = min(max(item_weight[i-2] + np.random.normal(0, 0.16, 1)[0],-5),45)
            elif 3768<= i <= 4967:  # book 1200
                item_weight[i-2] = min(max(item_weight[i-2] + np.random.normal(0, 0.019, 1)[0],-3),10)
            elif 4968 <= i <= 5967:  # doll 1000
                item_weight[i-2] = min(max(item_weight[i-2] + np.random.normal(0, 0.022, 1)[0],-5),15)
            elif 5968 <= i <= 6967:  # block 1000
                item_weight[i-2] = min(max(item_weight[i-2] + np.random.normal(0, 0.031, 1)[0],3),23)
            elif 6968 <= i <= 7167:  # gloves 200
                item_weight[i-2] = min(max(item_weight[i-2] + np.random.normal(0, 0.014, 1)[0],0),4)
                if (1 < item_weight[i-2] < 2): item_weight[i-2] = 1
                if (2 < item_weight[i-2] < 3): item_weight[i-2] = 3
        
        if abs(previous_error) < abs(self.average_error):
            # MUTATE
            if (self.generation % 3 == 0):
                for i in range(mutate_rate):
                    index = math.floor(random.random() * (len(item_weight)))
                    item_weight[index] = get_weight(index+2)
        # print("AFTER: ", item_weight[1])
        
        
        self.get_estimation_difference()
        
        if self.best_estimation_error > abs(self.average_error):
            self.best_estimation_error = abs(self.average_error)
        else:
            item_weight = copy.deepcopy(previous_item_weight)
            # self.get_estimation_difference()
            # print("UNDO: ", item_weight[1])
            
        
w1 = world()
w1.read_submission(r"C:\Users\TattChee\PycharmProjects\santa_gift\submitted\standard_name")
# for i in range(100):
    # w1.re_estimation_item_weight()
 
i1 = Individual() 

def run_test(): 
    global best_individual_fitness
    global item_weight
    load_item_weight(r"item_weight_v2_5_0.txt")
    
    w1.get_estimation_difference()
    next_autosave_version("item_weight_", ".txt")
    for i in range(5000):
        if (w1.best_estimation_error > 5):
            w1.re_estimation_item_weight() 
            if ((i+1) % 10 == 0): save_item_weight()
            if self_destruct() == True:
                save_item_weight()  
                print(" ====> Updating...") 
                return False 
    w1.get_estimation_difference()
    save_item_weight(True)
    
     
    next_autosave_version()
    for i in range(6000):
        if (i1.fitness < 48500):
            i1.next_generation()
            if ((i+1) % 10 == 0): save_to_file()
            if self_destruct() == True:
                save_to_file() 
                print(" ====> Updating...") 
                return False 
    i1.calculate_fitness()  
     
    global save_filename 
    
    save_to_file(True)   
    
    print("END") 



manual_version = 5 # Setting
save_filename = r"submission_temp.csv"
def save_to_file(msg=False):
    global save_filename
    
    with open(save_filename, 'w+') as submission_file:
        submission_file.write('Gifts\n')
        for i in range(1000):
            submission_file.write(i1.box[i].print())
    if msg:
        print("Saved %s" % save_filename)

def save_item_weight(msg=False):
    global save_filename
    
    old = list(item_weight)
    with open(save_filename, 'w+') as sf:
        for i in range(2,7168):
            sf.write(str(item_weight[i-2]) + "\n")
    if msg:
        print("Saved %s" % save_filename)
    
def load_item_weight(path = r"starting_weight.txt"):
    global item_weight
    with open(path, 'r') as sf:
        for i in range(2,7168):
            # item_weight.append(float(sf.readline()))
            item_weight[i-2] = float(sf.readline())
            
def next_autosave_version(name = "submission_", format = ".csv"):
    global save_filename
    global manual_version 
    
    auto_save_version = 0
    n = "v2_%d_%d" % (manual_version, auto_save_version)
    save_filename = r"%s%s%s" % (name, n, format)
    while os.path.isfile(save_filename): 
        auto_save_version += 1 
        n = "v2_%d_%d" % (manual_version, auto_save_version)
        save_filename = r"%s%s%s" % (name, n, format)
    
            
last_save_time = os.path.getmtime("evolution2.py")
def self_destruct(): 
    global last_save_time
    current_save_time = os.path.getmtime("evolution2.py")
    return (current_save_time != last_save_time)
    
