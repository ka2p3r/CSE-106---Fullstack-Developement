print('Press Enter to mark the end of numbers')
l =input('please enter the numbers\n').split()

ans=0.0
flg = True
if len(l)<2:
    print('More numbers required')
    exit()
else:
    for var in l:
        try:
            x = float(var)
            ans=ans+x
        except:
            print(f'the value {var} is not an integer or float')
            flg=False
            break

if flg == True:
    print(ans)