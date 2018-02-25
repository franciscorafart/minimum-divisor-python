#function that finds minimum divisor

def divisor(n):
    #start with the value as it is true
    isFactor = True
    smallest = 10
    while(isFactor):
        for x in range(1,n):
            #if smallest isn't divisible by x, then isFactor is false and we break the for loop
            if(smallest%x != 0):
                isFactor = False
                break
        #after breaking the loop
        #if isFactor is false, we add 1 to smallest for next evaluation, and set isFactor back to True
        if isFactor==False:
            smallest += 1
            print(smallest)
            isFactor = True
        #if isFactor is true, we break the while loop and return smallest
        else:
            break

    return(smallest)
divisor(20)
