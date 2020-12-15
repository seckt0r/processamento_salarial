from decimal import *

def calc_inss(sb,st,sa):
    inss1 = float(0)
    inss2 = float(0)
    inss1 = (sb + st + sa) * 0.03
    inss2 = sb * 0.03
    inss3 = (sb + st + sa) * 0.08
    sl = sb-inss2
    print("\nA contribuição do funcionário para o INSS é de: %s" % (inss1))
    print("\nA contribuição da empresa para o INSS é de: %s" % (inss3))
    print("\nO desconto de INSS para cálculo do IRT é de: %s \nO valor salarial para cálculo do IRT é: %s" % (inss2, sl))
    return sl

def calc_irt(sb):
    irt = float(0)
    if sb <= float(70000):
        irt = float(0)
    elif sb >= float(70001) and sb <= float(100000):
        irt = float(3000) + ((sb - float(70000)) * 0.10)
    elif sb >= float(100001) and sb <= float(150000):
        irt = float(6000) + ((sb - float(100000)) * 0.13)
    elif sb >= float(150001) and sb <= float(200000):
        irt = float(12500) + ((sb - float(150000)) * 0.16)
    elif sb >= float(200001) and sb <= float(300000):
        irt = float(31250) + ((sb - float(200000)) * 0.18)
    elif sb >= float(300001) and sb <= float(500000):
        irt = float(49250) + ((sb - float(300000)) * 0.19)
    elif sb >= float(500001) and sb <= float(1000000):
        irt = float(87250) + ((sb - float(500000)) * 0.20)
    elif sb >= float(1000001) and sb <= float(1500000):
        irt = float(187250) + ((sb - float(1000000)) * 0.21)
    elif sb >= float(1500001) and sb <= float(2000000):
        irt = float(292250) + ((sb - float(1500000)) * 0.22)
    elif sb >= float(2000001) and sb <= float(2500000):
        irt = float(402250) + ((sb - float(2000000)) * 0.23)
    elif sb >= float(2500001) and sb <= float(5000000):
        irt = float(517250) + ((sb - float(2500000)) * 0.24)
    elif sb >= float(5000001) and sb <= float(10000000):
        irt = float(1117250) + ((sb - float(5000000)) * 0.24,5)
    elif sb >= float(10000001):
        irt = float(2342250) + ((sb - float(10000000)) * 0.25)
    sl = sb - irt
    print("\nO desconto de IRT é de: %s" % (irt))
    return irt

sb = float(input("Digite o salário base: "))
st = float(input("Digite o subsídio de transporte: "))
sa = float(input("Digite o subsídio de alimentação: "))

#calc_inss(float(sb))
base = calc_inss(float(sb), float(st), float(sa))

salario_liquido = (sb + st + sa) - (calc_irt(float(base)))
print("\nO salário líquido é de: %s" % (salario_liquido))

