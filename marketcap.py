import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt 
import squarify as sq

url='https://companiesmarketcap.com/investment/largest-investment-companies-by-market-cap/'
response=requests.get(url)
soup=BeautifulSoup(response.text,'lxml')
rows=soup.findChildren('tr')

symbols=[]
market_caps=[]
sizes=[]

for row in rows:
    try:
        symbol=row.find('div',{'class':'company-code'}).text
        market_cap=row.findAll('td')[2].text
        market_caps.append(market_cap)
        symbols.append(symbol)
        
        if market_cap.endswith("T"):
            sizes.append(float(market_cap[1:-2])*10**12)
        elif market_cap.endswith("B"):
            sizes.append(float(market_cap[1:-2])*10**9)
            
    except AttributeError:
        pass
    
labels=[f"{symbols[i]}\n({market_cap[i]})" for i in range(len(symbols))]
colors=[plt.cm.SpectralColor(i/float(len(symbols))) for i in range(len(symbols))]
sq.plot(sizes=sizes,labels=labels,color=colors,bar_kwargs={"linewidth":0.5,"edgecolor":"#111111"})
plt.show()