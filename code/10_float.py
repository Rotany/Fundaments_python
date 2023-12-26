x= 3.3
print( x)
y= 2.2 + 1.1
print(y)
print(x == y)
y_str= format(y , "0.2g") # aqui convertimos  a la y sring y con format vamos a decirle que solo queremo 2 digitos
print('str=>', y_str)
print(y_str==str(x)) # convertimos a x en string para poder hacer la comparación.


tolerance = 0.00001  # forma matematicas de quitar la tolerancia de un decimal.
print(abs(x-y)<tolerance)