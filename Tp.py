def high(inputs):
    max=inputs[-1]
    for x in inputs:
        if x > 0 :
            if x <= 100:
                
               if x > max :
                  max=x
    return max            
inputs=[]
while True:
    inp=input()
    if int(inp) < 0:
        break
    inputs.append(int(inp))
print(high(inputs))
