# importing the required module
import matplotlib.pyplot as plt
p1 = [59,50,50,61,51,39,62,52,45,62,64,39,60,52,44,62,64]
p2 = [45,50,59,56,58,50,56,55,56]
p3 = [47,61,58,43,71,48,57,63,44]
p4 = [48,68,51,51,57,61,57,62,68]
p5 = [40,47,55,45,61,62,40,50,50]
p6 = [43,43,49,43,60,49,53,42,55]
p7 = [40,58,39,44,63,54,49,51,43]

p1_mean = (59+50+50+61+51+39+62+52+45+62+64+39+60+52+44+62+6)/17
p2_mean = (45+50+59+56+58+50+56+55+56)/9
p3_mean = (47+61+58+43+71+48+57+63+44)/9
p4_mean = (48+68+51+51+57+61+57+62+68)/9
p5_mean = (40+47+55+45+61+62+40+50+50)/9
p6_mean = (43+43+49+43+60+49+53+42+55)/9
p7_mean = (40+58+39+44+63+54+49+51+43)/9



# x axis values
x = [10,12,18,24,30,40,50]
# corresponding y axis values
y = [p1_mean,p2_mean,p3_mean,p4_mean,p5_mean,p6_mean,p7_mean]


plt.ylim(10,100)
plt.xlim(1,60)

# plotting the points
plt.plot(x, y, color='blue', linestyle='dashed', linewidth = 2,
         marker='o', markerfacecolor='black', markersize=8)

# naming the x axis
plt.xlabel('Confirmation Threshold Values')
# naming the y axis
plt.ylabel('Number of Forks ')

# giving a title to my graph
plt.title('TPS = 100, zipf = 0.8')

# function to show the plot
plt.show()
