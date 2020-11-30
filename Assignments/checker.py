import numpy as np
import pandas as pd

data_ = pd.DataFrame({'col1' : [0,1,2,3,4,0,1,2,3,4]})
data1_ = pd.Series([0,1,2,3,4,0,1,2,3,4])

def checker1(answer) :
    
    try : 
        if answer(data_)[0] == 10 :
            print('정답입니다!! 다음 단계로 넘어가셔도 좋습니다.')
        else :
            print('다시 한번 생각해보세요')

    except : 
        print('다시 생각해보세요')

def checker2(answer) :
    
    try : 
        if answer(data_).equals(pd.DataFrame({'col1' : range(5)})) :
            print('정답입니다!! 다음 단계로 넘어가셔도 좋습니다.')
        else :
            print('다시 한번 생각해보세요')

    except : 
        print('다시 생각해보세요')
        
def checker3(answer) :
    
    try : 
        if answer(data1_).equals(pd.Series({4: 2, 3: 2, 2: 2, 1: 2, 0: 2})) :
            print('정답입니다!! 다음 단계로 넘어가셔도 좋습니다.')
        else :
            print('다시 한번 생각해보세요')

    except : 
        print('다시 생각해보세요')