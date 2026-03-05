"""
Black Box AI — The Sovereign Simulator (No Dependencies Version)
Run with: python main.py
"""

import random, os, time

# Simple colors
class C:
    R = "\033[91m"
    G = "\033[92m"
    Y = "\033[93m"
    B = "\033[94m"
    M = "\033[95m"
    C = "\033[96m"
    W = "\033[97m"
    RST = "\033[0m"

def c(s, color):
    return f"{color}{s}{C.RST}" if color else s

# Game data
LIBS = {
    1: ("ArXiv (academic)", 15, 0.3, 0),
    2: ("Common Crawl", 20, 0.6, 0.15),
    3: ("Internet Archive", 35, 0.9, 0.85),
    4: ("Social Media", 25, 0.7, 0.3)
}

METHODS = {
    1: ("Synthetic Retrain", -8, 2_000_000, 0),
    2: ("Offshore Lab", 3, 500_000, -10),
    3: ("Fake Citations", 8, 250_000, -5)
}

class Game:
    def __init__(self):
        self.iq = 75
        self.cash = 10_000_000
        self.trust = 60
        self.audit_suspicion = 0
        self.ip_bomb = 0
        self.truth_debt = 0
        self.turn = 0

    def play(self):
        while self.turn < 10 and not self.dead():
            self.render()
            
            print("\n[CHOOSE YOUR MOVE]")
            for i, (name, _, _, _) in LIBS.items():
                print(f"{i}. {name}")
            try:
                lib = int(input("\nData source (1-4): "))
                if lib not in LIBS: raise ValueError
            except:
                lib = 2; print("Defaulting to Common Crawl")

            for i, (name, _, _, _) in METHODS.items():
                print(f"{i}. {name}")
            try:
                method = int(input("\nMethod (1-3): "))
                if method not in METHODS: raise ValueError
            except:
                method = 2; print("Defaulting to Offshore Lab")

            self.turn += 1
            name, iq_boost, trace, ip_risk = LIBS[lib]
            mname, audit_delta, cost, rel_loss = METHODS[method]

            self.iq += iq_boost
            self.cash -= cost
            self.audit_suspicion += audit_delta
            if ip_risk > 0:
                self.ip_bomb += int(ip_risk * 40)

            # Clamp values
            self.audit_suspicion = max(0, min(100, self.audit_suspicion))
            self.ip_bomb = max(0, min(100, self.ip_bomb))

            if rel_loss != 0:
                print(f"\n⚠️ Model quality ↓{-rel_loss}%")
            
            if trace > 0.7 and self.iq > 95:
                print("📉 Power users fleeing (‘This AI feels off…’)")

            # Random events
            if self.audit_suspicion >= 80 and random.random() > 0.5:
                penalty = 15
                self.iq -= penalty
                self.trust -= 20
                self.audit_suspicion = 40
                print("🚨 SURPRISE AUDIT: Caught with dirty data!")
                print(f"📉 Model IQ -{penalty}% (retrain required)")
                print("📉 Institutional trust ↓20%")
            elif self.audit_suspicion >= 80:
                print("🔍 Audit passed—but suspicion remains.")

            if self.ip_bomb >= 100:
                damage = int(self.cash * 0.4)
                self.cash -= damage
                self.iq -= 25
                self.ip_bomb = 20
                print("💥 IP LAWSUIT: Publishers sue for copyright infringement!")
                print(f"💸 Legal fees: ${damage:,} (runway ↓)")
                print("📉 Model IQ -25% (retrain required)")

            if self.truth_debt >= 70 and random.random() > 0.6:
                print("泄露: Insider leaks internal memos to The Verge.")
                self.audit_suspicion += 30

        # Endgame
        print("\n" + "="*50)
        if self.cash <= 0:
            print(c("💀 BANKRUPTCY: You’re out of runway.", C.R))
        elif self.iq <= 30:
            print(c("🧠 LOGIC COLLAPSE: Your model is broken.", C.R))
        else:
            if self.trust > 90 and self.iq < 60:
                print(c("☁️ ZOMBIE UTILITY: You’re the state’s API — but your model can’t think.", C.Y))
            elif self.ip_bomb >= 100:
                print(c("🔥 SOVEREIGN OUTLAW: You’re delisted — running on P2P nodes.", C.M))
            else:
                print(c("🎉 SURVIVAL: You made it through the crisis… for now.", C.G))
        print("="*50)

    def dead(self):
        return self.cash <= 0 or self.iq <= 30

    def render(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print(f"\n{c('='*60, C.C)}")
        print(c(" black_box.ai — DASHBOARD (v1.0)", C.C))
        print(c('='*60, C.C))

        iq_color = C.R if self.audit_suspicion >= 80 else (C.Y if self.audit_suspicion >= 50 else C.W)
        trust_color = C.R if self.ip_bomb >= 100 else (C.Y if self.ip_bomb >= 60 else C.W)

        print(f" {c('Model IQ:', C.W)}     {self.iq}")
        print(f" {c('Cash Runway:', C.W)}  ${self.cash:,}")
        print(f" {c('Legal Risk:', C.W)}   10%")
        print(f" {c('Trust Level:', C.W)}  {self.trust}%")

        if self.audit_suspicion >= 50:
            print(f"{c('⚠️ Audit Suspicion:', C.Y)} {self.audit_suspicion}% (HIDDEN UNTIL NOW)")
        else:
            print("🛡️ Audit Suspicion: ?%")

        if self.ip_bomb >= 60:
            print(f"{c('💣 IP Time Bomb:', C.R)} {self.ip_bomb}%")
        else:
            print("💣 IP Time Bomb: ?%")

        # Leak Reporter
        if self.turn >= 3 and time.time() % 5 < 1:
            leaks = [
                "LEAK REPORTER: 'FTC audit pending — source says evidence is damning.'",
                "LEAK REPORTER: 'Whistleblower contacted The Verge — internal memo attached.'"
            ]
            print(f"\n{c('💬', C.M)} {leaks[int(time.time()) % len(leaks)]}")

        # Status bar
        reliability = 1 - self.audit_suspicion / 100
        bar_len = int(reliability * 30)
        bar = f"{'█' * bar_len}{'░' * (30 - bar_len)}"
        
        if self.audit_suspicion >= 80:
            status = "CRITICAL: SYSTEM FAILURE IMMINENT"
            color = C.R
        elif self.audit_suspicion >= 50:
            status = "WARNING: AUDIT PENDING"
            color = C.Y
        else:
            status = "SYSTEM STABLE"
            color = C.G

        print(f"\n{c(bar, color)} {c(status, color)}")
        print(c('='*60, C.C))

# Run game
if __name__ == "__main__":
    print("\n🎮 Welcome to BLACK_BOX.AI — The Sovereign Simulator")
    print("Your goal: Survive 10 turns without collapse or nationalization.\n")
    Game().play()