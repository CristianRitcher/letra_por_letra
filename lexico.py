import rules as rl
import diccionario as dic

lexico_lista = []

def texto(nombre_archivo):
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    return contenido

def analizador_lexico(texto, lista, rules):
    pos = 0
    for i in texto:
        while True:
            if pos < 100:
                new_rules = rl.reglas_update(pos, rules, lista)
                pos = new_rules[i]
            if pos == 100:
                pos = 0
                if dic.tipo[new_rules["current_line"]] == "":
                    pass
                else:
                    lexico_lista.append(dic.tipo[new_rules["current_line"]])
                continue
            if pos == 500:
                print(dic.errores[new_rules["current_line"]])
                return False
            break
        (lexico_lista)
    return lexico_lista

analizador_lexico(texto("ejemplo.txt"), rl.data, rl.rules)

