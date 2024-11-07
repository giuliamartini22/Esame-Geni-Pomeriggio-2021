import flet as ft
from UI.view import View
from model.model import Model


class Controller:

    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_graph(self, e):
        self._model.build_graph()

        self._view.txt_result1.controls.clear()
        self._view.txt_result1.controls.append(ft.Text(f"Creato grafo con {self._model.get_num_of_nodes()} vertici e {self._model.get_num_of_edges()} archi"))

        self._view.update_page()

    def handle_adiacenti(self, e):
        self._loc = self._view.dd_loc.value
        if self._loc is None:
            self._view.create_alert("Gene non inserito")
            return

        self._view.txt_result2.controls.clear()
        lista = self._model.calcolaAdiacenti(self._loc)
        self._view.txt_result2.controls.append(ft.Text(f"Geni adiacenti a: {self._loc}"))
        for i in lista:
            self._view.txt_result2.controls.append(ft.Text(f"{i[0]} - {i[1]}"))
        self._view.update_page()


    def fillDDLoc(self):
        self._listLoc = self._model.getLocalization()
        for s in self._listLoc:
            self._view.dd_loc.options.append(ft.dropdown.Option(s))
        self._view.update_page()

    def read_loc(self, e):
        if e.control.value == "None":
            self._loc = None
        else:
            self._loc = e.control.value
