# Python while.........else statements

scores = [{'subject': 'Math', 'grade': 90},
          {'subject': 'Chem', 'grade': 93},
          {'subject': 'Comp', 'grade': 95}]

subject = input('Enter subject: ')
index = 0

while index < len(scores):
    item = scores[index]
    
    if item['subject'] == subject:
        print(f"{item['subject']} has a grade of {item['grade']}")
        found_it = True
        break

    index += 1
else:
    grade = int(input(f'Enter the grade for {subject}:'))
    scores.append({'subject': subject, 'grade': grade})
    print(scores)


# Finding Factorials

num = 10
factorial = 1
while num > 0:
    factorial *= num
    num -= 3
else:
    print("Factorial:", factorial)
