import ply.yacc as yacc
from analizadorLex import AnalizadorLexico
tokens = AnalizadorLexico.tokens



def p_blockSentence(p): 
    '''blockSentence : T sentence T blockSentence   
    | T sentence T 
    '''
    if(len(p)==5):
        if(p[2] is None):
            p[2]=''
        if(p[4] is None):
            p[4]=''     
        p[0]=p[2] + '\n' + p[4]

    elif(len(p)==4):
        if(p[2] is None):
            p[2]=''
        if('\n' in p[2]):
            p[0]=p[2]
        else:
            p[0]=p[2]

def p_T(p):
    '''T : T newline
    |
    '''
def p_sentence(p):
    '''sentence : assign
    | select
    | iter
    '''
    p[0]=p[1]



def p_elseIf(p):
    '''elseIf : elsif exprCond then_tok T blockSentence label
    |
    '''
    if len(p)==1 :
        p[0]=''
    else:
        #p[0]= str(p[2])
        temp2=''
        flag=False  
        if(len(queue_cond)!=0):
            a=queue_cond.pop(0)
            flag=True
        while(len(queue_cond)!=0):
            temp2+=a+'\n'
            a=queue_cond.pop(0)
        if(flag):
            temp2+=a
        p[0]= temp2+'ifFalse ' + str(p[2])+' goto '+str(p[6][:-1]) + '\n' + str(p[5]) +'\n' + 'goto '+ end_label[-1] +'\n' +str(p[6])

def p_ELSE(p):
    '''ELSE : else blockSentence
    |
    '''
    if len(p)==1 :
        p[0]=''
    else:
        p[0]= str(p[2])
            
    
def p_exprCond(p):
    '''exprCond : expr less expr
    | expr equals equals expr
    | expr great expr
    | expr great equals expr
    | expr less equals expr
    ''' 
    if(len(p)==4):
        flag=False
        if(len(queue)!=0):
            a=queue.pop(0)
            flag=True
        while(len(queue)!=0):
            queue_cond.append(a)
            a=queue.pop(0)
        if(flag):
            queue_cond.append(a)
        if(('=' in str(p[1])) or ('=' in str(p[3]))):
            temp1=''
            if('=' in str(p[1])):
                i=''    
                for i in str(p[1]):
                    if '=' not in i:
                        temp1+=i
                    else:
                        break
                queue_cond.append(p[1])             
                p[1]=temp1
            temp2=''
            if('=' in str(p[3])):
                i=''
                for i in str(p[3]):
                    if '=' not in i:
                        temp2+=i
                    else:
                        break
                queue_cond.append(p[3])             
                p[3]=temp2  
        p[0] = str(p[1]) + ' ' + str(p[2]) + ' ' + str(p[3])

    else:
        flag=False
        if(len(queue)!=0):
            a=queue.pop(0)
            flag=True
        while(len(queue)!=0):
            queue_cond.append(a)
            a=queue.pop(0)
        if(flag):
            queue_cond.append(a)
        if(('=' in str(p[1])) or ('=' in str(p[3]))):
            temp1=''
            if('=' in str(p[1])):
                i=''    
                for i in str(p[1]):
                    if '=' not in i:
                        temp1+=i
                    else:
                        break
                queue_cond.append(p[1])             
                p[1]=temp1
            temp2=''
            if('=' in str(p[4])):
                i=''
                for i in str(p[4]):
                    if '=' not in i:
                        temp2+=i
                    else:
                        break
                queue_cond.append(p[4])             
                p[4]=temp2  
        p[0] = str(p[1]) + ' ' + str(p[2]) + str(p[3]) + ' ' + str(p[4])    
        

def p_assign(p):
    '''assign : lhs equals expr
    '''
    temp1=''
    temp2=''
    if('=' in str(p[3])):
        i=''    
        for i in str(p[3]):
            if '=' not in i:
                temp1+=i
            else:
                break
        queue.append(p[3])              
        p[3]=temp1
        a=queue.pop(0)      
        while(len(queue)!=0):
            temp2+=a +'\n'
            a=queue.pop(0)
        temp2+=a
    try:
        a=int(p[3])
        symbol_table[p[1]]=a
        #print('symbol table updated')
        #print(symbol_table)
    except:
        symbol_table[str(p[1])]='defined'
    p[0]=temp2 + str(p[1]) + ' ' + str(p[2]) + ' ' + str(p[3])

def p_lhs(p):
    '''lhs : name
    '''
    p[0]=p[1]
    #print(p[1])
def p_expr(p):
    '''expr : expr plus expr
    | expr minus expr
    | expr times expr
    | expr divide expr
    | name
    | number
    '''
    if(len(p)==4):
        global temp_counter
        if(('=' in str(p[1])) or ('=' in str(p[3]))):
            temp1=''
            #print(p[1],"hello")
            if('=' in str(p[1])):
                i=''    
                for i in str(p[1]):
                    if '=' not in i:
                        temp1+=i
                    else:
                        break
                queue.append(p[1])              
                p[1]=temp1
            #print(p[1],"hello")
            temp2=''
            if('=' in str(p[3])):
                i=''
                for i in str(p[3]):
                    if '=' not in i:
                        temp2+=i
                    else:
                        break
                queue.append(p[3])              
                p[3]=temp2  
            #print(p[1],p[3])
        p[0]='t'+str(temp_counter)+' = '+str(p[1])+' '+str(p[2])+' '+str(p[3]) + '\n'
        temp_counter+=1
    elif(len(p)==2): #check in symbol table here
        try:
            int(p[1])
        except ValueError:
            if(symbol_table[p[1]]==None):
                raise ValueError("Variable "+ str(p[1])+ ' has not been defined')
        p[0]=p[1]
    

def p_select(p):
    '''select : if exprCond EMPTQC then_tok T BLOCKSTMT LABELMAKER LABEL_E ELSIF ELSE end 
    '''
    global end_label
    a=end_label.pop()
    p[0] = p[3]+'ifFalse ' + str(p[2]) +' '+ 'goto' + ' ' +p[7][:-1] +'\n'+ str(p[6])+'\n'+'goto '+ a + '\n'+ str(p[7]) + str(p[9])+ '\n' + str(p[10])+'\n' + a + ':'   
    
def p_LABEL_E(p):
    '''LABEL_E :'''
    global label_counter
    end_label.append('L'+str(label_counter))
    label_counter+=1

def p_emptQC(p):
    '''emptQC :'''
    temp2=''
    flag=False  
    if(len(queue_cond)!=0):
        a=queue_cond.pop(0)
        flag=True
    while(len(queue_cond)!=0):
        temp2+=a+'\n'
        a=queue_cond.pop(0)
    if(flag):
        temp2+=a
    p[0]=temp2


def p_label(p):
    '''label :'''
    global label_counter
    p[0]="L" + str(label_counter)+':'
    label_counter+=1



    

def p_iter(p):
    '''iter : while label exprCond emptQC do T blockSentence T end label
    '''
    p[0]= str(p[2]) + str(p[4]) + '\n' +'ifFalse ' + p[3] + ' goto ' + p[10][:-1] + '\n' + p[7] + '\n' + 'goto ' + str(p[2][:-1]) + '\n' + p[10]   
    
    



parser = yacc.yacc()

while True:
    try:
        s = input('>>')
    except EOFError:
        break
    if not s: continue
    resultado = parser.parse(s)
    print(resultado)


