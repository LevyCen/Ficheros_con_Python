#Abre un archivo y le escribe
for i in [0,1,2]:
    resultados = open('resultado.csv','a+')
    resultados.write("Cosa 3 \n")
    resultados.close()
