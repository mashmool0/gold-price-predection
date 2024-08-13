import pandas as pd 

def create_dataframe(data,index) : 
    df = pd.DataFrame(data=data,columns=['Open','High','Low','Close','detail','dt_percent','Volume'],index=index)
    df.index.name = 'Date'
    return df 

