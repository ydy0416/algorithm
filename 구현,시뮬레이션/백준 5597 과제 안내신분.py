dict={i:0 for i in range(1,31)}
for i in range(28):
    dict[int(input())]=1
    
for i in range(1,31):
    if dict[i]==0:
        print(i)