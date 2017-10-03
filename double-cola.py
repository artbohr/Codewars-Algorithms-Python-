'''
Sheldon, Leonard, Penny, Rajesh and Howard are in the queue for a "Double Cola" drink vending machine; there are no other people in the queue. The first one in the queue (Sheldon) buys a can, drinks it and doubles! The resulting two Sheldons go to the end of the queue. Then the next in the queue (Leonard) buys a can, drinks it and gets to the end of the queue as two Leonards, and so on.

For example, Penny drinks the third can of cola and the queue will look like this:

Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard, Penny, Penny

Write a program that will return the name of a man who will drink the n-th cola.

Note that in the very beginning the queue looks like that:

Sheldon, Leonard, Penny, Rajesh, Howard

##Input

The input data consist of an array which contains five names, and single integer n.

(1 ≤ n ≤ 1000000000).
'''

def whoIsNext(names, r):
    #tickets per person
    tickets = 1
    total = 5
    index = 5
    
    if r < total:
        return names[r-1]

    while total < r:
        total += tickets * 2 * len(names)
        tickets = tickets * 2
    
    while total > r:
        total -= tickets
        index -= 1
        
    return names[index]
          
print(whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 7230702951))  
# Outputs: "Leonard"

'''
 for every 1 out of queue you add two to the end queue
 for every iteration the amount of tickets of 1 person doubles

 1 1 1 1 1 = 5 [5]
 2 2 2 2 2 = 10 [15]
 4 4 4 4 4 = 20 [35]
 8 8 8 8 8 = 40 [75]
 16 16 16 16 16 = 80 [155]
'''
