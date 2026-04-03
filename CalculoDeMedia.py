#variaveis para armazenar as notas, nome e média
nota1 = int(input("insira a primeira nota")) #input de usuário para a nota 1
nota2 = int(input("insira a segunda nota"))
nota3 = int(input("insira a terceira nota"))
media = (nota1 + nota2 + nota3)/3 #calculo de média
nome = input("insira o nome do aluno") #inserindo o nome do aluno
if media<7: #verificando se a média é menor que 7
    print("O aluno " + nome + "está de recuperação") #a media é menor que 7
else:
    print("O aluno " + nome + "está aprovado") 
