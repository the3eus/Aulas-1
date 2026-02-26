#formulario 

nome = input('Qual seu nome: ')
sobrenome = input('Qual seu sobrenome: ')
dia_nasc = input('Qual dia de nascimento: ')
mes_nasc = input('Qual seu mes de nascimento: ')
ano_nasc = input('Qual seu ano de nascimento: ')
uni = input('Qual universidade voce estuda: ')


e_mail = nome.lower() + '.' + sobrenome.lower() + '@' + uni.lower() + '.br'
senha = 'a' + str(e_mail.count('a')) + 'e' + str(e_mail.count('e')) + 'i' + str(e_mail.count('i')) + 'o' + str(e_mail.count('o')) + 'u' + str(e_mail.count('u'))

print('seu email é: {}'.format(e_mail))
print('sua senha é: {}'.format(senha))

print('o seu email e sua senha são: {};{}'.format(e_mail,senha))



