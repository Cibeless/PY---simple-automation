#Automação Simples com PY
#codigo.py
#Automaçao simples
#Organazing the ideas to follow - Aula utomação de tarefas A1
#Passo a passo do Projeto para organizar as ideias
#Passo 1 - Entrar no sistema da empresa - link dlp.hashtagtreinamenttos.com/python/intensivao/login
#Passo 2 - Login senha  (qualquer - teste)
#Passo 3 - Pegar e importaro a passade de dados
#Passo 4 - cadastro dos produtos
#Passo 5 - Repetir o passo 4 ate todos os produtos forem esgotados

#Now using the code - Do the job!!!!
#apos intalar tem que importar né... pois pois
import pyautogui
import time

#Passo 1 - Entrar no sistema da empresa - link do exemplo dlp.hashtagtreinamenttos.com/python/intensivao/login

pyautogui.PAUSE = 2 #pausa em cada comendo 1 segundo para dar tempo
pyautogui.press("win") #abrir o windowns
pyautogui.write ("chrome") #digitar chrome
pyautogui.press("enter") #apertar enter
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")  #entrar no link tem que escrever o link  - ao dar run nao aparece porque ta faltando tempo é necessario dar uma pausa entre os comandos por isso foi adicionado no inicio (pyautogui.PAUSE = 0.5 )
pyautogui.press("enter") #ja carrega o site no chrome e abre no sistema pytho

 #para carregar o site demora entao precisa dar uma bausa de 3 segundos nesse local especifico para garatir que o site foi carregado (time controla o tempo)

time.sleep(5)

#----------------------------------------------------------
#Passo  2 - fazer o login no sistema

pyautogui.click(x=2138, y=291) # posicionamento no x=2138, y=291 descobertio no arquivo auxiliar
pyautogui.hotkey("ctrl", "a") #hotkey porque é combinaçao de teclas (ctrl + a) seleciona para digitar
pyautogui.write("pythonimpressionador@gmail.com")

#passar para o proximo campo é TAB que ja seleciona tudo
pyautogui.press("tab")
pyautogui.write("minhasenha")

#passar para botao de logar e clikcar
#Possicao do logar com o codigo auxiliar Point(x=2330, y=453)
pyautogui.click(x=2330, y=453) #clikcar no botao de logar
time.sleep(5) #para dar tempo para abrir a a pagina para a proxima etapa 

#----------------------------------------------------------
#Passo 3 - Pegar e importar a base de dados

import pandas


tabela = pandas.read_csv("C:/Users/Cibele C/Documents/Lira - Power up/Aula 1/produtos.csv") #variavel que vai armazenar as info de produtos.csv (tabela recebe os valores da base de dados produtos.csv)
print(tabela) # a tabela vai ser mostada no Terminal 

#----------------------------------------------------------
#Passo 4 - cadastro dos produtos

#para preencher temos as seções: marca, tipo, categoria, preço_unitario, custo, obs (o que deve ser cadastrado de cada produto)
#Codigo do Protuto --> Posição: (x=2046, y=174)


pyautogui.PAUSE = 2 #pausa em cada comendo 1 segundo para dar tempo


for linha in tabela.index:
    pyautogui.click(x=2046, y=174)
    #Codigo do Protuto 
    #codigo = str(tabela.loc[linha, "codigo"]) dentro da função de string - texto, para nao colocar tudo poe a variavel codigo
    codigo = str(tabela.loc[linha, "codigo"]) #dentro da variavel cidgo para ficar menior abaixo que esta na tabela
    pyautogui.write(codigo) #codigo sem as apas, valor da variavel 


    #fazer em todos os campos abaixo

    #Marca do produto
    #para passar para segundação - Marca do produto - aperta tab
    pyautogui.press("tab") #para passsar para a seção 'Marca do produto'
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)

    #Tipo do Produto
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha,"tipo"])
    pyautogui.write(tipo)

    #Categoria do Produto
    pyautogui.press("tab")
    categoria = str (tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    #Preço Unitario do Produto
    pyautogui.press("tab")
    preco = str (tabela.loc[linha, "preco_unitario"]) #preço unitario é o mesmo do capeçario da tabela
    pyautogui.write(preco)

    #Custo do Produto 
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    #OBS
    #tem que tomar cuidadno com NaN (Not a Number) pois ha informação vazia em Obs -> sendo necessaro tratar
    

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nam": #se for diferente de nam voce cadastra caso contrario passa pro proximo
        pyautogui.write(obs)

    # Enviar --> Posição: (x=2233, y=822) 
    pyautogui.press("tab")
    pyautogui.press ("enter") #Para apertar o botao de enviar


#----------------------------------------------------------
#Passo 5 - Repetir o passo 4 ate todos os produtos forem esgotados
#Nessa seção o primeiro ja foi cadastrado, loco o site preenchido some é necessario subir a pagina scroll the page para começar um novo cadastro
#Votar e preecher o todo processo novalmente - scroll
#pyautogui.scroll # vai rolar a pagina --> O numero é pixel mas observe que: Numero positivo o scroll vai para cima, Numero negativo scroll para baixo
#a principio nao sabemos o numero de pixels para dar o scrool
#paupite é colocar um numero grande positovo para voltar ao inicio da tela = ex 4000 (positivo)
pyautogui.scroll(4000) # coloque 4000 - poderia tambem dar um page up no teclado
