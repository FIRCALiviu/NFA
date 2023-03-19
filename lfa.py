
def bct(current_state,word,level):
    global s
    if len(word)==0:
        if current_state in final_states:
            buffer.append(s[:level])

    else:
        letter=word[0]
        if delta.get(current_state+' '+letter) is None:
            return
        else:
            for state in delta[current_state+' '+letter]:
                s[level]="{} {}".format(letter,state)
                bct(state,word[1:],level+1)
                
                


    

if __name__=='__main__':
    
    delta=dict()
    while True:
        current=input()
        if current.lower()=='stop':
            break
        else:
            current_state,letter,next_state=current.split()
            key=current_state+" "+letter
            if delta.get(key)== None:
                delta[key]=[next_state]
            else:
                delta[key].append(next_state)
    s=[None]*1100    
    final_states=input().split()
    initial_state=input()

    

    while True:
        current=input()
        if current.lower()=='stop':
            break
        else:
            buffer=[]
            bct(initial_state,current,0)
            if len(buffer)==0:
                print("not accepted")
            else:
                print('accepted')
                for path in buffer:
                    print(*path)
    
    

