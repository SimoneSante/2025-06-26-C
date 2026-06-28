from model.model import Model


def main():

    model = Model()
    c=2002
    b=2004
    print(f"Costruisco il grafo con c = {c}...")
    model.build_graph(c,b)
    n_nodi, n_archi = model.get_stats()
    print(f" il grafo creato contiene {n_nodi} nodes e {n_archi} edges")
    k = model.connesse()

    for costruttore, peso in k:
        print(f"{costruttore.constructorRef} -- {peso}")

if __name__ == "__main__":
    main()