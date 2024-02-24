
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