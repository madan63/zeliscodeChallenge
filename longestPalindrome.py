def Longpalindrome(st):
    palin = ''
    #checking whether given string itself a PALINDROME or not
    if st == st[::-1]:
        return f'{st} and is {len(st)} characters in length' 
    
    sub = ""
    s_iterator = st
    
    while len(s_iterator)>0:
        for char in s_iterator:
            sub = sub + char
            if len(sub)>1:
                if sub == sub[::-1]:
                    if len(sub) > len(palin):
                        palin = sub 
        sub=""
        s_iterator = s_iterator[1:]
        
    if palin:
        return f'{palin} and is {len(palin)} characters in length'
    else:
        return 'Palindrome not found in the given text'

test_words = ['vilkcwqdvbnoiehuaykiyrqtxejxoylihebckruwminfjkhzucrpymumalayalamkxbfvpfjhvkaeobecunzesiognzfmlkaortyudeshtfutsanxyqtnaowvrqhygogfjisjksmradqeblweypacbwqaosburgnxmcpjlfrticjhltbrkozlyemwjzyqvupqejgzsswhdegdobnslihexoccipwlybwckqgqnftmsthmadambgpugczqpknzpstfeafcuk', 
              'vilkcwqdvbiycnwtdlwrjpztuxrcbiuodpxvahvezwfdperjhxpkunoiehuaykiyrqtxejxoylihebckruwminfjkhzucrpymukxbfvpfjhqymrxbnyenvkaeobecunzesiognzfmlkaortyudeshtfutsanxyqtnaowvrqhygdogfjisjksmradqeblweypacbwqaosburgnxmcpjlfrticjhltbrkozlyemwjzyqvupqejgzskasdfswhdegdobnslihexocipwlybwckqgaqnftmsthbgpugczqpknzpstfeafcuk',
              'madam']

if __name__ == '__main__':
    for testword in test_words:
        ans = Longpalindrome(testword)
        print(ans)
