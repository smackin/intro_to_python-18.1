def any7(nums):
    """Are any of these numbers a 7? (True/False)"""
    for num in nums: 
        if num == 7: 
            print("True")
        else:
             print("False")


    # YOUR CODE HERE 
    # 1 - pass in a list of values 
    # 2- loop over the list 
    # set condition if num ==7: true 
    # else  false  
  

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))


def greet(person):
    print( f"Hello there, {person}" )

greet('Ruby')


def add_numbers(a,b):
    sum = a+b
    print ("DOING MATH!!")
    return sum 

def divide(a,b): # adding in a line to check type of for params. 
    if type(a) is int and type(b) is int:
        return a/b # if both are int - return a/b 
    return 'a and b must be integers!'  # else return this msg.  



