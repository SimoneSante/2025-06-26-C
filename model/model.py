import networkx as nx
from database.DAO import DAO

class Model:
    def __init__(self):
        self._graph =nx.Graph()
        self._idMap={}

    def build_graph(self,c,b):
        self._graph.clear()
        self._idMap.clear()

        nodi=DAO.get_nodi()
        riempinodi=DAO.riempi_nodi(c,b)
        self._graph.add_nodes_from(nodi)
        for n in nodi:
            self._idMap[n.constructorId]=n
        for k in riempinodi:
            if k.year not in self._idMap[k.constructorId].infGareAnno.keys():
                self._idMap[k.constructorId].infGareAnno[k.year]=[]
                self._idMap[k.constructorId].infGareAnno[k.year].append(k)
            else:
                self._idMap[k.constructorId].infGareAnno[k.year].append(k)

        edges = list(DAO.get_archi(c,b))
        mappa_pesi = DAO.get_pesi(c,b)
        for a in edges:
            p = self._idMap[a[0]]
            s = self._idMap[a[1]]
            peso1 = float(mappa_pesi[a[0]])
            peso2 = float(mappa_pesi[a[1]])

            somma = peso1 + peso2

            self._graph.add_edge(p, s, weight=somma)


    def get_stats(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def get_anni(self):
        lista=DAO.getAllYears()
        return lista



    def top3(self):
        archi=self._graph.edges(data=True)
        lista=sorted(archi, key=lambda x: x[2]["weight"], reverse=True)
        s=""
        for i in range(3):
            s=s+lista[i][0].__str__() + lista[i][1].__str__() + str(lista[i][2]["weight"]) + "\n"
        return s

    def connesse(self):
        largest = max(nx.connected_components(self._graph), key=len)
        sotto_grafo = self._graph.subgraph(largest)

        mappa_costr_peso = {}

        for k in sotto_grafo.nodes():
            archi_incidenti = list(sotto_grafo.edges(k, data=True))

            peso_massimo = 0

            for u, v, data in archi_incidenti:
                if int(data["weight"]) > peso_massimo:
                    peso_massimo = int(data["weight"])

            mappa_costr_peso[k] = peso_massimo

        lista_ordinata = sorted(
            mappa_costr_peso.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return lista_ordinata
    """ def connesse(self):
        largest=max(nx.connected_components(self._graph),key=len)
        sotto_grafo = self._graph.subgraph(largest)
        mappa_costr_peso={}
        for k in sotto_grafo:
            for t in list(sotto_grafo.edges(k, data=True)):
                if  k not in mappa_costr_peso.keys():
                    mappa_costr_peso[k]= int(t[2]["weight"])
                elif t[2]["weight"] > mappa_costr_peso[k]:
                    mappa_costr_peso[k]= mappa_costr_peso[k]+int(t[2]["weight"])
        return  mappa_costr_peso"""

    def get_anni(self):
        return list(DAO.getAllYears())