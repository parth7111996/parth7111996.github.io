import my_module

t = int(input())
for i in range(0, t):
    
    age = int(input())         
    p = my_module.Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")