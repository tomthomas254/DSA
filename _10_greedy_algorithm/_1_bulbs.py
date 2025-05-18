"""
Given N bulbs, either on (1) or off(0).
Turning on ith bulb causes all remaining bulbs  on the right to flip.

Find the min number of  switches to turn all the bulbs on.

naive solution: 
    time-O(n2)
    space - O(1)
optimized (below):
     time - O(n) 
     space - O(1)
"""

def bulbs(array):
    cost = 0 

    for bulb in array:
        if cost % 2 == 0:
            bulb = bulb
        else:
            bulb = not bulb
        
        if bulb % 2 == 1: continue
        else : cost += 1
    return cost