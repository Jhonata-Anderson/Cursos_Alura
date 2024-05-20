import os

restaurantes = [{"nome" : "Praça", "Categoria" : "Japonesa", "ativo" : False}, 
                {"nome" : "Pizza Suprema", "Categoria" : "Pizza", "ativo" : True},
                {"nome" : "Cantina", "Categoria" : "Italiano", "ativo" : False}]

def exibir_nome_do_programa():
      #Essa função serve para exibir o nome do programa
      print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def exibir_opcoes():
      #Essa função serve para exibir as opções do programa.
      print("1. Cadastrar Restaurante")
      print("2. Listar Restaurante")
      print("3. Alternar estado do Restaurante")
      print("4. Sair\n")

def finalizar_app():
      #Essa função serve para mostrar a mensagem ao finalizar o app.
      exibir_subtitulo("Finalizando o App.")

def voltar_ao_menu_principal():
      #Essa funçaõ serve para voltar ao menu principal.
      input("\nDigite uma tecla para voltar ao menu principal ")
      main()

def opcao_invalida():
      #Essa função serve para caso o usuario digite algo inválido.
      print("Opção Inválida!\n")
      voltar_ao_menu_principal()

def exibir_subtitulo(texto):
      #Essa função dá um subtitulo para a opção escolhida
      os.system("cls")
      linha = "*" * (len(texto))
      print(linha)
      print(texto)
      print(linha, "\n")

def cadastrar_novo_restaurante():
      #Essa funçãoo serve para cadastrar um novo restaurante.
      exibir_subtitulo("Cadastro de novos restaurantes")

      nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar: ")
      categoria = input(f"Digite o nome da categoria do restaurante {nome_do_restaurante}: ")
      dados_do_restaurante = {"nome" : nome_do_restaurante, "Categoria" : categoria, "Ativo" : False}
      restaurantes.append(dados_do_restaurante)
      print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso!")

      voltar_ao_menu_principal()

def listar_restaurante():
      #Essa função serve para listar todos os restaurantes cadastrados.
      exibir_subtitulo("Listando restaurantes")

      print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
      for restaurante in restaurantes:
            nome_restaurante = restaurante["nome"]
            categoria = restaurante["Categoria"]
            ativo = "ativado" if restaurante["Ativo"] else "desativado"
            print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")

      voltar_ao_menu_principal()

def alternar_estado_restaurante():
      #Essa função serve para alterar o estado do restaurante, deixando ativada ou desativada.
      exibir_subtitulo("Alterando estado do restaurante")

      nome_restaurante = input("Digite o nome do restaurante que deseja alterar o estado: ")
      restaurante_encontrado == False

      for restaurante in restaurantes:
            if nome_restaurante == restaurante["nome"]:
                  restaurante_encontrado = True
                  restaurante["Ativo"] = not restaurante["Ativo"]
                  mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante ["Ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
                  print(mensagem)
      
      if not restaurante_encontrado:
            print("O restaurante não foi encontrado")

      voltar_ao_menu_principal()

def escolher_opcao():
      #Essa função serve para escolher a opção fornecida para o usuário.
      try:
            opcao_escolhida = int(input("Escolha uma opção: "))

            if opcao_escolhida == 1:
                  cadastrar_novo_restaurante()
            elif opcao_escolhida == 2:
                  listar_restaurante()
            elif opcao_escolhida == 3:
                  alternar_estado_restaurante()
            elif opcao_escolhida == 4:
                  finalizar_app()
            else:
                  opcao_invalida()
      except:
            opcao_invalida()

def main():
      #Função principal que iniciar o programa.
      os.system("cls")
      exibir_nome_do_programa()
      exibir_opcoes()
      escolher_opcao()

if __name__ == "__main__":
      main()
