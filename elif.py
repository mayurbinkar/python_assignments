



def do_Operations(val1,val2,op):

    return_Result = None
    print(val1,val2,op)
    if(op == 'add'):
        return_Result = val1+val2
        print(f'{val1}+{val2} = {return_Result}')
        return val1+val2
    elif(op == 'sub'):
        return_Result = val1 - val2
        print(f'{val1}-{val2} = {return_Result}')
        return return_Result
    
    elif(op == 'mul'):
        return_Result = val1 * val2
        print(f'{val1}*{val2} = {return_Result}')
        return return_Result
    
    elif(op == 'div'):
        return_Result = val1 / val2
        print(f'{val1}/{val2} = {return_Result}')
        return return_Result
    else:
        print('choose correct operation') 
        return 'choose correct operation'
    
    
print()
Add_result = do_Operations(4,2,'add')
print(f'Add_ result={Add_result}')

print()
Sub_result = do_Operations(10,6,'sub')
print(f'Sub_result = {Sub_result}')

print()
Mul_result = do_Operations(3,4,'mul')
print(f'Mul_result = {Mul_result}')

print()
Div_result = do_Operations(10,2,'div')
print(f'Div_result = {Div_result}')

checkNone = None
print(f'checkNone={checkNone}')


'''print(f'do_Operations={do_Operations}')
print('//////')
print('//////')
print('//////')

print(f'type of do_Operations = {type(do_Operations)}')
print('//////')
print('//////')
print('//////')'''


#do_Operations(4,2,'add')