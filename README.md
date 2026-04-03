# Cálculo de média em Python
Um simples programa que computa a média de três notas de um aluno, qual deve ser aprovado se a media for maior que 7
<h2>Fluxograma</h2>
<img src="https://raw.githubusercontent.com/LeticiaHartstein/Calculo-de-media-Cpp/refs/heads/main/Fluxograma-Calculo_de_media.svg" alt = "fluxograma - média de idade">
<h2>Lógica</h2>
<ol>
  <li>Recebe as três notas dos alunos </li>
  <li>Recebe o nome do aluno</li>
  <li>Soma as três notas e as divide por três para calcular a média</li>
  <li>Verifica se a média é maior que 7</li>
  <li>Encerra o programa</li>
</ol>
<h2>Código</h2>

```python
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
````
<h2>Teste/Output: </h2>
<img width="471" height="113" alt="image" src="https://github.com/user-attachments/assets/1b125dfd-5636-40b1-b7ec-834a00855249" />
