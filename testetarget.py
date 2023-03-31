## Q2
search = input()
fibinit = 0
fib = 1
aux
while (fib < search):
  aux = fibinit + fib
  fibinit = fib
  fib = aux

if search == fib :
  print("Valor pertence a fibonacci")
if search != fib :
  print("Valor não pertence a fibonacci")


##  Q3  
fatMensal = [10, 14, 12, 13, 20]

minFatMensal = fatMensal[0]
for i in fatMensal:
	if minFatMensal > i:
		minFatMensal = i
print(minFatMensal, ': menor Valor')

maxFatMensal = 0
for i in fatMensal:
	if maxFatMensal < i:
		maxFatMensal = i
print(maxFatMensal, ': Maior Valor')

sumFatMensal = 0
for i in fatMensal:
	sumFatMensal = i + sumFatMensal
meanFatMensal = sumFatMensal / (len(fatMensal))
cont = 0
for i in fatMensal:
	if meanFatMensal < i:
		cont += 1
print(meanFatMensal, ': Média')
print(cont, ': Ocorrencias acima da media')

##  Q4

fatPorEstado = [6783643, 3667866, 2922988, 2716548, 1984953]
sumFat = 0

for i in fatPorEstado:
	sumFat = sumFat + i

print(
  'SP: ',100/(sumFat/fatPorEstado[0]),'%',
  '    RJ: ',100/(sumFat/fatPorEstado[1]),'%',
  '    MG: ',100/(sumFat/fatPorEstado[2]),'%',
  '    ES: ',100/(sumFat/fatPorEstado[3]),'%',
  '    Outros: ',100/(sumFat/fatPorEstado[4]),'%')

##  Q5

string = 'retrevni'
inverted = ''
for i in range(len(string)):
	aux = string[len(string) - 1 - i]
	inverted += aux
print(inverted)
