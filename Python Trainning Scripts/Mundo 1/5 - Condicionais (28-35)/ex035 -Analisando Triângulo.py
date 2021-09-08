print('Vamos avaliar se três retas podem formar um triângulo.')
r1 = float(input('Favor informar o tamanho da 1ª reta: '))
r2 = float(input('Agora o tamanho da 2ª reta: '))
r3 = float(input('Por fim, favor informar o tamanho da 1ª reta: '))
l = [r1, r2, r3]
l.sort()
if l[0] + l[1] > l[2]:
    print('As retas de tamanhos {}, {} e {} PODEM formar um triângulo!'.format(l[0], l[1], l[2]))
else:
    print('As retas de tamanhos {}, {} e {} NÃO PODEM formar um triângulo!'.format(l[0], l[1], l[2]))