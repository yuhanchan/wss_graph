import matplotlib.pyplot as plt
import numpy as np
from itertools import islice

data = np.loadtxt('output1', usecols=(0,3), skiprows=2)
# print(data)
time1 = data[:, 0]
ref1 = data[:, 1]
# # d = np.gradient(ref1)
# c_time1 = [time1[0]]
# for i in range(1, len(time1)):
#     c_time1.append(time1[i]+time1[i-1])
# c_time1 = np.array(c_time1)
d = np.diff(ref1)/np.diff(time1)
c_time1 = time1[0: len(time1)-1]
print(len(d))
print(len(c_time1))
# print(c_time1)
# plot1

# count = len(open('output2').readlines())
# rows = range(0, count+1, 3)

# with open('output2') as lines:
#     array = np.genfromtxt(islice(lines, 2, count, 3))
# data = array[:, (0, 3)]

data = []
f = open('output2', 'r')
lines = [line.rstrip('\n') for line in f]
for i in range(len(lines)):
    if(lines[i][0] != 'W' and lines[i][0] != 'E'):
        data.append([float(y) for y in lines[i].split()])
data = np.array(data)
data = data[:, (0, 3)]
# print(np.array(data))
# print(rows)
# print(data)
# print(len(data), '\n')
# for i in range(1, len(data)):
#     data[i][0] = data[i][0] + data[i-1][0]
    # print(data[i][0] + data[i-1][0])
for i in range(1, len(data)-2):
    if(data[i][0]+0.5<data[i-1][0]):
        for j in range(i,i+10):
            if(j==len(data)-1 or data[j+1][0]+0.5<data[j][0]):
                data[j][0] += data[i-1][0]
                break
            else:
                data[j][0] += data[i-1][0]
# for i in range(1, len(data)-9):
#     if(data[i][0]+0.5<data[i-1][0]):
#         for j in range(i,i+10):
#                 data[j][0] += data[i-1][0]
# for i in range(1, len(data)):
#     if(i>=10):
#         data[i][0] += data[i//10*10-1][0]
print(data)
time2 = data[:, 0]
ref2 = data[:, 1]
# plot2

plt.plot(time1, ref1, 'b')
plt.plot(time2, ref2, 'r')
# plt.plot(c_time1, d, 'g')
plt.xlabel('Time')
plt.ylabel('WSS(MB)')
plt.legend(['Accumulative','Every Second'])
plt.grid()
plt.ylim(bottom=0)
plt.show()