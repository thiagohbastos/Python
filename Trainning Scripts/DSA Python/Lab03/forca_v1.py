# Hangman Game (Jogo da Forca) 
# Programação Orientada a Objetos

# %%Import
import random

# Board (tabuleiro)
board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
    |
    |
    |
=========''', '''

+---+
|   |
O   |
|   |
    |
    |
=========''', '''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', '''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']


# Classe
class Hangman:

	# Método Construtor
	def __init__(self, word):
		self.word = word
		self.len_word = len(self.word)
		self.letras_erradas = []
		self.letras_corretas = []
		self.qtd_letras_desc = 0
		#status do game
		self.n = 0
		self.status = board[self.n]
		
	# Método para adivinhar a letra
	def guess(self, letter):
		if letter not in self.word and letter not in self.letras_erradas:
			self.letras_erradas.append(letter)
			self.n += 1
			self.status = board[self.n]
		elif letter in self.word and letter not in self.letras_corretas:
			self.letras_corretas.append(letter)
			self.qtd_letras_desc += self.word.count(letter)
		else:
			print('Letra digitada anteriormente! \nFavor digitar uma nova letra.\n')
		print(f'Letras erradas: {[x for x in self.letras_erradas]}\n')
		print(f'Letras corretas: {[x for x in self.letras_corretas]}\n')
		
	# Método para verificar se o jogo terminou
	def hangman_over(self) -> bool:
		if len(self.letras_erradas) >= 6 or self.qtd_letras_desc >= len(self.word):
			return True
		else:
			return False

	# Método para verificar se o jogador venceu
	def hangman_won(self):
		pass

	# Método para não mostrar a letra no board
	def hide_word(self):
		print(f'Palavra: {self.word}\n')
		
	# Método para checar o status do game e imprimir o board na tela
	def print_game_status(self):
		print(self.status)
		self.hide_word()
		print(f'Game finalizado? {self.hangman_over()}\n')

# Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
        with open("palavras.txt", "rt") as f:
                bank = f.readlines()
        return bank[random.randint(0,len(bank))].strip()


# Função Main - Execução do Programa
def main():

	# Objeto
	game = Hangman(rand_word())

	# Enquanto o jogo não tiver terminado, print do status, solicita uma letra e faz a leitura do caracter
	while True:
		game.print_game_status()
		letter = input('Digite uma letra: ')
		game.guess(letter)
		if game.hangman_over() == True:
			break

	# Verifica o status do jogo
	game.print_game_status()	


	# De acordo com o status, imprime mensagem na tela para o usuário
	if game.hangman_won():
		print ('\nParabéns! Você venceu!!')
	else:
		print ('\nGame over! Você perdeu.')
		print ('A palavra era ' + game.word)
		
	print ('\nFoi bom jogar com você! Agora vá estudar!\n')

# Executa o programa		
if __name__ == "__main__":
	main()


# %%
