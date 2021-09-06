"""

Criando jogo Forca com Python

Funções a serem realizadas:

- [X] Escolhe Palavra conforme genero
- [X] Esconde & cria qtd itens
- [X] Mostrar quais letras foram descobertas e quais estão escondidas
- [X] Conseguir Enviar uma nova letra

"""

from faker import Faker


def escolha_palavra_por_genero(dict_palavra, genero):
    from random import choice
    if genero in dict_palavras_por_genero:
        palavra = choice(dict_palavras_por_genero[genero])
    else:
        palavra = None
    return palavra


def esconde_palavra(palavra):
    palavra_encondida = []
    for letra in palavra:
        if letra != ' ':
            palavra_encondida.append('_')
        else:
            palavra_encondida.append(' ')
    return palavra_encondida


def trata_palavra_encondida(palavra):
    palavra_tratada = ' '.join(palavra)
    return palavra_tratada


def lista_ocorrencias_letra(palavra, letra):
    import re
    lista_index = []
    for index in re.finditer(letra, palavra):
        lista_index.append(index.start())
    return lista_index


letras_tentadas = []


dict_palavras_por_genero = {
    'filmes':['interestelar 2', 'interestelar 3'],
    'games':['war a', 'war az2']
}


genero = 'Nome pessoa'

# palavra = escolha_palavra_por_genero(dict_palavra=dict_palavras_por_genero, genero=genero)
# palavra = 'war az2'


fake = Faker(['PT-br'])
palavra = str(fake.name()).strip().lower()

palavra_encondida = esconde_palavra(palavra=palavra)
palavra_tratada = trata_palavra_encondida(palavra=palavra_encondida)

FORCAIMG = ['''
 
  +---+
  |   |
      |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
 
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

cont = 6
while True:
    print(FORCAIMG[cont])
    print(' '.join(palavra_encondida))
    print()
    print(f'genero : {genero}')
    print()
    tentativa = str(input('Digite uma letra: ')).strip().lower()

    print(f'Letras Tentadas: {"".join(letras_tentadas)}')

    if not tentativa in letras_tentadas:

        if tentativa in palavra:
            lista_index = lista_ocorrencias_letra(palavra=palavra, letra=tentativa)
            for index in lista_index:
                palavra_encondida[index] = tentativa

        else:
            cont -= 1
            letras_tentadas.append(tentativa)

            print(f"Nenhuma letra {tentativa} Encontrada")

        # print(f'tentativa numero: {len(letras_tentadas)}')
        if not '_' in palavra_encondida:
            print()
            print('Você Ganhou !!!')
            print(f'A palavra era "{palavra}"')
            print(f'Foram necessarias {len(letras_tentadas)} Tentativas')
            print()
            break

        if len(letras_tentadas) > 5:
            print()
            print(f'Enforcado !! ;0, a palavra era: {palavra}')
            print()
            break
    else:
        print(f'Ja tentou está letra {tentativa}')
        


