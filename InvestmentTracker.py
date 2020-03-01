import bs4 as bs
import pickle
import requests
from urllib import request
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def get_investment_fund():
    url = "https://uk.finance.yahoo.com/quote/0P00019YY3.L?p=0P00019YY3.L&.tsrc=fin-srch"
    html = request.urlopen(url).read().decode('utf8')
    html[:60]
    soup = bs.BeautifulSoup(html, 'html.parser')
    title = soup.find('title')
    print(title.string)

    test = soup.find(class_='Ta(end) Fw(600) Lh(14px)')

    print(test)

def gui():
    #labels = ["AJ Bell Balanced ", "FTSE 250", "HSBC"]
    x = np.linspace(0, 10, 100)
    #y = np.linspace(50, 45, 2)

    # Plot data
    plt.plot(x, x, label='AJ Bell Balanced Fund')
    plt.plot(0, 0, label='FTSE 250')
    plt.plot(0, 0, label='HSBC')

    plt.ylabel('Value', fontsize=14, color='blue')
    plt.xlabel('Time', fontsize=14, color='red')
    fig2 = plt.gcf()
    fig2.canvas.set_window_title('Pyvestment')

    plt.legend(title='Investments')
    plt.show()

print(pd.__version__)
get_investment_fund()
gui()

