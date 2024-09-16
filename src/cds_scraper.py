import pandas as pd
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import time

class CDSDataScraper:

    """
    Uma classe para fazer scraping de dados de CDS do Brasil a partir do site Investing.com.

    Atributos:
    ----------
    headers : dict
        Cabeçalhos HTTP para emular uma requisição feita por um navegador.
    lista_dfs : list
        Lista que armazena DataFrames de CDS para diferentes prazos.

    Métodos:
    --------
    fetch_data(ano_cds):
        Faz a requisição dos dados para o prazo de CDS especificado.
        
    get_combined_data():
        Retorna um DataFrame combinando todos os prazos de CDS coletados.
    """
    
    def __init__(self, headers):
        """
        Inicializa o scraper com os cabeçalhos HTTP fornecidos e uma lista vazia para armazenar DataFrames

        Args:
            headers (dict): Dicionário contendo os cabeçalhos HTTP para as requisições
        """
        self.headers = headers
        self.lista_dfs = []

    def fetch_data(self, ano_cds):
        """
        Faz  a requisição e coleta os dados de CDS com as durações especificadas

        Args:
            ano_cds(str): String representando o CDS a ser coletado (ex: 'cds-5-years').
        """

        url = f'https://br.investing.com/rates-bonds/brazil-{ano_cds}-usd-historical-data'
        req = Request(url, headers=self.headers)
        
        try:
            page = urlopen(req)
            soup = BeautifulSoup(page, features='lxml')
            
            table = soup.find_all("table")[0]
            df_cds = pd.read_html(str(table))[0][['Último', 'Data']]
            df_cds = df_cds.set_index("Data")
            df_cds.index = pd.to_datetime(df_cds.index, format="%d.%m.%Y")
            df_cds.columns = [ano_cds]
            
            self.lista_dfs.append(df_cds)
        
        except Exception as e:
            print(f'Erro ao coletar dados para {ano_cds}: {e}')
            return None
        
        time.sleep(2) # Pausa para evitar sobrecarga no servidor

    def get_combined_data(self):
        """
        Combina todos os DataFrames coletados em um único DataFrame.

        Returns:
            pd.DataFrame: DataFrame contendo todos os dados de CDS coletados.
        """
        if self.lista_dfs:
            return pd.concat(self.lista_dfs, axis=1)
        else:
            print("Nenhum dado foi coletado.")
            return pd.DataFrame()

