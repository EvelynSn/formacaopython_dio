def cadastrar_usuario():
    nome = input('Digite seu nome: ')
    data_nascimento = input('Digite sua data de nascimento (DD/MM/AAAA): ')
    cpf = input('Digite seu CPF (somente números): ')
    endereco = input('Digite seu endereço (logradouro, número, bairro, cidade, estado): ')
    return {'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco}


def cadastrar_conta_bancaria(agencia, numero_conta, usuario):
    return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}


def deposito(saldo_atual, depositos_realizados):
    valor_adicional = float(input('Digite o valor que você deseja depositar: '))
    print(f'O valor informado foi R${valor_adicional:.2f}')
    prosseguir = input('Deseja prosseguir? [1] SIM  [2] Não \n')
    if prosseguir == '1':
        depositos_realizados.append(valor_adicional)
        saldo_atual += valor_adicional
        print(f'O valor de R${valor_adicional:.2f} foi adicionado à sua conta!\n')
        print(f'Seu saldo atual é de R${saldo_atual:.2f}')
    else:
        print('Operação Interrompida!\n')
    return saldo_atual, depositos_realizados


def saque(saldo_atual, contador_saques_diarios, saques_realizados):
    valor_sacado = float(input('Digite o valor que você deseja sacar: '))
    if 0 < valor_sacado <= 500:
        if valor_sacado <= saldo_atual and contador_saques_diarios < 3:
            saques_realizados.append(valor_sacado)
            saldo_atual -= valor_sacado
            contador_saques_diarios += 1
            print(f'Saque de R${valor_sacado:.2f} realizado com sucesso. Novo saldo: R${saldo_atual:.2f}')
        elif contador_saques_diarios >= 3:
            print('Não é possível realizar a operação! Saques diários máximos atingidos.')
        else:
            print('Saldo insuficiente. Saque não realizado.')
    else:
        print('Digite um valor válido (maior que zero e menor ou igual a R$ 500,00).')
    return saldo_atual, contador_saques_diarios, saques_realizados


def extrato(saldo_atual, depositos_realizados=[], saques_realizados=[], usuario={}):
    extrato = f''' 
    Seu extrato está disponível:
    Nome: {usuario.get('nome', 'Não informado')}
    CPF: {usuario.get('cpf', 'Não informado')}
    Saldo atual: R${saldo_atual:.2f} \n
    Depósitos realizados: {', '.join(map(lambda x: f'R${x:.2f}', depositos_realizados))} \n
    Saques realizados: {', '.join(map(lambda x: f'R${x:.2f}', saques_realizados))}
    '''
    print(extrato.strip())


# Variáveis iniciais
saldo = 0
depositos_realizados = []
saques_realizados = []
contador_saques_diarios = 0
usuarios_cadastrados = []
contas_corrente = []
numero_conta = 1

# Cadastro de usuário
def criar_usuario():
    cpf = input('Digite seu CPF (somente números): ')
    for usuario in usuarios_cadastrados:
        if usuario['cpf'] == cpf:
            print('Usuário já cadastrado com este CPF!')
            return
    novo_usuario = cadastrar_usuario()
    novo_usuario['cpf'] = cpf
    usuarios_cadastrados.append(novo_usuario)
    print('Usuário cadastrado com sucesso!')


# Cadastro de conta corrente
def criar_conta_corrente():
    global numero_conta
    cpf = input('Digite o CPF do usuário (somente números): ')
    for usuario in usuarios_cadastrados:
        if usuario['cpf'] == cpf:
            nova_conta = cadastrar_conta_bancaria('0001', numero_conta, usuario)
            contas_corrente.append(nova_conta)
            numero_conta += 1
            print('Conta corrente criada com sucesso!')
            return
    print('CPF não encontrado. Cadastre o usuário primeiro.')


# Menu principal
menu = '''
#################
BANCO DO NORDESTE
#################
-----------------
[1] CRIAR USUÁRIO
[2] CRIAR CONTA CORRENTE
[3] DEPÓSITO
[4] SAQUE
[5] EXTRATO
[6] SAIR
-----------------
'''

# Loop principal
while True:
    opcao = input(menu)

    if opcao == '1':
        criar_usuario()

    elif opcao == '2':
        criar_conta_corrente()

    elif opcao == '3':
        saldo, depositos_realizados = deposito(saldo, depositos_realizados)

    elif opcao == '4':
        saldo, contador_saques_diarios, saques_realizados = saque(saldo, contador_saques_diarios, saques_realizados)

    elif opcao == '5':
        cpf = input('Digite o CPF do usuário para consultar o extrato (somente números): ')
        usuario = next((u for u in usuarios_cadastrados if u['cpf'] == cpf), {})
        if usuario:
            extrato(saldo, depositos_realizados, saques_realizados, usuario)
        else:
            print('Usuário não encontrado.')

    elif opcao == '6':
        break

    else:
        print('Operação inválida! Selecione novamente uma das operações válidas.')
