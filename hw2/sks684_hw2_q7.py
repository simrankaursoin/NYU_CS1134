'''
Simran Soin
CS UY 1134
22 February 2019
Homework 2 Question 7
'''

def findChange(lst01):
    start = 0
    end = len(lst01)
    prev = lst01[0]
    while True:
        midpoint = (start+end)//2
        if lst01[midpoint] == 0:
            start = midpoint
        elif lst01[midpoint] == 1 and (lst01[midpoint-1]!=0):
            end = midpoint
        else:
            return midpoint
