core/describer.py

descriptions = { "dog": "Cachorros são mamíferos domesticados, conhecidos por sua lealdade e inteligência.", "cat": "Gatos são animais independentes, ágeis e muito populares como pets domésticos.", "person": "Uma pessoa foi detectada. Humanos são seres sociais e conscientes.", "car": "Carros são veículos automotores comuns no transporte urbano.", "chair": "Cadeiras são móveis usados para sentar, com encosto e, geralmente, quatro pernas.", # adicione mais conforme desejar }

def describe_object(label): return descriptions.get(label.lower(), "Não há descrição disponível para este objeto.")

