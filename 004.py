#Desafio 004 -  Crie um programa que leia algo pelo teclado e mostrar na tela o seu tipo primitivo e todas as informações sobre ele.
y = input('Digite algo: ')
print('o tipo o primitivo é: ',type(y))
print('É alfa númerico?',y.isalnum())#verifica se todos os caracteres em uma determinada string são alfanuméricos ou não
print('Esta todos os caracteres maisculos?',y.isupper())#etorna “True” se todos os caracteres da string estiverem em maiúsculas, caso contrário, retorna “False”. Sintaxe: string
print('Todos caracteres são letras?',y.isalpha())#retorna “True” se todos os caracteres na string forem alfabetos, caso contrário, retorna “False”. Esta função é usada para verificar se o argumento inclui apenas caracteres do alfabeto
print('Todos caracteres são números?',y.isnumeric())#retorna “True” se todos os caracteres da string forem numéricos, caso contrário, retorna “False”. Sintaxe: Parâmetros string
print('É caractere ASCII',y.isascii())#Retorna True se a string é vazia ou se todos os caracteres na string são ASCII, False caso contrário. Caracteres ASCII têm pontos de código no intervalo U+0000-U+007F.
print('São todos caracteres decimais?',y.isdecimal())#Retorna True se todos os caracteres na string são caracteres decimais e existe pelo menos um caractere, False caso contrário. Caracteres decimais são aqueles que podem ser usados para formar números na base 10
print('São todos digitos os caracteres?',y.isdigit())#Retorna True se todos os caracteres na string são dígitos e existe pelo menos um caractere, False caso contrário.
print('É uma string',y.isidentifier())#Retorna True se a string é um identificador válido conforme a definição da linguagem, seção Identificadores e palavras-chave. - Chame keyword.iskeyword() para testar se a string s é uma palavra reservada, tal como def e class.
print('Existe algum cactere númerico?',y.islower())#Retorna True se todos os caracteres na string são caracteres numéricos, e existe pelo menos um caractere, False caso contrário. Caracteres numéricos incluem dígitos
print('Os caracteres da string podem ser impresos?',y.isprintable())#Retorna True se todos os caracteres na string podem ser impressos ou se a string é vazia, False caso contrário
print('Existem espaços em branco',y.isspace())#Retorna True se existem apenas caracteres de espaço em branco na string e existe pelo menos caractere, False caso contrário
print('Está capitalizada(maiscula com minuscula)?',y.istitle())#Retorna True se a string é titlecased e existe pelo menos um caractere, por exemplo caracteres maiúsculos somente podem proceder caracteres que não diferenciam maiúsculas/minúsculas, e caracteres minúsculos somente podem proceder caracteres que permitem ambos. Retorna False caso contrário.
