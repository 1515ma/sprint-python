# Sistema de Triagem de Pacientes - Hospital Sabará

emergencia = []
urgencia = []
normal = []

def avaliar_prioridade(febre, dor_intensa, dificuldade_respirar):
    if dificuldade_respirar == "sim":
        return "Emergência"
    elif dor_intensa == "sim" or febre == "sim":
        return "Urgência"
    else:
        return "Normal"

def adicionar_paciente():
    nome = input("\nNome do paciente: ")
    febre = input("Paciente com febre? (sim/nao): ").lower()
    dor_intensa = input("Paciente com dor intensa? (sim/nao): ").lower()
    dificuldade_respirar = input("Paciente com dificuldade para respirar? (sim/nao): ").lower()

    prioridade = avaliar_prioridade(febre, dor_intensa, dificuldade_respirar)

    paciente = {"nome": nome, "prioridade": prioridade}

    if prioridade == "Emergência":
        emergencia.append(paciente)
    elif prioridade == "Urgência":
        urgencia.append(paciente)
    else:
        normal.append(paciente)

    print(f"\nPaciente {nome} classificado como {prioridade}.")

def chamar_proximo():
    if emergencia:
        paciente = emergencia.pop(0)
    elif urgencia:
        paciente = urgencia.pop(0)
    elif normal:
        paciente = normal.pop(0)
    else:
        print("\nNenhum paciente aguardando triagem.")
        return

    print(f"\nChamando paciente {paciente['nome']} - Prioridade: {paciente['prioridade']}.")

def exibir_fila():
    print("\n--- Fila Atual de Pacientes ---")
    if emergencia:
        print("\n[Emergência]")
        for paciente in emergencia:
            print(f"- {paciente['nome']}")
    if urgencia:
        print("\n[Urgência]")
        for paciente in urgencia:
            print(f"- {paciente['nome']}")
    if normal:
        print("\n[Normal]")
        for paciente in normal:
            print(f"- {paciente['nome']}")
    if not (emergencia or urgencia or normal):
        print("\nNenhum paciente na fila.")

def menu():
    while True:
        print("\n--- Sistema de Triagem - Hospital Sabará ---")
        print("1. Adicionar paciente")
        print("2. Chamar próximo paciente")
        print("3. Exibir fila")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_paciente()
        elif opcao == "2":
            chamar_proximo()
        elif opcao == "3":
            exibir_fila()
        elif opcao == "4":
            print("\nEncerrando sistema de triagem. Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

menu()
