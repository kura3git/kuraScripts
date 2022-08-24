from hashlib import new
import sys
from tracemalloc import start
from xml.etree.ElementPath import prepare_child
import termcolor
from termcolor import colored, cprint
from pyfiglet import Figlet
import pyinputplus as pyip
from datetime import datetime
import time
import numpy as np
import os


## declare variables
# line break
newline = '\n'

# date
now = datetime.now()

#restaurant 
var_place = 'Flavor Factory'

# separator 
rose = "\N{rose}"
def rose_break():
    print(rose*5)

dollars = "\N{money with wings}"
def spend_break():
    print(dollars*5)

def get_dollars():
    global spend
    spend = int(input(f"How much do you have to spend tonight?:{newline}"))
    print(f"Excellent, ${spend} is the perfect amount for a romantic night ;)")

# welcome message
def welcome_message(g1='sir', g2='madam'):
    print(f"Good evening {g1} and {g2}!{newline}We're honored that you can join us \
this evening{newline}at the {var_place}")

# list of feelings
moods=['excited', 'nervous', 'surprised', 'happy', 'hungry', 'mehh']
moods_after=['']

class Eats:
    """details foods"""
    def __init__(self,name,price):
        self.price=int(price)
        self.name=str(name)

class Appetizers(Eats):
    """details for apps"""
    def __init__(self,name, price):
        Eats.__init__(self, name, price)
        self.shareable='yes'

class Mains(Eats):
    """details for mains"""
    def __init__(self, name, price, temp=None):
        Eats.__init__(self, name, price)
        if temp is None:
            self.cooked=None
        else:
            self.cooked=temp

class Sides(Eats):
    """details for apps"""
    def __init__(self,name, price):
        Eats.__init__(self, name, price)
        self.shareable='yes'

class Dessert(Eats):
    """details for sweets"""
    def __init__(self, name, price):
        Eats.__init__(self, name, price)

f = Figlet(font='isometric3',width=10)
print(colored(f.renderText("Date Night!"), "cyan"))
print(colored(f.renderText("At"), "white"))
print(colored(f.renderText("Flavor"), "cyan"))
print(colored(f.renderText('Factory'), "cyan"))

# # daters
p1=pyip.inputStr("Can I have name of the first guest? ", blank=False)
p2=pyip.inputStr("Can I have name of the second guest? ", blank=False)

os.system('clear')

rose_break()

# welcome the guests 
welcome_message(p1,p2)

rose_break()

p1feel=pyip.inputMenu(moods, prompt="How is out first guest feeling tonight? ",limit=2)
p2feel=pyip.inputMenu(moods, prompt="How is out other wonderful guest feeling tonight? ",limit=2)

if (p1feel == p2feel) & (p1feel != 'mehh') & (p2feel != 'mehh'):
    print(f"Both feeling {p1feel}, has to be a good sign yall on the same page!")
elif (p1feel == 'nervous') or (p2feel == 'nervous'):
    #print(newline)
    print(f"Only fair to be nervous on a this special {now:%A} night")
else:
    print(f"Wonderful, please follow me")


# menu
menu = {}
menu["appetizers"]=['spinach & artichoke dip', 'soup dumplings', 'charcuterie', 'edamame']
menu["entrees"]=['signature burger', 'branzino', 'pork chops', 'steak']
menu["sides"]=["broccoli", "mashed potatoes", "fries", "caesar salad"]
menu["desserts"]=['tres leches', 'pecan pie', 'cheesecake']

# prices
pricing = {}
pricing['appetizers'] = int(5) #10
pricing['entrees'] = int(25) #50
pricing['sides'] = int(7) #14
pricing['desserts'] = int(5) #10

# how much you got
# def pocketCheck():
#     pockets = input("Will you two be interested fine dining or balling on a budget?: ")
#     print(f"Very good {pockets}!!")
#pocketCheck()

print(newline)

get_dollars()
spend_break()

print(newline)

#print(pricing[m] for m in pricing.keys())

# for m in menu.keys() & pricing.keys():
#     print(m, menu[m], pricing[m])

# for m,foods in menu.items():
#     print(f"Our {m} for tonight are: ")
#     for f in foods:
#         print(f'{f:<30}' f'{next(pricing[m] for m in pricing.keys()):>30}')

for m,foods in menu.items():
    print(f"Allow us to present the 5-star menu{newline}The {m} for tonight are: ")
    for f in foods:
        print(f'{f:<30}' f'{"$":>3}' f'{pricing[m]:>3}')


def take_order(prompt, sequence):
    return pyip.inputMenu(sequence, prompt=prompt)

startorder=take_order("what would you like to start with: ", menu['appetizers'])
#print(f"Perfect! the {startorder} is always a top choice")
mainorder=take_order("what would you like as the main course: ", menu['entrees'])
sideorder=take_order("Any sides?: ", menu['sides'])
lastorder=take_order("And to end your meal?: ", menu['desserts'])

os.system('clear')
print(f"And what do you want for your meal {p2}? ")

# 2nd order
startorder2=take_order("what would you like to start with: ", menu['appetizers'])
#print(f"Perfect! the {startorder} is always a top choice")
mainorder2=take_order("what would you like as the main course: ", menu['entrees'])
sideorder2=take_order("Any sides?: ", menu['sides'])
lastorder2=take_order("And to end your meal?: ", menu['desserts'])

cooking=colored("Chef is cheffing....", 'magenta', "on_white", attrs=['blink'])
print(cooking)
time.sleep(2.5)
served=colored("Food is served. Buen provecho!", 'magenta', 'on_white', attrs=['blink'])
print(served)
time.sleep(2.5)

# make Eats child classes
p1_app=Appetizers(startorder, pricing['appetizers'])
p2_app=Appetizers(startorder2, pricing['appetizers'])

p1_main=Mains(mainorder, pricing['entrees'])
p2_main=Mains(mainorder, pricing['entrees'])

p1_side=Sides(sideorder, pricing['sides'])
p2_side=Sides(sideorder, pricing['sides'])

p1_last=Dessert(sideorder, pricing['sides'])
p2_last=Dessert(sideorder, pricing['sides'])

all_eats = [p1_app, p2_app, p1_main, p2_main, p1_side, p2_side, p1_last, p2_last]
totalcost = sum([eat.price for eat in all_eats])

def endofDate():
    if spend > totalcost:
        return f"the bill for tonights meal is {totalcost}{newline}you have {spend - totalcost} left for the after party"
    elif spend == totalcost:
        return f"the bill for tonights meal is {totalcost}{newline}you have {spend - totalcost} left to get home. Great night for a walk!"
    else:
        return f"the bill for tonights meal is {totalcost}{newline}you are short {totalcost - spend}. Lucky you we take credit cards\
        venmo and cash app"

endMessage = endofDate()
print(endMessage)

p1feeltwo=pyip.inputStr(prompt="What did you think of your date? you can be honest - ")
#p2feeltwo=pyip.inputStr(prompt="What did you think of your date? you can be honest - ")

prob_bored, prob_2nd = 0.25, {'fun':0.80, 'bored':0.30}
def date_outcome(prob_bored):
    vibe=np.random.choice(['bored','fun'], p=[prob_bored, 1-prob_bored])
    if vibe == 'fun':
        date2_prob = prob_2nd[vibe], 1-prob_2nd[vibe]
    else:
        date2_prob = 1-prob_2nd[vibe], prob_2nd[vibe]
    date_result = np.random.choice(['See you soon!', 'See you never'], p=date2_prob)
    return date_result

result=date_outcome(prob_bored)
print(newline)
print(f"Will there be a second date???")

f = Figlet(font='isometric2', width=8)
finalwords=result.split()

print(colored("Your date responds...", 'yellow', attrs=['blink']))
time.sleep(1.5)
print(colored(f.renderText(finalwords[0]), color='green'))
print(colored(f.renderText(finalwords[1]), color='green'))
print(colored(f.renderText(finalwords[2]), color='green'))