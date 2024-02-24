#maisde2disciplinas


import datetime
import time
from selenium import webdriver
import os.path

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.options import Options


sinalizador_de_disponibilidade = False


def preencher_login():
    with open('login.txt', 'r') as arquivo:
        user_login = arquivo.readlines()[0]
        arquivo.seek(0)
        password_login = arquivo.readlines()[1]
        #repete o codigo anterior
        arquivo.close()

    #Por enquanto autenticação manual via codigo
    user_box = driver.find_element("id", "form:usuario")
    user_box.send_keys('vinicius_calado')

    password_box = driver.find_element("id", "form:senha")
    password_box.send_keys('uva2027ccn')

    # marcar checkbox lembrar de manter conectado
    manter_logado = driver.find_element("id", "form:manterLogado")
    manter_logado.click()
    #click login
    logar = driver.find_element("id", "form:button")
    logar.click()




def matricular(id_disciplina):
    # Encontrar o elemento da checkbox pelo ID
    checkbox = driver.find_element("id", id_disciplina)

    #tornar as checkbox travadas em clicaveis para ver o status dela
    driver.execute_script("arguments[0].removeAttribute('disabled');", checkbox)

    # Clicar na checkbox para ativá-la
    checkbox.click()
    #time.sleep(4)

    ##verificar se o checkbox foi marcado, se sim no final pode apertar em matricular.
    if checkbox.is_selected():
        print("A disciplina [...] ESTÁ disponivel")
        global sinalizador_de_disponibilidade
        sinalizador_de_disponibilidade = True
        #remover esse que foi verificado; finalizar programa somente com a lista vázia
        lista_de_id_disciplinas.remove(id_disciplina)
    else:
        print("A disciplina [...] NÃO está disponivel")




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
        matricular(id_disciplina)

    #
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
        time.sleep(0)
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
#pressionar as três disciplinas e caso alguma esteja disponivel apertar em matricular; APÓS ISSO REMOVE AS QUE FOI MATRICULADO DO TESTE;
#QUANDO ACABA TODAS ENCERRAR O ALGORITMO.

