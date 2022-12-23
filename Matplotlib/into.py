import matplotlib.pyplot as plt

year = [2010, 2011, 2012, 2013, 2015, 2016, 2017]
cost_a = [0, 65, 0, 77, 55, 98, 105]
costb = [0, 85, 9, 85, 60, 105, 125]
ax = plt.axes()

# using set_facecolor() method
# Setting the background color of the plot
ax.set_facecolor("#4A6DE5")
plt.xlabel("Year")
plt.ylabel("Cost of items")
plt.plot(year, cost_a, marker='o', mec='red', color='yellow')
plt.plot(year, costb, marker='*', mec='yellow', color='yellow')
plt.legend(['Cost Of Item A ', 'Cost of Item B'])
plt.title("Comparision of two items")
plt.grid()
plt.show()
