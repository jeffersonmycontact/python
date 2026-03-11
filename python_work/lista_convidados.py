lista_convidados = ['Jesus', 'maria', 'josé']

"""
print(f"Eu gostaria de te convidar para jantar comigo Senhor {lista_convidados[0]}.")

print(f"Eu gostaria de te convidar para jantar comigo amanhã {lista_convidados[1].title()}.")

print(f"{lista_convidados[2].title()}, você gostaria de jantar comigo hoje?")
"""

print(f"\n{lista_convidados[2].title} não ira ao jantar")

lista_convidados[2] = 'miguel'
print(lista_convidados)

print(f"Você poderia jantar comigo {lista_convidados[2].title()}")

print("\nEncontrei uma mesa maior, agora posso convidar mais pessoas para o jantar.")

lista_convidados.insert(0, 'pedro')
print(lista_convidados)

lista_convidados.insert(2, 'thiago')
print(lista_convidados)

lista_convidados.append('judas')
print(lista_convidados)

print(f"Eu gostaria de te convidar para jantar comigo hoje à noite {lista_convidados[0].title()}. Você aceita?")

print(f"Eu gostaria de te convidar para jantar comigo hoje à noite {lista_convidados[1]}. Você aceita?")

print(f"Eu gostaria de te convidar para jantar comigo hoje à noite {lista_convidados[2].title()}. Você aceita?")

print(f"Eu gostaria de te convidar para jantar comigo hoje à noite {lista_convidados[3].title()}. Você aceita?")

print(f"Eu gostaria de te convidar para jantar comigo hoje à noite {lista_convidados[4].title()}. Você aceita?")

print(f"Eu gostaria de te convidar para jantar comigo hoje à noite {lista_convidados[5].title()}. Você aceita?")

print("\nAconteceu um problema e agora eu posso convidar apenas duas pessoas para o jantar\n")

print(lista_convidados)

judas = lista_convidados.pop()
print(lista_convidados)
print(f"Bom dia {judas.title()}. Infelizmente precisarei convidar o nosso jantar hoje, aconteceu um imprevisto, espero que compreenda. Peço desculpas.")

miguel = lista_convidados.pop()
print(lista_convidados)
print(f"Bom dia {miguel.title()}. Infelizmente precisarei convidar o nosso jantar hoje, aconteceu um imprevisto, espero que compreenda. Peço desculpas.")

pedro = lista_convidados.pop(0)
print(lista_convidados)
print(f"Bom dia {pedro.title()}. Infelizmente precisarei convidar o nosso jantar hoje, aconteceu um imprevisto, espero que compreenda. Peço desculpas.")

thiago = lista_convidados.pop(1)
print(lista_convidados)
print(f"Bom dia {thiago.title()}. Infelizmente precisarei convidar o nosso jantar hoje, aconteceu um imprevisto, espero que compreenda. Peço desculpas.")

print(f"Você ainda é meu convidado {lista_convidados[0]}.")
print(f"Você ainda é minha convidada {lista_convidados[1].title()}.")

del lista_convidados[0]
del lista_convidados[0]

print(f"\nLista de convidados: {lista_convidados}\n")