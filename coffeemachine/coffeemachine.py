from coffeedictionary import resources,MENU

#prints a report of the ingredients
def report(w,m,c,mon):
    print(f"Water : {w}ml")
    print(f"Milk : {m}ml")
    print(f"Coffee : {c}g")
    print(f"Money : ${mon}")
 
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
money = 0
operation = False

def insert_coins():
    quarters = float(input("insert quarters : "))
    dimes = float(input("insert dimes : "))
    nickles = float(input("insert nickles : "))
    pennies = float(input("insert pennies : "))

    quarters = quarters * 0.25
    dimes = dimes * 0.1
    nickles = nickles * 0.05
    pennies = pennies * 0.01

    return quarters + dimes + nickles + pennies


def check_ingredients(coffee_type,water1,milk1,coffee1):

    global water 
    global milk
    global coffee
    global money
    global operation
    w1 = (MENU[coffee_type]["ingredients"]["water"])
    c1 = (MENU[coffee_type]["ingredients"]["coffee"])
    m1 = (MENU[coffee_type]["ingredients"]["milk"])
    cost = (MENU[coffee_type]["cost"])

    if water1 >= w1 and coffee1 >= c1 and milk1 >= m1 and money >= cost:
        water = water - w1
        milk = milk - m1
        coffee = coffee - c1
        money = money - cost
        operation = True
    elif  water1 < w1:
        print("Not enough water in the machine")
        operation = False
    elif coffee1 < c1:
        print("Not enough coffee in the machine")
        operation = False
    elif milk1 < m1:
        print("Not enough milk in the machine")
        operation = False
    elif money < cost:
        print("Not enough money in the machine , insert coins please")
        operation = False

choice1 = "on"

while choice1 != "off":
        
    choice1 = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice1 == "report":
        report(water,milk,coffee,money)
    elif choice1 == "insert":
        money = money + insert_coins()
        report(water,milk,coffee,money)
    else:
        (check_ingredients(choice1,water,milk,coffee))
        report(water,milk,coffee,money)


