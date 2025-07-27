# Mestre de RPG Portátil – seu amigo IA nas aventuras de D&D, sempre pronto para a próxima cena!

**Mestre de RPG Portátil** é um bot de IA para RPG solo em texto. Ele atua como um *Dungeon Master* baseado em D&D 5ª edição, criando aventuras narrativas imersivas para um jogador. Ideal para quem ama RPG mas não tem mesa fixa, o bot gera descrições, encontra encontros aleatórios e gerencia regras de jogo em tempo real.

## Funcionalidades

- **Narrativa Dinâmica**: A IA cria cenas detalhadas de acordo com as ações do jogador (exploração, diálogos, batalhas, etc.).  
- **Coerência de Campanha**: Armazena informações-chave (personagens, locais, itens) para manter consistência narrativa ao longo da aventura:contentReference[oaicite:10]{index=10}:contentReference[oaicite:11]{index=11}.  
- **Regras de D&D 5e**: Calcula inimigos e desafios conforme as regras, ajustando dificuldades com base no progresso do personagem.  
- **Experiência Solo**: Ideal para jogo solo ou em duplas; o mestre IA reage a todas as escolhas do jogador, sugerindo consequências e rolando iniciativa automaticamente.  

## Tecnologias

- **Python** – Linguagem principal.  
- **Transformers (Hugging Face)** – Modelo de linguagem pré-treinado personalizado.  
- **JSON** – Armazenamento simples de estado do jogo e diálogos.  
- **(Opcional) Vector DB** – Para memória de longo prazo (usando FAISS/Chroma).  

## Instalação

1. Clone o repositório:  
   ```bash
   git clone https://github.com/seu-usuario/mestre-de-rpg-portatil.git
   cd mestre-de-rpg-portatil

Configure o ambiente Python:
bash
Copiar
Editar
python3 -m venv .venv
source .venv/bin/activate   # ou .venv\\Scripts\\activate no Windows
pip install -r requirements.txt

(Opcional) Baixe o modelo de linguagem:
Se houver script download_model.sh, execute bash download_model.sh.
Caso contrário, configure o caminho do modelo em config.json.

Uso Básico
Execute o arquivo principal:
bash
Copiar
Editar
python run_game.py

Siga as instruções na tela: crie seu personagem ou escolha pré-definido, e então descreva as ações do personagem. O mestre IA responderá com descrições de cena e continuará a narrativa.
O estado do jogo (personagem, mundo e memória) fica salvo em game_state.json.


Trecho simplificado de envio de prompt à IA:

from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("facebook/llama-2-7b")
model = AutoModelForCausalLM.from_pretrained("facebook/llama-2-7b")
 
context = load_json_context()     # carrega memória e descrições anteriores
prompt = context + "\n\nNPC: O que o aventureiro faz?"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=200)
print(tokenizer.decode(outputs[0]))

Contribuições são bem-vindas! Sinta-se livre para sugerir melhorias nas regras, adicionar mais dados de aventura (podemos expandir o treinamento) ou otimizar o gerenciamento de memória. Abra issues ou pull requests no GitHub.

Mestre de RPG Portátil – seu amigo IA nas aventuras de D&D, sempre pronto para a próxima cena!



Este projeto está sob a MIT License.
