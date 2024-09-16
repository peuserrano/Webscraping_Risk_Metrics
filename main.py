from src.cds_scraper import CDSDataScraper
from src.eda import plot_cds_data, correlation_matrix

if __name__ == "__main__":
    
    # Configuração dos headers
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    
    # Lista dos prazos de CDS
    lista_cds = ['cds-1-year', 'cds-2-years', 'cds-3-years', 
                 'cds-4-years', 'cds-5-years', 'cds-7-years', 'cds-10-years']
    
    # Coleta de dados
    scraper = CDSDataScraper(headers)
    
    for ano_cds in lista_cds:
        scraper.fetch_data(ano_cds)
    
    base_cds = scraper.get_combined_data()
    
    # Análise Exploratória dos Dados
    print(base_cds.describe())
    plot_cds_data(base_cds)
    correlation_matrix(base_cds)
