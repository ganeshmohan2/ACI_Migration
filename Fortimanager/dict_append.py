
#my_dict1 = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Washington"}
#my_dict1["mykey"] = "test_value"

#data =dict(list(my_dict1.items()) + list(my_dict2.items()))
#print(my_dict1)
l3out_int_name = "Ganesh"
current_vlan_interface = "guru"
interface_list=[]
interface_list.append(l3out_int_name)
interface_list.append(current_vlan_interface)
interface_list
print (interface_list)
"""
fruits = ["Apple", "Pear", "Peach", "Banana"]
a= [{'action': 0, 'exact-match': 0, 'flags': 0, 'id': 0, 'prefix': ['1.1.1.1', '255.255.255.252']}]
b=dict(a[0])
fruit_dictionary = b.keys()
fruit_dictionary1 = b.values()

print(fruit_dictionary)
prefix ="prefix"
if prefix  in fruit_dictionary:
  print("prefix in don't configure.")
else:
   print (" prefix missing configure")
  
######
prefix =['1.1.1.1','255.255.255.252']
print(fruit_dictionary1)
for i in fruit_dictionary1: 
 print(type(i))
if prefix in fruit_dictionary1:
 print("prefix exist.")
else:
  print (" prefix not exist configure")

###
prefix =['1.1.1.1','255.255.255.252']
list1 = fruit_dictionary1
print(list1)
#for i in fruit_dictionary1: 
#print(type(i))
if prefix in list1:
 print("prefix exist.")
else:
  print (" prefix not exist configure")
"""
a=['192.168.5.0', '255.255.255.1']
Network = "192.168.6.0"
SubnetMask = "255.255.255.0"
gwsubnet = Network +"/"+ SubnetMask
print(gwsubnet)
print(a[0])
if a[0]!=Network and a[1]!=SubnetMask:
    print ("entire not exist")
else:
    print (" exist")    


