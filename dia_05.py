import random

# Sorteio:
# definir a lista de nomes
var_listNomesSorteio = ['Ana', 'Beatriz', 'Clara', 'Daiane', 'Edna', 'Flavia']

# verificar o tamanho da lista
var_intTamanhoLista = len(var_listNomesSorteio)

var_listSorteados = []

# determina os 3 primeiros lugares do sorteio numa nova lista
for lugares in range(3): #pseudolista de 3 posições
    # randomizar o indice
    var_numRandomIndice = random.randint(0, (var_intTamanhoLista - 1))

    # removendo o nome sorteado
    var_strSorteado = var_listNomesSorteio.pop(var_numRandomIndice)

    # acrescentando o nome sorteado a lista de sorteados
    var_listSorteados.append(var_strSorteado)

print(var_listNomesSorteio)
print(var_listSorteados)

def ler_planilha(arg_caminhoARquivo):
    """FUncao para ler 

    Args:
        arg_caminhoARquivo (str): _description_
    """
 
    pass

# Acessando site banco itau

# inserindo credenciais
