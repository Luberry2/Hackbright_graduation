# name1 = raw_input("What is your name?")
# name2 = raw_input("What is your partner's name?")
# if len(name1)>len(name2):
#     print "My name is greater!"
# elif len(name1)<len(name2):
#     print "Your partner name is greater"
# else:
#     print "Your names are equal!"

# today_date = raw_input("What is today's date?")
# if today_date >= 15:
#     print "Oh, we're halfway there!"
# else:
#     print "The month is still young."

# day_of_the_week = raw_input("Which day is it?")
# if day_of_the_week == "Monday":
#     print "Yaaas Monday! Here we go!"
# elif day_of_the_week == "Tuesday":
#     print "Sigh, it's only Tuesday."
# elif day_of_the_week == "Wednesday":
#     print "Humpday!"
# elif day_of_the_week == "Thursday":
#     print "#tbt"
# elif day_of_the_week == "Friday":
#     print "TGIF!"
# else:
#     print "Yeah, it's the weekend!"

# num = 8
# if (num%2) == 0:
#     print "The number %i is even." %(num)
# else:
#     print "The number %i is odd." %(num)

# num = 8
# if (num%2) > 0:
#     print "The number %i is odd." %(num)
# else:
#     print "The number %i is even." %(num)

# num1 = 8
# num2 = 9
# # if (num1%2) == 0 and (num2%2) == 0:
# #     print "Both numbers are even."
# # else:
# #     print "Both numbers are not even."

# if (num1%2) == 0 or (num2%2) == 0:
#     if (num1%2) < (num2%2):
#         print "%i is even and %i is odd." %(num1,num2)
#     else:
#         print "%i is odd and %i is even." %(num1,num2)
# else:
#     print "Both numbers are odd."

# my_favorite_color = raw_input("What is my favorite color?")
# if my_favorite_color.capitalize() == "Blue":
#     print "My favorite color is blue!"
# else:
#     print "My favorite color is not blue."

my_favorite_color = raw_input("What is my favorite color?")
if my_favorite_color.capitalize() == "Red" or my_favorite_color.capitalize() == "Blue" or my_favorite_color.capitalize() == "Yellow":
    print "My favorite color is primary color."
else:
    print "My favorite color is a secondary color."

# line 63-67 did not work correctly. why?

# my_favorite_color = raw_input("What is my favorite color?")
# if my_favorite_color.capitalize() == "Red":
#     print "My favorite color is primary color."
# elif my_favorite_color.capitalize() == "Blue":
#     print "My favorite color is primary color"
# elif my_favorite_color.capitalize() == "Yellow":
#     print "My favorite color is primary color"
# else:
#     print "My favorite color is a secondry color."