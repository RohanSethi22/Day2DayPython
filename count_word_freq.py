name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
c={}
for line in handle:
    words=line.split()
    if len(words)>2 and words[0]=='From':
        hour=words[5][:2]
        c[hour]=c.get(hour,0)+1
#ans=sorted([(v,k) for (k,v) in c.items()],reverse=True)
ans=sorted(c.items(),reverse=True)
for w,c in ans:
	print(w,c)
