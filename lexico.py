import rules as rl
import letra_por_letra as lpl
import diccionario as dic



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
                    print(dic.tipo[new_rules["current_line"]])
                continue
            if pos == 500:
                print(dic.errores[new_rules["current_line"]])
                return False
            break

texto_prueba = lpl.texto("ejemplo.txt")

analizador_lexico(texto_prueba, rl.data, rl.rules)

