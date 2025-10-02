import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('https://github.com/ricardoahumada/data-for-auditors/raw/refs/heads/main/3.%20Procesamiento%20de%20Datos%20con%20ETLs/3.3.Visualizacion/Pokemon.csv', index_col=0, encoding='latin')

sns.lmplot(x='Attack', y='Defense', data=df)
