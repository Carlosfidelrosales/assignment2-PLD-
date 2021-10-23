total_money = float(input('How much money do you have?: '))
price_apple = int(input('What is the price for each apple: '))

max_apples= total_money // price_apple
change= total_money % price_apple

print(f"You can buy {max_apples} apples and your change is{change: .2f} pesos")
