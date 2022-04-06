MENU = { #dictionary
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 150,
            "coffee": 18,
        },
        "cost": 120,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 130,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 150,
    }
}
money=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def display_details(users_choice):
    #displays ingridients
    print('Ingridients ')
    items= MENU[users_choice]
    item_1=items["ingredients"]
    print(f"Water  : {item_1['water']}")
    print(f"Milk   : {item_1['milk']}")
    print(f"Coffee : {item_1['coffee']}")
    print(f"Cost   : {items['cost']}"  )
    return  items['cost']
def check_resource(users_choice):
    #checks the resources
    items = MENU[users_choice]
    item_1 = items["ingredients"]
    for item in item_1:
        if item_1[item] > resources[item]:
            print(f"Sorry no enough {item}")
            return False

    return True

def enter_cash():
    #calculates the amount entered
    print("Notes of '10' '20' '100'  and '5 rupee coins' are acceptable" )
    total = int(input('enter number of 5 rupee coin '))*5
    total+= int(input('enter number of 10 rupee note '))*10
    total += int(input('enter number of 20 rupee note '))*20

    total += int(input('enter number of 100 rupee note '))*100
    return total

def make_coffee(users_choice):
    #makes the coffee
    items = MENU[users_choice]
    item_1 = items["ingredients"]
    for item in item_1:
        resources[item]-=item_1[item]



coffe_machine=True
while coffe_machine:
    print('Coffee machine is on')
    user_choice=input("What would you like? espresso/latte/cappuccino: ")
    if user_choice == 'off':
        print('coffee machine is shutdown')
        coffe_machine=False

    elif user_choice =='report':
        #displays the available Ingridients
        print('Report')
        print(f"Water  :  {resources['water']}")
        print(f"Milk   :  {resources['milk']}")
        print(f"Coffee :  {resources['coffee']}")
        print(f"Money   : {money}")

    else:
        cost=display_details(user_choice)
        option=input('Would you like to continue y/n ')


        if option=='y':
            value=check_resource(user_choice)
            coffe_machine=value

            if option=='y' and coffe_machine :
                amount= enter_cash()

                print(f"you deposited {amount} rupees")

                if amount< cost:
                    print(f"you deposited {amount} rupees")
                    print("You deposited less money  coffee can't be made")
                    transaction=False

                if amount > cost:
                    change=amount-cost
                    print(f"Here is {change} rupee in change")
                    transaction=True

                if amount == cost or transaction:
                    make_coffee(user_choice)
                    money+=cost
                    print(f"Here is your {user_choice} Enjoy!")









