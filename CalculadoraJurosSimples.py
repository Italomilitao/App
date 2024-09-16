import locale

# Definir a localidade como 'pt_BR' para o formato brasileiro (ou outra região, se desejado)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

print("************************ Calculadora de Juros Compostos ************************")
valor_inicial=float(input("Valor Inicial: "))
print("")
taxa_de_juros_anual=float(input("Taxa de Juros Anual: "))
print("")
periodo=float(input("Período: "))
print("")

def taxaDeJurosAnualDeciaml():
    return taxa_de_juros_anual / 100
taxa_de_juros_anual_decimal = taxaDeJurosAnualDeciaml()
#print(taxa_de_juros_anual_decimal)

def PeriodoEmMeses():
    return periodo * 12
periodo_em_meses = PeriodoEmMeses()
#print(periodo_em_meses)

def jurosSimples():
    return valor_inicial * taxa_de_juros_anual_decimal * periodo
juros_acumulado = jurosSimples()
print("Tota em Juros")
print(locale.currency(juros_acumulado, grouping=True))

print("Valor Total Investido")
print(locale.currency(valor_inicial, grouping=True))

def montante():
    return valor_inicial + juros_acumulado
valor_final = montante()
print("Valor Total Final")
print(locale.currency(valor_final, grouping=True))

print("*************************************************************************")
print("*********************** Tabela de valor acumulado ***********************")
print("*************************************************************************")

juros_por_ano = valor_inicial

while juros_por_ano <= valor_final:
    print(locale.currency(juros_por_ano, grouping=True))
    juros_por_ano += (juros_acumulado / periodo_em_meses )
print("*********************** Fim ***********************")