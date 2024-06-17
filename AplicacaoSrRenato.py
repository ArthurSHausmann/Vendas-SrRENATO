from database import db, Usuario, Objeto, Manutencao, FerramentasEmManutencao, Emprestimo
import inquirer

db.connect()
db.create_tables([Usuario, Objeto, Manutencao, FerramentasEmManutencao, Emprestimo])

usuario = 0
tipo = 0
objeto = 0
manutencao = 0


def main():
    Menu()


def Menu():
    print("===========================================================")
    print("|             Sistema de Gestão de ferramentas             |")
    print("|1 - Cadastros de pessoas                                  |")
    print("|2 - Cadastros de um objeto                                |")
    print("|3 - Cadastros de manutenção                               |")
    print("|4 - Realizar um empréstimo de Ferramentas                 |")
    print("===========================================================")
    x = int(input("Selecione o que deseja fazer:\n"))
    if x == 1:
        CadastroDePessoa()
    elif x == 2:
        CadastroObjeto()
    elif x == 3:
        CadastroManutencao()
    elif x == 4:
        EmprestimoDeFerramentas()

    else:
        print("Por favor selecione uma das opções")
        Menu()

# MENU NUMERO 1 DO MENU PRINCIPAL


def CadastroDePessoa():
    print("======================================================================")
    print("|            Voce selecionou o menu 'Cadastros de pessoas'            |")
    print("|1 - Adicionar um novo cadastro                                       |")
    print("|2 - Consultar um cadastro existente                                  |")
    print("|3 - Alterar um cadastro existente                                    |")
    print("|4 - Excluir um cadastro existente                                    |")
    print("|0 - Voltar ao menu anterior                                          |")
    print("======================================================================")
    x1 = int(input("Selecione o que deseja fazer:\n"))
    if x1 == 0:
        Menu()
    elif x1 == 1:
        NovoCadastroDePessoa()
    elif x1 == 2:
        ConsultarUmCadastroDePessoa()
    elif x1 == 3:
        AlterarUmCadastroDePessoa()
    elif x1 == 4:
        ExcluirUmCadastroDePessoa()
    else:
        print("Por favor selecione uma das opções")
        CadastroDePessoa()


def ExcluirUmCadastroDePessoa():
    usuario = Usuario.select()
    if usuario.count() == 0:
        print("Não há pessoas cadastradas")
        CadastroDePessoa()
    for u in usuario:
        print("-", u.id, "|NOME", u.nome, "|CPF:", u.cpf)
        print ("Digite 0 para voltar ao menu anteirior")
        x = input("Ou digite o ID do cliente que deseja alterar:\n")
        
        z = Usuario.get(Usuario.id == x)
        z.delete_instance()
        CadastroDePessoa()

def AlterarUmCadastroDePessoa():
    x = Usuario.select()

    if x .count() == 0:
        print("Não há pessoas cadastradas")
        CadastroDePessoa()
    else:
        pass
    for u in x:
        print("-", u.id, "|NOME", u.nome, "|CPF:", u.cpf)
        x = input("Selecione o ID do usuario que deseja alterar:\n")
        z = Usuario.get(Usuario.id == x)
        z.nome = input("Digite o novo nome do usuario:\n")
        z.email = input("Digite o novo e-mail do usuario:\n")
        z.cpf = int(input("Digite o novo CPF/CNPJ do usuario:\n"))
        z.save()
        print("Usuario alterado com sucesso!")
        CadastroDePessoa()

def ConsultarUmCadastroDePessoa():
    lista_usuario = Usuario.select()
    print("Listando usuarios:")
    for u in lista_usuario:
        print("-", u.id, u.nome)
    print("Para voltar ao menu anterior digite 0")
    Consulta = int(input("Ou digite o ID do usuario que deseja visualizar:\n"))
    if Consulta == 0:
        CadastroDePessoa()
    else:
        pass
    usuario1 = Usuario.get(Usuario.id == Consulta)
    print("NOME DO USUARIO:", usuario1.nome, "\nCPF/CNPJ DO USUARIO:",
          usuario1.cpf, "\nE-MAIL DO USUARIO:", usuario1.email)
    CadastroDePessoa()


def NovoCadastroDePessoa():
    global usuario
    usuario = Usuario.create(nome=input('Digite o nome do usuário a ser adicionado:\n').upper(),
                             email=input(
                                 'Digite o e-mail do usuário:\n').upper(),
                             cpf=int(input('Digite o CPF/CNPJ:\n')))
    print('O Usuário', usuario.nome, 'foi cadastrado!')
    CadastroDePessoa()

# NUMERO 2 DO MENU PRINCIPAL


def CadastroObjeto():
    print("======================================================================")
    print("|            Voce selecionou o menu 'Cadastro de um Objeto'           |")
    print("|1 - Adicionar um objeto                                              |")
    print("|2 - Consultar um objeto existente                                    |")
    print("|3 - Alterar um objeto existente                                      |")
    print("|4 - Excluir um objeto existente                                      |")
    print("|0 - Voltar ao menu anterior                                          |")
    print("======================================================================")
    x1 = int(input("Selecione o que deseja fazer:\n"))
    if x1 == 0:
        Menu()
    elif x1 == 1:
        NovoCadastroObj()
    elif x1 == 2:
        ConsultarUmCadastroObj()
    elif x1 == 3:
        AlterarUmCadastro()
    elif x1 == 4:
        ExcluirUmCadastro()
    else:
        print("Por favor selecione uma das opções")
        CadastroObjeto()


def ExcluirUmCadastro():
    usuario = Objeto.select()
    if usuario.count() == 0:
        print("Não há ferramentas cadastradas")
        CadastroObjeto()
    for u in usuario:
        print("-", u.id, "|NOME", u.NomeDaFerramenta, "|Estado da ferramenta:", u.estado_ferramentas)
        print('Digite 0 para voltar ao menu anterior')
        x = input("Ou selecione o ID da pessoa que deseja alterar: \n")
        if x == 0:
            CadastroObjeto()
        z = Objeto.get(Objeto.id == x)
        z.delete_instance()
        CadastroObjeto()
        
def AlterarUmCadastro():
    x = Objeto.select()
    if x.count() == 0:
        print("Não há ferramentas cadastradas")
        CadastroObjeto()
    else:
        pass
    for u in x:
        print("-", u.id, "|NOME", u.NomeDaFerramenta, "|Estado da ferramenta::", u.estado_ferramentas)
        x = input("Selecione o ID do usuario que deseja alterar:\n")
        z = Objeto.get(Objeto.id == x)
        z.NomeDaFerramenta = input("Digite o novo nome da ferramenta:\n")
        z.MarcaDaFerramenta = input("Digite a nova marca da ferramenta:\n")
        
        question = [inquirer.List("estado", message="Selecione o novo estado da ferramenta", choices=['Ótimo estado', 'Bom estado', 'Estado moderado', 'Péssimo estado', 'Necessita reparos'])]
        
        resposta = inquirer.prompt(question)
        z.estado_ferramentas = resposta['estado']
        z.save()
            
        print("Ferramenta alterada com sucesso!")
        CadastroObjeto()


def ConsultarUmCadastroObj():

    lista_ferramentas = Objeto.select()
    if lista_ferramentas.count() == 0:
        print("Não há ferramentas cadastradas")
        CadastroObjeto()
    else:
        print("Imprimindo lista de ferramentas: \n")
        for f in lista_ferramentas:
            print('-', f.id,"|Nome:", f.NomeDaFerramenta, "|Marca:", f.MarcaDaFerramenta, "|Condição:", f.estado_ferramentas)
        CadastroObjeto()


def NovoCadastroObj():
    resposta = 0
    question = [
        inquirer.List("Opção selecionada:",
                      message="Para começar, selecione o estado da ferramenta",
                      choices=['Ótimo estado', 'Bom estado', 'Estado moderado', 'Péssimo estado', 'Necessita reparos'])]
    resposta = inquirer.prompt(question)
    if resposta == {'Opção selecionada:': 'Ótimo estado'}:
        resposta = 'Ótimo estado'
    elif resposta == {'Opção selecionada:': 'Bom estado'}:
        resposta = 'Bom estado'
    elif resposta == {'Opção selecionada:': 'Estado moderado'}:
        resposta = 'Estado moderado'
    elif resposta == {'Opção selecionada:': 'Péssimo estado'}:
        resposta = 'Péssimo estado'
    elif resposta == {'Opção selecionada:': 'Necessita reparos'}:
        resposta = 'Necessita reparos'

    x = resposta

    ferramenta = Objeto.create(NomeDaFerramenta=input('Digite o nome da ferramenta a ser adicionado:\n').upper(),
                               MarcaDaFerramenta=input(
                                   'Digite a marca da ferramenta a ser adicionada:\n').upper(),
                               estado_ferramentas=x)
    if resposta == 'Necessita reparos':
        print("O objeto necessita ser reparado, iniciando cadastro de manutenção")
        NovoCadastroManutencao()
    if resposta != 'Necessita reparos':
        print('A ferramenta', ferramenta.NomeDaFerramenta,'foi cadastrada com sucesso e está disponivel para empréstimos!')
        CadastroObjeto()

# NUMERO 3 DO MENU PRINCIPAL


def CadastroManutencao():
    print("======================================================================")
    print("|           Voce selecionou o menu 'Cadastros de manutenção'          |")
    print("|1 - Adicionar uma manutenção                                         |")
    print("|2 - Consultar uma manutenção existente                               |")
    print("|3 - Excluir uma manutenção existente                                 |")
    print("|0 - Voltar ao menu anterior                                          |")
    print("======================================================================")
    x1 = int(input("Selecione o que deseja fazer:\n"))
    if x1 == 0:
        Menu()
    elif x1 == 1:
        NovoCadastroManutencao()
    elif x1 == 2:
        ConsultarUmCadastroManutencao()
    elif x1 == 3:
        ExcluirUmCadastro()
    else:
        print("Por favor selecione uma das opções")
        CadastroManutencao()


def ExcluirUmCadastroManutencao():
    usuario = Manutencao.select()
    if usuario.count() == 0:
        print("Não há manutenções cadastradas")
        CadastroManutencao()
    for u in usuario:
        print("-", u.id, "|Ferramenta", u.NomeDaFerramenta, "|Data de inicio:", u.dia_inicio,'/', u.mes_inicio,'/', u.ano_inicio)
        print ('Digite 0 para voltar ao menu anterior')
        x = input("Selecione o ID da manutenção que deseja excluir:\n")
        if x == 0:
            CadastroManutencao()
        z = Manutencao.get(Manutencao.id == x)
        z.delete_instance()
        CadastroManutencao()

def ConsultarUmCadastroManutencao():
    print("Ferramentas em manutenção:")
    ferramanut = FerramentasEmManutencao.select()
    
    if ferramanut.count() == 0:
        print("Não há ferramentas em manutenção")
    else:
        for f in ferramanut:
            print("|Nome:", f.NomeDaFerramenta, "\n|Marca:", f.MarcaDaFerramenta,
                  "\n|Começo da manutenção:", f.dia_inicio,'/',f.mes_inicio,'/',f.ano_inicio)
    
    CadastroManutencao()


def NovoCadastroManutencao():
    lista_obj = Objeto.select()
    if lista_obj.count() == 0:
        print("Não há ferramentas cadastradas")
        CadastroManutencao()
    else:
        for o in lista_obj:
            print('-', o.id, "|Nome:", o.NomeDaFerramenta, "|Marca",o.MarcaDaFerramenta, "|Condição:", o.estado_ferramentas)
    z = input("Digite o ID do objeto que deseja adicionar a lista de manutenção:\n")
    ferramenta = Objeto.get(Objeto.id == z)
    x = Manutencao.create(NomeDaFerramenta=ferramenta.NomeDaFerramenta,
                          dia_inicio=int(
                              input('Digite o dia de inicio da manutenção:\n')),
                          mes_inicio=int(
                              input('Digite o mês de inicio da manutenção:\n')),
                          ano_inicio=int(input('Digite o ano de inicio da manutenção:\n')))
    ferraest = Manutencao.get(
        Manutencao.NomeDaFerramenta == ferramenta.NomeDaFerramenta)

    print("A ferramenta", ferramenta.NomeDaFerramenta, "foi adicionada a lista de manutenção e removida da lista de ferramentas disponiveis \nO inicio da manutenção será na data:",
          ferraest.dia_inicio,"/",ferraest.mes_inicio,"/", ferraest.ano_inicio)
    print("A previsão de término de manutenção de uma ferramente é de 7 dias.")
    xy = FerramentasEmManutencao.create(NomeDaFerramenta=ferramenta.NomeDaFerramenta,
                                        MarcaDaFerramenta=ferramenta.MarcaDaFerramenta,
                                        estado_ferramentas=ferramenta.estado_ferramentas,
                                        dia_inicio=ferraest.dia_inicio,
                                        mes_inicio=ferraest.mes_inicio,
                                        ano_inicio=ferraest.ano_inicio)
    xz = Objeto.get(Objeto.id == ferramenta)
    xz.delete_instance()

    CadastroManutencao()

# NUMERO 4 DO MENU PRINCIPAL


def EmprestimoDeFerramentas():
    print("======================================================================")
    print("|   Voce selecionou o menu 'Realizar um empréstimo de Ferramentas'    |")
    print("|1 - Adicionar um Empréstimo                                          |")
    print("|2 - Consultar um Empréstimo existente                                |")
    print("|3 - Excluir um Empréstimo existente                                  |")
    print("|0 - Voltar ao menu anterior                                          |")
    print("======================================================================")
    x1 = int(input("Selecione o que deseja fazer:\n"))
    if x1 == 0:
        Menu()
    elif x1 == 1:
        AdicionarUmEmprestimo()
    elif x1 == 2:
        ConsultarUmEmprestimo()
    elif x1 == 3:
        ExcluirUmEmprestimo()
    else:
        print("Por favor selecione uma das opções")
        EmprestimoDeFerramentas()


def AdicionarUmEmprestimo():
    usuarios = Usuario.select()
    for u in usuarios:
        print('-', u.id, "|Nome:", u.Nome,
              "|CPF:", u.CPF, "|Email:", u.Email)
    x = input("Selecione o usuario que para fazer o empréstimo: \n")
    ferramentas = Objeto.select()
    for f in ferramentas:
        print('-', f.id, "|Nome:", f.NomeDaFerramenta,
              "|Marca:", f.MarcaDaFerramenta, "|Condição:", f.estado_ferramentas)
    z = input("Selecione o ID da ferramenta que deseja emprestar: \n")
    ferramenta = Objeto.get(Objeto.id == z)
    user = Usuario.get(Usuario.id == x)
    print( "A ferramenta",ferramenta.NomeDaFerramenta,"Será emprestada para o usuario", user.nome)
    question = inquirer.List("Opção selecionada:", message="Deseja continuar?", choices=['Sim','Voltar'])
    annswer = inquirer.prompt(question)
    
    if annswer == {'Opção selecionada:': 'Sim'}:
        Emprestimo.create(cliente = user.nome, ferramenta = ferramenta.NomeDaFerramenta)
        print ("Empréstimo concluido, por favor recadastre a ferramenta assim que ela for devolvida.")
        ferramenta.delete_instance()
    else:
        EmprestimoDeFerramentas()

def ConsultarUmEmprestimo():
    emprestimo = Emprestimo.select()
    if emprestimo.count() == 0:
        print("Não há ferramentas emprestadas")
    else:
        for e in emprestimo:
            print("|Cliente:", e.cliente, "\n|Ferramenta:", e.ferramenta)
    EmprestimoDeFerramentas()

def ExcluirUmEmprestimo():
    usuario = Emprestimo.select()
    if usuario.count() == 0:
        print("Não há emprestimos cadastrados no momento")
        EmprestimoDeFerramentas()
    for u in usuario:
        print("-", u.id, "|NOME", u.cliente, "|Ferramenta:", u.ferramenta)
        print('Digite 0 para voltar ao menu anterior')
        x = input("Selecione o ID do usuario que deseja excluir:\n")
        if x == 0:
            print('Não há emprestimos cadastrados no momento')
            EmprestimoDeFerramentas()
        z = Emprestimo.get(Emprestimo.id == x)
        z.delete_instance()
        EmprestimoDeFerramentas()

main()
