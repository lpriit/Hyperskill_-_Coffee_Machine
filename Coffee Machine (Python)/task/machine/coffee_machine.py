class CoffeeMachine:
    def __init__(self, water, milk, beans, cups, money, status='main_menu'):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money
        self.status = status

    def machine_status(self):
        print('The coffee machine has:')
        print('{} ml of water'.format(self.water))
        print('{} ml of milk'.format(self.milk))
        print('{} g of coffee beans'.format(self.beans))
        print('{} disposable cups'.format(self.cups))
        print('${} of money'.format(self.money))

    def fill_machine(self):
        print('Write how many ml of water you want to add:')
        self.water += int(input())
        print('Write how many ml of milk you want to add:')
        self.milk += int(input())
        print('Write how many grams of coffee beans you want to add:')
        self.beans += int(input())
        print('Write how many disposable cups you want to add:')
        self.cups += int(input())

    def prepare_drink(self, drink_name):
        if self.water < drink_name.water:
            print('Sorry, not enough water!')
        elif self.milk < drink_name.milk:
            print('Sorry, not enough milk!')
        elif self.beans < drink_name.beans:
            print('Sorry, not enough beans!')
        elif self.cups < 1:
            print('Sorry, not enough cups!')
        else:
            print('I have enough resources, making you a coffee!')
            self.water -= drink_name.water
            self.milk -= drink_name.milk
            self.beans -= drink_name.beans
            self.cups -= 1
            self.money += drink_name.price

    def buy_drink(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        self.status = input()
        if self.status == '1':
            self.prepare_drink(espresso)
        elif self.status == '2':
            self.prepare_drink(latte)
        elif self.status == '3':
            self.prepare_drink(cappuccino)
        else:
            self.status = 'main_menu'
            self.choose_action()

    def take_money(self):
        print('I gave you ${}'.format(self.money))
        self.money -= self.money

    def choose_action(self):
        if self.status == 'main_menu':
            print('Write action (buy, fill, take, remaining, exit):')
            self.status = input()
            if self.status == 'fill':
                self.fill_machine()
            elif self.status == 'remaining':
                self.machine_status()
            elif self.status == 'exit':
                exit()
            elif self.status == 'take':
                self.take_money()
            elif self.status == 'buy':
                self.buy_drink()
        self.status = 'main_menu'
        self.choose_action()


class Recipe:
    def __init__(self, name, water, milk, beans, price):
        self.name = name
        self.water = water
        self.milk = milk
        self.beans = beans
        self.price = price


coffe_machine = CoffeeMachine(400, 540, 120, 9, 550)
espresso = Recipe('Espresso', 250, 0, 16, 4)
latte = Recipe('Latte', 350, 75, 20, 7)
cappuccino = Recipe('Cappuccino', 200, 100, 12, 6)

coffe_machine.choose_action()
