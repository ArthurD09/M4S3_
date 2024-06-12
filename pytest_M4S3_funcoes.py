'''                     01
def calcula_desconto(quantidade):
    if quantidade >= 10 and quantidade <= 99:
        return 0.95
    elif quantidade >= 100 and quantidade <= 999:
        return 0.90
    elif quantidade >= 1000:
        return 0.85
    else:
        return 1.0  

def calcula_valor_total(valor_unitario, desconto, quantidade):
    return valor_unitario * desconto * quantidade

def calcula_valor_sem_desconto(valor_unitario, quantidade):
    return valor_unitario * quantidade

if __name__ == '__main__':
    valor_unitario = float(input('Valor unitário do produto: '))
    quantidade = int(input('Quantidade: '))
    desconto = calcula_desconto(quantidade)
    valor_com_desconto = calcula_valor_total(valor_unitario, desconto, quantidade)
    valor_sem_desconto = calcula_valor_sem_desconto(valor_unitario, quantidade)

    print(f'Valor total sem desconto: {valor_sem_desconto:.2f} R$')
    print(f'Valor total com desconto: {valor_com_desconto:.2f} R$')
'''
'''                     02                  '''


    
