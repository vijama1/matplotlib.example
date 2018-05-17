#!/usr/bin/python2
import time
import  socket
import collections
val=[]
count=0
values=[]
keys=[]
flist=[]
i=0
rec_ip="127.0.0.1"
myport=10656
#                 ipv4       ,  for UDP
#   only  for rec
#  below method with argument creating a socket called  s
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((rec_ip,myport))
# s.connect(("127.0.0.1",10656))
#  now connecting ip  and port
tim=int(round(time.time() * 1000))
timeout=int(round(time.time() * 1000))+20
print("time is:"+str(tim))
print("timeout is:"+str(timeout))
print(time.time())
a=time.time()+10
print(type(time.time()))
print(type(a))
#  buffer size
while i<5:
	#while(int(time.time())<int(a)):
	#print("Inside while")
	data=s.recvfrom(1000)
	a=str(data[0].strip().split())
	val.append(a[3:].replace("]","").replace("'",""))
	i=i+1
	#print("Hello world")
	'''inp=input("Enter reply")
	os.send(inp.encode())'''
#elem=v[0]
counter=collections.Counter(val)
keys=list(counter.keys())
values=list(counter.values())
print(keys)
print(values)
for i in range(0,len(values)):
	print(str(keys[i])+" occurs "+str(values[i])+" times")
#variable.append(counter)
#print(type(counter))
#print(type(variable[0]))
#print(variable)
#for i in variable.keys():
#	flist.append(i)
#print(flist)


'''for i in (0,len(val)):
	for j in (i+1,len(val)+1):
		if(val[i]==val[j]):
			count=count+1;'''
print(count)
