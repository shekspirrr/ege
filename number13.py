'''from ipaddress import*
for mask in range(33):
    net=ip_network(f'111.91.200.28/{mask}',0)
    print(net,net.netmask)'''
'''print(net[0])'''
'''for ip in net:
    print(ip)'''




'''from ipaddress import*
for mask in range(33):
    net=ip_network(f'158.116.11.146/{mask}',0)
    print(net,net.netmask)'''


'''from ipaddress import*
net = ip_network('98.81.154.195/255.252.0.0',0)
print(net[-2])'''

'''from ipaddress import*
net = ip_network('235.86.56.0/255.255.248.0',0)
k=0
for ip in net:
    b=f'{ip:b}'
    #b=bin(int(ip))[2:].zfill(32)
    if b[-2:]=='11':
        k+=1
        print(k)
'''


'''from ipaddress import*
net=ip_network('122.159.136.144/255.255.255.248',0)
k=0
for ip in net:
    b=f'{ip:b}'
    if b.count('1')%4!=0:
        k+=1
print(k)'''

'''from ipaddress import*
net= ip_network('123.222.111.192/255.255.255.248',0)
k = 0
for ip in net:
    b = f'{ip:b}'
    if b[24:].count('1')%3!=0:
        k += 1
print(k)'''

'''from ipaddress import*
net = ip_network('87.226.26.72/255.255.255.252',0)
k = 0
for ip in net:
    b = f'{ip:b}'
    if b[2:].count('0')%2==0:
        k+=1
print(k)'''

'''from ipaddress import*
for mask in range(33):
    net1 = ip_network(f'61.58.73.42/{mask}',0)
    net2 = ip_network(f'61.58.75.136/{mask}',0)
    if net1==net2:
        print(net1,net1.netmask)
k = 0
net = ip_network('61.58.73.42/255.255.252.0',0)
for ip in net:
    b = f'{ip:b}'
    if b.count('1')%2!=0 and ip not in [net.network_address,net.broadcast_address]:
        k+=1
print(k)'''

'''from ipaddress import*
for mask in range(33):
    net1 = ip_network(f'151.172.115.121/{mask}',0)
    net2 = ip_network(f'151.172.115.156/{mask}',0)
    if net1!=net2 and  net1.netmask == net2.netmask:
        print(net1, net1.netmask,net2, net2.netmask)
'''

'''from ipaddress import*
net = ip_network('192.168.160.0/255.255.224.0',0)
k = 0
for ip in net:
    b = f'{ip:b}'
    if b.count('1')==19:
        k+=1
print(k)'''
'''from ipaddress import*
net = ip_network('192.168.76.160/255.255.255.240',0)
k = 0
n = 0
for ip in net:
    b = f'{ip:b}'
    k+=1
    if k%2==0 and b[24:].count('1')%2==0 and ip not in [net.network_address,net.broadcast_address]:
        n+=1
print(n)'''

