import matplotlib.pyplot as plt

x_values = list(range(1,10,1))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,c='red',edgecolors='blue',s=20)

plt.title("Square Numbers", fontsize='24')
plt.xlabel("Value",fontsize=14)
plt.ylabel("Value of Numbers",fontsize=14)
plt.axis([0,10,0,100])
plt.tick_params(axis='both',which='major',labelsize=14)

plt.show()