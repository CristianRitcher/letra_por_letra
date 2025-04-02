import csv
import lexico as lex
import rules as rl
import diccionario as dic

reservados = ["{", "}", "!init", "!end", ":=", ";", "$", "true", "false"]

def read_csv(datos_csv):
    datos = {}
    with open(datos_csv, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)  
        for fila in lector:
            nombre = fila.pop("nombre")  
            datos[nombre] = fila
    return datos

def check_sintaxis(text, sintax_table, prods):
    print("\n")
    print("\033[1mArgumento a validar: \033[0m", f"\033[103m{" ".join(text)}\033[0m")
    print("\n")
    pile = ["$", "<PROGRAM>"]
    token = text[0]
    try:
        while True:
            if token == pile[-1]:
                print("\033[1mPila se cancela: \033[0m", " ".join(pile))
                print("\033[1mCon elemento de: \033[0m", " ".join(text))
                text.pop(0)
                pile.pop()
                print("\033[1mPila queda: \033[0m", " ".join(pile))
                print("\033[1my argumento: \033[0m", " ".join(text))
                print(" ")

                if (pile == []) or (text == []):
                    
                    if pile == text:
                        return "\033[92mSINTAXIS VÁLIDA ✅ ✅ ✅\033[0m"
                    else:
                        return "\033[91mSINTAXIS INVÁLIDA ⚠️⚠️⚠️\033[0m"
                token = text[0]
            else:
            
                print("\033[1mNo terminal: \033[0m", pile[-1])
                print("\033[1mTerminal: \033[0m", token)
                index = sintax_table[pile[-1]][token]
                print("\033[1mProducción: \033[0m", index, "\n")
                print("\033[1mPila se transforma de: \033[0m", " ".join(pile))
                pile.pop()
                
                for i in  range(7, 0, -1):
                    i = str(i)
                    if prods[index][i] != "":
                        pile.append(prods[index][i])
                        if pile[-1] == "ε":
                            pile.pop()
                            print("\033[1ma\033[0m", " ".join(pile), "[' ']")
                            print("\033[1mSe elimina: '' \033[0m")
                print("\033[1men: \033[0m", " ".join(pile))
                print(" ")
    except:
        return "\033[91mSINTAXIS INVÁLIDA ⚠️⚠️⚠️\033[0m"

reglas_sintaxis = read_csv("SYNTAX/SYNTAX_TABLE.csv")
producciones = read_csv("SYNTAX/PRODUCTIONS.csv")

with open("ejemplo.txt", "r", encoding="utf-8") as file:
    file = file.read()
    text = [word for word in file.split()]

lex_text = lex.analizador_lexico(lex.texto("ejemplo.txt"), rl.data, rl.rules)

print("\n")
print("\033[1mArgumento: \033[0m", f"\033[103m{" ".join(text)}\033[0m", "\n")
print("\033[1mTokenización: \033[0m","\033[34m | \033[0m".join(lex_text) , "\n")


text_2 = []
for i in range(0, len(text)):
    
    if (lex_text[i] == "identifier") and (lex_text[i+1] == "Igual a"):
        
        if lex_text[i+2] == "Palabra reservada":
            lex_text[i+2] = "bool"
        ite = 0
        for pos1, pos2, pos3 in text_2:
            if (pos1 == text[i]) and (pos3 != lex_text[i+2]):
                print("\n")
                err = f"Error en variable: la variable {text[i]} es {pos3} y se trató de asignar un valor de tipo {lex_text[i+2]}"
                raise TypeError(err)
            elif (pos1 == text[i]) and (pos3 == lex_text[i+2]):
                text_2[ite][0] = ""
                text_2[ite][1] = ""
                text_2[ite][2] = ""
            ite += 1
        print("\n")
        print("\033[1mLista de variables:\033[0m")
        text_2.append([text[i], text[i+2], lex_text[i+2]])
        for j in text_2:
            if j[0] != "":
                print(j)

    if text[i] not in reservados:
        text[i] = lex_text[i]
        

print(text)    
    
print(check_sintaxis(text, reglas_sintaxis, producciones))