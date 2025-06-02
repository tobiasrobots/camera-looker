# camera-looker

📷 Camera Looker

Camera Looker é um assistente com visão computacional simples, baseado em Python, capaz de capturar imagens, gravar vídeos e reconhecer objetos a partir de comandos em linguagem natural.

Ele foi idealizado como uma função independente, útil para integrar em projetos com assistentes inteligentes, mas também funciona de forma autônoma em qualquer sistema com câmera.


---

✅ Funcionalidades

📸 Captura de fotos por comando

🎥 Gravação de vídeos com duração personalizada

👁️ Detecção de objetos ao vivo via webcam

🗣️ Comandos interpretados em linguagem natural

🧠 Identificação específica com foco no objeto mencionado (ex: "olha aquele gato")



---

💻 Requisitos

Python 3.8+

Webcam (interna ou USB)



---

📦 Instalação

git clone https://github.com/seu-usuario/camera-looker.git
cd camera-looker
pip install -r requirements.txt


---

🧪 Exemplos de uso

python main.py "tira uma foto"
python main.py "grava um vídeo de 5 segundos"
python main.py "olha aquilo"
python main.py "olha aquele cachorro"


---

🧠 Tecnologias usadas

OpenCV – para acesso à câmera e manipulação de imagem

Transformers ou MediaPipe (opcional em futuras versões) – para detecção de objetos

Wikipedia API (futura versão) – para descrever objetos identificados



---

🧩 Pode ser integrado com:

Assistentes pessoais

Aplicações com comando de voz

Robôs com visão computacional

Softwares educacionais



---

📁 Estrutura

camera-looker/
├── main.py
├── requirements.txt
├── README.md
├── core/
│   ├── camera.py
│   ├── detector.py
│   ├── nlp_parser.py
│   ├── describer.py
└── assets/output/


---

📃 Licença

Este projeto está licenciado sob a MIT License.

