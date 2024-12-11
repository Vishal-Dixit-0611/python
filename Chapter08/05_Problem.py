# Write a recursive function to calculate the sum of the first n natural number.


'''
sum(1) = 1
sum(2) = 1 + 2
sum(3) = 1 + 2 + 3
sum(4) = 1 + 2 + 3 + 4
sum(5) = 1 + 2 + 3 + 4 + 5

sum(n) = sum(n-1) + n
'''

def sum(n):
    if n == 1:
        return 1
    # s = sum(n-1) + n
    # return s
    return sum(n-1) + n

print(sum(4))