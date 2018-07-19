a = [1,1,1,1,2,2,2,2,3,3,3,4,4]

d = {}
for item in a:
    if item in d:
        d[item] = d.get(item)+1
    else:
        d[item] = 1

for k,v in d.items():
    print(str(k)+':'+str(v))

# output
#1:4
#2:4
#3:3
#4:2

#remove dups
d = set(a)
print(d)
#{1, 2, 3, 4}
