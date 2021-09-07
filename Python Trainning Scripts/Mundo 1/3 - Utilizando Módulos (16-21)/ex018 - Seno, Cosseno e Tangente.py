from math import sin, cos, tan, degrees, radians
angulo = float(input('Favor digitar um ângulo para conversão (em graus º): '))
conv = radians(angulo)
print('Seguem as conversões do ângulo de {:.0f}º: \n- Seno: {:.2f}\n- Cosseno: {:.2f}\n- Tangente: {:.2f}'.format(angulo, sin(conv), cos(conv), tan(conv)))

