



def two_sum(num,target):

    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if i + j == target:
                print(f"{i},{j}")
            
numbers = {2,4,6,7,8,9}     
print(two_sum(numbers,5))

