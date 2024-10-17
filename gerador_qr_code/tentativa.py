class Medicamento():
    def __init__(self, nome = None, tipo = None, dosagem = None, pbula = None, validade = None):
        self._nome = nome #vai mostrar o nome do remédio
        self._tipo = tipo #vai mostrar o tipo de remédio, se é comprimido ou liquido
        self._dosagem = dosagem #vai mostrar o quanto de remédio a pessoa vai ter que tomar por dia
        self._pbula = pbula #vai mostrar a bula do remédio
        self._validade = validade #vai mostrar a validade

    def __iter__(self):
        # Retorna um iterador que itera sobre atributos específicos da classe
        return iter([self._nome,self._tipo,self._dosagem, self._pbula, self._validade]) #retorna sobre tudo a respeito do remédio..O tipo, nome, dosagem, bula e validade.
        # return iter([self._nome, self._tipo, self._dosagem, self._pbula, self._validade])

# Criando algumas instâncias da classe Medicamento
medicamento1 = Medicamento(nome = 'Neosaldina', tipo = 'comprimido', dosagem = '1 comprimido por dia', pbula = 'Neosaldina® é um medicamento com atividade analgésica (diminui a dor) e antiespasmódica (diminui contração involuntária) indicado para o tratamento de diversos tipos de dor de cabeça, incluindo enxaquecas ou para o tratamento de cólicas.', validade = 'válido até 24 meses a partir da data de sua fabricação.')
medicamento2 = Medicamento(nome = 'Trembolona', tipo = 'líquido', dosagem = '1 injetada por dia', pbula = 'O Trembolona pode afetar, em certa medida, a função cardiovascular, o que significa que não é adequado para aqueles pacientes que sofrem alguma deficiência a este nível ou naqueles em que participam regularmente em esportes ou atividades em que eles exigem um nível decente de esforço cardiovascular.', validade = '1 dia')
medicamento3 = Medicamento(nome = 'Dipirona', tipo = 'líquido', dosagem = '1 injetada por dia', pbula = 'é um fármaco que tem ação antipirética (febre) e analgésica (dor), sendo indicada para dores de cabeça, dores musculares, cólica renal, cólica menstrual, pós-operatórias e de outras origens.', validade = '1 ano')
medicamento4 = Medicamento(nome = 'Buscopan', tipo = 'comprimido', dosagem = '1 comprimido por dia', pbula = 'Buscopan® é indicado para tratamento dos sintomas de cólicas gastrintestinais (estômago e intestinos), cólicas e movimentos involuntários anormais das vias biliares e cólicas dos órgãos sexuais e urinários.', validade = '1 ano')
medicamento5 = Medicamento(nome = 'Dorflex', tipo = 'comprimido', dosagem = '1 comprimido por dia', pbula = 'Dorflex é indicado no alívio da dor associada a contraturas musculares, incluindo dor de cabeça tensional.', validade = '1 ano')

# Iterando sobre as instâncias da classe Medicamento
for atributo in medicamento1: 
    print(atributo)

for atributo in medicamento2:
    print(atributo)

for atributo in medicamento3:
    print(atributo)

for atributo in medicamento4:
    print(atributo)

for atributo in medicamento5:
    print(atributo)