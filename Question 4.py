# Nousheen Siddiqui
# Edited on 02/11/2021
# A range of numbers that are divisible by 3,5, both or neither.


for i in range(1,50):
    print(i)
    if i % 15 == 0:
        print("Divisible by both")
    elif i % 3 == 0:
        print("Divisible by 3")
    elif i % 5 == 0:
        print("Divisible by 5")
    else:
        print("Not divisible by both")





