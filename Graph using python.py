"""
Created on Sun Dec 16 10:05:23 2018

@author: vishal
"""

import matplotlib.pyplot as plt
import pandas
import seaborn
import numpy
a = range(1,16)
mean = 50 
sigma = 10
b = numpy.random.normal(mean,sigma,15).astype(int)
plt.bar(a,b)
plt.show()

a = [3,6,6,8,9]
color_list = ['Red','Green','Blue','Yellow','Grey']
plt.pie(a,labels= ['AA','BB','CC','DD','EE'],colors = color_list)
plt.show()

hist_data = numpy.random.normal(mean,sigma,500).astype(int)
plt.hist(hist_data)
plt.show()

scatter_data_1 = numpy.sort(numpy.random.normal(mean,sigma,50).astype(int))
scatter_data_2 = numpy.sort(numpy.random.normal(mean,sigma,50).astype(int))
plt.scatter(scatter_data_1,scatter_data_2)
plt.show()

box_data = numpy.random.normal(60,10,50).astype(int)
plt.boxplot(box_data)
plt.show()

"""PLOTING USING OBJECT ORIENTED WAY"""
a = range(1,16)
mean = 50
sigma = 10
b = numpy.random.normal(mean,sigma,15).astype(int)
#we define figure object
figure_object = plt.figure()
#add axes
axes = figure_object.add_axes([.1,.1,1,1])
#adding grid
axes.grid()
#set axes labels
axes.set_xlabel('X')
axes.set_ylabel('Y')
#set axes ticks
axes.set_xticks(range(1,15))
axes.set_yticks(range(20,100,10))
#set axes limit
axes.set_xlim([1,15])
axes.set_ylim([20,80])
#generating plot
axes.plot(a,b)



"""Creating The Subplot"""
mean =20
sigma = 5
a = range(1,16)
b = numpy.random.normal(mean,sigma,15).astype(int)
c = numpy.random.normal(mean,sigma,15).astype(int)
#create figure object
figure_object = plt.figure()
#two axes inside the figure axes
number_of_rows = 1
number_of_columns = 2
fig_sub_object,(axes1,axes2) = plt.subplots(number_of_rows,number_of_columns)
axes1.plot(a,b)
axes2.plot(a,c)

"""seaborn library"""

mean = 25
sigma = 10
dist_data_1 = numpy.random.normal(mean,sigma,500).astype(int)
dist_data_2 = numpy.random.normal(mean,sigma,500).astype(int)
dist_data_3 = numpy.random.normal(mean,sigma,500).astype(int)
dist_data = pandas.DataFrame({"A":dist_data_1,"B":dist_data_2,"C":dist_data_3})
# first we need to create categorial data 
data = ["Delhi","Pune","Ajmer"]
# This code will create categorial data of 500 length with some predefined parobabilty of each class
dist_data['city'] = numpy.random.choice(data,500,p = [0.5,0.2,0.3]).tolist()
#create class variable
dist_data['gender'] = numpy.random.choice(['Male','Female'],500,p = [0.6,0.4]).tolist()
# ploting Distplot Graph
seaborn.distplot(dist_data_1,bins = 10)
# ploting Jointplot using Seaborn
seaborn.jointplot(x = dist_data_2, y = dist_data_1)
seaborn.jointplot(x = dist_data_2, y = dist_data_1,kind = "kde")
# ploting Pairplot using Seaborn
seaborn.pairplot(dist_data)
# ploting Stripplot using Seaborn
seaborn.stripplot(x = "city", y ="A",data = dist_data,jitter = True)
# ploting Violinplot using Seaborn
seaborn.violinplot(x ="B",y = "city",data = dist_data)
# ploting Pointplot using Seaborn
seaborn.pointplot(x = "A",y = "city",hue = 'gender',data = dist_data)
