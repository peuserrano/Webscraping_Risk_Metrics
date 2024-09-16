import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_cds_data(df):
    """
    Plota a evolução dos spreads de CDS ao longo do tempo.
    """

    plt.figure(figisize=(12,8))
    
    for column in df.columns:
        plt.plot(df.index, df[column], label=column)

    plt.title('Evolução dos Spreads de CDS ao longo do tempo')
    plt.xlabel('Período')
    plt.ylabel('Spread (bps)')
    plt.legend()
    plt.grid(True)
    plt.show()

def correlation_matrix(df):
    """
    Plota a matriz de correlação dos spreads de CDS
    """    

    correlation_matrix = df.corr()
    plt.figure(figsize=(10,8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Matriz de Correlação dos spreads de CDS')
    plt.show()
    