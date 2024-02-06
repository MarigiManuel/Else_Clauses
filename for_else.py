# Use Python for else statement to execute a code block if the loop doesn’t encounter a break statement or if the iterables object has no item.
# Python for else statement example

countries = [{'country': 'Kenya', 'city': 'Nairobi'},
             {'country': 'Tanzania', 'city': 'Dodoma'},
             {'country': 'Uganda', 'city': 'Kampala'}]

country = input('Enter country name: ')

for country_input in countries:
    if country_input['country'] == country:
        print(country_input)
        break
else:
    print(f'Sorry, {country} not found!')


# Finding Prime numbers

for num in range(2, 11):
    for i in range(2, num):
        if num % i == 0:
            print(num, 'is not a prime number')
            break
    else:
        print(num, 'is a prime number')


# Searching for an element
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 4:
        print('Number found')
        break
else:
    print('Number not found')
