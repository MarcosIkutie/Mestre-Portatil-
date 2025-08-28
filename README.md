# Portable RPG Master

A local, text-based AI Dungeon Master for solo or small-group D&D 5e adventures. This tool uses a locally-run language model to generate coherent, persistent narratives based on player actions.

## Overview

This project is a Python application that provides a text-based interface for playing D&D solo. It acts as an AI Dungeon Master, generating descriptions, managing non-player characters (NPCs), and adhering to D&D 5e rules for combat and challenges.

## Key Features

- **Dynamic Narrative:** Generates detailed scenes based on player input (exploration, dialogue, combat).
- **Campaign Consistency:** Maintains a persistent game state (characters, locations, items) using a JSON-based memory system, optionally enhanced with a vector database for long-term context recall.
- **D&D 5e Ruleset:** Calculates enemy stats, difficulty checks, and combat outcomes based on standard D&D 5e rules.
- **Solo/Co-op Play:** Designed for one player or duos, reacting to all player choices in real-time.

## Technical Architecture

- **Core Language:** Python
- **Language Model:** Hugging Face Transformers library (e.g., LLaMA 2, GPT-NeoX)
- **State Management:** JSON file for game state
- **Optional - Long-Term Memory:** FAISS or ChromaDB for vector-based memory retrieval (RAG)

## Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/seu-usuario/mestre-de-rpg-portatil.git
    cd mestre-de-rpg-portatil
    ```

2.  **Set up a Python virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # Linux/MacOS
    # .venv\Scripts\activate  # Windows
    pip install -r requirements.txt
    ```

3.  **Download the Language Model:**
    - If a `download_model.sh` script is provided, run it.
    - Otherwise, download a suitable model (e.g., "facebook/llama-2-7b") and configure the path in `config.json`.

## Basic Usage

1.  **Run the game:**
    ```bash
    python run_game.py
    ```

2.  **Follow on-screen instructions** to create a character or choose a pre-made one.

3.  **Describe your character's actions** in text. The AI DM will respond with narrative descriptions and continue the story.

4.  Your game state is automatically saved to `game_state.json`.

## Example Code Snippet

```python
# Simplified example of prompting the AI model
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("facebook/llama-2-7b")
model = AutoModelForCausalLM.from_pretrained("facebook/llama-2-7b")

context = load_json_context()  # Loads previous memory and descriptions
prompt = context + "\n\nNPC: What does the adventurer do?"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=200)
print(tokenizer.decode(outputs[0]))







Contributing
Contributions are welcome. Feel free to suggest rule improvements, add more adventure data for training, or optimize memory management. Please open issues or pull requests on GitHub.

License
This work is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License.

You are free to:

Share: Copy and redistribute the material in any medium or format.

Adapt: Remix, transform, and build upon the material.

Under the following terms:

Attribution: You must give appropriate credit, provide a link to the license, and indicate if changes were made.

NonCommercial: You may not use the material for commercial purposes without explicit, formal authorization.

ShareAlike: If you remix, transform, or build upon the material, you must distribute your contributions under the same license as the original.

Any use, implementation, or monetization without formal authorization is subject to retroactive compensation.




