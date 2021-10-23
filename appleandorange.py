print('APPLE IS 20PHP EACH WHILE ORANGE IS 25PHP EACH. ')
apple_str = input('Enter how many apples do you want to buy: ') 
apple = int(apple_str)

orange_str = input('Enter how many oranges do you want to buy: ')
orange = int(orange_str)

apple_price = 20
orange_price = 25

apple_total = (apple * apple_price)
orange_total = (orange * orange_price)

grand_total= apple_total + orange_total
print(f'The total amount is {grand_total}.')