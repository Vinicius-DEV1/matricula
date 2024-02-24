#maisde2disciplinas


import datetime
import time
from selenium import webdriver
import os.path

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options


from source import preencher_login
from source import checar_disponibilidade

sinalizador_de_disponibilidade = False


interface_grafica = input("COM INTERFACE GRÁFICA? (Y/n)")

if (interface_grafica=="Y" or interface_grafica=="y" or interface_grafica==""):
    # Inicializa o driver do navegador
    driver = webdriver.Chrome()
    # Acessar a pagina de login
    driver.get("https://aluno.uvanet.br/")
    time.sleep(5)
else:
    # Configurando as opções do Chrome para executar em modo headless
    chrome_options = Options()
    # Adiciona a opção de headless
    chrome_options.add_argument('--headless')

    # Inicializa o driver do navegador
    driver = webdriver.Chrome(options=chrome_options)

    # Acessar a pagina de login
    driver.get("https://aluno.uvanet.br/")
    time.sleep(5)


if (os.path.isfile('login.txt') == False):
    print("Digite seu LOGIN")
    user_log = input("Digite user: ")
    password_log = input("Digite password: ")

    #Escreve as credencias no arquivo
    with open('login.txt', 'w') as arquivo:
        arquivo.write(user_log + '\n')
        arquivo.write(password_log + '\n')
    arquivo.close()

    preencher_login()
else:
    preencher_login()

##LOOP
lista_de_id_disciplinas=['ofertas_55695','ofertas_55725','ofertas_55726']
tentativas=0
loop=True

driver.get("https://aluno.uvanet.br/matricula_reajuste_form.php")
# Esperar a página de reajuste carregar
# troca por uma funcao
time.sleep(10)

while (loop==True):



    for id_disciplina in lista_de_id_disciplinas:
        #para cada elemento na lista a function checar_disponibilidade  verifica
        # se a disciplina está disponivel para matricula
        checar_disponibilidade(id_disciplina)

    if sinalizador_de_disponibilidade == True:
        print("Matricula disponivel.")
        ##APERTAR EM MATRICULAR
        botao_class = "botao_matricula"
        wait = WebDriverWait(driver, 5)
        matricula = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, botao_class)))
        #matricula.click()
        print("Matricula Executada com sucesso.")
        sinalizador_de_disponibilidade = False

        #Quando fizer todas as matriculas encerrar o programa
        if not lista_de_id_disciplinas:
            print("=============================================================")
            print("TODAS AS DISCIPLINAS INSERIDAS FORAM MATRICULADAS COM SUCESSO")
            print("FIM.")
            loop = False

    else:
        #time.sleep(0)
        tentativas+=1
    
        #Obter a hora e a data atual
        agora = datetime.datetime.now()
        #Extrair a hora e o minuto
        hora = agora.hour
        minuto = agora.minute
        segundo = agora.second
        #Formatar a hora e o minuto com dois dígitos cada (por exemplo: 09:05)
        hora_formatada = f'{hora:02}:{minuto:02}:{segundo:02}'
        print(f' {hora_formatada} : Tentar Novamente: \n Já foram {tentativas} Tentativas de Matricula')
        print('\n')



# Fechar o navegador
time.sleep(5)
driver.quit()


#RECEBE 1,2,...N
#RECEBE 1,2,...N ID DE DISCIPLINA
#pressionar as três disciplinas e caso alguma esteja disponivel apertar em matricular;
#APÓS ISSO REMOVE AS QUE FOI MATRICULADO DO TESTE;
#QUANDO ACABA TODAS ENCERRAR O ALGORITMO.

