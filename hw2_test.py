'''
def loadCatalog(file):
    with open(file, "r") as f:
        course_info = f.read()
    lst=course_info.split("\n")
    temp=[]
    for i in range(len(lst)):
        temp.append(lst[i].split(','))
    
    for i in range(len(temp)):
        #temp[i][2]=int(temp[i][2])
        param=' , '.join(temp[i])
    return param


x=loadCatalog("cmpsc_catalog_small.csv")
print(x)
'''
d={'one':1}
def remove(d,key):
    if key not in d:
        return f'No such course'
    else:
        d[key]-=d
    return d 
x=remove(d,'one')
print(x)
