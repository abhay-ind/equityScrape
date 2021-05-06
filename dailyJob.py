from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from zipfile import ZipFile
from io import StringIO,BytesIO
import pandas as pd
from redislite import Redis
req = Request('https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req)
soup=BeautifulSoup(webpage,'html.parser')
link=soup.find(id='ContentPlaceHolder1_btnhylZip')
req = Request(link['href'], headers={'User-Agent': 'Mozilla/5.0'})
data=urlopen(req)
myzip = ZipFile(BytesIO(data.read()))
file=myzip.extract(myzip.namelist()[0])
df=pd.read_csv(file)
# print(df)
redis_instance = Redis('/tmp/redis.db')

# redis_instas                       port=6379, db=0)
filteredDF=df[["SC_CODE","SC_NAME","OPEN","HIGH","LOW","CLOSE"]]
for i in filteredDF.index:
    l=[filteredDF['SC_CODE'][i],filteredDF['OPEN'][i],filteredDF['HIGH'][i],filteredDF['LOW'][i],filteredDF['CLOSE'][i]]
    redis_instance.set(filteredDF['SC_NAME'][i],str(l))