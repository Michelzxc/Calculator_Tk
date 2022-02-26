def operatron(texto):
    '''Opera la cadena texto de entrada devolviendo el resultado.
    Si la cadena es invalida devuelve "syntax error".'''

    valores_y_operadores = []

    # Validador
    valor_provisorio = ""
    for x in texto:
        if x in ".0123456789":
            valor_provisorio += x

            continue

        if x in "+-*/":
            try:
                valores_y_operadores.append(float(valor_provisorio))
                valor_provisorio = ""
                valores_y_operadores.append(x)

                continue
            
            except:
                return "syntax error"

    try:
        valores_y_operadores.append(float(valor_provisorio))
        valor_provisorio = ""
            
    except:
        return "syntax error"
    
    # Estandarizador
    while True:
        if "-" in valores_y_operadores:
            pos_r = valores_y_operadores.index("-")
            valores_y_operadores[pos_r] = "+"
            valores_y_operadores[pos_r+1] = valores_y_operadores[pos_r+1] * (-1)

            continue

        if "/" in valores_y_operadores:
            pos_d = valores_y_operadores.index("/")
            valores_y_operadores[pos_d] = "*"
            valores_y_operadores[pos_d+1] = 1/(valores_y_operadores[pos_d+1])
            
            continue

        break

    # Calculadora
    while True:
        if "*" in valores_y_operadores:
            pos_m = valores_y_operadores.index("*")
            resultado_provisorio = valores_y_operadores[pos_m-1] * valores_y_operadores[pos_m+1]
            valores_y_operadores[pos_m] = resultado_provisorio
            valores_y_operadores.pop(pos_m+1)
            valores_y_operadores.pop(pos_m-1)

            continue

#        elif "/" in valores_y_operadores:
#            pos_m = valores_y_operadores.index("/")
#            resultado_provisorio = valores_y_operadores[pos_m-1] / valores_y_operadores[pos_m+1]
#            valores_y_operadores[pos_m] = resultado_provisorio
#            valores_y_operadores.pop(pos_m+1)
#            valores_y_operadores.pop(pos_m-1)
#
#            continue
        
        elif "+" in valores_y_operadores:
            pos_m = valores_y_operadores.index("+")
            resultado_provisorio = valores_y_operadores[pos_m-1] + valores_y_operadores[pos_m+1]
            valores_y_operadores[pos_m] = resultado_provisorio
            valores_y_operadores.pop(pos_m+1)
            valores_y_operadores.pop(pos_m-1)

            continue

#        elif "-" in valores_y_operadores:
#            pos_m = valores_y_operadores.index("-")
#            resultado_provisorio = valores_y_operadores[pos_m-1] - valores_y_operadores[pos_m+1]
#            valores_y_operadores[pos_m] = resultado_provisorio
#            valores_y_operadores.pop(pos_m+1)
#            valores_y_operadores.pop(pos_m-1)
#
#            continue

        break
    
    return str(valores_y_operadores[0])
