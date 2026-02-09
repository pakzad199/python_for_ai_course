category = {}


for i in range(10):
    user = {"name": "", "family": "", "age": 0}
    name = input("Enter your name please? ")
    family = input("Enter your family please? ")
    age = input("Enter your age please? ")
    user['name'] = name
    user['family'] = family
    user["age"] = age
    charecters = list(name)
    # print(charecters[0])
    # print(category.get(charecters[0], []))
    # print(category)
    # x = category.get(charecters[0], []).append(user)
    if category.get(charecters[0]):
        category[charecters[0]] = category[charecters[0]] + [name]
    else:
        category[charecters[0]] = [name]
    print(category)
    
