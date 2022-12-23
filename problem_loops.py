# Get rich quick aggency
p = 10000
rate = 5
term = 5
total_intrest = 0
for year in range(term):
    print(p)
    intrest = (p*(rate/100))
    print(intrest)
    p = p+intrest
    total_intrest = total_intrest+intrest
print(total_intrest)
print(p)
