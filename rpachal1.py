import pandas as pd
import rpa as r

#leitura e captura dos dados
df = pd.read_excel(r"C:\Users\gusta\PROJETOS\pyprojects\rpa\challenge.xlsx")
# verifica os dados
# print(df)
r.init(turbo_mode=True)

#abre nav
r.url('http://www.rpachallenge.com/')
r.wait(5)
#começa o desafio
r.click('/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button')
#insere os dados nos campos
for index,row in df.iterrows():
    r.type('//input[@ng-reflect-name="labelFirstName"]',row['First Name'])
    r.type('//input[@ng-reflect-name="labelLastName"]',row['Last Name '])
    r.type('//input[@ng-reflect-name="labelCompanyName"]',row['Company Name'])
    r.type('//input[@ng-reflect-name="labelRole"]',row['Role in Company'])
    r.type('//input[@ng-reflect-name="labelAddress"]',row['Address'])
    r.type('//input[@ng-reflect-name="labelEmail"]',row['Email'])
    r.type('//input[@ng-reflect-name="labelPhone"]',str(row['Phone Number']))
    r.click('//input[@value="Submit"]')

#Print da pagina
#r.snap('/html/body/app-root/div[2]','resultado.png')
#fecha o processo 
#r.close()
