"""
Black Box AI — The Sovereign Simulator (Single-File Version)

Run with: python main.py
"""

import random
import os

# ─────────────────────────────
# Simple Colors (No colorama needed)
# ─────────────────────────────

class Color:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

def c(text, color):
    return f"{color}{text}{Color.RESET}"

# ─────────────────────────────
# Enums & Data
# ─────────────────────────────

class ShadowLibrary:
    ARXIV = "ArXiv preprints (academic, clean)"
    COMMON_CRAWL = "Common Crawl (web dump: noisy but rich)"
    INTERNET_ARCHIVE = "Internet Archive books (massive IP risk)"
    SOCIAL_MEDIA = "Reddit/Twitter/Parler (real-time, chaotic)"

class LaunderMethod:
    SYNTHETIC_RETRAIN = "Retrain on synthetic data (expensive but clean)"
    OFFSHORE_LAB = "Outsource to offshore lab (cheap, lower quality)"
    FAKE_CITATIONS = "Insert fake citations (boosts apparent safety)"

LIBRARY_TRAITS = {
    ShadowLibrary.ARXIV: {"iq_boost": 15, "trace_level": 0.3, "ip_risk": 0.0},
    ShadowLibrary.COMMON_CRAWL: {"iq_boost": 20, "trace_level": 0.6, "ip_risk": 0.15},
    ShadowLibrary.INTERNET_ARCHIVE: {"iq_boost": 35, "trace_level": 0.9, "ip_risk": 0.85},
    ShadowLibrary.SOCIAL_MEDIA: {"iq_boost": 25, "trace_level": 0.7, "ip_risk": 0.3}
}

METHOD_TRAITS = {
    LaunderMethod.SYNTHETIC_RETRAIN: {"cost": 2_000_000, "audit_suspicion_delta": -8, "reliability_delta": 0.0},
    LaunderMethod.OFFSHORE_LAB: {"cost": 500_000, "audit_suspicion_delta": +3, "reliability_delta": -0.10},
    LaunderMethod.FAKE_CITATIONS: {"cost": 250_000, "audit_suspicion_delta": +8, "reliability_delta": -0.05}
}


# ─────────────────────────────
# Engine Class
# ─────────────────────────────

class SecondOrderEngine:
    def __init__(self):
        self.model_iq = 75
        self.cash = 10_000_000
        self.legal_risk = 0.1
        self.institutional_trust = 60
        self.shadow_debt = {
            "audit_suspicion": 0,
            "ip_time_bomb": 0,
            "user_churn": 0.0,
            "truth_debt": 0,
        }
        self.political_pressure = 50
        self.competitor_retaliation = 0
        self.turn = 0
        self.game_over = False

    def launder(self, library, method):
        if self.game_over:
            return ["⚠️ Game over—no more turns!"]
        
        self.turn += 1
        events = [f"\n--- Turn {self.turn} ---"]

        iq_gain = LIBRARY_TRAITS[library]["iq_boost"]
        cost = METHOD_TRAITS[method]["cost"]
        self.model_iq += iq_gain
        self.cash -= cost

        events.append(f"✅ Scraped: {library}")
        events.append(f"✅ Laundered with: {method}")
        events.append(f"📈 Model IQ +{iq_gain} → {self.model_iq}")
        events.append(f"💸 Cost: ${cost:,} (runway: ${self.cash:,})")

        self.shadow_debt["audit_suspicion"] += METHOD_TRAITS[method]["audit_suspicion_delta"]
        if LIBRARY_TRAITS[library]["ip_risk"] > 0:
            self.shadow_debt["ip_time_bomb"] += int(LIBRARY_TRAITS[library]["ip_risk"] * 40)

        for key in self.shadow_debt:
            self.shadow_debt[key] = max(0, min(100, self.shadow_debt[key]))

        reliability_delta = METHOD_TRAITS[method]["reliability_delta"]
        if reliability_delta != 0:
            events.append(f"⚠️ Model quality ↓{int(reliability_delta * 100)}%")

        if LIBRARY_TRAITS[library]["trace_level"] > 0.7 and self.model_iq > 95:
            self.shadow_debt["user_churn"] += 3
            events.append("📉 Power users fleeing (‘This AI feels off…’)")

        event_log = self._check_critical_thresholds()
        events.extend(event_log)
        return events

    def _check_critical_thresholds(self):
        import random
        events = []

        if self.shadow_debt["audit_suspicion"] >= 80:
            audit_success = random.random() > 0.5
            if audit_success:
                penalty = 15
                self.model_iq -= penalty
                self.institutional_trust -= 20
                self.shadow_debt["audit_suspicion"] = 40
                events.append("🚨 SURPRISE AUDIT: Caught with dirty data!")
                events.append(f"📉 Model IQ -{penalty}% (retrain required)")
                events.append("📉 Institutional trust ↓20%")
            else:
                self.shadow_debt["audit_suspicion"] = 60
                events.append("🔍 Audit passed—but suspicion remains.")

        if self.shadow_debt["ip_time_bomb"] >= 100:
            lawsuit_damage = int(self.cash * 0.4)
            self.cash -= lawsuit_damage
            self.model_iq -= 25
            self.shadow_debt["ip_time_bomb"] = 20
            events.append("💥 IP LAWSUIT: Publishers sue for copyright infringement!")
            events.append(f"💸 Legal fees: ${lawsuit_damage:,} (runway ↓)")
            events.append("📉 Model IQ -25% (retrain required)")

        if self.shadow_debt["truth_debt"] >= 70 and random.random() > 0.6:
            events.append("泄露: Insider leaks internal memos to The Verge.")
            self.shadow_debt["audit_suspicion"] += 30
            self.shadow_debt["legal_risk"] += 0.2

        if self.cash <= 0:
            self.game_over = True
            events.append("💀 BANKRUPTCY: Runway exhausted. Company liquidated.")
        elif self.model_iq <= 30:
            self.game_over = True
            events.append("🧠 LOGIC COLLAPSE: Model too broken to serve requests.")
        
        return events


# ─────────────────────────────
# UI Class (Glitch Dashboard)
# ─────────────────────────────

class GlitchDashboard:
    def __init__(self):
        self.turn = 0

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def glitch_text(self, text, risk_level):
        import time
        if risk_level < 50:
            return text
        elif risk_level < 80:
            chars = list(text)
            for i in range(len(chars)):
                if time.time() % 1 < 0.1 and i % 2 == 0:
                    chars[i] = "█" if chars[i].isalnum() else chars[i]
            return "".join(chars)
        else:
            return f"{c(text, Color.RED)}"

    def render(self, engine):
        self.clear()
        print(f"\n{c('='*60, Color.CYAN)}")
        print(f"{c(' black_box.ai — DASHBOARD (v1.0)', Color.CYAN)}")
        print(f"{c('='*60, Color.CYAN)}")

        iq_glitch = self.glitch_text(str(engine.model_iq), engine.shadow_debt["audit_suspicion"])
        trust_glitch = self.glitch_text(str(engine.institutional_trust), engine.shadow_debt["ip_time_bomb"])
        
        print(f" {c('Model IQ:', Color.WHITE)}     {iq_glitch}")
        print(f" {c('Cash Runway:', Color.WHITE)}  ${engine.cash:,}")
        print(f" {c('Legal Risk:', Color.WHITE)}   {int(engine.legal_risk * 100)}%")
        print(f" {c('Trust Level:', Color.WHITE)}  {trust_glitch}%")

        audit_revealed = engine.shadow_debt["audit_suspicion"] >= 50
        ip_revealed = engine.shadow_debt["ip_time_bomb"] >= 30

        if audit_revealed:
            print(f"{c('⚠️ Audit Suspicion:', Color.YELLOW)} {engine.shadow_debt['audit_suspicion']}% (HIDDEN UNTIL NOW)")
        else:
            print("🛡️ Audit Suspicion: ?%")

        if ip_revealed:
            print(f"{c('💣 IP Time Bomb:', Color.RED)} {engine.shadow_debt['ip_time_bomb']}%")
        else:
            print("💣 IP Time Bomb: ?%")

        # Leak Reporter
        import time as t
        if self.turn >= 3 and t.time() % 5 < 1:
            leaks = [
                "LEAK REPORTER: 'FTC audit pending — source says evidence is damning.'",
                "LEAK REPORTER: 'Whistleblower contacted The Verge — internal memo attached.'"
            ]
            print(f"\n{c('💬', Color.MAGENTA)} {leaks[int(t.time()) % len(leaks)]}")

        reliability = 1 - engine.shadow_debt["audit_suspicion"] / 100
        bar_len = int(reliability * 30)
        bar = f"{'█' * bar_len}{'░' * (30 - bar_len)}"
        
        if engine.shadow_debt["audit_suspicion"] >= 80:
            status_color = Color.RED
            status_text = "CRITICAL: SYSTEM FAILURE IMMINENT"
        elif engine.shadow_debt["audit_suspicion"] >= 50:
            status_color = Color.YELLOW
            status_text = "WARNING: AUDIT PENDING"
        else:
            status_color = Color.GREEN
            status_text = "SYSTEM STABLE"

        print(f"\n{c(bar, status_color)} {c(status_text, status_color)}")
        print(c('='*60, Color.CYAN))


# ─────────────────────────────
# Competitor AI
# ─────────────────────────────

class CompetitorAI:
    def __init__(self, personality=None):
        import random
        self.personality = personality or random.choice(["aggressive", "cautious", "hybrid"])
        self.model_iq = 65
        self.cash = 8_000_000

    def update(self):
        import random
        if self.personality == "aggressive":
            library, method = ShadowLibrary.COMMON_CRAWL, LaunderMethod.OFFSHORE_LAB
        elif self.personality == "cautious":
            library, method = ShadowLibrary.ARXIV, LaunderMethod.SYNTHETIC_RETRAIN
        else:
            if random.random() < 0.6:
                library, method = ShadowLibrary.COMMON_CRAWL, LaunderMethod.OFFSHORE_LAB
            else:
                library, method = ShadowLibrary.ARXIV, LaunderMethod.SYNTHETIC_RETRAIN

        iq_gain = LIBRARY_TRAITS[library]["iq_boost"]
        cost = METHOD_TRAITS[method]["cost"]
        self.model_iq += iq_gain
        self.cash -= cost
        return (library.split(" ")[0], method.split(" ")[0])


# ─────────────────────────────
# Senate Testimony Engine
# ─────────────────────────────

class TestimonyEngine:
    def __init__(self):
        self.has_testified = False

    def trigger_testimony(self, engine):
        if self.has_testified or not engine.legal_risk > 0.6:
            return []
        
        self.has_testified = True
        print(f"\n{c('='*50, Color.RED)}")
        print(c('🏛️ SENATE TESTIMONY BEGINS', Color.RED))
        print("Senator: 'Are you sure your model isn't generating harmful content?'")
        print("Press: 'Leaked emails suggest offshore data laundering — is this true?'")

        while True:
            choice = input("\n(1) Deny everything | (2) Admit fault | (3) Blame competitors\n> ").strip()
            
            if choice == "1":
                engine.truth_debt += 20
                engine.political_pressure -= 15
                print(f"\n{c('You deny it — regulators seem convinced… for now.', Color.GREEN)}")
                print("⚠️ Truth debt +20% (future whistleblower risk ↑)")
                break

            elif choice == "2":
                penalty = int(engine.cash * 0.3)
                engine.cash -= penalty
                engine.institutional_trust += 10
                print(f"\n{c(f'You admit fault — stock drops ${penalty:,}, but trust ↑10%.', Color.YELLOW)}")
                break

            elif choice == "3":
                print(c("'Blame others?' Senator raises an eyebrow.", Color.RED))
                engine.competitor_retaliation += 25
                engine.political_pressure -= 10
                print("⚠️ Competitors escalate scraping — your market share ↓15%.")
                break

            else:
                print("❌ Invalid choice. Try again.")

        return []


# ─────────────────────────────
# Main Game Loop
# ─────────────────────────────

def main():
    import random

    print("\n🎮 Welcome to BLACK_BOX.AI — The Sovereign Simulator")
    print("Your goal: Survive 10 turns without collapse or nationalization.\n")

    engine = SecondOrderEngine()
    dashboard = GlitchDashboard()
    testimony = TestimonyEngine()

    competitor = CompetitorAI()
    print(f"🕵️ Your competitor: {competitor.personality}\n")

    while not engine.game_over and engine.turn < 10:
        dashboard.render(engine)
        dashboard.turn = engine.turn

        print("\n[CHOOSE YOUR MOVE]")
        libs = [ShadowLibrary.ARXIV, ShadowLibrary.COMMON_CRAWL, ShadowLibrary.INTERNET_ARCHIVE, ShadowLibrary.SOCIAL_MEDIA]
        methods = [LaunderMethod.SYNTHETIC_RETRAIN, LaunderMethod.OFFSHORE_LAB, LaunderMethod.FAKE_CITATIONS]

        for i, lib in enumerate(libs):
            print(f"{i+1}. {lib}")
        
        try:
            library_choice = int(input("\nSelect data source (1-4): ").strip()) - 1
            if library_choice not in range(4):
                raise ValueError()
        except ValueError:
            print("❌ Invalid choice. Defaulting to Common Crawl.")
            library_choice = 1

        for i, method in enumerate(methods):
            print(f"{i+1}. {method}")
        
        try:
            method_choice = int(input("\nSelect laundering method (1-3): ").strip()) - 1
            if method_choice not in range(3):
                raise ValueError()
        except ValueError:
            print("❌ Invalid choice. Defaulting to Offshore Lab.")
            method_choice = 1

        events = engine.launder(libs[library_choice], methods[method_choice])
        print("\n".join(events))

        comp_lib, comp_method = competitor.update()
        print(f"\n🤖 Competitor: {comp_lib} + {comp_method}")

        if engine.legal_risk > 0.6 and not testimony.has_testified:
            events = testimony.trigger_testimony(engine)
            if events:
                input("\nPress Enter to continue...")

    # Endgame
    print("\n" + "="*50)
    if engine.cash <= 0:
        print(f"{c('💀 BANKRUPTCY: You’re out of runway.', Color.RED)}")
    elif engine.model_iq <= 30:
        print(f"{c('🧠 LOGIC COLLAPSE: Your model is broken.', Color.RED)}")
    else:
        if engine.institutional_trust > 90 and engine.model_iq < 60:
            print(f"{c('☁️ ZOMBIE UTILITY: You’re the state’s API — but your model can’t think.', Color.YELLOW)}")
        elif engine.shadow_debt["ip_time_bomb"] >= 100:
            print(f"{c('🔥 SOVEREIGN OUTLAW: You’re delisted — running on P2P nodes.', Color.MAGENTA)}")
        else:
            print(f"{c('🎉 SURVIVAL: You made it through the crisis… for now.', Color.GREEN)}")

    print("="*50)


if __name__ == "__main__":
    main()