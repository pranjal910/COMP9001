# 🗝️ Vault of Shadows

**Vault of Shadows** is a terminal-based escape room game where players choose three rooms to explore, each filled with logic puzzles and brain teasers. Solve the puzzles, collect the digits, and unlock the final vault—before you run out of lives!

---

## 🚀 How to Run the Game

### 1. Requirements

Ensure you have **Python 3** installed on your system. You also need to install the `pyfiglet` package for the ASCII art banner:

```bash
pip install pyfiglet
```

### 2. Clone or Download the Repository

If using Git:

```bash
git clone https://github.com/yourusername/vault-of-shadows.git
cd vault-of-shadows
```

Or just download and extract the ZIP file, then open a terminal inside the project folder.

### 3. Run the Game

From the project directory, run:

```bash
python main.py
```

---

## 🧩 Game Overview

- Choose **3 out of 5** rooms, each containing a unique puzzle.
- Solve riddles, ciphers, and logic challenges to earn vault code digits.
- Use the correct **3-digit code** to escape.
- You start with **3 lives**. Each wrong answer costs one life.
- Lose all lives and the vault remains sealed forever.

---

## 📁 Project Structure

```
vault_of_shadows/
├── main.py              # Entry point
├── game.py              # Game flow controller
├── player.py            # Player and life system
├── utils.py             # Color, printing, and ASCII banner
├── rooms/
│   ├── __init__.py
│   ├── base_room.py
│   ├── lion_room.py
│   ├── serpent_room.py
│   ├── mirror_room.py
│   ├── library_room.py
│   └── music_room.py
```

---

## 🎮 Tips

- Think carefully—some puzzles rely on logic, some on lateral thinking.
- Replay the game to try different rooms.
- Each session randomizes the digits to ensure variety.
