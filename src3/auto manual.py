import pyautogui
import time
import pandas as pd


pyautogui.PAUSE = 1

# Carregar tabela
tabela = pd.read_csv(r"C:\Users\PC\Desktop\Concertar CPF DATA\1-nicolas.csv")
time.sleep(2)

for linha in range(len(tabela)):
    pyautogui.PAUSE = 0.9  
    # Outras ações 
    #pyautogui.click(896, 336)0
    #pyautogui.hotkey('shift', 'd')
    #time.sleep(40)
    pyautogui.click(x=240, y=557) # Caixa opções
    time.sleep(0.4)
    pyautogui.click(x=240, y=578) # Caixa opções
    pyautogui.click(x=300, y=223) 
    #time.sleep(10.4)
    pyautogui.click(x=536, y=342) # Parâmetro tributário seta
    pyautogui.press('down')
    pyautogui.click(x=1023, y=370) # Q livro caixa335700,0000

    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.click(x=240, y=414) # Caixa Gerar Q
    pyautogui.click(x=732, y=223) # Presumido
    #pyautogui.click(x=931, y=398) # Código 8

    # Preencher tri1, tri1cen, tri2, tri2cen, tri3, tri3cen, tri4, tri4cen

#pyautogui.click(x=516, y=259) # clica no tri1

    #TRI1

    pyautogui.click(x=931, y=398) #cod 8
    tri1 = tabela.loc[linha, "tri1"]
    tricen1 = tabela.loc[linha, "tricen1"]
    pyautogui.write(str(tri1)) # Código 8
    pyautogui.press(',')
    pyautogui.write(str(tricen1))
    pyautogui.press('enter')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('right')  
    
    #TRI2    
    
    pyautogui.click(x=931, y=398) #cod 8
    tri2 = tabela.loc[linha, "tri2"]
    tricen2 = tabela.loc[linha, "tricen2"]
    pyautogui.write(str(tri2)) # Código 8
    pyautogui.press(',')
    pyautogui.write(str(tricen2))
    pyautogui.press('enter')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('right') 
    
    #TRI3

    pyautogui.click(x=931, y=398) #cod 8
    tri3 = tabela.loc[linha, "tri3"]
    tricen3 = tabela.loc[linha, "tricen3"]
    pyautogui.write(str(tri3)) # Código 8
    pyautogui.press("backspace")
    pyautogui.press(',')
    pyautogui.write(str(tricen3))
    pyautogui.press('enter')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('right') 
    
    #TRI4

    pyautogui.click(x=931, y=398) #cod 8
    tri4 = tabela.loc[linha, "tri4"]
    tricen4 = tabela.loc[linha, "tricen4"]
    pyautogui.write(str(tri4)) # Código 8
    pyautogui.press("backspace")
    pyautogui.press(',')
    pyautogui.write(str(tricen4))
    pyautogui.press('enter')
    '''pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('right')'''

    #Y400
    pyautogui.click(x=274, y=306)
    pyautogui.click(x=982, y=361) #cod 4
    tri1 = tabela.loc[linha, "tri1"]
    tricen1 = tabela.loc[linha, "tricen1"]
    pyautogui.write(str(tri1)) # Código 8
    pyautogui.press(',')
    pyautogui.write(str(tricen1))
    pyautogui.press('enter')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('right')

    
    pyautogui.click(x=982, y=361) #cod 4
    tri2 = tabela.loc[linha, "tri2"]
    tricen2 = tabela.loc[linha, "tricen2"]
    pyautogui.write(str(tri2)) # Código 8
    pyautogui.press(',')
    pyautogui.write(str(tricen2))
    pyautogui.press('enter')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('right')

    
    pyautogui.click(x=982, y=361) #cod 4
    tri3 = tabela.loc[linha, "tri3"]
    tricen3 = tabela.loc[linha, "tricen3"]
    pyautogui.write(str(tri3)) # Código 8
    pyautogui.press("backspace")
    pyautogui.press("right")
    pyautogui.write(str(tricen3))
    pyautogui.press('enter')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('right')


    pyautogui.click(x=982, y=361) #cod 4
    tri4 = tabela.loc[linha, "tri4"]
    tricen4 = tabela.loc[linha, "tricen4"]
    pyautogui.write(str(tri4)) # Código 8
    pyautogui.press('backspace')
    pyautogui.press(',')
    pyautogui.write(str(tricen4))
    pyautogui.press('enter')
    '''pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('shift', 'tab')
    pyautogui.press('right')'''

    # Preencher CPF e Data
    pyautogui.click(x=224, y=372) # infor 600
    pyautogui.click(x=272, y=402) # 600
    pyautogui.click(x=833, y=612) # Incluir
    cpf = tabela.loc[linha, "cpf"]
    pyautogui.write(str(cpf))
    pyautogui.press('tab')
    data = tabela.loc[linha, "data"]
    pyautogui.write(str(data))
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write(str('83,67'))
    pyautogui.press('tab')

    pyautogui.click(x=836, y=611)
    pyautogui.write(str('21609217000173'))
    pyautogui.press('tab')
    data = tabela.loc[linha, "data"]
    pyautogui.write(str(data))
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.write(str('16,33'))
    pyautogui.press('tab')    
  


    #Y720
    pyautogui.click(x=269, y=434)
    pyautogui.click(x=490, y=258)
    pyautogui.press('tab')
    pyautogui.press('down')
    pyautogui.press('down')

    

    pyautogui.click(x=973, y=685) # OK INTERNO
    time.sleep(10)
    pyautogui.click(x=901, y=239) # OK PARA PARA GERAR
    time.sleep(1000)    