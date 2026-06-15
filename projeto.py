import os         
            #########################################################
            ############# CADERNO VIRTUAL DE RECEITAS ###############
            #########################################################

receitas = { 
    'Receita 1' : ['Bolo de chocolate', 'Farinha, açúcar, ovos, chocolate em pó, manteiga', 'Sobremesa', '1 hora', 'Bater os ingredientes, assar no forno']

}

ingredientes = {
    'Ingrediente 1': ['Farinha de trigo', 'Finna', 'Utilize para bolos e pães']
}

categoria = {
    'Sobremesa': 'Sobremesa'
}   

dicas = {
    'Dica 1': ['Se o bolo que deu tanto trabalho queimou, não se desespere: passe um ralador de queijo côncavo na parte queimada até retirar a crosta.']
}

resp = ''
while resp != '0':
    os.system('cls')
    print("#########################################################")
    print("#######  CADERNO VIRTUAL DE RECEITAS CULINARIAS   #######")  
    print("#########################################################")
    print("#######           1 - Receitas                    #######")
    print("#######           2 - Ingredientes                #######")
    print("#######           3 - Categoria                   #######")
    print("#######           4 - Dicas Culinárias            #######")
    print("#######           5 - Informações                 #######")
    print("#######           0 - Sair                        #######")
    print("#########################################################")
    resp = input("Escolha sua opção: ")

    if resp == "1":
        os.system('cls')
        print()
        print("######################################################## ")
        print("#######             Receita                      ####### ")
        print("######################################################## ")
        print("####### 1- Nova Receita                          ####### ")
        print("####### 2- Ver Receita                           ####### ")
        print("####### 3- Editar Receita                        ####### ")
        print("####### 4- Apagar Receita                        ####### ")
        print("####### 0- Voltar                                ####### ")
        print("######################################################## ")
        resp_r = input("EScolha sua opção: ")
        print()
        if resp_r == '1': 
            os.system('cls')
            print()
            print("############################################")
            print("#####           Nova Receita            ####")
            print("############################################")
            print()
            rec = input("## Nome da receita: ")
            print()
            ing = input("## Ingredientes: ")
            print()
            cat = input("## Digite a categoria da receita: ")
            print()
            tempo = input("## Digite o tempo da receita: ")
            print()
            modo_p = input("## Modo de preparo: ")
            print()
            receitas[rec] = [rec, ing, cat, tempo, modo_p]
            print("## Receita cadastrada! ")
            print()
            print("## Receita: ", receitas[rec])

            with open('receitas.txt', 'a') as arquivo:
                    arquivo.write(rec + '\n')
                    arquivo.write(ing + '\n')
                    arquivo.write(cat + '\n')
                    arquivo.write(tempo + '\n')
                    arquivo.write(modo_p + '\n')


        elif resp_r == '2':
            os.system('cls')
            print()
            print("############################################")
            print("#####           Ver receita             ####")
            print("############################################")
            print()
            tam = len(receitas)
            print("## Receitas cadastradas: ", tam)
            for receita in receitas:
                print("## ", receita)
                print()
            rec = input("## Digite o nome da receita: ")
            print()
            if rec in receitas:
                print("## Nome: ", receitas[rec][0])
                print("## Ingredientes: ", receitas[rec][1])
                print("## Categoria: ", receitas[rec][2])
                print("## Tempo: ", receitas[rec][3])
                print("## Modo de preparo: ", receitas[rec][4])
            else:
                print("## Nenhuma receita cadastrada! ")
            print()


        elif resp_r == '3':
            os.system('cls')
            print()
            print("############################################")
            print("#####           Editar Receita          ####")
            print("############################################")
            print()
            rec = input("## Nome da receita: ")
            print()
            if rec in receitas:
                print("## Receita atual: ")
                print("## Nome: ", receitas[rec][0])
                print("## Ingredientes: ", receitas[rec][1])
                print("## Categoria: ", receitas[rec][2])
                print("## Tempo: ", receitas[rec][3])
                print("## Modo de preparo: ", receitas[rec][4])
                print()
                print("## Digite os novos dados da receita: ")
                nome = input("## Nome da receita: ")
                ing = input("## Ingredientes: ")
                cat = input("## Digite a categoria da receita: ")
                tempo = input("## Digite o tempo da receita: ")
                modo_p = input("## Modo de preparo: ")
                receitas[rec] = [rec, ing, cat, tempo, modo_p]
                print()
                print("#### Receita Editada! ")
                print()
                print("## Receita atualizada: ", receitas[rec])

        elif resp_r == '4':
            os.system('cls')
            print()
            print("############################################")
            print("#####           Exluir Receita          ####")
            print("############################################")
            print()
            rec = input("## Nome da receita: ")
            print()
            if rec in receitas:
                print("## Nome: ", receitas[rec][0])
                print("## Ingredientes: ", receitas[rec][1])
                print("## Categoria: ", receitas[rec][2])
                print("## Tempo: ", receitas[rec][3])
                print("## Modo de preparo: ", receitas[rec][4])
                print()
                confirma = input("## Tem certeza que deseja excluir essa receita? (s/n): ")
                if confirma.lower() == 's':
                    del receitas[rec]
                    print("## Receita Excluida! ")
                    print()
                    print("## Receita: ", receitas)
                else:
                    print("## Exclusão cancelada! ") 
            else:
                print("## Nenhuma receita cadastrada! ")

    
        print()
        input("Tecle <ENTER> para continuar...")  

    elif resp == '2':
        print()
        print("######################################################## ")
        print("#######            Ingredientes                  ####### ")
        print("######################################################## ")
        print("####### 1- Adicionar Ingrediente                 ####### ")
        print("####### 2- Ver Ingrediente                       ####### ")
        print("####### 3- Editar Ingrediente                    ####### ")
        print("####### 4- Apagar Ingrediente                    ####### ")
        print("####### 0- Voltar                                ####### ")
        print("######################################################## ")
        resp_i = input("Escolha sua resposta: ")

        if resp_i == '1':
            os.system('cls')
            print()
            print("############################################")
            print("#####      Adicionando Ingrediente      ####")
            print("############################################")
            print()
            ing= input("## Nome do Ingrediente: ")
            print()
            marca_i = input("## Marca do ingrediente: ")
            print()
            obs_i = input("## Deixe uma observação sobre o ingrediente: ")
            print()
            ingredientes[ing] = [ing, marca_i, obs_i]
            print("## Ingrediente cadastrado! ")
            print()
            print("## Ingrediente: ", ingredientes[ing])

            with open('ingredientes.txt', 'a') as arquivo:
                    arquivo.write(ing + '\n')
                    arquivo.write(marca_i + '\n')
                    arquivo.write(obs_i + '\n')

        elif resp_i == '2':
            os.system('cls')
            print()
            print("############################################")
            print("#####         Ver Ingrediente           ####")
            print("############################################")
            print()
            tam = len(ingredientes)
            print("## Ingredientes cadastrados: ", tam)
            for ingrediente in ingredientes:
                print("## ", ingrediente)
                print()
            ing = input("## Nome do Ingrediente: ")
            print()
            if ing in ingredientes:
                print("## Nome:", ingredientes[ing][0])
                print("## Marca:", ingredientes[ing][1])
                print("## Observação:", ingredientes[ing][2])
            else:
                print("## Nenhum ingrediente cadastrado! ")
            
        elif resp_i == '3':
            os.system('cls')
            print()
            print("############################################")
            print("#####         Editar Ingrediente        ####")
            print("############################################")
            print() 
            ing = input("## Digite o nome do ingrediente: ")
            print()
            if ing in ingredientes:
                print("## Ingrediente atual: ")
                print("## Nome:", ingredientes[ing][0])
                print("## Marca:", ingredientes[ing][1])
                print("## Observação:", ingredientes[ing][2])
                print()
                print("## Digite os novos dados do ingrediente: ")
                print()
                ing = input("## Nome do Ingrediente: ")
                marca_i = input("## Marca do ingrediente: ")
                obs_i = input("## Deixe uma observação sobre o ingrediente: ")
                ingredientes[ing] = [ing, marca_i, obs_i]
                print()
                print("## Ingrediente atualizado! ", ingredientes[ing])
                print()
                print("#### Ediçao feita! #### ")
                print()

        elif resp_i == '4':
            os.system('cls')
            print()
            print("############################################")
            print("#####         Excluir Ingrediente       ####")
            print("############################################")
            print() 
            ing = input("## Digite o nome do ingrediente: ")
            print()
            if ing in ingredientes:
                print("## Nome:", ingredientes[ing][0])
                print("## Marca:", ingredientes[ing][1])
                print("## Observação:", ingredientes[ing][2])
                print()
                confirma = input("## Tem certeza que deseja excluir esse ingrediente? (s/n): ")
                if confirma.lower() == 's':
                    del ingredientes[ing]
                    print("## Ingrediente Excluido! ")
                    print()
                    print("## Ingredientes: ", ingredientes)
                else:
                    print("## Exclusão cancelada! ")
            else:
                print("## Nenhum ingrediente cadastrado! ")
        
        print()
        input("Tecle <ENTER> para continuar...")

    elif resp == '3': 
        print()
        print("########################################################")
        print("#######        Categoria de ingredientes         #######")
        print("########################################################")
        print("####### 1- Adicionar Categoria                   #######")
        print("####### 2- Ver Categoria                         #######")
        print("####### 3- Editar Categoria                      #######")
        print("####### 4- Apagar Categoria                      #######")
        print("####### 0- Voltar                                #######")
        print("########################################################")
        print()
        resp_c = input("Escolha sua opção: ")
       
        if resp_c == '1':
            os.system('cls')
            print()
            print("############################################")
            print("#####     Adicionando Categoria         ####")
            print("############################################")
            print()
            cat = input("## Digite o nome da categoria: ")
            categoria[cat] = [cat]
            print()

            with open('cateegorias.txt', 'a') as arquivo:
                    arquivo.write(cat + '\n')
                    
        
        elif resp_c == '2': 
            os.system('cls')
            print()
            print("############################################")
            print("#####           Ver Categoria           ####")
            print("############################################")
            print()
            tam = len(categoria)
            print("## Categorias cadastradas: ", tam)
            for categoria in categoria:
                print("## ", categoria)
                print()

        elif resp_c == '3':
            os.system('cls')
            print()
            print("############################################")
            print("#####       Editando  Categoria         ####")
            print("############################################")
            print()
            cat = input("## Digite a categoria atual: ")
            print()
            if cat in categoria:
                print("## Categoria atual: ", categoria[cat])
                print()
                print("## Digite a nova categoria: ")
                print()
                cat = input("## Digite o nome da categoria: ")
                categoria[cat] = [cat]
                print()
                print("#### Categoria Editada! ", categoria[cat])
                print()
            else:
                print("## Nenhuma categoria cadastrada! ")
                print()

        elif resp_c == '4':
            os.system('cls')
            print()
            print("############################################")
            print("#####        Exluir  Categoria          ####")
            print("############################################")
            print()
            cat = input("## Digite a categoria: ")
            print()
            if cat in categoria:
                print("## Categoria: ", categoria[cat])
                print()
                confirma = input("## Tem certeza que deseja excluir essa categoria? (s/n): ")
                if confirma.lower() == 's':
                    del categoria[cat]
                    print("## Categoria Excluida! ")
                    print()
                    print("## Categoria: ", categoria)
                else:
                    print("## Exclusão cancelada! ")
            else:
                print("## Nenhuma categoria cadastrada! ")
                print()

        print()
        input("Tecle <ENTER> para continuar...")

    elif resp== '4':
        print("########################################################")
        print("#######            Dicas Culinárias              ####### ")
        print("######################################################## ")
        print("####### 1- Adicionar Dica Culinária              ####### ")
        print("####### 2- Ver Dicas Culinária                   ####### ")
        print("####### 3- Editar Dica Culinária                 ####### ")
        print("####### 4- Apagar Dica Culinária                 ####### ")
        print("####### 0- Voltar                                ####### ")
        print("########################################################")
        print()
        resp_d = input("Escolha sua opçao: ")
        print()
        if resp_d == '1':
            os.system('cls')
            print()
            print("############################################")
            print("#####         Adicionando Dica          ####")
            print("############################################")
            print()
            dica = input("## Digite sua Dica: ")
            print()
            print("Você adicionou uma dica! ")
            dicas[dica] = [dica]
            print()
            print("## Dica: ", dicas)

            with open('dicas.txt', 'a') as arquivo:
                    arquivo.write(dica + '\n')

        elif resp_d == '2':
            os.system('cls')
            print()
            print("############################################")
            print("#####         Dica Culinária            ####")
            print("############################################")
            print()
            tam = len(dicas)
            print("## Dicas cadastradas: ", tam)
            for dica in dicas:
                print("## ", dica)
                print()
            dica = input("## Digite a dica: ")
            print() 
            if dica in dicas:
                print("## Dica: ", dicas[dica][0])
                print()
            else:
                print("## Nenhuma dica cadastrada! ")
                print()

        elif resp_d == '3':
            os.system('cls')
            print()
            print("############################################")
            print("#####         Editando Dica             ####")
            print("############################################")
            print()
            dica = input("## Digite sua dica: ")
            print()
            if dica in dicas:
                print("## Dica cadastrada:" )
                print("## Dica: ", dicas)
                print()
                nova_dica = input("## Digite a nova Dica: ")
                dicas[dica] = [nova_dica]
                print()
                print("#### Dica Editada! ", dicas)
                print()
            else:
                print("## Nenhuma dica cadastrada! ")
                print()
                
        elif resp_d == '4': 
            os.system('cls')
            print()
            print("############################################")
            print("#####         Excluindo  Dica           ####")
            print("############################################")
            print()
            dica = input("## Digite o nome da dica: ")
            print()
            if dica in dicas:
                print("## Dica: ", dicas[dica])
                print()
                confirma = input("## Tem certeza que deseja excluir essa dica? (s/n): ")
                if confirma.lower() == 's':
                    del dicas[dica]
                    print("## Dica Excluida! ")
                    print()
                    print("## Dicas: ", dicas)
                else:
                    print("## Exclusão cancelada! ")
            else:
                print("## Nenhuma dica cadastrada! ")
                print()

        print()
        input("Tecle <ENTER> para continuar...")

    elif resp=='5': 
        print("################################################################## ")
        print("#######                    Informações                     ####### ")
        print("################################################################## ")
        print("#######  Projeto: Caderno Virtual de Receitas culinárias   ####### ")
        print("#######  Desenvolvido por:                                 ####### ")
        print("#######  Ian Gabriel                                       ####### ")
        print("#######  UFRN - 2026                                       ####### ")
        print("################################################################## ")
        print()
        input("Tecle <ENTER> para continuar...")

    elif resp=='0':
        print()
        print("############################################")
        print("#####  Você encerrou o programa, até logo! #")
        print("############################################")
        print()
        input("Tecle <ENTER> para continuar...")
    else:
        print()
        print("############################################")
        print("#####   Você digitou uma opção inválida ####")
        print("############################################")
        print("#####                                   ####")
        print("#####      Retorne ao menu anterior     ####")
        print("#####         e tente novamente         ####")
        print("#####                                   ####")
        print("############################################")
        print()
        input("Tecle <ENTER> para continuar...")

print("Obrigado por utilizar o Caderno Virtual de Receitas Culinárias! ")


