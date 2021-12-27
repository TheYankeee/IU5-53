import random

def gen_random(num_count, min, max):
    result = []
    for x in range(num_count):
        x=random.randint(min,max)
        result.append(x)
    return result