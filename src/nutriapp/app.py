"""
Uma vida saudavel em poucos clicks!
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class NutriApp(toga.App):
    
    def startup(self):
        
        altura_box = toga.Box(style=Pack(direction=ROW, padding=5,flex=1))
        altura_label = toga.Label("Altura: ", style=Pack())
        self.altura_input = toga.TextInput(placeholder="Insira sua altura", style=Pack(flex=1))
        altura_box.add(altura_label)
        altura_box.add(self.altura_input)

        peso_box = toga.Box(style=Pack(direction=ROW, padding=5,flex=1))
        peso_label = toga.Label("Peso (kg): ", style=Pack(padding=(0, 5)))
        self.peso_input = toga.TextInput(placeholder="Insira seu peso", style=Pack(flex=1))
        peso_box.add(peso_label)
        peso_box.add(self.peso_input)

        imc_info_box = toga.Box(
            children=[
                altura_box,
                toga.Divider(style=Pack(padding=10)),
                peso_box
            ],
            style=Pack(direction=ROW)
        )

        btn_calcIMC = toga.Button(
            "Calcular IMC",
            on_press=self.calc_imc,
            style=Pack(padding=5, height=50,font_size=13),
        )

        main_box = toga.Box(
            children=[
                toga.Label("Calculadora de IMC", style=Pack(font_size=25,text_align='center',padding_top=15)),
                imc_info_box,
                btn_calcIMC,
                toga.Divider(style=Pack(padding=20)),
                toga.Label("Second section"),
            ],
            style=Pack(direction=COLUMN, flex=1, padding=10)
        )

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def calc_imc(self, widget):
        altura = self.format_to_float(self.altura_input.value)
        peso = self.format_to_float(self.peso_input.value)
        imc = peso / (altura * altura)
        self.altura_input.value = ''
        self.peso_input.value = ''
        self.main_window.info_dialog('Calculadora IMC',f"IMC = {imc}")
        

    def format_to_float(self, value: str) -> float:
        if value.__contains__(','):
            value = value.replace(',','.')
        return float(value)

def main():
    return NutriApp()
