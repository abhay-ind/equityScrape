import pandas as pd
from redislite import Redis
redis_instance = Redis('/tmp/redis.db')
filteredDF=pd.read_csv("../wholedownload(2).csv")
for i in filteredDF.index:
    l=[filteredDF['CODE'][i],filteredDF['OPEN'][i],filteredDF['HIGH'][i],filteredDF['LOW'][i],filteredDF['CLOSE'][i]]
    redis_instance.set(filteredDF['NAME'][i],str(l))
