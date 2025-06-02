core/nlp_parser.py

def extract_target_object(command): """ Analisa o comando e extrai o alvo pretendido, se houver. Ex: "olha aquele cachorro" → "cachorro" """ comandos_base = [ "olha aquilo", "olha isso", "olha pra isso", "olha essa coisa", "olha ali" ]

for base in comandos_base:
    if command.lower().strip() == base:
        return None  # genérico

palavras = command.lower().split()
if "olha" in palavras:
    try:
        idx = palavras.index("olha")
        # Pega a última palavra do comando (pode ajustar com NLP real)
        if idx + 2 < len(palavras):
            return palavras[-1]  # Ex: "aquele gato" → "gato"
    except:
        pass

return None

