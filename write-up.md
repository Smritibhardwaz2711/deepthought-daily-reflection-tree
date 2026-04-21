# DeepThought Daily Reflection Tree — Write-up

## Design Rationale

## Why I Chose These Questions

The core challenge of this assignment was not technical. It was psychological design.

An employee using this tool is likely tired, mentally overloaded, and low on patience. At that moment, abstract questions such as *“Do you have an internal locus of control?”* are useless. Reflection only works when the question feels human, immediate, and emotionally recognizable.

So I translated each psychological construct into natural evening prompts.

Examples:

- *“When you replay today in your head, what feeling arrives first?”* captures emotional residue faster than asking for a summary.
- *“What most influenced the better moments today?”* surfaces agency without jargon.
- *“When you think about today’s hardest moment, who appears first?”* reveals radius of concern through instinct, not theory.

The goal was to create questions that feel like a wise colleague speaking for two minutes, not a survey collecting responses.

---

## How I Designed the Branching

The reflection tree follows a deliberate three-axis sequence:

## 1. Agency (Victim ↔ Victor)

The first task is restoring proportion.

Many difficult days are experienced as something that happened *to* the employee. That is emotionally real, but incomplete. So the first branch helps the user notice where choice, effort, preparation, or response still existed.

This axis is first because people rarely think constructively about contribution or perspective while feeling powerless.

---

## 2. Contribution (Entitlement ↔ Contribution)

Once some agency is restored, the next question becomes:

**Did value move through me today, or did I mainly measure what I received?**

This axis surfaces hidden entitlement gently, without accusation. Wanting fairness is human. But dependence on recognition often drains motivation.

The branching therefore distinguishes between:

- contribution-led days  
- recognition-led days  
- mixed states

---

## 3. Radius (Self ↔ Others)

The final axis widens the frame.

Stress naturally narrows attention toward self-preservation. But meaning at work often returns when attention expands toward team, colleague, or customer.

This is why the final questions ask who comes to mind first, and what would make tomorrow meaningful.

The tool therefore ends not with productivity pressure, but perspective.

---

## Why the Sequence Matters

These are not three separate quizzes.

They are one psychological movement:

**Agency → Contribution → Perspective**

When people notice their choices, they become more able to contribute.  
When they contribute, concern naturally widens beyond self.

That progression is the real product.

---

## Why Deterministic Instead of LLM-Based

Reflection tools should be:

- predictable  
- repeatable  
- auditable  
- emotionally safe

LLM-generated coaching can be impressive, but inconsistent. It may moralize one day, flatter the next, or hallucinate advice.

A deterministic tree gives the same quality for the same answers every time.

The intelligence lives in the structure, not in improvisation.

---

## Trade-Offs I Made

I intentionally prioritized:

- clarity over excessive branching complexity  
- emotionally honest wording over academic precision  
- structured insight over open-ended journaling  
- maintainability over novelty

A larger tree with dozens more branches was possible, but would reduce readability and testing speed.

I chose a design another developer could inspect, extend, and trust.

---

## Psychological Sources Used

This design was informed by the following concepts:

- **Julian Rotter** — Locus of Control  
- **Carol Dweck** — Growth Mindset  
- **Campbell et al.** — Psychological Entitlement  
- **Dennis Organ** — Organizational Citizenship Behavior  
- **Abraham Maslow** — Self-Transcendence  
- **C. Daniel Batson** — Perspective Taking

These ideas were translated into fixed-choice prompts suitable for end-of-day reflection.

---

## What I Would Improve With More Time

Given more time, I would extend the system in five directions:

1. Multi-day pattern tracking (weekly drift toward victimhood, entitlement, or narrow focus)  
2. Personalized summaries using historical trends  
3. Team-level anonymous insights for managers  
4. Browser-based UI with better experience design  
5. Expanded branches for burnout, conflict, and recovery states

---

## Final Design Philosophy

Most people do not need more advice.

They need better mirrors.

This project aims to be a structured mirror: one that helps a tired employee end the day with more agency, more generosity, and a wider lens than they began with.