# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = [90,100,120,130,150,200,250,300,350]
# corresponding y axis values
y = [45,50,59,56,58,50,56,55,56]

plt.ylim(10,100)
plt.xlim(10,400)

# plotting the points
plt.plot(x, y, color='blue', linestyle='dashed', linewidth = 2,
         marker='o', markerfacecolor='black', markersize=8)

# naming the x axis
plt.xlabel('Number of Nodes')
# naming the y axis
plt.ylabel('Number of Forks ')

# giving a title to my graph
plt.title('TPS = 100 ,Threshold 15, zipf = 0.8')

# function to show the plot
plt.show()
