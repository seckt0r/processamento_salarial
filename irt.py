from decimal import *

def calc_irt(sb):
    irt = float(0)
    if sb <= float(34450):
        irt = float(0)
    elif sb >= float(34451) and sb <= float(35000):
        irt = float(sb) - (34450)
    elif sb >= float(35001) and sb <= float(40000):
        irt = float(550) + ((sb - float(35000)) * 0.07)
    elif sb >= float(40001) and sb <= float(45000):
        irt = float(900) + ((sb - float(40000)) * 0.08)
    elif sb >= float(45001) and sb <= float(50000):
        irt = float(1300) + ((sb - float(45000)) * 0.09)
    elif sb >= float(50001) and sb <= float(70000):
        irt = float(1750) + ((sb - float(50000)) * 0.10)
    elif sb >= float(70001) and sb <= float(90000):
        irt = float(3750) + ((sb - float(70000)) * 0.11)
    elif sb >= float(90001) and sb <= float(110000):
        irt = float(5950) + ((sb - float(90000)) * 0.12)
    elif sb >= float(110001) and sb <= float(140000):
        irt = float(8350) + ((sb - float(110000)) * 0.13)
    elif sb >= float(140001) and sb <= float(170000):
        irt = float(12250) + ((sb - float(140000)) * 0.14)
    elif sb >= float(170001) and sb <= float(200000):
        irt = float(16450) + ((sb - float(170000)) * 0.15)
    elif sb >= float(200001) and sb <= float(230000):
        irt = float(20950) + ((sb - float(200000)) * 0.16)
    elif sb >= float(230001):
        irt = float(25750) + ((sb - float(230000)) * 0.17)
    sl = sb - irt
#    return print("\nO desconto é de: %s" % (irt))
    return print("\nO desconto é de: %s \nO Salário líquido é: %s" % (irt, sl))

sb = float(input("Digite o salário base: "))
calc_irt(float(sb))

