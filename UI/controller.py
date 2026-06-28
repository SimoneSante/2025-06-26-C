import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def ddda(self):
        self._view._ddYear1.options.clear()
        self._view._ddYear1.value = None

        listaS = self._model.get_anni()

        for l in listaS:
            self._view._ddYear1.options.append(
                ft.dropdown.Option(
                    key=l,
                    text=l,
                )
            )
        self._view.update_page()

    def dda(self):
        self._view._ddYear2.options.clear()
        self._view._ddYear2.value = None

        listaS = self._model.get_anni()

        for l in listaS:
            self._view._ddYear2.options.append(
                ft.dropdown.Option(
                    key=l,
                    text=l,
                )
            )
        self._view.update_page()


    def handleBuildGraph(self, e):
        self._view._txtGraphDetails.controls.clear()
        try:
            anno1 = int(self._view._ddYear1.value)
            anno2 = int(self._view._ddYear2.value)

        except ValueError:
            self._view._txtGraphDetails.controls.append(ft.Text("selezionare entrambi gli anni"))
        if anno1 is None or anno2 is None or anno1 > anno2:
            self._view._txtGraphDetails.controls.append(
                ft.Text("selezionare entrambi i campi validi", color="red")

            )
        else:
            self._model.build_graph(anno1, anno2)
            stats = self._model.get_stats()
            self._view._txtGraphDetails.controls.append(
                ft.Text(f"il grafo ha:{stats[0]} nodi e {stats[1]} archi", color="green"))

            self._view.update_page()


    def handlePrintDetails(self, e):
        lista_lunga = self._model.connesse()
        for k in lista_lunga:
            self._view._txtGraphDetails.controls.append(ft.Text(f"{k[0].name}:  {k[1]}", color="blue"))
        self._view.update_page()

    def handleCercaTeamSfortunati(self, e):
        pass
