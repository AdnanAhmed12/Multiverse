# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = [10,20,30,40,50,60,70,80,90,100,120,130,150,200,250,300,350]
# corresponding y axis values
y = [59,50,50,61,51,39,62,52,45,62,64,39,60,52,44,62,64]

plt.ylim(10,100)
plt.xlim(10,350)

# plotting the points
plt.plot(x, y, color='blue', linestyle='dashed', linewidth = 2,
         marker='o', markerfacecolor='black', markersize=8)

# naming the x axis
plt.xlabel('Number of Nodes')
# naming the y axis
plt.ylabel('Number of Forks ')

# giving a title to my graph
plt.title('TPS = 100 ,Threshold 10, zipf = 0.8')

# function to show the plot
plt.show()
