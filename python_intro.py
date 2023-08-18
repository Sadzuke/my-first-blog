balance = 50
price = 75
finaly = balance - price
total = price - balance

if balance >= price:
    print("I will buy it and now I have", finaly)
elif balance < price:
    print("I don't have enough money", total)


def test (name):
    if name == 'Ola':
            print("Hi Ola")
    elif name == 'Sonja':
            print("Hi Sonja")
    else:
            print("Hi anonymous")
test('Azalya')

def hi(name):
    print('Hi ' + name + '!')
hi("Azalya")

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'Azalya']
for name in girls:
    hi(name)

def multiple(number1, number2):
    print('answer:')
    print(number1*number2)
multiple(4, 5)

def hellofriend(name, surname):
    print('Hi ' + name + ' ' + surname + '!')
hellofriend('Azalya', 'Salavatova')

def name(atr1, atr2):
    print('result:')
    print(atr1/atr2)
name(10, 5)


def name(atr1, atr2):
    result = atr1/atr2
    print(result)
name(10, 5)
name(14, 2)
name(15, 5)

def taxi(km, base, km1):
    result = base + (km - 3) * km1
    if km < 3:
        print(base)
    else:
        print(result)

taxi(20, 2, 0.3)
