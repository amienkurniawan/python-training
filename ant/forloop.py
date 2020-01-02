friends = ["amien","kurniawan","john","mika"]
number = input("take a number to print array: ")

for index in range(int(number)):
    if index >= len(friends):
        print("the number out of range, maksimum number array is "+str(len(friends)))
        break
    else:
        print(friends[index])
