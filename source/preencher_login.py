def preencher_login():
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