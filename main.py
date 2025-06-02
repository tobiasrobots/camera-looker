main.py

from core.camera import capture_photo, record_video from core.detector import detect_objects from core.nlp_parser import extract_target from core.describer import describe_object import sys

def main(): if len(sys.argv) < 2: print("\n[❗] Use: python main.py "comando de voz"\n") return

command = sys.argv[1].lower()

if "tira uma foto" in command:
    capture_photo()
elif "grava um vídeo" in command:
    record_video(duration=5)  # valor padrão
elif "olha" in command:
    target = extract_target(command)
    results = detect_objects(target)

    if results:
        for obj in results:
            desc = describe_object(obj)
            print(f"\n✅ Detectado: {obj}\nℹ️ {desc}")
    else:
        print("\n[🤔] Nenhum objeto correspondente encontrado.")
else:
    print("\n[❓] Comando não reconhecido.")

if name == "main": main()

