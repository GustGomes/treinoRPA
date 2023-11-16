import pandas as pd
import rpa as r
import json
import re

#r.init(turbo_mode=True)
#Download json
#r.url('https://www.4devs.com.br/gerador_de_pessoas/')
#r.wait(5)
#r.type('//*[@id="txt_qtde"]','1')
#r.click('//*[@id="bt_gerar_pessoa"]')
#r.wait(3)
#r.click('//*[@id="area_resposta_json"]/div/button[1]')

# leitura e extração dados json
data = pd.read_json(r"C:\Users\gusta\PROJETOS\pyprojects\data.json")
#print(data)

#caminho onde vai ficar o txt
txt = (r"C:\Users\gusta\PROJETOS\pyprojects\data_formatada.txt")

# salva os dados em um arquivo txt, separados por um tab
data.to_csv(txt, sep='\t', index=False) 

