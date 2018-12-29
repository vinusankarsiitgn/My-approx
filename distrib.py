from matplotlib import pyplot as plt
import numpy as np 

f = open('idea1.txt', 'r')
a = f.read()
f.close()


a = a.split()

dic = {}

for j,i in  enumerate(a):
	if  j%2==0 and j%4!=0:
		x = int(a[j])
		y = int(a[j+1])
		try:
			r = abs(x-y)/x
		except:
			r = 0
		if r in dic:
			dic[r] += 1
		else:
			dic[r] = 1

arr = sorted(dic)
dic1 = {(i):dic[i] for i in arr[1:]}

plt.xlabel('Relative Error')
plt.ylabel('Frequency')
plt.plot(list(dic1.keys()), list(dic1.values()))
plt.show()

# plt.bar(dic1.keys(), dic1.values(), width=0.1,color='b')
# plt.show()