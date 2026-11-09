scores = int(input("enter scores 1 to 10: "))
if scores > 8:
    print("you passed")
elif scores < 5:
    print("you failed ")
elif scores < 8 and scores > 5:
    print("you passed with an average")

num =int(input("input first number: "))
numb =int(input("input second number: "))
if num > numb:
    print("the first number is larger")
elif num  < numb:
    print("the second number is larger")  
elif num == numb:
    print("the numbers are equal")