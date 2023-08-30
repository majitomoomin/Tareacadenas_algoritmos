producto=str(input("Introduce el precio de algún producto con decimales: "))
print(producto[:producto.find('.')], ' euros y ', producto[producto.find('.')+1:],'centimos')
