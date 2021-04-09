import os

# Input
# ---aaattcc---cccc--
# aactgtgactgcatgcatgactgactg
# Output
# aaattcc---cccc
# tgtgactgcatgcatgactgac

def contar_no_comeco(sequencia):
  tracos = 0
  for c in sequencia:
    if c == '-':
      tracos = tracos + 1
    else:
      break
  return tracos

def contar_no_final(sequencia):
  return contar_no_comeco(reversed(sequencia))


def teste():
  seq1 = '---aaattcc---cccc--'
  seq2 = 'aactgtgactgcatgcatgactgactg'

  inicio = contar_no_comeco(seq1)
  final = contar_no_final(seq2)

  print(seq1[inicio:-f])
  print(seq2[inicio:-f])

with open('input/DEV1-X-gb_A75711.fasta.aln') as fasta:
  conteudo = fasta.read()
  linhas = conteudo.split('\n')
  cabecalho1 = linhas[0]
  indice = 0
  for l in linhas:
    if '>gb' in l:
      break
    indice = indice + 1

  cabecalho2 = linhas[indice]
  seq1 = ''.join(linhas[1:indice])
  seq2 = ''.join(linhas[indice+1:])

  with open(os.path.join('output', 'resultado.fasta', 'w')) as res:
    res.write(cabecalho1 + '\n')
    tracos_inicio = contar_no_comeco(seq1)
    tracos_final = contar_no_final(seq1)
    # escreve sequencia editada
    res.write(seq1[tracos_inicio:-tracos_final] + '\n')
    res.write(cabecalho2 + '\n')
    res.write(seq2)

def write():
  with open('cabecalho1.txt', 'w') as temp:
    temp.write(seq1)
  
  with open('cabecalho2.txt', 'w') as temp:
    temp.write(seq2)

  with open('sequencia1.txt', 'w') as temp:
    temp.write(seq1)

  with open('sequencia2.txt', 'w') as temp:
    temp.write(seq2)
