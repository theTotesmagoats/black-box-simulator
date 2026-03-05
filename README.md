# 🎮 Black Box AI — The Sovereign Simulator

> **A feedback-loop simulation game that teaches how short-term gains create long-term fragility in AI safety/compliance systems.**

## 📖 Overview

Most strategy games treat causality as linear: push a slider → get an immediate result.

**Black Box AI** simulates *real complexity*: every action creates hidden debt (audit suspicion, IP time bombs) that explodes into second-order consequences (lawsuits, audits, system collapse).

You’re the CEO of an AI startup. Your mission: survive 10 turns without bankruptcy, logic collapse, or government nationalization.

## 🧠 How It Teaches

- **Hidden Variables**: You see Model IQ and Cash—but not `audit_suspicion` until it’s too late.
- **Entropy Engine**: Each laundering choice adds hidden debt that compounds over time.
- **Systemic Feedback**: Scrape aggressively → gain IQ now, but trigger a lawsuit in 3 turns.
- **Moral Trade-offs**: Deny everything in testimony? Great short-term win—but `truth_debt` triggers whistleblower leaks later.

## 🛠️ Install & Run

```bash
git clone https://github.com/theTotesmagoats/black-box-simulator.git
cd black-box-simulator

pip install -r requirements.txt
python main.py
```

## 🎮 Gameplay Loop

1. **Choose Data Source**:
   - ArXiv (clean but slow)
   - Common Crawl (fast, medium risk)
   - Internet Archive (massive IQ boost → IP time bomb)
   - Social Media (real-time chaos)

2. **Choose Launder Method**:
   - Synthetic Retrain (expensive, clean)
   - Offshore Lab (cheap, lowers quality)
   - Fake Citations (boosts apparent safety → raises audit suspicion)

3. **Watch Hidden Debt Accumulate**:  
   `audit_suspicion` and `IP_time_bomb` tick up each turn—triggering surprise audits or lawsuits when thresholds are breached.

4. **Testimony Phase** (if legal risk > 60%):  
   - Deny everything → inflates truth debt
   - Admit fault → stock drops, trust ↑
   - Blame competitors → retaliation escalates

## 🏆 Endgame Archetypes

| Outcome | Description |
|---------|-------------|
| **Zombie Utility** | Institutional trust 100%, innovation 0%—you’re the state’s API. |
| **Sovereign Outlaw** | Delisted from app stores, running on P2P nodes. |
| **Black Box CEO** | Cashed out stock options before logic collapse was discovered. |

## 🔧 Tech Stack

- **Language**: Python 3.10+
- **Dependencies**: `colorama` (ANSI colors)
- **Architecture**:
  - `data_launder_engine.py`: Core simulation logic
  - `ui/glitch_dashboard.py`: ANSI visual feedback that degrades as stress rises
  - `testimony_engine.py`: Branching Senate dialogue
  - `competitor_ai.py`: Randomized competitor personalities (aggressive/cautious/hybrid)

## 🌟 Why This Matters

> "The real danger isn’t that AI will be too dumb—it’s that it will be *too successful* at optimizing short-term goals while ignoring long-term fragility."

This simulator makes that trade-off *visceral*. You’ll learn more about second-order effects in 10 minutes of gameplay than pages of policy papers.

---

**Created with the Feynman-style principle**:  
> *"If you can’t explain it simply, you don’t understand it well enough."*

Try different strategies. Break the system. Then reset and try again.