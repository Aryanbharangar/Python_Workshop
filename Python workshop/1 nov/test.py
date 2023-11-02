# dict={"x":10,"y":20,"z":30}
# for key,value in dict.items():
#     print(F"{key}:{value}")

# 4
# n=int(input("Enter a number:"))
# dict={}
# for i in range(1,n+1):
#     key=i
#     value=i*i
#     dict[key]=value
# print(dict)

#12
color_dict={'red':"#FF0000",'green':'#008000','black':'#00000','white':'#FFFFF'}
d=list(color_dict)
d.sort()
color_dict=dict(d)
print(color_dict)









#5
# dict={num:num**2 for num in range(1,16)}
# print(dict)
     
#08
# dicto={"value1":23,"value2":30,"value3":63}
# sum=0
# for i in dicto.values():
#     i+=i
# print(i)
#or  print(sum(dicto.values()))  