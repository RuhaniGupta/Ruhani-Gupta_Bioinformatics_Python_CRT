JobRole={101:'Full Stack Developer',102:'Data Analyst',103:'Data Science',104:'Data Engineer'}
print(JobRole)
JobRole[105]='Cloud Engineer'
print(JobRole)
#more Job roles
JobRole.pop(101)
print(JobRole)
print(len(JobRole))
print(JobRole.keys())
print(JobRole.values())
print(JobRole.items())
print(JobRole.copy())
#Update method
Dict1={1:'a',2:'b',3:'c',4:'d'}
print(Dict1)
Dict2={5:'e',6:'f',7:'g'}
print(Dict1)
Dict1.update(Dict2)
print(Dict1)