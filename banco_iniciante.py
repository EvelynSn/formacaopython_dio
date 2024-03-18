def cadastrar_usuario():
    nome = input('Digite seu nome: ')
    cpf = input('Digite seu CPF: ')
    return nome, cpf


def cadastrar_conta_bancaria():
    agencia = input('Digite o número da agência: ')
    conta = input('Digite o número da conta: ')
    return agencia, conta


def deposito(saldo_atual, depositos):
    valor_adicional = float(input('Digite o valor que você deseja depositar: '))
    print(f'O valor informado foi R${valor_adicional:.2f}')
    prosseguir = input('Deseja prosseguir? [1] SIM  [2] Não \n')
    if prosseguir == '1':
        depositos.append(valor_adicional)
        saldo_atual += valor_adicional
        print(f'O valor de R${valor_adicional:.2f} foi adicionado à sua conta!\n')
        print(f'Seu saldo atual é de R${saldo_atual:.2f}')
    else:
        print('Operação Interrompida!\n')
    return saldo_atual, depositos


def saque(saldo_atual, contador_saques, saques):
    valor_sacado = float(input('Digite o valor que você deseja sacar: '))
    if 0 < valor_sacado <= 500:
        if valor_sacado <= saldo_atual and contador_saques < 3:
            saques.append(valor_sacado)
            saldo_atual -= valor_sacado
            contador_saques += 1
            print(f'Saque de R${valor_sacado:.2f} realizado com sucesso. Novo saldo: R${saldo_atual:.2f}')
        elif contador_saques >= 3:
            print('Não é possível realizar a operação! Saques diários máximos atingidos.')
        else:
            print('Saldo insuficiente. Saque não realizado.')
    else:
        print('Digite um valor válido (maior que zero e menor ou igual a R$ 500,00).')
    return saldo_atual, contador_saques, saques


def extrato(saldo_atual, depositos, saques):
    extrato = f''' 
    Seu extrato está disponível:
    Saldo atual:
    R${saldo_atual:.2f} \n
    Depósitos realizados:
    {', '.join(map(lambda x: f'R${x:.2f}', depositos))} \n
    Saques realizados: 
    {', '.join(map(lambda x: f'R${x:.2f}', saques))}
    '''
    print(extrato.strip())


# Menu principal
menu = '''
#################
BANCO DO NORDESTE
#################
-----------------
[1] DEPÓSITO
[2] SAQUE
[3] EXTRATO
[4] SAIR
-----------------
'''

# Variáveis iniciais
saldo = 0
extrato_cliente = ""
contador_saques_diarios = 0
depositos_realizados = []
saques_realizados = []

# Cadastro de usuário e conta bancária
nome_cliente, cpf_cliente = cadastrar_usuario()
agencia_cliente, conta_cliente = cadastrar_conta_bancaria()

print(f'Bem-vindo(a), {nome_cliente}!')
print(f'Conta bancária cadastrada - Agência: {agencia_cliente}, Conta: {conta_cliente}')

# Loop principal
while True:
    opcao = input(menu)

    if opcao == '1':
        saldo, depositos_realizados = deposito(saldo, depositos_realizados)

    elif opcao == '2':
        saldo, contador_saques_diarios, saques_realizados = saque(saldo, contador_saques_diarios, saques_realizados)

    elif opcao == '3':
        extrato(saldo, depositos_realizados, saques_realizados)

    elif opcao == '4':
        break

    else:
        print('Operação inválida! Selecione novamente uma das operações válidas.')

