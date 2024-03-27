import re

def text2num(text, res=0):
    num = 0
    master = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6,
              'seven':7, 'eight':8, 'nine':9, 'ten':10, 'eleven':11, 
              'twelve':12, 'thirteen':13, 'fourteen':14, 'fifteen':15,
              'sixteen':16, 'seventeen':17, 'eighteen':18, 'ninteen':19, 
              'twenty':20, 'thirty':30, 'fourty':40, 'fifty':50, 'sixty':60,
              'seventy':70, 'eighty':80, 'ninty':90, 'hundred':100, 
              'thousand': 1000, 'million': 1000000}
    ones = [1,2,3,4,5,6,7,8,9]
    mults = [100, 1000, 1000000]
    
    if text in master:
        dig = master.get(text, 'invalid text')
        if dig not in mults:
            return res + dig
        else:
            return res * dig

tests = ['four', 'fourty', 'negative four', 'negative fourteen', 'negative fourty', 'fourty four', 
         'four hundred', 'four hundred fourty', 'four hundred fourty four']
for test in tests:
    ans = test.split() if ' ' in test else test
    if isinstance(ans, str):
        number = text2num(ans)
        print(f'{test} => {number}')

    elif len(ans) == 2 and re.match('negative', test):
        number = 0 - text2num(test.split()[1])
        print(f'{test} => {number}')

    elif len(ans) == 2:
        res = text2num(test.split()[0])
        number = text2num(test.split()[1], res)
        print(f'{test} => {number}')





