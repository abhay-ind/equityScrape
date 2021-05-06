import pandas as pd
from redislite import Redis
import os
redis_instance = Redis(os.path.join('/tmp/redis.db'))
filteredDF=pd.read_csv("../wholedownload.csv")
for i in filteredDF.index:
    l=[filteredDF['CODE'][i],filteredDF['OPEN'][i],filteredDF['HIGH'][i],filteredDF['LOW'][i],filteredDF['CLOSE'][i]]
    redis_instance.set(filteredDF['NAME'][i],str(l))
