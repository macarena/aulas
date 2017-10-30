def calcularamedia(ab,cd):
    return (ab + cd) /2


def tirar_media(aluno):
    nota1 = input("qual foi a nota da primeira prova de {}".format(aluno))
    nota2 = input("qual foi a nota de segunda prova de {}".format(aluno))
    nota1 = float(nota1)
    nota2 = float(nota2)
    media = calcularamedia(nota1, nota2)
    print("a media de {} foi {}".format(aluno,media))
    return media


alunos = ["João", "Pedro", "Marco", "Gustavo", "Fernando"]
medias = {}

for aluno in alunos:
    media = tirar_media(aluno)
    medias[aluno] = media

print(medias)