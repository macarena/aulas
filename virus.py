import random
import time
print('\n\n[--system--] um arquivo é bom outro ruim... advinhe qual.\n')
print('\n\nconectando....')
time.sleep(1)
print('....')
time.sleep(1)
print('....')
time.sleep(1)
print('....')
time.sleep(1)
print('\nconexão estabelecida')

def displayIntro():
	print('------------')
	print('SYSTEM FILES')
	print('------------\n')
	print('1.) arquivo.')
	print('2.) arquivo.\n')
	
def chooseOption():
	option = ''
	while option != '1' and option != '2':
		print('qual baixar? 1 ou 2')
		option = raw_input('user:> ')
		
	return option
	
def checkOption(chosenOption):
	print('\niniciando download....')
	time.sleep(1)
	print('acessando arquivo....')
	time.sleep(1)
	print('baixando....')
	time.sleep(1)
	print('....')
	time.sleep(1)
	print('....')
	time.sleep(1)
	
	goodfile = random.randint(1, 2)
	
	if chosenOption == str(goodfile):
		print('\ndownload completo.')
		print('\nVocê Venceu!!')
		
	else:
		print('\narquivo corrompido')
		print('sistema infectado.')
		print('\nGAME OVER')
		
		
playAgain = 'sim'
while playAgain == 'sim':
	displayIntro()
	optionNumber = chooseOption()
	checkOption(optionNumber)
	
	print('\nbaixar novamente? .... (sim ou não)')
	playAgain = raw_input('user:> ')
