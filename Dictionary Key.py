my_string=input("Enter the About Me Section or string :")
split_string = my_string.split()
my_dict={}
for elem in split_string:
   if(elem[0] not in my_dict.keys()):
      my_dict[elem[0]]=[]
      my_dict[elem[0]].append(elem)
   else:
      if(elem not in my_dict[elem[0]]):
         my_dict[elem[0]].append(elem)
print("The dictionary created is")
for k,v in my_dict.items():
   print(k,":",v)