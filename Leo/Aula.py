list01 = [5,10,15,20]
list02 = ["","",""]
list03 = ["unipê",10.5,4,list01]
print(list03)
minha_lista = ["Ana","Bia","Pedro","Caio"]
print (minha_lista[2])

# FUNÇÃO LEN------------------------------------
list = ["Ana",50,10,"Unipê", (1,2,3,4),"bia","marcelo","caio"]
print(len(list))

# FUNÇÃO REMOVE----------------------------------
list = [2,4,6,8]
list.remove (6)

print (list)

# MAIS DE UMA LISTA------------------------------
list = [1,2,3,4,5]
list02 = [6,7,8,9,10]
list03 = list = list02

print(list03)

#ATIVIDADE 01-------------------------------------
list01 = ["Detergente","desinfetante","Água sanitária","Sabão em pó","Papel toalha"]

print (list01)

list[0] = "Sabão em barra"
print(len(list))

print(len(list))

list.remove[5]
list02 = ["Esponja", "vassoura", "Espanador"]
print((list01 + list02 ))

#FUNÇÃO POP---------------------------------------
list = [1,2,3,4]
list02 = [5,6,7,8,9,10]
list03 = list = list02
print (list03)

list03.pop(0) #removendo o primeiro elemento da lista
list03.pop(len(list03 - 1)) #removendo o ultimo elemento da lista
print(list03)

#FUNÇÃO APPEND-------------------------------------
notas = []

notas.append (float(input("Digite a nota do primeiro aluno: ")))
notas.append (float(input("Digite a nota do segundo aluno: ")))
notas.append (float(input("Digite a nota do terceiro aluno: ")))

print(notas)

#ATIVIDADE 02----------------------------------------
notas = []

notas.append (float(input("Digite a nota do primeiro aluno: ")))
notas.append (float(input("Digite a nota do segundo aluno: ")))
notas.append (float(input("Digite a nota do terceiro aluno: ")))

soma = (notas[0] + notas[1] + notas[2])/len(notas)
print(notas)

print("A média dos alunos é: {}" .format(soma))

#FUNÇÃO INSERT----------------------------------------
list01 = [1,2,3,4]
list02 = [5,6,7,8,9,10]
list03 = list01 + list02
print(list03)

list03.insert(2, 15) #Adiciona 15 na posição de indice 2
print(list03)

list03.insert(len(list03), 18) #Adiciona 185 na ultima posição da lista
print(list03)

#for e list-------------------------------
notas = [12.0, 7.5, 90, 4.5]
for i in range (4):
 print(notas[i])

#------------------------------------------
num_alunos = 4
nomes = []
notas = []
media = 0

for i in range(num_alunos):
 nomes.append(input("Informe o nome do aluno: "))
 notas.append(float(input("Informe a nota de" + nomes[i] + ": ")))
 media = media = notas[i]
media = media / num_alunos

print("A média de turma é: {}" .format)

for i in range(num_alunos):
 if notas[i] > media:
 print("Parabéns {}!" .format(nomes[i]))