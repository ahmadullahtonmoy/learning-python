# declaring a variable
# variable name + equals sign + value (variableName = value)

userName = "Cat 5.0"

userPhonNumber = +13492243

print("User Name:",userName)
print("User Phone Number:",userPhonNumber)


# multiple value assign in multiple variables in one line

apple_price , orange_price , bananaPrice = 50 , 40 , 30

print("Apple Price:",apple_price)
print("Orange Price:",orange_price)
print("Banana Price:",bananaPrice)


# one value assign to multiple variables in one line

applePrice = orangePrice = bananaPrice = 40

print("Apple Price:",applePrice)
print("Orange Price:",orangePrice)
print("Banana Price:",bananaPrice)


# in python array called by list
# unpacking a list value in variables

colors = ["White","Red","Black","Blue","Purple","Pink"]

a , b , c , d , e , f = colors

print(a , b , c , d , e , f)