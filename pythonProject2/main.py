# Your code goes here!

# Remember the advice about ordering if-elif statements: sometimes it's easiest if you do *most restrictive* first!

# Another tip: Python lets you use _ to separate digits in large numbers for readability, such as:
# x = 10_000_000  <--- 10 million.
user_income = int(input('What is your 2019 taxable income? '))
user_income1 = user_income
tax = 0
if user_income > 510300:
    user_income -= 510299
    tax = user_income * .37
    user_income = 510299
if 204101 <= user_income <= 510300:
    user_income -= 204100
    tax += user_income * .35
    user_income = 204100
if 160726 <= user_income <= 204100:
    user_income -= 160725
    tax += user_income * .32
    user_income = 160725
if 84201 <= user_income <= 160725:
    user_income -= 84200
    tax += user_income * .24
    user_income = 84200
if 39476 <= user_income <= 84200:
    user_income -= 39475
    tax += user_income * .22
    user_income = 39475
if 9701 <= user_income <= 39475:
    user_income -= 9700
    tax += user_income * .12
    user_income = 9700
if user_income <= 9700:
    tax += user_income * .1

tax_rate = (tax / user_income1) * 100

print(f'Your tax liability is ${tax:,.2f}')
print(f'Your effective tax rate is {tax_rate:.1f}%')
