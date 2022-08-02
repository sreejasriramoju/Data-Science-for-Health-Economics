df=pd.read_csv(r'C://Users//sreej//Downloads//Paschim Medinipur.csv',header=None)
df.rename(columns = {0:'State',1:'District',2:'From Date',3:'To Date',4:'TB Unit',5:'Public Notified'
                     , 6:'Private Notified'}, inplace = True)
#df['From Date']=pd.to_datetime(df['From Date'],dayfirst=True)
#df['From Date'] = df['From Date'].dt.strftime('%d-%m-%Y')
#df['From Date']=pd.to_datetime(df['From Date'],dayfirst=True)
df_t=pd.read_csv(r'C://Users//sreej//Downloads//Paschim Medinipur_tbu.xlsx - Paschim Medinipur_tbu.csv')
df3=pd.DataFrame(columns=['State','District','From Date','To Date',
                                                  'TB Unit','Public Notified','Private Notified','PHI','Microscopy','Cbnaat'])
s=0
while s<len(df):
    for i in range(len(df_t)):
        if df_t.iloc[i,2] == df.iloc[s,4]:
            df2 = pd.DataFrame([['West Bengal',df.iloc[s,1],df.iloc[s,2],df.iloc[s,3],
                                 df.iloc[s,4],df.iloc[s,5],df.iloc[s,6],df_t.iloc[i,4],df_t.iloc[i,6],df_t.iloc[i,7]]], columns=['State','District','From Date','To Date',
                                                     'TB Unit','Public Notified','Private Notified','PHI','Microscopy','Cbnaat'])
            df3=df3.append(df2)
    s=s+1
      
df3.to_csv('C://Users//sreej//Downloads//Paschim Medinipur_new.csv')
df3