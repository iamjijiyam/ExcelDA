import pandas as pd

data = { '이름' : ['유정', '유나', '민영', '은지']
         '나이' : [30, 28, 31, 29]
         '생일' : ['1991.5.2', '1993.4.6', '1990.9.12', '1192.7.19']}
df1 = pd.DataFrame(data)
df1
df2 = pd.DataFrame(data, index=['하나', '둘', '셋','넷'])
df2 