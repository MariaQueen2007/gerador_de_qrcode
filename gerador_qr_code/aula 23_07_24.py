class Medicamento():
    def __init__(self, nome = None, tipo = None, dosagem = None): 
        self._nome = nome 
        self._tipo = tipo
        self._dosagem = dosagem
    def nome(self):
        return self._nome
    def tipo(self):
        return "ml" if self._tipo == "liquido" else "un"
    def dosagem(self):
        return self._dosagem
dipirona = Medicamento(nome = 'Dipirona', tipo = 'comprimido', dosagem = '500 mg')
print(dipirona.nome())
print(dipirona.tipo())
print(dipirona.dosagem())
