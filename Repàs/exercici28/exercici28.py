import random

def aleatori(input1, input2):
    if input1 < input2:
        a = random.randint(input1, input2)
    else:
        a = random.randint(input2, input1)   
    return a