import pandas as pd
import robot

# Lendo o arquivo excel
df = pd.read_excel('cadastro_clientes.xlsx')
robot.cadastro_web(df)
