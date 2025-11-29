import datetime

def selecionar_periodo():
    data_inicial = input("Digite a data inicial (dd/mm/aaaa): ")
    data_final = input("Digite a data final (dd/mm/aaaa): ")

    try:
        d1 = datetime.datetime.strptime(data_inicial, "%d/%m/%Y")
        d2 = datetime.datetime.strptime(data_final, "%d/%m/%Y")
        
        if d1 > d2:
            print("A data inicial não pode ser maior que a final.")
        else:
            print(f"Período selecionado: {data_inicial} até {data_final}")
    except:
        print("Formato inválido. Use dd/mm/aaaa.")

selecionar_periodo()
