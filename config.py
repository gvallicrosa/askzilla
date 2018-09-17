WAIT_TIME = 30  # wait when failed to restart

# pregunta, resposta(en text), timer(int)
questions = [
    ["Quant son 12x13?", "156", 10],
    ["Quant son 156/13?", "12", 10],
    ["Les lletres del cartell de nomes veins son de color?", "groc", 10],
    ["Les lletres del cartell de propietat privada son de color?", "blanc", 10],
    ["El fons del cartell de propietat privada es de color?", "vermell", 10],
    ["Les caixes de plastic apilades a l'entrada de la finca son de color?", "vermell", 10],
    ["Quantes totxanes fa d'alt la barbacoa?", "5", 10],
    ["Quantes totxanes senceres fa d'ample la barbacoa?", "7", 10],
    ["Quants escalons fa has de pujar per l'escala de metall que porta al pis de dalt?", "13", 10],
    ["Quants testos llargs i blancs hi ha a davant la casa?", "4", 10],
    ["De quin color es el 3 del rellotge dels plats de paret?", "groc", 10],
    ["De quin color es el cavall blanc de Santiago?", "blanc", 10],
    ["Quants quadrats amb cireres hi ha al drap?", "25", 10],
    ["Quantes pinces hi ha a l'estenedor?", "17", 10],
    ["Quants racimos de raim hi han penjats a la paret de la cuina?", "16", 10],
    ["Entrant a l'esquerra hi ha una foto de dues persones. A quina banda esta la dona [dreta/esquerra]?", "dreta", 10],
    ["Quants ereu a dinar?", "9", 10],
    ["Quin numero te la casa?", "48", 10],
    ["Quin es l'any xines (numero) que es va iniciar el passat febrer?", "4716", 10],
    ["Quant val el simbol del peix?", "0", 10],
]

TOTAL_VALID = len(questions) # total needed to success