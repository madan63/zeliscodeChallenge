def wordFormation(masterCheck, pieces):
    #Collecting the pieces used for successful match in the masterCheck 
    used_pieces = []

    #below loop will form the combination of words using pieces 
    #while checking the piece of words are not found in 'used_pieces'
    for pie in pieces:
        whole = {pie+pi : (pie, pi) for pi in pieces if pi not in used_pieces 
                and pie not in used_pieces} 
        
        #output dict is used to campture the total attempts 
        #been made and the successful match
        output = {'found': '', 'attempts':[], 'one':''}
        
        if whole:
            for one in whole:
                if one in masterCheck:  #checks whether the 'one' 
                                        #found in the masterCheck
                    output['one'] = one
                    output['found'] = f'{one} => {whole[one][0]} + {whole[one][1]}'
                    used_pieces.append(whole[one][0])
                    used_pieces.append(whole[one][1])            

                else:
                    #Collecting the failure attempt  
                    atmpt = f'{whole[one][0]} + {whole[one][1]} => {one}'
                    output['attempts'].append(atmpt)
            
            #displaying the output
            if output['found']:
                print('------------')
                print(f"The word '{output['one']}' been found \
                    \n\t{output['found']}", end='\n')
                print(f"Below are the Failed attempts:")
                for attempt in output['attempts']:
                    print(f"\t{attempt} != {output['one']}")
        
#Given look up pool of words
words = ['albums', 'barely', 'befoul', 'convex', 'hereby', 'jigsaw', 
               'tailor', 'weaver']
#Given group of pieces
pieces = ['al', 'bums', 'bar', 'ely', 'be', 'foul', 'con', 'vex', 'here', 
          'by', 'jig', 'saw', 'tail', 'or', 'we', 'aver']

wordFormation(words, pieces)