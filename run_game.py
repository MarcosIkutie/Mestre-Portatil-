import os
import json
import torch
from transformers import pipeline

# Defina o modelo HF desejado (ex: "gpt2" ou "EleutherAI/gpt-neo-2.7B")
MODEL_NAME = "gpt2"

# Seleciona dispositivo (GPU se disponível)
device = 0 if torch.cuda.is_available() else -1
generator = pipeline("text-generation", model=MODEL_NAME, tokenizer=MODEL_NAME, device=device)

state_file = "game_state.json"

# Carrega histórico de jogo (se existir)
if os.path.exists(state_file):
    with open(state_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if isinstance(data, dict) and "history" in data and isinstance(data["history"], list):
        game_state = data
    else:
        game_state = {"history": []}
else:
    game_state = {"history": []}

print("Bem-vindo ao jogo de RPG IA! (Digite 'sair' para encerrar)")

while True:
    user_input = input("Você: ")
    if user_input.strip().lower() == "sair":
        print("Encerrando o jogo.")
        break

    game_state["history"].append({"player": user_input, "mestre": ""})

    context = game_state["history"][-5:]
    prompt = ""
    for turn in context:
        if turn.get("player"):
            prompt += f"Jogador: {turn['player']}\n"
        if turn.get("mestre"):
            prompt += f"Mestre: {turn['mestre']}\n"
    prompt += "Mestre:"

    generated = generator(prompt, max_new_tokens=100, do_sample=True, top_k=50, top_p=0.95, temperature=0.7)
    result_text = generated[0]['generated_text']
    response = result_text[len(prompt):].strip()
    if response.lower().startswith("mestre:"):
        response = response[len("Mestre:"):].strip()

    print(f"Mestre: {response}")
    game_state["history"][-1]["mestre"] = response

    with open(state_file, 'w', encoding='utf-8') as f:
        json.dump(game_state, f, ensure_ascii=False, indent=2)
