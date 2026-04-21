# DeepThought Daily Reflection Tree Diagram

```mermaid
flowchart TD

START([Start Reflection]) --> Q1

%% =========================
%% AXIS 1
%% =========================
subgraph AXIS1[Axis 1 — Agency | Victim ↔ Victor]

Q1[Feeling First] --> Q2H[Better Moments Source]
Q1 --> Q2L[Hard Moments Response]

Q2H --> Q3A[Choices Matter?]
Q2L --> Q3B[Smallest Point of Choice]

Q3A --> D1{Internal ≥ External?}
Q3B --> D1

D1 -->|Yes| R1I[Agency Reflection]
D1 -->|No| R1E[External Reflection]

end

R1I --> B1[Shift: What moved through you?]
R1E --> B1

%% =========================
%% AXIS 2
%% =========================
subgraph AXIS2[Axis 2 — Contribution | Entitlement ↔ Contribution]

B1 --> Q4[Today's Contribution Moment]
Q4 --> Q5[What Mattered Most?]
Q5 --> Q6[Hardest Truth to Remember]

Q6 --> D2{Contribution ≥ Entitlement?}

D2 -->|Yes| R2C[Contribution Reflection]
D2 -->|No| R2E[Recognition Reflection]

end

R2C --> B2[Shift: Move from me to us]
R2E --> B2

%% =========================
%% AXIS 3
%% =========================
subgraph AXIS3[Axis 3 — Radius | Self ↔ Others]

B2 --> Q7[Who Appears First?]
Q7 --> Q8[Meaningful Tomorrow]
Q8 --> Q9[Wiser Sentence]

Q9 --> D3{Others ≥ Self?}

D3 -->|Yes| R3O[Widened Perspective]
D3 -->|No| R3S[Narrowed Focus]

end

R3O --> DS{Overall Pattern?}
R3S --> DS

%% =========================
%% DYNAMIC SUMMARY
%% =========================
DS -->|Agency + Contribution + Perspective| SH[High Growth Summary]
DS -->|Pressure + Expectation + Narrow Focus| SL[Low Awareness Summary]
DS -->|Mixed Signals| SM[Balanced Human Summary]

SH --> END([End Session])
SL --> END
SM --> END