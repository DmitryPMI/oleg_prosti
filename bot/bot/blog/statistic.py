import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy.random as rand 
import matplotlib.dates as mdates
import datetime as dt
import csv

#---------------------------------
#график активности
x = np.arange(10) #временная шкала
y = np.random.sample(10) #активность пользователей 
plt.xlim(0, max(x))
plt.title('Activity of users')
plt.xlabel('Date')
plt.ylabel('Activity')
plt.plot(x,y)
plt.show() 

#-----------------------------------
#диаграмма по всем ответам на все вопросы 
data_names = ['first question', 'second question', 'third question', 'fourth question']
data_answers = [[9124, 8652, 7592, 7515], [8124, 8752, 7092, 7815], [0, 0, 1000, 0]] #Данные по ответам, первые числа - количество первых вариантов
colors = ['red', 'blue', 'green', 'orange', 'black', 'yellow'] #Надо сразу установить, что максимальное количество вариантов ответа - 6(ну либо добавить ещё пару цветов)
labels = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth']

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (522 / dpi, 394 / dpi) )
mpl.rcParams.update({'font.size': 10})

plt.title('Aswers for questions')

ax = plt.axes()
ax.yaxis.grid(True, zorder = 1)

xs = range(len(data_names))

for i in range(len(data_answers)): #создание столбцов 
    c = i * 0.25
    plt.bar([(x + 0.05 + c) for x in xs], data_answers[i],
        width = 0.2, color = colors[i], alpha = 0.7, label = labels[i] + ' possible answer', zorder = 2)

plt.xticks(xs, data_names)

fig.autofmt_xdate(rotation = 25)

plt.legend(loc='upper right')
plt.show() 

#-----------------------------------
#Создание диаграмм для каждого вопроса на примере первого вопроса
data_names = ['']
data_answers = [100, 800, 1000] #Данные по количеству ответов
colors = ['red', 'blue', 'green', 'orange', 'black', 'yellow'] #Надо сразу установить, что максимальное количество вариантов ответа - 6(ну либо добавить ещё пару цветов)
labels = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth']

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (522 / dpi, 394 / dpi) )
mpl.rcParams.update({'font.size': 10})

plt.title('Aswers for the first question')

ax = plt.axes()
ax.yaxis.grid(True, zorder = 1)

xs = range(len(data_names))

for i in range(len(data_answers)): #создание столбцов 
    c = i * 0.25
    plt.bar([(x + 0.05 + c) for x in xs], [data_answers[i]],
        width = 0.2, color = colors[i], alpha = 0.7, label = labels[i] + ' possible answer',
        zorder = 2)

plt.xticks(xs, data_names)

fig.autofmt_xdate(rotation = 25)

plt.legend(loc='upper right')
plt.show() 