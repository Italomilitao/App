import locale

# Esse condigo não está pronto

# Definir a localidade como 'pt_BR' para o formato brasileiro (ou outra região, se desejado)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

print("************************ Calculadora de Juros Compostos ************************")
valor_inicial=float(input("Valor Inicial: "))
print("")
taxa_de_juros_anual=float(input("Taxa de Juros Anual: "))
print("")
periodo=float(input("Período: "))
print("")

def jurosporanodecimal():
    return  taxa_de_juros_anual / 100
juros_por_ano_decimal = jurosporanodecimal()
#print(f"{juros_por_ano_decimal:.2f}")

def jurosComposto():
    return (1 + juros_por_ano_decimal)**periodo
juros_composto = jurosComposto()
#print(f"{juros_composto:.3f}")

def ValorTotalFinal():
    return valor_inicial * juros_composto
valor_total_final = ValorTotalFinal()
print("Valor Total Final")
print(locale.currency(valor_total_final, grouping=True))

print("*************************************************************************")
print("*********************** Tabela de valor acumulado ***********************")
print("*************************************************************************")

def jurosPorMes():
    return  ((taxa_de_juros_anual / 100) / 12) * 12
juros_por_mes = jurosPorMes()
#print(f"{juros_por_mes:.4f}")

acumulado = valor_inicial
while acumulado <= valor_total_final:
    print(locale.currency(acumulado, grouping=True))
    #print(acumulado)
    acumulado += (juros_por_mes * 100)
print("*********************** Fim ***********************")

# Esse condigo não está pronto