# 🎲 BingoEngine

> **A lightweight, modular Python game engine designed for building games with a strong emphasis on code reusability, clean architecture, and developer experience.**

---

## 📖 About

**BingoEngine** is an experimental game engine built entirely in **Python**, focused on creating  games while promoting modular development and reusable components.

Unlike traditional game engines that target graphics and rendering, BingoEngine focuses on building a scalable gameplay framework where multiple games can share common systems such as:

The project serves as both a personal learning journey and an exploration of software architecture through game development.

---
# 📂 Project Structure

```text
BingoEngine/
│
├── Engine/
│   ├── GameEngine.py
│   └── ...
│
├── DiceGAME/
│   ├── DICEBATTLE.py
│   ├── DB_ACTION.py
│   ├── DB_SCOREBRD.py
│   └── ...
│
├── RPSGAME/
│
├── docs/
│
├── main.py
└── README.md
```

---

# 🎮 Current Games

| Game                   | Status            |
| ---------------------- | ----------------- |
| 🎲 DiceBattle          | ✅ Available       |
| ✂️ Rock Paper Scissors | 🚧 In Development |
| 🔢 Guess The Number    | 📅 Planned        |
| ⭕ Tic Tac Toe          | 📅 Planned        |

---

# Design Philosophy

BingoEngine follows one simple principle:

> **Build games that improve the engine, and build an engine that improves future games.**

Instead of writing every game from scratch, common systems are gradually extracted into reusable modules that can be shared across multiple projects.

Each new game helps identify repeated logic, allowing the engine to evolve naturally over time.

---

# 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/<your-username>/BingoEngine.git
```

Navigate into the project:

```bash
cd BingoEngine
```

Launch the engine:

```bash
python main.py
```

# 🎯 Goals

* Learn software architecture through practical development.
* Build reusable systems instead of isolated projects.
* Create a collection of games powered by a common engine.
* Continuously improve code quality with each iteration.

---

# 🤝 Contributing

Suggestions, ideas, bug reports, and improvements are always welcome.

Feel free to open an issue or submit a pull request.

---

# License

This project is currently under active development.

A formal license will be added before the first stable release.
