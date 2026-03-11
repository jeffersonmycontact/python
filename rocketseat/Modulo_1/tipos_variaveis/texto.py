# Declaração
nome_completo = "Jefferson Santana"

# string com 3 aspas permite quebra de linha
nome_completo_aspas = """Jefferson
Santana"""

# usando a barra invertida \, para quebra de linha 
nome_completo_quebra = "Jefferson \
Santana"

nome = "Jefferson"
sobrenome = "Santana"

# Formatação
print("Nome completo (1º forma):", nome_completo) # vírgula mostra um espaço no output
print("Nome completo (2º forma):" + nome_completo) # o sinal de mais não mostra um espaço no output
print("Nome completo (3º forma):" + "Jefferson" + "Santana")
print("Nome completo (4º forma):" + "Jefferson", "Santana")
print("Nome completo (5º forma):", nome_completo_aspas)
print("Nome completo (6º forma):", nome_completo_quebra)
print("Nome completo (7º forma): %s" % nome_completo)
print("Nome completo (8º forma): %s %s" % (nome, sobrenome))
print(f"Nome completo (9º forma): {nome} {sobrenome}")
print("Nome completo (10º forma): {} {}".format(nome, sobrenome))
