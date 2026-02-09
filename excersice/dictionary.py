x = {"lessThan50": [], "greaterThan50": []}

for i in range(10):
    d = int(input('Enter your number: '))
    if d > 50:
        x['greaterThan50'].append(d)
    else: 
        x['lessThan50'].append(d)

print(x)