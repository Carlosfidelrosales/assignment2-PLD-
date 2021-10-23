money = input('How much money do you have in your pocket?: ')
total_money= float(money)
apple = input('What is the amount for each apple: ')
total_apple = float(apple)


max_apples = total_money // total_apple
change = total_money % total_apple

print(f"You can buy {max_apples} apples and your change is{change: .2f} pesos")
