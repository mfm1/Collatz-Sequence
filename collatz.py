"""
    This program works based on the Collatz Sequence
    It devides the number given by the user un it is no 
    more divisible ( i.e the number is devided untill it is equal to 1)
"""

def collatz(num):
    #Check to see if num is an even number
    if num % 2 == 0:
        n = num // 2
        if n != 1:
            print(n)
            return collatz(n)
        elif n == 1:
            print(n)

    #Check to see if the number is an odd number
    elif num % 2 != 0:
        """n converts the odd number to even number 
            and pass it back to collatz"""
        n = 3 * num + 1
        print(n)
        return collatz(n)
    
user_num = int(input())
collatz(user_num)