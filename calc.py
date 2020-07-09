num = input('What is your weight in pounds? ')
planet = input("Choose a planet: Mars, Venus, Mercury, Jupiter, Saturn, Uranus, Neptune --> ")
new = None

num = float(num)


if planet == "Mars":
    new = num/9.81 * 3.711
elif planet == "Venus":
    new = num/9.81 * 8.87
elif planet == "Mercury":
    new = num/9.81 * 3.7
elif planet == "Jupiter":
    new = num/9.81 * 24.79
elif planet == "Saturn":
    new = num/9.81 * 10.44
elif planet == "Uranus":
    new = num/9.81 * 8.69
elif planet == "Neptune":
    new = num/9.81 * 11.15

print(str(new))

# # taxes = {
# #             #$0 - $8,500 | $8,500 - $11,700 | $11,700 - $13,900 | $13,900 - $21,400 | $21,400 - $80,650 | $80,650 - $215,400
# #     "NY": ["0.04" , "0.045", "0.0525", "0.059" , "0.0621" , "0.0649" ]
# #     # "NJ": "The Flash",
# #     # "CA": "Spiderman",
# #     # "TX": "Lex Luthor",
# #     # "WA": "Deadpool"
# # }

# salary = input('What is your yearly salary? ')
# bonuses = input("How much do you make in terms of bonuses in a year? ")
# # state = input("What state do you live in? (Example: NY) ")
# income = None 

# fed_income = None

# salary = float(salary)
# bonuses = float(bonuses)


# if 0 <= salary <= 8500 :
#     income = (salary + bonuses)* (1-0.04)
# elif 8500 < salary <= 11700 :
#     income = (salary + bonuses)* (1-0.045)
# elif 11700 < salary <= 13900 :
#     income = (salary + bonuses)* (1-0.0525)
# elif 13900 < salary <= 21400 :
#     income = (salary + bonuses)* (1-0.059)
# elif 21400 < salary <= 80650 :
#     income = (salary + bonuses)* (1-0.0621)
# elif 80650 < salary <= 215400 :
#     income = (salary + bonuses)* (1-0.0649)

# print('Your income before federal tax reductions is ' + str(income))

# if 0 <= income <= 9700 :
#     fed_income = income * (1-0.1)
# elif 9701 <= income <= 39475 :
#     fed_income = income * (1-0.12)
# elif 39476 <= income <= 84200 :
#     fed_income = income * (1-0.22)
# elif 84201 <= income <= 160725 :
#     fed_income = income * (1-0.24)
# elif 160726 <= income <= 204100 :
#     fed_income = income * (1-0.32)
# elif 204101 <= income <= 510300 :
#     fed_income = income * (1-0.32)

# print('Your income after federal tax reductions is ' + str(fed_income))