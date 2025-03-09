# Assistente de IA - Versão Básica

Este projeto é um assistente de inteligência artificial básico, atualmente em desenvolvimento.

## Funcionalidades
Atualmente, o assistente possui apenas duas funcionalidades principais:
1. Gravação de áudio
 - O assistente pode gravar áudio do microfone do usuário.
 - A gravação começa quando o usuário pressiona a tecla `]`.
 - A gravação é interrompida quando o usuário pressiona a tecla `esc`.
2. Transcrição de áudio
 - O assistente utiliza o modelo <strong>Whisper</strong> da OpenAI em sua versão `base` para transcrever o áudio gravado em texto.

## Dependências
- <strong>Python 3.10+</strong>
- <strong>ffmpeg 4.4.2+</strong>
- <strong>Libs:</strong> `pyaudio`, `keyboard`, `openai-whisper`, `wave`