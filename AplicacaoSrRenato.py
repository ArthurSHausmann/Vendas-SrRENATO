from database import db, Usuario, Objeto, Manutencao, FerramentasEmManutencao
import inquirer

db.connect()
db.create_tables([Usuario, Objeto, Manutencao, FerramentasEmManutencao])

usuario = 0
tipo = 0
objeto = 0
manutencao = 0


def main():
    Menu()


def Menu():
    print ("===========================================")
    print ("|1 - Cadastros de pessoas                  |")
    print ("|2 - Cadastros de um objeto                |")
    print ("|3 - Cadastros de manutenção               |")
    print ("|4 - Realizar um empréstimo de Ferramentas |")
    print ("===========================================")
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
        print ("Por favor selecione uma das opções")
        Menu()

#MENU NUMERO 1 DO MENU PRINCIPAL
def CadastroDePessoa(): 
    print ("======================================================================")
    print ("|Voce selecionou o menu 'Cadastros de pessoa'                         |")
    print ("|1 - Adicionar um novo cadastro                                       |")
    print ("|2 - Consultar um cadastro existente                                  |")
    print ("|3 - Alterar um cadastro existente (TEMPORARIAMENTE INATIVO)          |")
    print ("|4 - Excluir um cadastro existente (TEMPORARIAMENTE INATIVO)          |")
    print ("|0 -  Voltar ao menu anterior                                         |")
    print ("======================================================================")
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
        print ("Por favor selecione uma das opções")
        CadastroDePessoa()

def ExcluirUmCadastroDePessoa():
    print ("Essa Opção estará disponivel em breve")

def AlterarUmCadastroDePessoa():
    print ("Essa Opção estará disponivel em breve")

def ConsultarUmCadastroDePessoa():
    lista_usuario = Usuario.select()
    print("Listando usuarios:")
    for u in lista_usuario:
        print ("-", u.id, u.nome)
    print("Para voltar ao menu anterior digite 0")
    Consulta = int(input("Ou digite o ID do usuario que deseja visualizar:\n"))
    if Consulta == 0:
        CadastroDePessoa()
    else:
        pass
    usuario1 = Usuario.get(Usuario.id == Consulta)
    print ("NOME DO USUARIO:",usuario1.nome,"\nCPF/CNPJ DO USUARIO:", usuario1.cpf, "\nE-MAIL DO USUARIO:", usuario1.email)
    CadastroDePessoa()

def NovoCadastroDePessoa():
    global usuario
    usuario = Usuario.create(nome=input('Digite o nome do usuário a ser adicionado:\n').upper(), 
                             email=input('Digite o e-mail do usuário:\n').upper(),
                             cpf = int(input('Digite o CPF/CNPJ:\n')))
    print('O Usuário', usuario.nome, 'foi cadastrado!')
    CadastroDePessoa()

#NUMERO 2 DO MENU PRINCIPAL
def CadastroObjeto():
    print ("======================================================================")
    print ("|Voce selecionou o menu 'Cadastros de um Objeto'                      |")              
    print ("|1 - Adicionar um objeto                                              |")
    print ("|2 - Consultar um objeto existente                                    |")
    print ("|3 - Alterar um objeto existente (TEMPORARIAMENTE INATIVO)            |")
    print ("|4 - Excluir um objeto existente (TEMPORARIAMENTE INATIVO)            |")
    print ("|0 -  Voltar ao menu anterior                                         |")
    print ("======================================================================")
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
        print ("Por favor selecione uma das opções")
        CadastroObjeto()

def ExcluirUmCadastro():
    print ("Essa Opção estará disponivel em breve")

    
def AlterarUmCadastro():
    print ("Essa Opção estará disponivel em breve")

    
def ConsultarUmCadastroObj():
    lista_ferramentas = Objeto.select()
    print("Imprimindo lista de ferramentas")
    for f in lista_ferramentas:
        print ('-',f.id, f.NomeDaFerramenta,"Marca:",f.MarcaDaFerra,"Condição:",f.estado_ferramenta)
    CadastroObjeto()


def NovoCadastroObj():
    resposta = 0
    question = [
        inquirer.List("Opção selecionada:",
                    message="Para começar, selecione o estado da ferramenta",
                    choices=['Ótimo estado','Bom estado','Estado moderado','Péssimo estado','Necessita reparos'])]
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
                             MarcaDaFerramenta=input('Digite a marca da ferramenta a ser adicionada:\n').upper(),
                             estado_ferramentas=x)
    if resposta == 'Necessita reparos':
        print ("O objeto necessita ser reparado, iniciando cadastro de manutenção")
        NovoCadastroManutencao()
    if resposta != 'Necessita reparos':       
        print('A ferramenta', ferramenta.NomeDaFerramenta, 'foi cadastrada com sucesso e está disponivel para empréstimos!')
        CadastroObjeto()

#NUMERO 3 DO MENU PRINCIPAL
def CadastroManutencao():
    print ("======================================================================")
    print ("|Voce selecionou o menu 'Cadastros de manutenção'                     |")
    print ("|1 - Adicionar uma manutenção (TEMPORARIAMENTE INATIVO)               |")
    print ("|2 - Consultar uma manutenção existente (TEMPORARIAMENTE INATIVO)     |")
    print ("|3 - Alterar uma manutenção existente (TEMPORARIAMENTE INATIVO)       |")
    print ("|4 - Excluir uma manutenção existente (TEMPORARIAMENTE INATIVO)       |")
    print ("|0 -  Voltar ao menu anterior                                         |")
    print ("======================================================================")
    x1 = int(input("Selecione o que deseja fazer:\n"))
    if x1 == 0:
        Menu()
    elif x1 == 1:
        NovoCadastroManutencao()
    elif x1 == 2:
        ConsultarUmCadastroManutencao()
    elif x1 == 3:
        AlterarUmCadastro()
    elif x1 == 4:
        ExcluirUmCadastro()
    else:
        print ("Por favor selecione uma das opções")
        CadastroManutencao()

def ExcluirUmCadastroManutencao():
    print ("Essa Opção estará disponivel em breve")

    
def AlterarUmCadastroManutencao():
    print ("Essa Opção estará disponivel em breve")

    
def ConsultarUmCadastroManutencao():
    print ("Essa Opção estará disponivel em breve")


def NovoCadastroManutencao():
    lista_obj = Objeto.select()
    for o in lista_obj:
        print ('-', o.id,"|Nome:",o.NomeDaFerramenta,"|Marca",o.MarcaDaFerramenta,"|Condição:",o.estado_ferramentas)
    z = input("Digite o ID do objeto que deseja adicionar a lista de manutenção:\n")
    ferramenta = Objeto.get(Objeto.id == z)
    x = Manutencao.create(ferramenta_estragada=ferramenta,
                        dia_inicio=int(input('Digite o dia de inicio da manutenção:\n')),
                        mes_inicio=int(input('Digite o mês de inicio da manutenção:\n')),
                        ano_inicio=int(input('Digite o ano de inicio da manutenção:\n')))
    datainicio = Manutencao.dia_inicio,"/",Manutencao.mes_inicio,"/",Manutencao.ano_inicio
    print ("A ferramenta",ferramenta.NomeDaFerramenta,"foi adicionada a lista de manutenção e removida da lista de ferramentas disponiveis \nO inicio da manutenção será na data:",datainicio)
    print("A previsão de término de manutenção de uma ferramente é de 7 dias.")
    xy = FerramentasEmManutencao.create(NomeDaFerramenta = ferramenta.NomeDaFerramenta, MarcaDaFerramenta= ferramenta.MarcaDaFerramenta, estado_ferramentas= ferramenta.estado_ferramentas)
    xz = Objeto.remove(ferramenta.NomeDaFerramenta, ferramenta.MarcaDaFerramenta, ferramenta.estado_ferramenta)
    CadastroManutencao()

#NUMERO 4 DO MENU PRINCIPAL
def EmprestimoDeFerramentas(): 
    print ("======================================================================")
    print ("|Voce selecionou o menu 'Realizar um empréstimo de Ferramentas'       |")
    print ("|1 - Adicionar um Empréstimo (TEMPORARIAMENTE INATIVO)                |")
    print ("|2 - Consultar um Empréstimo existente (TEMPORARIAMENTE INATIVO)      |")
    print ("|3 - Alterar um Empréstimo existente (TEMPORARIAMENTE INATIVO)        |")
    print ("|4 - Excluir um Empréstimo existente (TEMPORARIAMENTE INATIVO)        |")
    print ("|0 -  Voltar ao menu anterior                                         |")
    print ("======================================================================")
    x1 = int(input("Selecione o que deseja fazer:\n"))
    if x1 == 0:
        Menu()
    elif x1 == 1:
        AdicionarUmEmprestimo()
    elif x1 == 2:
        ConsultarUmEmprestimo()
    elif x1 == 3:
        AlterarUmEmprestimo()
    elif x1 == 4:
        ExcluirUmEmprestimo()
    else:
        print ("Por favor selecione uma das opções")
        EmprestimoDeFerramentas()

def AdicionarUmEmprestimo():
    print ("Essa Opção estará disponivel em breve")

    
def ConsultarUmEmprestimo():
    print ("Essa Opção estará disponivel em breve")

    
def AlterarUmEmprestimo():
    print ("Essa Opção estará disponivel em breve")


def ExcluirUmEmprestimo():
    print ("Essa Opção estará disponivel em breve")





main()
