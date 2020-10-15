# x = 6
# y = 7
# print(x is y)

# x = 6
# y = 7
# print(x is y)

# name = 'Alex'
# name2 = 'alex'
# print(name is name2)

# about_me = "I am Aleksandr Shaghbatyan i have Covid19,sorry my friend i cannot Covid19"
# word = "Covid19"
# name = "Aleksandr"
# result = word in about_me
# print(result)
# result = word not in about_me
# print(result)
# result = word in about_me and name in about_me
# print(result)

# item_banana  = input("Have you a banana") == 'y'
# item_light = input('Have you light') == 'y'
# res = item_banana and not item_light, 'get banana'
# print(res)


# HARC
# first = input("is your water machine broken ") == 'no'
# second = input("do you have water") == 'yes'
# result = no first and second
# print(result)

name = input("\n\tPlease mention your name ")
name = name.lower()
word = 'a'
result = (word in name)
print(result)

fridge = " banana, orange, "
first_object = 'banana'
second_object = 'orange'


third_object = 'apple'
result1 = first_object in fridge
result2 = second_object in fridge
result3 = third_object in fridge
print("Banana",result1,"Orange",result2,"Apple",result3)


banana = input("\n\tDo you have a banana in your fridge? ") == "y"
electircity = input("\n\tDo you have electircity? ") == "no"
result = banana and electircity
print(result)
print("\n\tTake out bananas from the fridge")