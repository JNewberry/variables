#John Newberry
#15/09/14

elevator_height = int(input("Please enter the height of the lift in cm: "))
elevator_width = int(input("Please enter the width of the lift in cm: "))
elevator_depth = int(input("Please enter the depth of the lift in cm: "))

fridge_height = int(input("Please enter the height of the fridge in cm: "))
fridge_width = int(input("Please enter the width of the fridge in cm: "))
fridge_depth = int(input("Please enter the depth of the fridge in cm: "))

elevator_size = (elevator_height * elevator_width * elevator_depth)

fridge_size = (fridge_height * fridge_width * fridge_depth)

answer = elevator_size - fridge_size

print("The room remaining in the elevator is {0} cm3.".format(answer))
