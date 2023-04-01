# Segunda fase do Sistema de Ouvidoria, integrando Phyton e MySQL
# Grupo composto por : Hugo Bezerra, Micael Lima, Wendel Gomes, Kleidson Almeda, Diego Silva e Nicollas Samuel



from operacoesbd import *


conexaoComBanco = abrirBancoDados("localhost","root","hugobezerra2005","sistemadeouvidoria")


print('Seja bem-vindo(a) ao Sistema de Ouvidoria. Segue abaixo suas opções : ')



sql = "SELECT * FROM sistema;"
listagemDoBanco = listarBancoDados(conexaoComBanco,sql)


opcao = 0
while opcao != 5 :

    print() #Espaço
    menu = ("1) Listar as reclamações","2) Adicionar nova reclamação","3) Remover uma reclamação","4) Pesquisar uma reclamação por código","5) Sair ")
    for item in menu :
        print(item)

    opcao = int(input('Digite aqui sua opção : '))


    if opcao == 1 :

        if len(listagemDoBanco) == 0 :
            print() #Espaço
            print('Nenhuma reclamação cadastrada no sistema')

        else :
            print() #Espaço
            print('As reclamações cadastradas no sistema são : ')
            for reclamacoes in listagemDoBanco :
                print(reclamacoes[0],')',reclamacoes[1])


    elif opcao == 2 :

        print() #Espaço
        novaReclamacao = input('Digite aqui sua reclamação : ')
        sql = "insert into sistema (Reclamação) values (%s);"
        dados = (novaReclamacao,)

        novaReclamacaoNoBanco = insertNoBancoDados(conexaoComBanco,sql,dados)
        print() #Espaço
        print('Reclamação inserida com suscesso. O código da nova reclamação é ',novaReclamacaoNoBanco)


    elif opcao == 3 :

        if len(listagemDoBanco) == 0 :
            print() #Espaço
            print('Nenhuma reclamação cadastrada no sistema')

        else :

            print() #Espaço
            print('As reclamações cadastradas no sistema são : ')
            for reclamacoes in listagemDoBanco :
                print(reclamacoes[0],')',reclamacoes[1])


            print() #Espaço
            codigoRemocao = int(input('Digite o código da reclamação ao qual você deseja remover : '))
            sql = "DELETE FROM sistema WHERE Código = (%s);"
            dados = (codigoRemocao,)

            linhasAfetadas = excluirBancoDados(conexaoComBanco,sql,dados)

            if linhasAfetadas == 1 :
                print() #Espaço
                print('Reclamação removida com suscesso.')
            else :
                print() #Espaço
                print('Código inválido')


    elif opcao == 4 :

        if len(listagemDoBanco) == 0 :
            print() #Espaço
            print('Nenhuma reclamação cadastrada no sistema')


        else :
            print() #Espaço
            codigoPesquisa = int(input('Digite o código da reclamação que você deseja pesquisar : '))
            sql = "SELECT * FROM sistema WHERE Código = " + str(codigoPesquisa)

            codigoPesquisado = listarBancoDados(conexaoComBanco,sql)

            if len(codigoPesquisado) == 1 :
                print() #Espaço
                print('O código pesquisado foi : ')
                for item in codigoPesquisado :
                    print(item[0],')',item[1])

            else :
                print() #Espaço
                print('Código inválido')



    elif opcao != 5 :
        print() #Espaço
        print('Opção inválida, tente novamente por favor')

print('Obrigado por usar o sistema de ouvidoria.')

encerrarBancoDados(conexaoComBanco)


'''
    observações :
    - Nome do Schema : "sistemadeouvidoria"
    - Nome da tabela : "sistema"
    - Colunas da tabela : "Código" e "Reclamação"    


    Create table sistema (
        Código int auto_increment,
        Reclamação varchar(300),
        primary key (Código)
    );    
'''
