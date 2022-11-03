#the authors' names are Cadyn and Sarah
#this is manually
R_cake = {"flour": 1, "baking soda": 2, "cocoa powder": 3, "salt": 4, "butter": 5, "sugar": 6, "vegetable oil": 7, "eggs": 8, "vanilla extract": 9, "buttermilk": 10}
L_cake = {"flour": 1, "baking powder": 2, "baking soda": 3, "salt": 4, "butter": 5, "sugar": 6, "eggs": 7, "vanilla extract": 8, "milk": 9, "lemon zest": 10}
def similar(c):
    x = R_cake
    y = L_cake
    if c in x:
        if c in y:
            print("shares", c, "as an ingredient")
        else:
            print("doesn't share", c, "as an ingredient")
    else:
        print("doesn't share", c, "as an ingredient")



similar("flour")
similar("salt")
similar("baking powder")
similar("cocoa powder")

#this one automatically check the full dictionary for similarities
R_cake = {"flour": 1, "baking soda": 2, "cocoa powder": 3, "salt": 4, "butter": 5, "sugar": 6, "vegetable oil": 7, "eggs": 8, "vanilla extract": 9, "buttermilk": 10}
L_cake = {"flour": 1, "baking powder": 2, "baking soda": 3, "salt": 4, "butter": 5, "sugar": 6, "eggs": 7, "vanilla extract": 8, "milk": 9, "lemon zest": 10}


def similar1():
    cake = []
    x = R_cake
    y = L_cake
    for ingredient in x:
        if ingredient in y:
            cake.append(ingredient)
    print cake


similar1()
