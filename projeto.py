import os  
import pickle

            #########################################################
            ############# CADERNO VIRTUAL DE RECEITAS ###############
            #########################################################

receitas = {}
try: 
    arq_receitas = open("receitas.csv", "rt", encoding="utf-8")

    for linha in arq_receitas:
        linha = linha.strip()
        if linha:
            campos = linha.split(';')
            rec = campos[0]
            ing = campos[1]
            cat = campos[2]
            tempo = campos[3]
            modo_p = campos[4]
            ativo = campos[5] == "True"
            receitas[rec] = [rec, ing, cat, tempo, modo_p, ativo]
    arq_receitas.close()

except:
    receitas = { 
        'Bolo de chocolate' : 
            ['Bolo de chocolate', 
            'Farinha, açúcar, ovos, chocolate em pó, manteiga', 
            'Sobremesa', 
            '60', 
            'Bater os ingredientes, assar no forno', True],
        
        'Bolo de laranja' : 
            ['Bolo de laranja',
            '4 ovos, 2 xícaras de açúcar, 1 xícara de óleo, suco de 2 laranjas, casca de 1 laranja, 2 xícaras de farinha de trigo, 1 colher de fermento',
            'Sobremesa',
            '50',
            'Bata os ovos, o açúcar, o óleo, o suco e a casca da laranja. Adicione a farinha, misture bem e acrescente o fermento. Coloque em uma forma untada e asse até dourar.', True],
       
        "Omelete": 
            ["Omelete",
            "2 ovos, 50g de queijo, 1 pitada de sal",
            "Salgado",
            "15",
            "Bata os ovos, misture o queijo e o sal e frite em fogo baixo.", True],

        "Macarrão ao Alho e Óleo": 
            ["Macarrão ao Alho e Óleo",
            "250g de macarrão, 3 dentes de alho, 2 colheres de sopa de azeite, sal a gosto",
            "Salgado",
            "30",
            "Cozinhe o macarrão, doure o alho no azeite e misture tudo.", True],
       
        "Lasanha": 
            ["Lasanha",
            "500g de massa para lasanha, 300g de queijo muçarela, 300g de presunto, 500ml de molho de tomate",
            "Salgado",
            "60",
            "Monte camadas de massa, molho, queijo e presunto. Repita as camadas e asse até dourar.", True]

    }
    arq_receitas = open("receitas.csv", "wt", encoding="utf-8")
    for rec, dados in receitas.items():
        arq_receitas.write(f"{rec}; {dados[1]}; {dados[2]}; {dados[3]}; {dados[4]}; {dados[5]}\n")
    arq_receitas.close()



ingredientes = {}
try:
    arq_ingredientes = open("ingredientes.csv", "rt", encoding='utf-8')
    for linha in arq_ingredientes:
        linha = linha.strip()
        if linha:
            campos = linha.split(";")
            ing = campos[0]
            marca_i = campos[1]
            obs_i = campos[2]
            ativo_1 = campos[3] == "True"
            ingredientes[ing] = [ing, marca_i, obs_i, ativo_1]
    arq_ingredientes.close()

except:
    ingredientes = {
        'Farinha': ['Farinha de trigo', 'Finna', 'Utilize para bolos e pães', True],
        'Açúcar': ["Açúcar refinado", "União", "Ideal para sobremesas e bebidas", True],
        'Leite': ["Leite integral", "Itambé", "Conservar sob refrigeração após aberto", True]

    }
    arq_ingredientes = open("ingredientes.csv", "wt", encoding='utf-8')
    for ing, dados in ingredientes.items():
        arq_ingredientes.write(f"{ing}; {dados[1]}; {dados[2]}; {dados[3]}\n")
    arq_ingredientes.close()



categorias = {}
try:
    arq_categorias = open("categorias.csv", "rt", encoding="utf-8")
    for linha in arq_categorias:
        linha = linha.strip()
        if linha:
            campos = linha.split(';')
            cat = campos[0]
            ativo_2 = campos[1] == "True"
            categorias[cat] = [cat, ativo_2]
    arq_categorias.close()

except:
    categorias = { 
          'Lanche' : ['Lanche', True], 
          'Massas' : ['Massas', True], 
          'Sobremesa' : ['Sobremesa', True] 
    }   
    arq_categorias = open("categorias.csv", "wt", encoding='utf-8' )
    for cat, dados in categorias.items():
        arq_categorias.write(f"{cat}; {dados[1]}\n")
    arq_categorias.close()

def msg_inicial():
    print                  ("Bem vindo(a) ao:")
    print("#########################################################")
    print("######   CADERNO VIRTUAL DE RECEITAS CULINARIAS    ######")
    print("#########################################################")

resp = ''
while resp != '0':
    os.system('cls')
    msg_inicial()
    print()
    print("#########################################################")
    print("#######  CADERNO VIRTUAL DE RECEITAS CULINARIAS   #######")  
    print("#########################################################")
    print("#######           1 - Módulo Receitas             #######")
    print("#######           2 - Módulo Ingredientes         #######")
    print("#######           3 - Módulo Categoria            #######")
    print("#######           4 - Módulo Relatório            #######")
    print("#######           5 - Módulo Informações          #######")
    print("#######           0 - Sair                        #######")
    print("#########################################################")
    resp = input("Escolha sua opção: ")

    if resp == "1":
        os.system('cls')
        print()
        print("######################################################## ")
        print("#######                Receita                   ####### ")
        print("######################################################## ")
        print("####### 1- Cadastrar Receita                     ####### ")
        print("####### 2- Consultar Receita                     ####### ")
        print("####### 3- Editar Receita                        ####### ")
        print("####### 4- Excluir Receita                       ####### ")
        print("####### 0- Voltar                                ####### ")
        print("######################################################## ")
        resp_r = input("EScolha sua opção: ")
        print()

        if resp_r == '1': 
            os.system('cls')
            print()
            print("############################################")
            print("#####         Cadastrar Receita        #####")
            print("############################################")
            print()
            rec = input("## Nome da receita: ")
            if rec in receitas:
                print("Receita já cadastrada! ")
            else:
                print()
                ing = input("## Ingredientes: ")
                print()
                cat = input("## Digite a categoria da receita: ")
                print()
                tempo = int(input("## Digite o tempo da receita(em minutos!): "))
                print()
                modo_p = input("## Modo de preparo: ")
                print()
                receitas[rec] = [rec, ing, cat, tempo, modo_p, True]
                print("## Receita cadastrada! ")
                print()
                print("## Receita: ", receitas)
            print()
            input("Tecle <ENTER> para continuar...")

        elif resp_r == '2':
            os.system('cls')
            print()
            print("############################################")
            print("#####         Consultar receita        #####")
            print("############################################")
            print()
            print("## Receitas cadastradas: ")
            for receita in receitas:
                if receitas[receita][5]:
                    print("-", receita)
                    print("-" * 25)
                    print()
            rec = input("## Digite o nome da receita: ")
            print()
            if rec in receitas and receitas[rec][5]:
                print("## Nome: ", receitas[rec][0])
                print("## Ingredientes: ", receitas[rec][1])
                print("## Categoria: ", receitas[rec][2])
                print("## Tempo: ", receitas[rec][3])
                print("## Modo de preparo: ", receitas[rec][4])
            else:
                print("## Nenhuma receita cadastrada! ")
            print()
            input("Tecle <ENTER> para continuar...")

        elif resp_r == '3':
            os.system('cls')
            print()
            print("############################################")
            print("#####           Editar Receita         #####")
            print("############################################")
            print()
            for rec in receitas:
                print("-", rec)
            print()
            rec = input("## Nome da receita: ")
            print()
            if rec in receitas:
                print("## Receita atual: ")
                print("- Nome: ", receitas[rec][0])
                print("- Ingredientes: ", receitas[rec][1])
                print("- Categoria: ", receitas[rec][2])
                print("- Tempo: ", receitas[rec][3])
                print("- Modo de preparo: ", receitas[rec][4])
                print()
                print("## Digite os novos dados da receita: ")
                novo_rec = input("- Nome da receita: ")
                ing = input("- Ingredientes: ")
                cat = input("- Digite a categoria da receita: ")
                tempo = input("- Digite o tempo da receita(em minutos): ")
                modo_p = input("- Modo de preparo: ")
                del receitas[rec]
                receitas[novo_rec] = [novo_rec, ing, cat, tempo, modo_p, True]
                print()
                print("#### Receita Editada! ")
                print()
                print("## Receita atualizada: ", receitas)
            else:
                print("ReCeita não encontrada")
            print()
            input("Tecle <ENTER> para continuar...")  

        elif resp_r == '4':
            os.system('cls')
            print()
            print("############################################")
            print("#####           Exluir Receita         #####")
            print("############################################")
            print()
            for rec in receitas:
                if receitas[rec][5]:
                    print("-", rec)
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
                    receitas[rec][5] = False
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
        print("####### 1- Cadastrar Ingrediente                 ####### ")
        print("####### 2- Consultar Ingrediente                 ####### ")
        print("####### 3- Editar Ingrediente                    ####### ")
        print("####### 4- Excluir Ingrediente                   ####### ")
        print("####### 0- Voltar                                ####### ")
        print("######################################################## ")
        resp_i = input("Escolha sua resposta: ")

        if resp_i == '1':
            os.system('cls')
            print()
            print("############################################")
            print("#####       Cadastrar Ingrediente      #####")
            print("############################################")
            print()
            ing= input("## Nome do Ingrediente: ")
            if ing in ingredientes:
                print("## Ingrediente já cadastrado! ")
            else:
                print()
                marca_i = input("## Marca do ingrediente: ")
                print()
                obs_i = input("## Deixe uma observação sobre o ingrediente: ")
                print()
                ingredientes[ing] = [ing, marca_i, obs_i, True]
                print("## Ingrediente cadastrado! ")
                print()
                print("## Ingrediente: ", ingredientes)
            print()
            input("Tecle <ENTER> para continuar...")

        elif resp_i == '2':
            os.system('cls')
            print()
            print("############################################")
            print("#####       Consultar Ingrediente      #####")
            print("############################################")
            print()
            print("## Ingredientes cadastrados: ")
            for ingrediente in ingredientes:
                if ingredientes[ingrediente][3]:
                    print("-", ingrediente)
                    print()
            ing = input("## Nome do Ingrediente: ")
            print()
            if ing in ingredientes and ingredientes[ing][3]:
                print("## Nome:", ingredientes[ing][0])
                print("## Marca:", ingredientes[ing][1])
                print("## Observação:", ingredientes[ing][2])
            else:
                print("## Nenhum ingrediente cadastrado! ")
            print()
            input("Tecle <ENTER> para continuar...")

        elif resp_i == '3':
            os.system('cls')
            print()
            print("############################################")
            print("#####         Editar Ingrediente       #####")
            print("############################################")
            print() 
            for ing in ingredientes:
                print("-", ing)
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
                novo_ing = input("## Nome do Ingrediente: ")
                marca_i = input("## Marca do ingrediente: ")
                obs_i = input("## Deixe uma observação sobre o ingrediente: ")
                del ingredientes[ing]
                ingredientes[novo_ing] = [novo_ing, marca_i, obs_i, True]
                print()
                print("## Ingrediente atualizado! ", ingredientes)
                print()
                print("#### Ediçao feita! #### ")
                print()
            else:
                print("Nenhum ingrediente encontrado!")
            print()
            input("Tecle <ENTER> para continuar...")

        elif resp_i == '4':
            os.system('cls')
            print()
            print("############################################")
            print("#####         Excluir Ingrediente      #####")
            print("############################################")
            print() 
            for ing in ingredientes:
                print("-", ing)
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
                    ingredientes[ing][3] = False
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
        print("#######              Categorias                  #######")
        print("########################################################")
        print("####### 1- Cadastrar Categoria                   #######")
        print("####### 2- Consultar Categoria                   #######")
        print("####### 3- Editar Categoria                      #######")
        print("####### 4- Excluir Categoria                     #######")
        print("####### 0- Voltar                                #######")
        print("########################################################")
        print()
        resp_c = input("Escolha sua opção: ")

        if resp_c == '1':
            os.system('cls')
            print()
            print("############################################")
            print("#####       Cadastrar Categoria        #####")
            print("############################################")
            print()
            cat = input("## Digite o nome da categoria: ")
            if cat in categorias:
                print("Categoria já cadastrada! ")
            else:
                categorias[cat] = [cat, True]
                print("Categorias:", categorias)
                print("Categoria cadastrada!")
            print()
            input("Tecle <ENTER> para continuar...")

        elif resp_c == '2': 
            os.system('cls')
            print()
            print("############################################")
            print("#####        Consultar Categoria       #####")
            print("############################################")
            print()

            for categoria in categorias:
                if categorias[categoria][1]:
                    print("- Categoria encontrada: ", categoria)
            print()
            cat = input("Digite a categoria: ")
            if cat not in categorias or not categorias[cat][1]:
                print("## Categoria não encontrada!")
            else:
                encontrou = False
                for receita in receitas:
                    if receitas[receita][2] == cat and receitas[receita][5]:
                        print("##", receitas[receita][0])
                        encontrou = True
                if not encontrou:
                    print("## Nenhuma receita encontrada nessa categoria.")  

            print()
            input("Tecle <ENTER> para continuar...")

        elif resp_c == '3':
            os.system('cls')
            print()
            print("############################################")
            print("#####        Editar  Categoria         #####")
            print("############################################")
            print()
            for cat in categorias:
                print("-", cat)
            print()
            cat = input("## Digite a categoria atual: ")
            print()
            if cat in categorias:
                print("## Categoria atual: ", categorias[cat])
                print()
                print("## Digite a nova categoria: ")
                print()
                nova_cat = input("- Digite o nome da categoria: ")
                categorias[nova_cat] = [nova_cat, True]
                del categorias[cat]
                print()
                print("#### Categoria Editada! ", categorias[cat])
                print()
            else:
                print("## Nenhuma categoria cadastrada! ")
            print()
            input("Tecle <ENTER> para continuar...")

        elif resp_c == '4':
            os.system('cls')
            print()
            print("############################################")
            print("#####          Exluir  Categoria       #####")
            print("############################################")
            print()
            for cat in categorias:
                print("-", cat)
            print()
            cat = input("## Digite a categoria: ")
            print()
            if cat in categorias:
                print("## Categoria: ", categorias[cat])
                print()
                confirma = input("## Tem certeza que deseja excluir essa categoria? (s/n): ")
                if confirma.lower() == 's':
                    categorias[cat][1] = False
                    print("## Categoria Excluida! ")
                    print()
                    print("## Categoria: ", categorias)
                else:
                    print("## Exclusão cancelada! ")
            else:
                print("## Nenhuma categoria cadastrada! ")
            print()
            input("Tecle <ENTER> para continuar...")

    elif resp == '4':
        os.system('cls')
        print("################################################################ ")
        print("#######                    Relatório                     ####### ")
        print("################################################################ ")
        print("####### 1- Lista geral de receitas                       ####### ")
        print("####### 2- Lista geral de ingredientes                   ####### ")
        print("####### 3- Lista geral de categorias                     ####### ")
        print("####### 4- Lista geral de receitas por tempo de preparo  #######" )
        print("####### 5- Lista geral de receitas por categoria         ####### ")
        print("####### 0- Voltar                                        ####### ")
        print("################################################################ ")
        print()
        resp_rel = input("Escolha sua opçao: ")
        print()

        if resp_rel == '1' :
            print()
            print("############################################")
            print("#####      Lista geral de receitas     #####")
            print("############################################")
            print()

            if len(receitas) == 0:
                 print("## Nenhuma receita cadastrada!")

            else:
                for rec in receitas:
                    if receitas[rec][5]:
                        print("Nome:", receitas[rec][0])
                        print("Ingredientes:", receitas[rec][1])
                        print("Categoria:", receitas[rec][2])
                        print("Tempo:", receitas[rec][3])
                        print("Modo de preparo:", receitas[rec][4])
                        print("-" * 50)
            print()
            input("Tecle <ENTER> para continuar...")
        
        elif resp_rel == '2': 
            print()
            print("############################################")
            print("#####    Lista geral de ingredientes   #####")
            print("############################################")
            print()
            
            if len(ingredientes) == 0:
                print("## Nenhum ingrediente cadastrado!")
             
            else:
                for ingrediente in ingredientes:
                    if ingredientes[ingrediente][3]:
                        print("Nome:", ingredientes[ingrediente][0])
                        print("Marca do ingrediente:", ingredientes[ingrediente][1])
                        print("Observação:", ingredientes[ingrediente][2])
                        print("-" * 65)
            print()
            input("Tecle <ENTER> para continuar...")

        elif resp_rel == '3':
            print()
            print("############################################")
            print("#####    Lista geral de categorias     #####")
            print("############################################")
            print()

            if len(categorias) == 0:
                print("## Nenhuma categoria cadastrada!")
            
            else:
                for categoria in categorias:
                    if categorias[categoria][1]:
                        print("Categoria:", categorias[categoria][0])
                        print("-" * 45)
            print()
            input("Tecle <ENTER> para continuar...")

        elif resp_rel == '4':
            print()
            print("###############################################################")
            print("#####    Lista geral de receitas por tempo de preparo     #####")
            print("###############################################################")
            print()
            print("1 - Prontas em 15 minutos")
            print("2 - Prontas em 30 minutos")
            print("3 - Prontas em 60 minutos")
            print()
            opc = input("Escolha uma opção: ")

            valido = True
            if opc == '1':
                tempo_max = 15

            elif opc == "2":
                tempo_max = 30

            elif opc == "3":
                tempo_max = 60

            else:
                print("## Opção inválida!")
                input("Tecle <ENTER> para continuar...")
                valido = False

            if valido:
                for receita in receitas:
                    tempo = int(receitas[receita][3])

                    if tempo == tempo_max:
                        print("Nome:", receitas[receita][0])
                        print("Tempo:", receitas[receita][3], "minutos")
                        print("-" * 50)
            print()
            input("Tecle <ENTER> para continuar...")
        
        elif resp_rel == '5':
            print()
            print("###############################################################")
            print("#####       Lista geral de receitas por categoria         #####")
            print("###############################################################")
            print()

            contagem = {}

            for receita in receitas:
                 if receitas[receita][5]:
                    categoria = receitas[receita][2]

                    if categoria in contagem:
                        contagem[categoria].append(receitas[receita][0])
                    else:
                        contagem[categoria] = [receitas[receita][0]]

            for categoria in contagem:
                print(f"[ {categoria} ] : {len(contagem[categoria])} receita(s)")
                for nome in contagem[categoria]:
                    print("  -", nome)
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


arq_receitas = open("receitas.csv", "wt", encoding="utf-8")
for rec, dados in receitas.items():
    arq_receitas.write(f"{rec};{dados[1]}; {dados[2]}; {dados[3]}; {dados[4]}; {dados[5]}\n")
arq_receitas.close()


arq_ingredientes = open("ingredientes.csv", "wt", encoding='utf-8')
for ing, dados in ingredientes.items():
    arq_ingredientes.write(f"{ing};{dados[1]}; {dados[2]}; {dados[3]}\n")
arq_ingredientes.close()


arq_categorias = open("categorias.csv", "wt", encoding='utf-8' )
for cat, dados in categorias.items():
    arq_categorias.write(f"{cat}; {dados[1]}\n")
arq_categorias.close()
