# CDS Brazil Data Scraper

Este projeto consiste em um scraper para coletar dados históricos de Credit Default Swaps (CDS) do Brasil a partir do site Investing.com. O objetivo é fornecer uma base de dados consolidada para análise de risco soberano e outras aplicações financeiras.

## Funcionalidades

- Coleta dados de diferentes prazos de CDS (1 ano, 2 anos, 5 anos, etc.).
- Combina os dados coletados em um único DataFrame para fácil análise.
- Tratamento de erros para lidar com possíveis mudanças na estrutura da página ou problemas de conexão.

## Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/peuserrano/Webscraping_Risk_Metrics.git
   cd Webscraping_Risk_Metrics

2. Instale as dependências:

   ```bash
   pip install -r requirements.txt

## USO

No script principal, você pode ajustar os prazos de CDS que deseja coletar e iniciar o processo:
```bash
if __name__ == "__main__":
    headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}
    lista_cds = ['cds-1-year', 'cds-2-years', 'cds-3-years', 'cds-4-years', 'cds-5-years', 'cds-7-years', 'cds-10-years']

    scraper = CDSDataScraper(headers)

    for ano_cds in lista_cds:
        scraper.fetch_data(ano_cds)

    base_cds = scraper.get_combined_data()
    print(base_cds)

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e enviar pull requests.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
