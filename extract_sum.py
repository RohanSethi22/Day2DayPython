import re
try:
	f=open('regex_sum_428417.txt','r')
except:
	print('File not found.')
	exit()
s=0
for line in f:
	nums=re.findall('[0-9]+',line)
	numi=[int(x) for x in nums]
	s+=sum(numi)
print(s)
