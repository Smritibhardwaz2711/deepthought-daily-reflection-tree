import json
import os

# ======================================
# Load Tree
# ======================================
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TREE_PATH = os.path.join(BASE_DIR, "tree", "reflection-tree.json")

with open(TREE_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

nodes = {node["id"]: node for node in data["nodes"]}
current = data["start"]

# ======================================
# State
# ======================================
state = {
    "signals": {},
    "answers": {},
    "question_count": 0
}

# ======================================
# Helpers
# ======================================
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input("\nPress Enter to continue...")

def add_signal(signal):
    if signal:
        state["signals"][signal] = state["signals"].get(signal, 0) + 1

def get_sig(name):
    return state["signals"].get(name, 0)

def print_header():
    print("=" * 60)
    print("         DEEPTHOUGHT DAILY REFLECTION AGENT")
    print("=" * 60)
    print("Deterministic • Structured • No Runtime AI")
    print("=" * 60)

def total_questions():
    return sum(1 for n in nodes.values() if n["type"] == "question")

def progress():
    done = state["question_count"]
    total = total_questions()
    filled = "█" * done
    empty = "░" * (total - done)
    print(f"\nProgress: [{filled}{empty}] {done}/{total}\n")

# ======================================
# Decision Engine
# ======================================
def run_decision(node_id):
    internal = get_sig("internal")
    external = get_sig("external")
    contribution = get_sig("contribution")
    entitlement = get_sig("entitlement")
    others = get_sig("others")
    self_focus = get_sig("self")

    if node_id == "D1":
        return "R1_INT" if internal >= external else "R1_EXT"

    elif node_id == "D2":
        return "R2_CONTRIB" if contribution >= entitlement else "R2_ENT"

    elif node_id == "D3":
        return "R3_OTH" if others >= self_focus else "R3_SELF"

    elif node_id == "D_SUMMARY":
        if internal >= external and contribution >= entitlement and others >= self_focus:
            return "SUMMARY_HIGH"
        elif internal < external and contribution < entitlement and others < self_focus:
            return "SUMMARY_LOW"
        else:
            return "SUMMARY_MIXED"

    return "END"

# ======================================
# UI Start
# ======================================
clear()
print_header()
pause()

# ======================================
# Main Loop
# ======================================
while True:
    node = nodes[current]
    ntype = node["type"]

    clear()
    print_header()

    # -------------------------
    # Question Node
    # -------------------------
    if ntype == "question":
        state["question_count"] += 1
        progress()

        print(node["text"] + "\n")

        for i, option in enumerate(node["options"], start=1):
            print(f"{i}. {option['label']}")

        while True:
            try:
                choice = int(input("\nChoose option number: "))
                if 1 <= choice <= len(node["options"]):
                    selected = node["options"][choice - 1]

                    state["answers"][current] = selected["label"]
                    add_signal(selected.get("signal"))

                    current = selected["next"]
                    break
                else:
                    print("Please choose a valid option.")
            except:
                print("Enter numbers only.")

    # -------------------------
    # Decision Node
    # -------------------------
    elif ntype == "decision":
        current = run_decision(current)

    # -------------------------
    # Reflection / Bridge / Start
    # -------------------------
    elif ntype in ["start", "reflection", "bridge"]:
        print(node["text"])
        pause()
        current = node["next"]

    # -------------------------
    # Summary Node
    # -------------------------
    elif ntype == "summary":
        print("\n" + "=" * 60)
        print("                 PERSONAL SUMMARY")
        print("=" * 60)
        print(node["text"])
        print("\nSignal Snapshot:")
        print(f"- Agency: {get_sig('internal')} | External Pressure: {get_sig('external')}")
        print(f"- Contribution: {get_sig('contribution')} | Entitlement: {get_sig('entitlement')}")
        print(f"- Others Focus: {get_sig('others')} | Self Focus: {get_sig('self')}")
        print("=" * 60)
        pause()
        current = node["next"]

    # -------------------------
    # End Node
    # -------------------------
    elif ntype == "end":
        print("\n" + "=" * 60)
        print("                SESSION COMPLETE")
        print("=" * 60)
        print(node["text"])
        print("=" * 60)
        break