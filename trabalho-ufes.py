#Importando as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

"""Foi necessário dar rename em inúmeras sheets, pois elas estavam como "Unnamed", tive que printar as colunas do dataframe
e depois printar em específico as colunas para descobrir a coluna que continha as informações de interesse, depois de descobrir,
bastou renomear"""
#dropna() para excluir células vazias das planilhas
#header para ler as colunas de determinada linha em diante
ranking_df=pd.read_csv('ranking_folha.csv')
info_tabA_df= pd.read_excel('Tabelas de divulgação - 2022.xls' , sheet_name= 'Tab A',header=4).dropna() 
info_tabA_df.rename(columns={'Unnamed: 0': 'Ano'},inplace=True)

info_tabB_df= pd.read_excel('Tabelas de divulgação - 2022.xls' , sheet_name= 'Tab B',header=4).dropna() 
info_tab201_df= pd.read_excel('Tabelas de divulgação - 2022.xls' , sheet_name= 'Tab2.01',header=4).dropna()
info_tab201_df.rename(columns={'Unnamed: 0': 'Ano'},inplace=True)


info_tab203_df= pd.read_excel('Tabelas de divulgação - 2022.xls' , sheet_name= 'Tab2.03',header=4).dropna() 
info_tab205_df= pd.read_excel('Tabelas de divulgação - 2022.xls' , sheet_name= 'teste').dropna() 
"""
A tabela 2.05 estava com um problema, pois todos os cursos estão agrupados em determinado ano, então isso complicou muito a
filtragem de informações, quando eu dava o query pegava só a primeira informação, meu df ficou com 11 linhas, sendo que a tabela
tem cerca de 110. Dado isso, a única alternativa encontrada foi criar uma nova sheet, copiar e colar as informações de interesse, o
que deu certo, uma vez que, caso precisasse dos anos, poderia simplesmente dar iloc nas linhas de interesse dentro da minha coluna, como 
foi o caso na hora de calcular a média de ingressantes e concluintes
"""
info_tab206_df= pd.read_excel('Tabelas de divulgação - 2022.xls' , sheet_name= 'Tab2.06 e 2.07',header=4).dropna() 
info_tab303_df= pd.read_excel('Tabelas de divulgação - 2022.xls' , sheet_name= 'Tab3.03',header=4).dropna() 
info_tab303_df.rename(columns={'Unnamed: 0': 'Ano'},inplace=True)
info_tab303_df.rename(columns={'Unnamed: 6': 'Privadas'},inplace=True)
info_tab303_df.rename(columns={'Unnamed: 1': 'Total Geral'},inplace=True)

info_tab304_df= pd.read_excel('Tabelas de divulgação - 2022.xls' , sheet_name= 'Tab3.04',header=4).dropna() 

info_tab306_df= pd.read_excel('Tabelas de divulgação - 2022.xls' , sheet_name= 'Tab3.06',header=4).dropna() 
info_tab306_df.rename(columns={'Unnamed: 6': 'Mulheres'},inplace=True)
info_tab306_df.rename(columns={'Unnamed: 7': 'Homens'},inplace=True)

info_tab310_df= pd.read_excel('Tabelas de divulgação - 2022.xls' , sheet_name= 'Tab3.10',header=4).dropna() 
info_tab310_df.rename(columns={'Unnamed: 0': 'DF'},inplace=True)
info_tab310_df.rename(columns={'Unnamed: 1': 'Número matriculados'},inplace=True)



#PARTE 1 - CRESCIMENTO NAS MATRÍCULAS E INGRESSANTES, DESTAQUE PRO EAD + REDE PRIVADA + MULHERES 

#CONCLUSÃO PRIMEIRA PARTE: O NÚMERO DE MATRÍCULAS AUMENTOU AO LONGO DOS ANOS, SENDO QUE AS PÚBLICAS NÃO CONSEGUIRAM OFERTAR VAGA PARA TODOS, ENTÃO A PARTICULAR CRESCEU

with PdfPages('Gráficos.pdf') as pdf: #criando o pdf que conterá os gráficos
  #PRIMEIRA PÁGINA - MATRÍCULAS AO LONGO DOS ANOS + CRESCIMENTO DAS MATRICULAS COMPARADOS C CRESCIMENTO DA POPULAÇÃO (década a década)
  plt.figure(figsize=(8, 6)) #Definindo o tamanho da imagem
  plt.plot(info_tab303_df['Ano'], info_tab303_df['Total Geral'])
  plt.xlabel('Ano')
  plt.ylabel('Número de matrículas em milhões')
  plt.title('Aumento do número de matrículas ao longo dos anos',fontsize=18)
  plt.tight_layout() #comando para evitar overlap
  pdf.savefig()
  plt.close()

  #Segunda página - Comparação entre número de matriculados e crescimento populacional
  plt.figure(figsize=(8, 6))  
  alunos_1980 =info_tab303_df.query('Ano==1980')['Total Geral'] #Filtrando o total geral de matrículas década a década
  alunos_1990 =info_tab303_df.query('Ano==1990')['Total Geral'] #query para pegar uma coluna e escolher a linha dela desejada
  alunos_2000 =info_tab303_df.query('Ano==2000')['Total Geral']
  alunos_2010 =info_tab303_df.query('Ano==2010')['Total Geral']
  alunos_2020 =info_tab303_df.query('Ano==2020')['Total Geral']

  pop=[alunos_1980/122300000,alunos_1990/150700000,alunos_2000/175900000,alunos_2010/196400000,alunos_2020/213200000] #esses números se referem a população da década em questão
  anos=['1980','1990','2000','2010','2020'] #eixo x
  plt.plot(anos, pop)
  plt.xlabel('Ano')
  plt.title('Razão entre número de matriculados e número de habitantes',fontsize=13) #gráfico retrata a porcentagem de estudantes da população brasileira
  plt.tight_layout()
  pdf.savefig()
  plt.close()
  
  
  #Terceira página - COMPARAÇÃO ENTRE O NÚMERO DAS MATRÍCULAS EM PRIVADAS E PARTICULARES AO LONGO DOS ANOS
  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 6)) #subplots para colocar mais de um gráfico na mesma página
  plt.suptitle('Comparação entre número de matrículas em privadas e públicas (em milhões)',fontsize=12) #Título da página
  ax1.plot(info_tab303_df['Ano'], info_tab303_df['Privadas'])
  ax1.plot(info_tab303_df['Ano'], info_tab303_df['Total'])
  ax1.set_xlabel('Anos')
  ax1.set_ylabel('Comparação públicas e privadas') 
  ax1.legend(['Privadas','Públicas']) #Legendas para as cores das curvas
 
  anos=['1980','1990','2000','2010','2020']
  matriculas_privadas= info_tab303_df['Privadas'].iloc[[1,11,21,31,41]] #COmo eu sei as linhas de interesse, dei iloc para pegá-las
  matriculas_públicas=info_tab303_df['Total'].iloc[[1,11,21,31,41]]
  ax2.bar(anos, matriculas_privadas, color='blue')
  ax2.bar(anos, matriculas_públicas, color='red') #Gráfico de barras mostrando o aumento década a década
  ax2.set_ylabel("Proporção entre matrículas")
  ax2.set_xlabel("Anos")
  ax2.legend(['Privadas','Públicas'])
  
  plt.tight_layout()
  pdf.savefig()
  plt.close()

  #Quarta página - Aumento do número de cursos nos últimos 10 anos
  plt.plot(info_tabA_df['Ano'], info_tabA_df['Cursos']) #plotando de 2012 até 2022
  plt.xlabel('Anos')
  plt.ylabel('Número de cursos')
  plt.title('Aumento do número de cursos ao longo dos anos',fontsize=15)
  plt.tight_layout()
  pdf.savefig()
  plt.close()

  #página 5 - Aumento do número de matrículas EAD nos últimos 10 anos
  plt.plot(info_tab201_df['Ano'], info_tab201_df['A distância']) #Gráfico de curva mostrando o aumento das matrículas EAD
  plt.xlabel('Anos')
  plt.ylabel('Número de estudantes EAD')
  plt.title('Aumento exponencial do EAD',fontsize=20)
  plt.tight_layout()
  pdf.savefig()
  plt.close()

  #página 6 -Média superior de mulheres matriculadas nos últimos 8 anos
  plt.figure(figsize=(8, 6))
  media_mulheres=info_tab306_df['Mulheres'].mean() #Pegando todos o número de mulheres matriculadas e fazendo uma média
  media_homens=info_tab306_df['Homens'].mean()
  valores=[media_mulheres,media_homens] #Definindo os valores da pizza
  labels=['Mulheres','Homens'] #Definindo o que será escrito em cada parte da pizza
  plt.title('Comparação de matrículas entre sexos:',fontsize=20)
  plt.pie(valores,labels=labels, autopct='%1.1f%%', startangle=90,shadow=True,textprops={'fontsize': 12}) #Gráfico de setor mostrando o número médio de homens e mulheres matriculados 
  #autocpt para colocar em porcentagem. Startangle para definir um ângulo da pizza. Shadow e textpros para gerar ajustar o desing/layout
  plt.tight_layout()
  pdf.savefig()
  plt.close()

  
#PARTE 2 - cursos, ingressantes e concluintes
#página 7 - quantos por cento vão para cada um dos 3 cursos mais concorridos - média dos últimos 10 anos
  plt.figure(figsize=(8, 6))
  #Escolhi adm, ped e dir, pois este são os 3 cursos com maior número de ingressantes em todos os anos da pesquisa
  med_adm=info_tab205_df.query("cursos_ingressantes=='Administracao'")['num_ingressantes'].mean() #Média do número de ingressantes de ADM
  med_dir=info_tab205_df.query("cursos_ingressantes=='Direito'")['num_ingressantes'].mean() #Dei query para ir na coluna cursos ingressantes e pegar a linha que contém o curso de interesse
  med_ped=info_tab205_df.query("cursos_ingressantes=='Pedagogia'")['num_ingressantes'].mean()
  med_ingre=info_tab304_df['Total'].mean()
  soma=med_adm+med_dir+med_ped+med_dir 
  med_ingre-=soma #Tirando o número de ingressantes em cada um dos 3 cursos, para comparar quantos indíviduos entram nesses 3 cursos separadamente e nos demais
  valores=[med_adm,med_dir,med_ped,med_ingre]
  labels=['Administração','Direito','Pedagogia','Demais cursos']
  plt.title('Médias das 3 carreiras mais escolhidas',fontsize=18)
  plt.pie(valores,labels=labels, autopct='%1.0f%%', startangle=90,shadow=True,textprops={'fontsize': 10}) #Gráfico de setor mostrando o número médio de homens e mulheres matriculados 

  plt.tight_layout()
  pdf.savefig()
  plt.close()


#página 8 - Relação entre concluintes e ingressantes
  fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(11, 5)) #Novamente, fazendo subplots, dessa vez 3 gráficos na mesma página
  plt.suptitle('Porcentagem de concluintes',fontsize=20)
  """Como se demora no mínimo 4 anos para se formar em adm e ped e 5 em dir e meu dataframe tem 11 anos, eu fiz uma média dos
    7 primeiros anos  de ingressantes e dos 7 últimos anos de concluintes (no caso de adm e ped) e dos 6 primeiros e 6 últimos
    para dir.
  """
  #O iloc serve justamente para pegar os anos de interesse desses ingressantes, bem como o curso
  med_adm_ing= info_tab205_df['num_ingressantes'].iloc[[1,11,21,31,42,52,62]].mean() 
  med_dir_ing= info_tab205_df['num_ingressantes'].iloc[[2,12,22,32,43,53]].mean()
  med_ped_ing= info_tab205_df['num_ingressantes'].iloc[[3,13,23,33,41,51,61]].mean()
    
  med_adm_conc= info_tab205_df['num_concluintes'].iloc[[42,53,63,73,83,93,103]].mean()
  med_dir_conc= info_tab205_df['num_concluintes'].iloc[[52,61,72,82,92,102]].mean()
  med_ped_conc= info_tab205_df['num_concluintes'].iloc[[41,51,62,71,81,91,101]].mean()

  valores=[med_adm_conc,med_adm_ing]
  labels=['Concluintes','Não concluintes']
  ax1.pie(valores,labels=labels, autopct='%1.0f%%', startangle=90,shadow=True) 
  ax1.set_title('Administração')

  valores=[med_ped_conc,med_ped_ing]
  ax2.pie(valores,labels=labels, autopct='%1.0f%%', startangle=90,shadow=True) 
  ax2.set_title('Pedagogia')
  
  valores=[med_dir_conc,med_dir_ing]
  ax3.pie(valores,labels=labels, autopct='%1.0f%%', startangle=90,shadow=True) 
  ax3.set_title('Direito')
  
  plt.tight_layout()
  pdf.savefig()
  plt.close()


#PARTE 3 - Matrícula e regiões
#Página 9 - Comparar a porcentagem de matrícula de cada região com o seu número de habitantes
  fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 6))
  plt.suptitle('Relações entre matriculas e regiões',fontsize=20)
  """
   Tive que dar iloc[0], pois estava recebendo uma informação 
   indesejada da posição 1, não sei o porquê, mas o iloc funcionou perfeitamente, foi a alternativa encontrada
  """
  info_N=info_tab310_df.query("DF=='Norte'")['Número matriculados'].iloc[0] #Query para pegar a linha Norte dentro da coluna DF
  info_NE = info_tab310_df.query("DF=='Nordeste'")['Número matriculados'].iloc[0]
  info_SE=info_tab310_df.query("DF=='Sudeste'")['Número matriculados'].iloc[0]
  info_CO=info_tab310_df.query("DF=='Centro-Oeste'")['Número matriculados'].iloc[0]
  info_S=info_tab310_df.query("DF=='Sul'")['Número matriculados'].iloc[0]
  
  #Distribuição das matrículas por região
  valores=[info_N,info_NE,info_SE,info_CO,info_S]
  labels=['Norte','Nordeste','Sudeste','Centro-Oeste','Sul']
  ax1.pie(valores,labels=labels, autopct='%1.1f%%', startangle=90,shadow=True,textprops={'fontsize': 9}) 
  ax1.set_title('Distribuição de matrículas')
  
  #Relação entre número de matrículas para cada 10mil habitantes de cada região
  k=10000 
  valores=[info_N*k/17355778,info_NE*k/54657621,info_SE*k/84840113,info_CO*k/16289538,info_S*k/29937706]
 
  """Os valores já possuem a relação para 10mil habitantes, é uma proporção relativamente simples. Esses números se referem ao número de habitantes
  da região em 2022, de acordo com o IBGE"""
  ax2.pie(valores,labels=labels, autopct='%1.1f%%', startangle=90,shadow=True,textprops={'fontsize': 9}) #Gráfico de setor mostrando uma boa distribuição do número de universidades pelas regiões 
  ax2.set_title('Número de matriculas por 10 mil habitantes')
 
  plt.tight_layout()
  pdf.savefig()
  plt.close()

  #Último página - distribuição melhores faculdades pelo território brasileiro
  fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(11, 5))
  plt.suptitle('Distribuição das melhores universidades brasileiras',fontsize=20)
 
  """Estado.value_counts() serve para ir na coluna Estado (pude fazer isso, pois não há whitespace, caso haja teria que colocar entre aspas
    e value_counts() para, dentro dessa coluna, somar as regiões com o mesmo nome. A variável que recebe essa informação já tem o número 
    de vezes que o nome de cada região aparece.
  """
  top10=ranking_df.iloc[0:10].Estado.value_counts() #Dei iloc para pegar apenas as posições de interresse
  top20=ranking_df.iloc[0:20].Estado.value_counts()
  top50=ranking_df.iloc[0:50].Estado.value_counts()


  labels=['Sudeste','Sul','Nordeste','Centro-Oeste']
  ax1.pie(top10,labels=labels, autopct='%1.0f%%', startangle=90,shadow=True,textprops={'fontsize': 9})
  ax1.set_title('TOP 10',fontsize=14)
  ax2.pie(top20,labels=labels, autopct='%1.0f%%', startangle=90,shadow=True,textprops={'fontsize': 9})
  ax2.set_title('TOP 20',fontsize=14)
  labels.append('Norte')
  ax3.pie(top50,labels=labels, autopct='%1.0f%%', startangle=90,shadow=True,textprops={'fontsize': 9})
  ax3.set_title('TOP 50',fontsize=14)

  plt.tight_layout()
  pdf.savefig()
  plt.close()