import bs4 as bs
import pickle
import requests
from urllib import request

def get_investment_fund():
    url = "https://uk.finance.yahoo.com/quote/0P00019YY3.L?p=0P00019YY3.L&.tsrc=fin-srch"
    html = request.urlopen(url).read().decode('utf8')
    html[:60]
    soup = bs.BeautifulSoup(html, 'html.parser')
    title = soup.find('title')
    print(title.string)

    test = soup.find(class_='Ta(end) Fw(600) Lh(14px)')

    print(test)

get_investment_fund()
