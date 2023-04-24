#Recorte de documento Centro de Costos
l1 = []
with open(r"C:\AUTOMATE\Centro_de_costos.csv", 'r') as fp:
    l1 = fp.readlines()
with open(r"C:\AUTOMATE\Centro_de_costos.csv", 'w') as fp:
    for number, line in enumerate(l1):
        if number not in range (491, 4411):
            fp.write(line)
            

#Reemplazar nombre de cubos
# with open(r"C:\AUTOMATE\Centro_de_costos.csv", 'r') as fp:
    # cubo = fp.read()
# with open(r"C:\AUTOMATE\Centro_de_costos.csv", 'w') as fp:
    # cubo = cubo.replace("GASTOS","PLA_CAP")
    # fp.write(cubo)
    
#Reemplazar nombre de cubos
# with open(r"C:\AUTOMATE\Empresas.csv", 'r') as fp:
    # cubo1 = fp.read()
# with open(r"C:\AUTOMATE\Empresas.csv", 'w') as fp:
    # cubo1 = cubo1.replace("EEFF","PLA_CAP")
    # fp.write(cubo1)