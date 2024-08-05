import pyautogui
import time
import pandas as pd
import shutil
import os

pyautogui.PAUSE = 1.70

# Carregar tabela
tabela = pd.read_csv(r"C:\Users\PC\Desktop\milagre20.csv")
time.sleep(5)

# Caminhos das pastas
#source_folder = r'C:\ECF generator'
#destination_folder = r'C:\ECF CONCLUIDOS'

for linha in range(len(tabela)):
    time.sleep(3)
    pyautogui.click(x=22, y=61)
    time.sleep(5)

    pyautogui.click(x=655, y=216) # CNPJ
    pyautogui.write('21.609.217/0001-73')
    pyautogui.click(x=524, y=258) # NOME
    pyautogui.write('MEDICALMAIS SERVICOS EM SAUDE LTDA')
    pyautogui.click(x=600, y=433) # DATA
    pyautogui.write('01/01/2023')
    pyautogui.click(x=707, y=572) # CODIGO TIPO
    pyautogui.click(x=570, y=663) # 2 
    pyautogui.click(x=749, y=609) # CNPJ SCP
    cnpj = tabela.loc[linha, "cnpj"]
    pyautogui.write(str(cnpj))
    time.sleep(1)
    pyautogui.press('enter')
    pyautogui.click(x=644, y=687) # PROXIMO 
    time.sleep(1)

    pyautogui.click(x=576, y=213) # CAMPO
    pyautogui.press('5')
    pyautogui.press('enter')
    time.sleep(8)

    pyautogui.click(x=498, y=270) # CAMPO
    pyautogui.write('01')
    pyautogui.press('enter')
    time.sleep(3)

    pyautogui.click(x=499, y=338) # CAMPO
    pyautogui.press('L')
    pyautogui.press('enter')
    time.sleep(8)

    pyautogui.click(x=574, y=512)
    pyautogui.press('1')
    pyautogui.press('enter')
    time.sleep(8)

    pyautogui.click(x=679, y=686) # PROXIMO
    time.sleep(2)

    pyautogui.click(x=687, y=684) # CRIAR
    time.sleep(8)

    # VIZUALIZAR
    pyautogui.click(x=460, y=126)
    pyautogui.click(x=475, y=150)
    time.sleep(3)

    # DADOS DE CADASTRO
    pyautogui.click(x=445, y=165)
    pyautogui.click(x=480, y=199)
    pyautogui.click(x=498, y=215)
    #pyautogui.click(x=440, y=201) # DADOS CAD
    #pyautogui.click(x=498, y=219) # 030
    pyautogui.click(x=1084, y=301) # CAMPO
    pyautogui.write('2062')  # NAT JURIDICA
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.write('8610101')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.write('R AIRES DA CUNHA') 
    pyautogui.press('enter')
    pyautogui.write('06')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.write('MAURICIO DE NASSAU')
    pyautogui.press('enter')
    pyautogui.write('PE')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.write('2604106')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.write('55014415')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.write('JULIOCESAR@CONTROLLERSBR.COM')
    pyautogui.press('enter')
    time.sleep(3)

    pyautogui.click(x=1319, y=586) # DESCER
    pyautogui.click(x=1041, y=561) # SALVAR
    pyautogui.click(x=679, y=389) # OK
    time.sleep(3)

    # CADASTRO SIGNATARIO
    #pyautogui.click(x=445, y=165)
    pyautogui.click(x=523, y=235)
    #pyautogui.click(x=471, y=165)
    #pyautogui.click(x=508, y=216)
    pyautogui.click(x=786, y=327)
    pyautogui.click(x=563, y=282)
    pyautogui.write('JULIO CESAR DIAS OLIVEIRA')
    pyautogui.press('enter')
    pyautogui.write('86827790487')
    pyautogui.press('enter')
    pyautogui.write('900')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.write('PE/024639-0')
    pyautogui.press('enter')
    pyautogui.write('JULIOCESAR@CONTROLLERSBR.COM')
    pyautogui.press('enter')
    pyautogui.write('8134475550')
    pyautogui.press('enter')
    pyautogui.click(x=653, y=484) # SALVAR
    time.sleep(3)

    pyautogui.click(x=792, y=333)
    pyautogui.click(x=563, y=282)
    pyautogui.write('JULIO CESAR DIAS OLIVEIRA')
    pyautogui.press('enter')
    pyautogui.write('86827790487')
    pyautogui.press('enter')
    pyautogui.write('309')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.write('PE/024639-0')
    pyautogui.press('enter')
    pyautogui.write('JULIOCESAR@CONTROLLERSBR.COM')
    pyautogui.press('enter')
    pyautogui.write('8134475550')
    pyautogui.press('enter')
    pyautogui.click(x=653, y=484) # SALVAR
    time.sleep(3)

    # IRPJ
    #pyautogui.click(x=421, y=250)
    #pyautogui.click(x=441, y=268) # PRESUMIDO
    #pyautogui.click(x=505, y=302) # P200

    #pyautogui.click(x=554, y=336) # P400

    pyautogui.click(x=477, y=303) #INFORMAÇÃO GER

    pyautogui.click(x=499, y=334) #Y600

    pyautogui.click(x=788, y=328) #+


    pyautogui.click(x=583, y=197)
    data = tabela.loc[linha, "data"]
    pyautogui.write(str(data))
    pyautogui.press('enter')

    pyautogui.press('enter')

    pyautogui.write('105')
    pyautogui.press('enter')

    pyautogui.press('enter')

    pyautogui.write('pf')
    pyautogui.press('enter')

    pyautogui.press('enter')

    cpf = tabela.loc[linha, "cpf"]
    pyautogui.write(str(cpf))
    pyautogui.press('home')
    pyautogui.press('del')
    pyautogui.press('enter')

    nome = tabela.loc[linha, "nome"]
    pyautogui.write(str(nome))
    pyautogui.press('enter')

    pyautogui.write('02')
    pyautogui.press('enter')

    pyautogui.press('enter')

    pyautogui.write('83,67')
    pyautogui.press('enter')

    pyautogui.press('0')
    pyautogui.press('enter')



    pyautogui.click(x=650, y=560) #SALVAR


    pyautogui.click(x=784, y=329) #+

    pyautogui.click(x=704, y=199) 
    data = tabela.loc[linha, "data"]
    pyautogui.write(str(data))
    pyautogui.press('enter')

    pyautogui.press('enter')

    pyautogui.write('105')
    pyautogui.press('enter')

    pyautogui.press('enter')

    pyautogui.write('pj')
    pyautogui.press('enter')

    pyautogui.press('enter')

    pyautogui.write('21609217000173')
    pyautogui.press('enter')

    pyautogui.write('MEDICALMAIS SERVICOS EM SAUDE LTDA')
    pyautogui.press('enter')

    pyautogui.write('04')
    pyautogui.press('enter')

    pyautogui.press('enter')

    pyautogui.write('16,33')
    pyautogui.press('enter')

    pyautogui.press('0')
    pyautogui.press('enter')


    pyautogui.click(x=651, y=555) #SALVAR
    time.sleep(5)
    #Y720
    pyautogui.click(x=529, y=368)
    pyautogui.click(x=1300, y=593)
    pyautogui.click(x=1195, y=384) #CAMPO
    pyautogui.press('N')
    pyautogui.press('enter')

    pyautogui.click(x=931, y=450) #SALVAR
    pyautogui.click(x=683, y=390) #OK
    time.sleep(3)
    #PASSO A PASSO
    pyautogui.click(x=550, y=125) 

    #VALIDAÇÃO
    pyautogui.click(x=669, y=450)
    time.sleep(200)

    #GERAR
    pyautogui.click(x=682, y=392)
    pyautogui.click(x=487, y=101)
    pyautogui.click(x=772, y=455)
    time.sleep(3)
    #NA GERAÇÃO EM ALGUM MOMENTO TEM QUE TER DIGITÇÃO DA MAT NO NOME DO ARQUIVO
    pyautogui.click(x=834, y=506)
    pyautogui.click(x=679, y=392)
    time.sleep(5)
    #Assinar
    pyautogui.click(x=881, y=461)
    time.sleep(4)
    pyautogui.click(x=649, y=309)
    time.sleep(4)
    pyautogui.click(x=650, y=502)
    time.sleep(4)
    pyautogui.click(x=609, y=324)
    time.sleep(4)
    pyautogui.click(x=893, y=498)
    time.sleep(4)
    pyautogui.click(x=686, y=392)
    time.sleep(4)
    pyautogui.click(x=639, y=388)
    time.sleep(4)
    pyautogui.click(x=639, y=311)
    time.sleep(4)
    pyautogui.click(x=638, y=509)
    time.sleep(4)
    pyautogui.click(x=567, y=326)
    time.sleep(4)
    pyautogui.click(x=896, y=493)
    time.sleep(4)    
    pyautogui.click(x=680, y=394)
    time.sleep(4)
    #TRANSMITIR
    pyautogui.click(x=981, y=447)
    time.sleep(1)
    pyautogui.click(x=616, y=295)
    time.sleep(1)
    pyautogui.click(x=639, y=561)
    time.sleep(8)
    pyautogui.click(x=728, y=555)
    time.sleep(3)
    pyautogui.click(676, 394)
    time.sleep(3)
    pyautogui.click(692, 556) #
    time.sleep(5)
    pyautogui.click(637, 558) #
    time.sleep(5)
    pyautogui.click(272, 558) #
    time.sleep(3)
    #EXCLUSÃO
    pyautogui.click(x=123, y=178)
    time.sleep(3)
    pyautogui.click(x=69, y=193)
    time.sleep(2)
    pyautogui.click(x=156, y=211)
    time.sleep(3)
    pyautogui.click(x=83, y=63)
    time.sleep(2)
    pyautogui.click(x=639, y=388)
    time.sleep(3)
    pyautogui.click(x=693, y=395)
    time.sleep(4)

    # Move arquivos
    #for file_name in os.listdir(source_folder):
        #shutil.move(os.path.join(source_folder, file_name), destination_folder)

    pyautogui.click(x=646, y=398) # OK
    time.sleep(5)
