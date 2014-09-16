#John Newberry
#15/09/14

first_integer = int(input("Please enter the first integer: "))
second_integer = int(input("Please enter the second integer: "))

answer_one = (first_integer // second_integer)
answer_two = (first_integer % second_integer)

print("the answer is {0} with a remainder of {1}!".format(answer_one,answer_two))
