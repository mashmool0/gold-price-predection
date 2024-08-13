def columns_values(x,y) :     # 
    values = x 
    lst = ['O','H','L','C']
    
    try : 
        detail = values[values.index('−'):]
        values = values[:values.index('−')]
    except : 
        detail = values[values.index('+'):]
        values = values[:values.index('+')]

    detail = detail.split(' ')

    for i in values : 
        if i in lst : 
            values = values.replace(i,' ')
        
    values = values.split(' ')[1:]

    for i in range(len(values)) : 
        values[i] = float(values[i])        

    for i in detail : 
        if '+' in i and '(' in i : 
            i = float(i[2:i.index('%')])  * 100 
        elif '−' in i and '(' in i : 
            i = float(i[2:i.index('%')])    * -100     
        elif '+' in i and '(' not in i : 
            i = float(i[1:])
        elif '−' in i and '(' not in i : 
            i = float(i[1:]) * -1 

            
        values.append(i)
    values.append(y*1000)
    
    return values 



     


    