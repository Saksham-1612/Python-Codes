dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}
dict4 = {}
for m in (dict1, dict2, dict3):
    dict4.update(m)
print(dict4)
