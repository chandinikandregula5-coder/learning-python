'''num = 0
num_2 = 1
def fibnacci(num,num_2):
    limit_ = int(input("enter the limit:"))
    print(num,num_2,end=" ")
    for i in range(1,limit_):
        num_3 = num + num_2
        num = num_2
        num_2 = num_3
        print(num_3,end=" ")

        
fibnacci(num,num2)        
'''    
'''
any = [2,5,7,9,2,7]
new_ = []
def dup(any,new_):
    for j in any:
        if j not in new_:
            new_.append(j)
    print(new_)
dup(any,new)    
'''

count =0
so ="Haven’t found the right opportunity yet? Receive the latest updates on job opportunities, recruitment events and company news tailored just for you. otes through our Be Well program"

def word_str(so,count):
    for j in so:
        count += 1
    print(count)
word_str(so,count)    
