import math

while True:
    x = float(input("Digite o 1 numero\n"))
    y = float(input("Digite o 2 numero\n"))

    x1 = x**3 + 5*math.sin(x)
    x2 = y**3 + 5*math.sin(y)

    y1 = -2*x - 4
    y2 = -2*y - 4

    if x1 < 0 and x2 > 0 or x1 > 0 and x2 < 0 :
        print("a equação tem pelo menos uma solução neste intervalo\n")
    elif y1 < 0 and y2 > 0 or y2 < 0 and y1 > 0:
        print("a equação tem pelo menos uma solução neste intervalo\n")
    else:
        print("não é possível afirmar que existe solução neste intervalo, tente outros dois números")
    a = int(input("Digite 0 para parar e digite 1 para tentar outro intervalo\n"))
    if a == 0:
        break