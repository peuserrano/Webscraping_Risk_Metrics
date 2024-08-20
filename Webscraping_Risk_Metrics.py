import pandas as pd
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

class CDSDataScraper:
    
    def __init__(self, headers):
        self.headers = headers
        self.lista_dfs = []

    def fetch_data(self, ano_cds):
        url = f'https://br.investing.com/rates-bonds/brazil-{ano_cds}-usd-historical-data'
        req = Request(url, headers=self.headers)
        page = urlopen(req)
        soup = BeautifulSoup(page, features='lxml')
        
        table = soup.find_all("table")[0]
        df_cds = pd.read_html(str(table))[0][['Último', 'Data']]
        df_cds = df_cds.set_index("Data")
        df_cds.index = pd.to_datetime(df_cds.index, format="%d.%m.%Y")
        df_cds.columns = [ano_cds]
        
        self.lista_dfs.append(df_cds)
        
    def get_combined_data(self):
        return pd.concat(self.lista_dfs, axis=1)

if __name__ == "__main__":
    
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    
    lista_cds = ['cds-1-year', 'cds-2-years', 'cds-3-years', 
                 'cds-4-years', 'cds-5-years', 'cds-7-years', 'cds-10-years']

    scraper = CDSDataScraper(headers)

    for ano_cds in lista_cds:
        scraper.fetch_data(ano_cds)

    base_cds = scraper.get_combined_data()
    print(base_cds)
