condicion = 10
if condicion == True :
    print("La condición es verdadera")
elif condicion == False:    
    print("La condición es falsa")
else:
    print("Condición no reconocida")    
    
numero = int(input("Proporciona un número entre 1 y 3:"))
if numero == 1:
    numeroTexto = "número uno"
elif numero == 2:
    numeroTexto = "número dos"    
elif numero == 3:
    numeroTexto = "número tres"  
else:
    numeroTexto = "Valor fuera de rango"
    
print("número proporcionado:", numeroTexto)        
    