salario = float(input('Digite o seu salário mensal: '));
comissao = float(input('Digite qual o ganho de comissão por carro vendido: '));
vendas = int(input('Digite quantos carros você vendeu esse mês: '));
vendas_totais = float(input('Digite o valor total de vendas este mês: '));

comissao_total = comissao * vendas;
segunda_comissao = vendas_totais * (5 / 100);
salario_final = salario + comissao_total + segunda_comissao;

print(f'Se seu salário fixo é de {salario} reais, recebe {comissao} por carro vendido, e vendeu {vendas} neste mês, então seu salário final é de {salario_final}.');