"""
    This program works based on the Collatz Sequence
    It devides the number given by the user untill it is no 
    more divisible ( i.e the number is divided untill it is equal to 1)
"""

def collatz(number):
    #Check to see if number is an even number
    if number % 2 == 0:
        n = number // 2
        if n != 1:
            print(n)
            return collatz(n)
        elif n == 1:
            print(n)

    #Check to see if the number is an odd number
    elif number % 2 != 0:
        """n converts the odd number to even number 
            and pass it back to collatz"""
        n = 3 * number + 1
        print(n)
        return collatz(n)
    
user_num = int(input())
collatz(user_num)
