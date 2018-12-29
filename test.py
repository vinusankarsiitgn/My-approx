file = input("Enter file name: ")
f = open(file, "r")
a = f.read().split()
change = []

for i in range(0, len(a), 4):
	try:
		x = abs(int(a[i+3])-int(a[i+2]))/int(a[i+3])
		change.append(x)
	except:
		change.append(0)

print("Relative error:", sum(change)/len(change)) 
