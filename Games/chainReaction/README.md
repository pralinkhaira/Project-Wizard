# 🎮 Chain Reaction

A beautiful, polished recreation of the classic Chain Reaction strategy game with stunning 3D orbs, smooth animations, and exciting chain reaction effects!

---

## 📖 Table of Contents
- [What is Chain Reaction?](#what-is-chain-reaction)
- [Quick Start](#quick-start)
- [How to Play](#how-to-play)
- [Game Rules](#game-rules)
- [Strategy Tips](#strategy-tips)
- [Features](#features)
- [Controls](#controls)
- [Installation](#installation)
- [Technical Details](#technical-details)

---

## 🎯 What is Chain Reaction?

Chain Reaction is a strategic multiplayer game where players compete to dominate a grid by placing orbs that explode in chain reactions. The last player remaining wins!

**Perfect for:**
- 2-8 players local multiplayer
- Quick 5-10 minute matches
- Strategic thinking and planning
- Exciting reversals and comebacks

---

## ⚡ Quick Start

```bash
# 1. Install dependencies
pip install pygame numpy

# 2. Generate game assets (one-time setup)
python generate_assets.py

# 3. Play!
python game.py
```

---

## 🎲 How to Play

### Game Objective
**Be the last player with orbs on the board!**

### Your Turn
1. **Click on any empty cell** to place your first orb
2. **Click on your own cells** to add more orbs
3. **Watch the chain reactions** as cells explode!

### What Happens When Cells Explode?

When a cell reaches its **critical mass**, it explodes:
- The orbs spread to **neighboring cells** (up, down, left, right)
- **Enemy cells are captured** and turn into your color
- This can trigger **more explosions** → Chain Reaction! 💥

---

## 📋 Game Rules

### Critical Mass by Position

Each cell has a different critical mass based on its position:

| Position | Critical Mass | Neighbors |
|----------|---------------|-----------|
| **Corner** (4 cells) | 2 orbs | 2 neighbors |
| **Edge** (24 cells) | 3 orbs | 3 neighbors |
| **Center** (48 cells) | 4 orbs | 4 neighbors |

### Turn Sequence

1. **Click a cell** to place an orb
2. If the cell reaches critical mass → **Explosion!**
3. Orbs spread to neighbors (which may also explode)
4. Chain reactions continue until all cells are stable
5. Next player's turn

### Winning Condition

After the first round (when everyone has played once):
- If only **one player has orbs remaining** → That player wins! 🏆
- Game continues until a winner is determined

### Important Rules

✅ **You can only click:**
- Empty cells (no owner)
- Your own cells (your color)

❌ **You cannot click:**
- Enemy cells (different color)

⚠️ **During explosions:**
- You must wait for all chain reactions to complete
- Cannot place orbs while explosions are happening

---

## 💡 Strategy Tips

### Early Game (First Round)
- **Spread out** across the board
- Try to claim **corner cells** - they explode faster!
- Don't stack too many orbs in one place yet

### Mid Game
- **Build up critical cells** (one orb away from exploding)
- **Control key areas** - corners and edges are powerful
- Watch for opponent weak spots

### Late Game
- **Trigger chain reactions** into enemy territory
- **Protect your strongholds** with extra orbs
- One good chain reaction can reverse the entire game!

### Pro Tips
🔥 **Corners are powerful** - Only need 2 orbs to explode  
⚡ **Chain reactions win games** - Set up cascading explosions  
👀 **Pulsating cells** are about to explode - use this to your advantage!  
🛡️ **Defensive play** - Sometimes it's better to reinforce than attack  
🎯 **Timing matters** - Wait for the right moment to strike  

---

## ✨ Features

### Visual Effects
- 🎨 **Beautiful 3D orbs** with glow effects and highlights
- 💥 **Particle explosions** with radial bursts
- 📳 **Screen shake** on explosions
- ⚡ **Pulsating critical cells** - Warning before explosion
- 🖱️ **Hover highlights** - See valid cells before clicking
- 📊 **Dominance meter** - Visual bar showing player control

### Audio
- 🔊 **Place sound** - Satisfying pop when placing orbs
- 💣 **Explosion sound** - Bass-heavy boom for explosions
- 🎺 **Victory fanfare** - Musical celebration when you win
- 🎵 **Background music** - Ambient 30-second loop

### Animations
- ✨ **Smooth orb placement** - Grow animation (0.25s)
- 🏃 **Smooth orb travel** - Eased movement between cells
- ⏱️ **Explosion delays** - 0.15s between explosions for visibility
- 🎭 **Easing functions** - Natural acceleration/deceleration

### Gameplay
- 👥 **2-8 players** - Local multiplayer
- 🎯 **Smart turn system** - Skips eliminated players
- 🔄 **Endless replayability** - Return to menu after each game

---

## 🎮 Controls

| Action | Control |
|--------|---------|
| Place orb | **Left Click** on cell |
| Navigate menu | **Left Click** on buttons |
| See valid cells | **Hover** with mouse |
| Quit game | **Close window** (X button) |

---

## 🚀 Installation

### Requirements
- **Python 3.7+**
- **pip** (Python package manager)

### Step-by-Step Setup

#### 1. Install Python Dependencies
```bash
pip install pygame numpy
```

#### 2. Generate Game Assets
This creates sound effects and downloads the custom font:
```bash
python generate_assets.py
```

**What this generates:**
- `assets/place.wav` - Orb placement sound
- `assets/explode.wav` - Explosion sound effect
- `assets/win.wav` - Victory fanfare
- `assets/music.wav` - Background music
- `assets/GameFont.ttf` - Orbitron font

#### 3. Run the Game
```bash
python game.py
```

### Troubleshooting

**Problem: "pygame could not be imported"**
```bash
pip install --upgrade pygame
```

**Problem: "numpy could not be imported"**
```bash
pip install --upgrade numpy
```

**Problem: No sound playing**
- Re-run `python generate_assets.py`
- Check that `assets/` folder exists with `.wav` files

**Problem: Font looks wrong**
- Game uses system Arial font as fallback
- Custom font is optional - game will still work!

---

## ⚙️ Technical Details

### Game Configuration
```
Grid: 8 columns × 10 rows
Cell Size: 75 × 75 pixels
Screen Resolution: 600 × 860 pixels
Frame Rate: 60 FPS
```

### Animation Parameters
```
Orb Placement: 0.25 seconds (ease-in-out)
Orb Travel: 0.3 seconds (smoothstep)
Explosion Delay: 0.15 seconds
Pulsate Speed: 0.05
```

### Visual Design
```
Orb Radius: 16 pixels
Glow Layers: 3 layers
Particle Count: 15 per explosion
Shake Intensity: 4 pixels
```

### File Structure
```
chainReaction/
├── game.py              ← Main game file (run this!)
├── generate_assets.py   ← Asset generator script
├── README.md            ← This file
└── assets/              ← Generated assets folder
    ├── GameFont.ttf     ← Orbitron font
    ├── place.wav        ← Placement sound
    ├── explode.wav      ← Explosion sound
    ├── win.wav          ← Victory sound
    └── music.wav        ← Background music
```

---

## 🎨 About the Assets

### Sounds (Procedurally Generated!)
All sound effects are mathematically generated using NumPy:
- **Sine waves** for tones
- **ADSR envelopes** for realistic attack/decay
- **Noise** for explosion texture
- **Musical notes** for victory (C-E-G-C arpeggio)

### Font
**Orbitron** by Matt McInerney from Google Fonts
- Futuristic, geometric design
- Perfect for sci-fi/gaming aesthetic
- Falls back to Arial if unavailable

---

## 🏆 Credits

- **Game Design**: Based on the classic Chain Reaction game
- **Implementation**: Python + Pygame
- **Visual Effects**: Custom particle system & animations
- **Sound Design**: Procedurally generated with NumPy
- **Font**: Orbitron by Matt McInerney (Google Fonts)

---

## 📜 License

This is a fan project created for educational and entertainment purposes. Feel free to modify, share, and enjoy!

---

## 🎉 Enjoy the Game!

**May your chain reactions be ever explosive!** 💥✨

Start your first game with 2-4 players to learn the mechanics, then challenge yourself with more players for chaotic fun!

Good luck, and remember: **One good chain reaction can change everything!** 🔥
