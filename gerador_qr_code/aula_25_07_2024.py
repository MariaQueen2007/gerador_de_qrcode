class Medicamento ():
    for Medicamento in range(0, 4):
       def __init__(self, nome = None, tipo = None, dosagem = None, pbula = None, validade = None):
           self._nome = nome
           self._tipo = tipo
           self._dosagem = dosagem
           self._pbula = pbula
           self._validade = validade
    def nome(self):
        return self._nome
    def tipo(self):
        if self._tipo == 'ml':
            return 'liquido'
        else:
            return 'unidade'
    def dosagem(self):
        return self._dosagem
    def pbula(self):
        return self._pbula
    def validade(self):
        return self._validade
neosaldina = Medicamento(nome = 'neosaldina', tipo = 'comprimido', dosagem = '1 comprimido por dia', pbula = 'Neosaldina® é um medicamento com atividade analgésica (diminui a dor) e antiespasmódica (diminui contração involuntária) indicado para o tratamento de diversos tipos de dor de cabeça, incluindo enxaquecas ou para o tratamento de cólicas.', validade = 'válido até 24 meses a partir da data de sua fabricação.')
print(neosaldina.nome())
print(neosaldina.tipo())
print(neosaldina.dosagem())
print(neosaldina.pbula())
print(neosaldina.validade())


        
