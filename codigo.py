import pyautogui
import time

pyautogui.PAUSE = 0.5

# pyautogui.click -> clica com mouse
# pyautogui.write -> escreve texti
# pyautogui.press -> pressionar tecla do teclado
# pyautogui.hotkey -> apertar um conjunto de teclas 

# 1. abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press ("enter") 

# aqui pode ser que ele demora alguns segundos para carregar o site
time.sleep(2)

# 2. fazer login
pyautogui.click(x=737, y=422)
pyautogui.write("emailteste5@gmail.com")
pyautogui.press("tab") # passa para o campo de senha
pyautogui.write("senha123")

pyautogui.press("tab") # passa para o botão de login
pyautogui.press("enter")

time.sleep(2)

# 3. Abrir base de dados de produtos
import pandas as pd

tabela = pd.read_csv("produtos.csv")

# 4. Cadastrar um produto

for linha in tabela.index:
    codigo = str(tabela.loc[linha, "codigo"])
    marca = str(tabela.loc[linha, "marca"])
    tipo = str(tabela.loc[linha, "tipo"])
    categoria = str(tabela.loc[linha, "categoria"])
    preco = str(tabela.loc[linha, "preco_unitario"])
    custo = str(tabela.loc[linha, "custo"])
    
    # clicar no campo do codigo do produto
    pyautogui.click(x=711, y=309)
    # preencher o codigo
    pyautogui.write(codigo)
    #passar para o proximo campo
    pyautogui.press("tab")

    # marca
    pyautogui.write(marca)
    #passar para o proximo campo
    pyautogui.press("tab")
    # tipo
    pyautogui.write(tipo)
    #passar para o proximo campo
    pyautogui.press("tab")
    # categoria
    pyautogui.write(categoria)
    #passar para o proximo campo
    pyautogui.press("tab")
    # preço
    pyautogui.write(preco)
    #passar para o proximo campo
    pyautogui.press("tab")
    # custo
    pyautogui.write(custo)
    #passar para o proximo campo
    pyautogui.press("tab")
    # obs
    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    #passar para o proximo campo
    pyautogui.press("tab")
    # apertar o botão
    pyautogui.press("enter")
    pyautogui.scroll(5000)
