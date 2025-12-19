string="banana"
dict={}
for i in string:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i]=1
   
print(dict)