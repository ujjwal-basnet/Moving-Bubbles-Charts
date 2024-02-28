import pandas as pd 
import numpy as np 

#defining time range with 5 min interval 
time_range = pd.date_range(start = '2024-02-29 00:00:00' , end = '2024-02-29 23:59:59',freq = '5min' )


# state  
states = ['home' , 'school' , 'work' , 'eating' , 'coffee'  , 'sleeping']

#we are creating 5 different person and their tiem span like when they go school , work , when they eat and drink cofee and sleep

#creating sample data for each individual movements 
sample1_data ={
    'datetime':time_range , 
    'state' : np.random.choice(states , len(time_range))  #taking random 288 data from list 
    
    
}

sample2_data = {
    'datetime' : time_range , 
    'state' : np.random.choice(states  , len(time_range))
}


sample3_date =  {
    'datetime' :time_range , 
    'state' :np.random.choice(states , len(time_range))
}

#creating dataframe for each sample 
df1  = pd.DataFrame(sample1_data)
df2 = pd.DataFrame(sample2_data)
df3 = pd.DataFrame(sample3_date)


#combining 
df = pd.concat(df1 , df2 , df2  , ignore_index = True) 
