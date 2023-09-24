#Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o
# empréstimo será negado.

valorcasa = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
anos = int(input('Quantos anos de financiamento: '))
meses = anos * 12
parcela = valorcasa / meses
porcento = (salario / 100) * 30
print('Para pagar uma casa de R${:.2f} em {} anos, a prestaçao sera de R${:.2f}'.format(valorcasa, anos, parcela))
if parcela <= porcento:
    print('Emprestimo APROVADO')
else:
    print('Emprestimo NEGADO')
