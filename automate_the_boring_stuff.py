import numpy as np
import pandas as pd
import os
import glob
#### Utilities ###################################
def df_date(df,year,month):
    m_list = list(range(1, month+1))
    df = df[df['ANIO'] == year]
    df=df[df['MES NUMERO'].isin(m_list)]
    return df

def df_summarize(df,name):
    df_ly=df_date(df,year-1,month)
    df_ry=df_date(df,year,month)
    sum_ly=df_ly['VtasValor'].sum()
    sum_ry=df_ry['VtasValor'].sum()
    return(([name,sum_ly,sum_ry]))

### creating the functions for each category ##############
def default():
    print('!')

def aguas_industry(df):
    df = df[df['MERCADO'] == 'TOTAL MEXICO']
    return df_summarize(df,'aguas industry')

def aguas_natural(df):
    pesos = [1000,1100,1200,1250,1300,1500,1550,1800,1850,1875,1890,1892,2000,236,237,250,2500,260,290,300,3000,3100,330,350,355,360,365,3700,3710,375,3750,3758,3780,3785,3800,3870,3875,390,400,4000,473,475,480,500,5000,505,5250,5500,5670,591,600,6000,620,650,700,707,710,740,750,770,800,850,900,950,960]
    df = df[df['PesoConvertido'].isin(pesos)]
    df = df[df['MERCADO'] == 'TOTAL MEXICO']

    return df_summarize(df,'aguas natural')

def aguas_saborizadas(df):
    filt1 = (df['SUBMARCA']=='ACTIVE WATER')
    filt2 = (df['SEGMENTO']=='AGUA SABORIZADA')&(df['MARCA'].isin(['CRISTAL', 'BE LIGHT', 'SUN LIGHT', 'AGUAFIEL', 'SKARCH']))
    filt3 = (df['SEGMENTO']=='AGUA SABORIZADA')&(df['FABRICANTE'].isin(['PASCUAL','GUGAR','EL DUQUE','WATER PEOPLE','ARBOLITO','TE27','NATURAL GOOD SHAPE','O.FAB.', 'ALEX & TONY','BEVCO', 'COMER.DE LOS ALTOS DE ARANDAS', 'SANTA ANA SPRINGS', 'NESTLE', 'ARROWHEAD', 'BEBIDAS RECA', 'MEXICANA DE BEBIDAS','GRUPO GEPP']))
    filt4 = (df['MARCA'].isin(['CLIGHT', 'JULIGHT']))
    filt5 = (df['SEGMENTO']=='BEBIDAS REFRESCANTES')&(df['FABRICANTE'].isin(['NESTLE','GRUPO GEPP', 'AGA DE MEXICO']))&(df['MARCA'].isin(['AGUITAS','E-PURITA','PUREZA VITAL', 'PUREZA VITAL KIDS', 'SKARCH']))
    filt6 = (df['SEGMENTO'].isin(['AGUA SABORIZADA', 'BEBIDAS REFRESCANTES']))&(df['FABRICANTE']=='DANONE')&(df['SUBMARCA'].isin(['JUIZZY', 'KIDS', 'LEVITE BALANCE', 'LEVITE CERO', 'LEVITE CLASICA', 'LEVITE INFUSIONES']))
    filt7 = (df['SEGMENTO'].isin(['AGUA SABORIZADA','BEBIDAS REFRESCANTES']))&(df['FABRICANTE']=='COCA-COLA COMPANY')&(df['MARCA'].isin(['CIEL', 'MINUTE MAID']))
    filt8 = (df['SEGMENTO']=='AGUA VITAMINADA')&(df['MARCA']=='GLACEAU')
    df = df[filt1|filt2|filt3|filt4|filt5|filt6|filt7|filt8].copy()
    df = df[df['MERCADO'] == 'TOTAL MEXICO']
    return df_summarize(df,'aguas saborizadas')
    

def alimentos_mascotas(df):
    df = df[df['MERCADO'] == 'TOTAL MEXICO SIN TRADICIONALES']
    return df_summarize(df,'alimentos mascotas')

def alimentos_infantiles(df):
    df.rename(columns={'MARKET':'MERCADO','VENTAS EN VALOR (in 000 PESOS)':'VtasValor'},inplace=True)
    df = df[df['MERCADO'] == 'TOTAL MEXICO']
    return df_summarize(df,'alimentos infantiles')

def cafe_tym(df):
    df = df[df.MERCADO == 'TOTAL AUTOS SCANNING MEXICO']
    df = df[df['SUB CATEGORY'] != 'PORTIONED FOR SYSTEM']
    df['FABRICANTE UNIF.'] = np.where((df['FABRICANTE UNIF.']=='NESTLE') | (df['FABRICANTE UNIF.']=='STARBUCKS COFFEE')  ,'NESTLE','COMPETENCIA')
    return df_summarize(df,'cafe TyM')

def cereales(df):
  df = df[df['MERCADO'] == 'TOTAL MEXICO']
  return df_summarize(df,'cereales')

def chocolates_golosina(df):
  df = df[df['MERCADO'] == 'TOTAL MEXICO']
  return df_summarize(df,'chocolates golosina')

def chocolate_mesa(df):
  df = df[df['MERCADO'] == 'TOTAL MEXICO']
  return df_summarize(df,'chocolate mesa')

def condimentos(df):
  df = df[df['MERCADO'] == 'TOTAL MEXICO']
  filt1 = (df['SEGMENTO']=='CONDIMENTOS LIQUIDOS')|(df['SEGMENTO']=='CONTROLLED LABEL')
  filt2 = (df['TIPO']=='SALSA DE SOYA')|(df['TIPO']=='OTHERS TIPO UNIF.')|(df['TIPO']=='SAZONADOR VEGETAL')|(df['TIPO']=='SALSA INGLESA')|(df['TIPO']=='SALSAS PREPARADAS')|(df['TIPO']=='JUGO SAZONADOR')|(df['TIPO'].isna())  
  df=df[filt1&filt2].copy()
  df=df.drop(df[df.DESCRIPCION =='CONDIMENTOS LIQUIDOS'].index)
  return df_summarize(df,'condimentos liquidos')

def consome(df):
  df.rename(columns={'MESNUM':'MES NUMERO','VentasValor':'VtasValor'},inplace=True)
  df = df[df['MERCADO'] == 'TOTAL AUTOS SCANNING MEXICO']
  return df_summarize(df,'consome')

def consome_mayoreo(df):
  df = df[df['MERCADO'] == 'TOTAL MAYORISTAS']
  return df_summarize(df,'consome mayoreo')

def cremadores(df):
  df = df[df['MERCADO'] == 'TOTAL MEXICO']
  return df_summarize(df,'cremadores')

def cereales_infantiles(df):
  df.rename(columns={'MARKET':'MERCADO','VENTAS EN VALOR (in 000 PESOS)':'VtasValor'},inplace=True)
  df = df[df['MERCADO'] == 'TOTAL MEXICO']
  return df_summarize(df,'cereales_infantiles')

def formulas_infantiles(df):
  df.rename(columns={'MARKET':'MERCADO','[VENTAS EN VALOR (in 000 PESOS)]':'VtasValor'},inplace=True)
  return df_summarize(df,'formulas_infantiles')

def jugos(df):
  df.rename(columns={'MESNUM':'MES NUMERO','VentasValor':'VtasValor'},inplace=True)
  df = df[df['FABRICANTE'].isin(['HEINZ','GERBER'])]
  df = df[df['MERCADO'] == 'TOTAL AUTOS SCANNING MEXICO']
  return df_summarize(df,'jugos')

def leche_condensada(df):
  df = df[df['MERCADO'] == 'TOTAL MEXICO']
  return df_summarize(df,'leche condensada')

def leche_evaporada(df):
  df = df[df['MERCADO'] == 'TOTAL MEXICO']
  return df_summarize(df,'leche evaporada')

def sustitutos_leche(df):
  df = df[df.MERCADO == 'TOTAL AUTOS SCANNING MEXICO']
  df = df[df.MARCA == 'CARNATION']
  return df_summarize(df,'sustitutos leche')

def leche_polvo(df):
  df = df[df['MERCADO'] == 'TOTAL MEXICO + FARMACIAS DE CADENA SIN MS']
  return df_summarize(df,'leche en polvo')

def soluble(df):
  df = df[df['MERCADO'] == 'TOTAL MEXICO']
  return df_summarize(df,'soluble')

###### Set our Dictionary #######################
my_dict = {'AGUA MINERAL NATURAL Y SABORIZADA' : aguas_industry, 
           'AGUA NATURAL' : aguas_natural, 
           'AGUAS SABORIZADAS + BEB. REF' : aguas_saborizadas, 
           'ALIM_MASCOTA' : alimentos_mascotas,
           'H1 ALIMENTO PARA BEBES' : alimentos_infantiles, 
           'CAFE TYM INDUSTRY' : cafe_tym, 
           'CEREALES_P' : cereales,
           'CHOCOLATE GOLOSINA': chocolates_golosina,
           'CHOCOLATE MESA' : chocolate_mesa,
           'CONDIMENTO LIQUIDO' : condimentos,
           'CONSOME': consome,
           'H1 CONSOME + CALDOS' : consome_mayoreo,
           'CREMADORES' : cremadores,
           'H1 CEREALES INFANTILES' : cereales_infantiles,
           'FORMULAS INFANTILES' : formulas_infantiles,
           'JUGOS' : jugos,
           'LECHE CONDENSADA': leche_condensada,
           'LECHE EVAPORADA' : leche_evaporada,
           'SUSTITUTOS LECHE': sustitutos_leche,
           'LECHE POLVO' : leche_polvo,
           'SOLUBLE' : soluble
           }


############################################# Main Function ########################################

def main(path,year,month):
  dfs=[]
  csv_files = glob.glob(os.path.join(path, "*.csv"))
  c=1
  for x in csv_files:
    f_name= x.split("/")[-1][:-4]
    df=pd.read_csv(x)
    if 'CATEGORIA' in df.columns.tolist():
      ls_cat=df['CATEGORIA'].unique().tolist()
    else:
      ls_cat=df['CATEGORY VIEW'].unique().tolist()
    if len(ls_cat)<=1:
      #print(ls_cat)
      print(c)
      print(f'el nombre del archivo es: {f_name} | y la categoría : {ls_cat[0]}')
      c+=1
      a=my_dict[ls_cat[0]](df)
      print(a)
      dfs.append(a)
    else:
      print('error')
      a=[f_name,'verifique los datos','verifique los datos']
      dfs.append(a)
  dfa = pd.DataFrame(dfs, columns = ['Nombre','last_year','rolling_year'])
  dfa.to_csv(f'{path_output}/validar_data.csv',index=False)

##Setting the config vars 

path='/content/drive/MyDrive/Automating the boring stuff/DATA'
path_output='/content/drive/MyDrive/Automating the boring stuff/Salida'
year=2021
month=7
#Execute Main
main(path,year,month)