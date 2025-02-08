import cloudscraper
import pandas as pd
from bs4 import BeautifulSoup


def get_trending_stocks():
    sc = cloudscraper.create_scraper()
    page = sc.get("https://in.investing.com/")
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table', {'class': 'common-table js-table js-streamable-table'})

    headers = []
    for i in table.find_all('th'):
        title = i.text
        headers.append(title)
    headers = ['', 'Name', 'Last', 'High', 'Low', 'Chg', '%Chg', 'Volume', 'Time']

    mydata = pd.DataFrame(columns=headers)

    rows = table.find_all('tr')
    for row in rows[1:]:
        cells = row.find_all(['td'])
        cells_text = [cell.get_text(strip=True) for cell in cells]
        length = len(mydata)
        mydata.loc[length] = cells_text
        mydata.to_csv('trending_stock_info.csv', index=False)


def get_most_active_stocks():
    sc = cloudscraper.create_scraper()
    page = sc.get("https://in.investing.com/equities/most-active-stocks")
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table', {'class': "common-table medium js-table js-streamable-table"})

    header = []
    for i in table.find_all('th'):
        title = i.text
        header.append(title)
    header = ['', '', 'Name', 'Last', 'High', 'Low', 'Chg', '%Chg', 'Volume', 'Time']

    mydata = pd.DataFrame(columns=header)
    rows = table.find_all('tr')
    for row in rows[1:]:
        cells = row.find_all(['td'])
        cells_text = [cell.get_text(strip=True) for cell in cells]
        length = len(mydata)
        mydata.loc[length] = cells_text
        mydata.to_csv('most_active_stock_info.csv', index=False)


def get_top_stock_gainers():
    sc = cloudscraper.create_scraper()
    page = sc.get("https://in.investing.com/equities/top-stock-gainers")
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table', {'class': "common-table medium js-table js-streamable-table"})
    # print(table)

    header = []
    for i in table.find_all('th'):
        title = i.text
        header.append(title)
    header = ['', '', 'Name', 'Last', 'High', 'Low', 'Chg', '%Chg', 'Volume', 'Time']
    # print(header)

    mydata = pd.DataFrame(columns=header)
    rows = table.find_all('tr')
    for row in rows[1:]:
        cells = row.find_all(['td'])
        cells_text = [cell.get_text(strip=True) for cell in cells]
        length = len(mydata)
        mydata.loc[length] = cells_text
        # print(cells_text)

        mydata.to_csv('top_stock_gainers_info.csv', index=False)

def get_top_stock_losers():
    sc = cloudscraper.create_scraper()
    page = sc.get("https://in.investing.com/equities/top-stock-losers")
    soup = BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table', {'class': "common-table medium js-table js-streamable-table"})
    # print(table)

    header = []
    for i in table.find_all('th'):
        title = i.text
        header.append(title)
    header=['', '', 'Name', 'Last', 'High', 'Low', 'Chg', '%Chg', 'Volume', 'Time']
    # print(header)

    mydata = pd.DataFrame(columns=header)
    rows = table.find_all('tr')
    for row in rows[1:]:
        cells = row.find_all(['td'])
        cells_text = [cell.get_text(strip=True) for cell in cells]
        length = len(mydata)
        mydata.loc[length] = cells_text
        # print(cells_text)

        mydata.to_csv('top_stock_losers_info.csv', index=False)

def get_stock_data(url):
    sc = cloudscraper.create_scraper()
    page = sc.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    company = soup.find('h1', {'class': 'main-title js-main-title'}).find_all('span')[0].text
    price = soup.find('bdo', {'class': 'last-price-value js-streamable-element'}).text
    try:
        change = soup.find('bdo', {'class': 'text u-down js-streamable-element'}).text
    except(BaseException):
        change = soup.find('bdo', {'class': "text u-up js-streamable-element"}).text

    return [company, price, change]


# get_trending_stocks()
# get_most_active_stocks()
# get_top_stock_gainers()
# get_top_stock_losers()

# print(get_stock_data("https://in.investing.com/equities/reliance-industries"))
# hiraku