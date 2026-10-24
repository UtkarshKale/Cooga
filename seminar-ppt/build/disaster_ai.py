"""Seminar-I deck: AI in Disaster Management (Vedika Dandade, B344) — redesigned."""
import sys

from design import *  # noqa: F401,F403

TEMPLATE, ICONS, OUT = sys.argv[1:4]
P = DISASTER
d = Deck(TEMPLATE, ICONS, P, "AI in Disaster Management  ·  Vedika Dandade (B344)")
INK, PRI, ACC, MUT, TXT = P["ink"], P["primary"], P["accent"], P["muted"], P["text"]
DMG = [("No damage", GOOD), ("Minor", AMBER), ("Major", "F2994A"), ("Destroyed", BAD)]


def motif(deck, s):
    """Alert ripples radiating from an event point."""
    cx, cy = 8.05, 3.6
    for k, r in enumerate((0.45, 0.9, 1.35, 1.8)):
        box(s, cx - r, cy - r, 2 * r, 2 * r, shape="oval", line=P["on_dark"], lw=1.25, line_alpha=70 - k * 15)
    box(s, cx - 0.3, cy - 0.3, 0.6, 0.6, bg=ACC, shape="oval", alpha=30)
    box(s, cx - 0.16, cy - 0.16, 0.32, 0.32, bg=ACC, shape="oval")
    for x, y, r in ((8.05 + 0.9, 3.6, .16), (8.05 - 0.95, 3.6 - 0.95, .2), (8.05 + 0.6, 3.6 + 1.25, .14),
                    (8.05 - 1.5, 3.6 + 1.0, .12)):
        box(s, x - r / 2, y - r / 2, r, r, bg=PRI, shape="oval")


# 1. Cover
s = d.cover("Seminar-I  ·  2025–26", "AI in Disaster Management", None, motif,
            info=[("Presented by", "Vedika Dandade", "Roll No. B344  ·  Third Year, Semester V"),
                  ("Under the guidance of", "Name of Faculty", "Designation of faculty")], title_size=40)
notes(s, "Good morning. My seminar topic is AI in Disaster Management: how artificial intelligence helps predict "
         "disasters, assess damage, extract critical information and plan the response.")

# 2. Agenda
s = d.agenda(["Introduction", "Objectives", "Literature review", "Literature survey", "Baseline papers",
              "System architecture", "Algorithms studied", "Features & trade-offs", "Applications",
              "Analysis & comparison", "Conclusion & future scope", "References"])
notes(s, "This is the flow of the presentation, following the seminar template.")

# 3. Introduction
s = d.content("01  ·  Introduction", "Disasters move fast; data now moves faster")
blocks = [("house", "Background", INK,
           "Floods, cyclones, earthquakes, wildfires and landslides cause loss of life, infrastructure damage "
           "and economic setbacks."),
          ("clock", "Problem", BAD,
           "Traditional management relies on manual surveys and delayed reports, which slows decisions."),
          ("lightbulb", "Inspiration", ACC,
           "Satellites, IoT sensors and social media give real-time data; AI turns it into early, actionable "
           "insight [1].")]
for i, (ic, head, col, body) in enumerate(blocks):
    y = 1.7 + i * 1.7
    d.icon_circle(s, ic, 0.6, y + 0.05, 0.55, bg=col)
    text(s, 1.35, y, 3.4, 0.4, head, size=17, bold=True, font=HEAD, color=col)
    text(s, 1.35, y + 0.42, 3.4, 1.1, body, size=13.5, color=TXT)
    if i < 2:
        line(s, 0.6, y + 1.58, 4.75, y + 1.58, P["line"], 0.75)
box(s, 5.05, 1.6, 4.35, 5.2, bg=P["card"], radius=0.14)
text(s, 5.05, 1.75, 4.35, 0.3, "DISASTER MANAGEMENT CYCLE", size=10, bold=True, color=PRI, align="c", spc=160)
cx, cy = 7.225, 4.3
box(s, cx - 0.6, cy - 0.6, 1.2, 1.2, bg=P["soft"], shape="oval",
    paras=[[("AI", {"bold": True, "size": 24, "font": HEAD})], "support"], size=11, color=PRI)
phases = [((cx, cy - 1.75), "Mitigation", "risk mapping", INK),
          ((cx + 1.35, cy), "Preparedness", "early warning", PRI),
          ((cx, cy + 1.75), "Response", "damage & info extraction", ACC),
          ((cx - 1.35, cy), "Recovery", "planning & reports", GOOD)]
for (nx, ny), t, sub, col in phases:
    box(s, nx - 0.78, ny - 0.42, 1.56, 0.84, bg=col, paras=[[(t, {"bold": True, "size": 13.5})], sub],
        size=10.5, color=WHITE)
for (x1, y1, x2, y2) in ((cx + 0.78, cy - 1.6, cx + 1.2, cy - 0.42), (cx + 1.2, cy + 0.42, cx + 0.78, cy + 1.6),
                         (cx - 0.78, cy + 1.6, cx - 1.2, cy + 0.42), (cx - 1.2, cy - 0.42, cx - 0.78, cy - 1.6)):
    arrow(s, x1, y1, x2, y2, MUT, 1.75)
notes(s, "Disasters such as floods, cyclones and earthquakes cause huge losses every year. Traditional management "
         "depends on manual surveys and delayed information. Today we have satellite and drone imagery, IoT sensors "
         "and social media giving data in real time, and AI can process it quickly. The diagram shows the disaster "
         "management cycle - mitigation, preparedness, response and recovery - and AI supports every phase.")

# 4. Objectives
s = d.content("02  ·  Objectives", "What this seminar sets out to do")
d.numbered_rows(s, [
    ("Disaster lifecycle", "Understand the role of AI in mitigation, preparedness, response and recovery.", "sync"),
    ("AI techniques", "Study ML, deep learning, computer vision, NLP and spatio-temporal analysis.", "brain"),
    ("Applications", "Explore flood prediction, wildfire detection, damage assessment and crisis information.", "water"),
    ("System design", "Analyse an end-to-end AI-based disaster management pipeline.", "sitemap"),
    ("Challenges", "Identify issues in data, generalization, interpretability and fairness.", "balance"),
])
notes(s, "My objectives are to understand where AI fits in each phase of disaster management, study the main AI "
         "techniques, explore real applications, analyse a complete system pipeline, and discuss challenges and "
         "future directions.")

# 5. Literature review
s = d.content("03  ·  Literature review", "Four research threads link AI to disasters")
d.subtitle(s, "Peer-reviewed reviews and surveys from 2024–2026, grouped by theme.")
cards = [("book", "Reviews & frameworks", "[1] [2]",
          "Map AI methods to every disaster phase (96 studies in [1]); stress trustworthy, explainable deployment [2]."),
         ("layers", "Hazard-specific deep learning", "[3] [4] [5]",
          "CNNs, LSTMs and AIoT for floods, earthquakes and wildfires: prediction, detection, damage assessment."),
         ("comment", "Large language models", "[6]",
          "LLMs across disaster phases: classifying crisis messages, extracting information, generating reports."),
         ("eye", "Vision-language agents", "[7]",
          "DisasTeller: four specialised agents turn post-disaster imagery into assessments, alerts and plans.")]
for i, (ic, t, r, b) in enumerate(cards):
    d.theme_card(s, 0.6 + (i % 2) * 4.5, 1.85 + (i // 2) * 2.05, 4.3, 1.9, ic, t, r, b, alt=i in (1, 2), size=14)
d.insight(s, 6.05, "Common finding", "AI helps most when several data sources are fused and its outputs are "
          "trustworthy enough for responders to act on.")
notes(s, "I grouped the literature into four themes. Systematic reviews give the overall map - the Muthukumar review "
         "alone synthesises 96 studies. Hazard-specific papers cover floods, earthquakes and wildfires. The ACL survey "
         "covers large language models, and the Nature Communications paper presents DisasTeller, a multi-agent "
         "vision-language system for damage assessment and reporting.")

# 6-7. Literature survey tables
lit = [
    ("A systematic review of AI frameworks for holistic disaster management",
     "S. Muthukumar et al. · Discover Artificial Intelligence, 2026",
     "Synthesises 96 peer-reviewed studies; maps AI approaches to each disaster-management phase."),
    ("A systematic review of trustworthy AI applications in natural disasters",
     "Computers & Electrical Engineering, 2024",
     "Reviews AI for prediction, risk assessment, early warning and evacuation, focusing on trustworthy deployment."),
    ("Deep AI applications for natural disaster management systems: a methodological review",
     "Akhyar et al. · Ecological Indicators, 2024",
     "Reviews deep-learning applications for forest fires, earthquakes and floods."),
    ("AI for flood risk management: a comprehensive state-of-the-art review", "Int. J. Disaster Risk Reduction, 2025",
     "Reviews ML/DL models, input data and applications in flood-risk management."),
    ("Survey of AI-Enabled IoT for Wildfire Prediction, Detection, and Post-Operations", "IEEE Access, 2026",
     "AIoT for wildfire prediction, real-time detection, damage assessment and recovery."),
    ("Harnessing Large Language Models for Disaster Management: A Survey", "Z. Lei et al. · Findings of ACL, 2025",
     "Taxonomy of LLM uses across disaster phases; datasets, use cases and open challenges."),
    ("Integration of large vision language models for post-disaster damage assessment and reporting",
     "Z. Chen et al. · Nature Communications, 2026",
     "DisasTeller: four vision-language agents for assessment, alerts, emergency reports, resource allocation and "
     "recovery planning."),
]
for part, chunk in enumerate((lit[:4], lit[4:])):
    s = d.content("04  ·  Literature survey", f"Literature survey in tabular form ({part + 1}/2)")
    start = 1 if part == 0 else 5
    d.lit_table(s, [(f"{i:02d}", t, v, w) for i, (t, v, w) in enumerate(chunk, start)], row_h=1.12)
    notes(s, "This table summarises each paper and what it reports. " +
          ("The first four are broad reviews and hazard-specific reviews for floods, fires and earthquakes."
           if part == 0 else
           "These cover AIoT for wildfires, large language models, and the DisasTeller vision-language system."))

# 8. Baseline papers
s = d.content("05  ·  Baseline papers", "Three papers anchor this seminar")
d.baseline(s, ("PRIMARY BASELINE", "[1]", "A systematic review of AI frameworks for holistic disaster management",
               "Discover Artificial Intelligence, 2026",
               "Most comprehensive recent review — 96 studies across all disaster phases.",
               "Overall structure (phases × AI techniques) and the system pipeline."),
           [("SUPPORTING", "[6]", "Harnessing Large Language Models for Disaster Management: A Survey",
             "Findings of ACL, 2025", "broad survey of LLMs in disaster management.",
             "the NLP / LLM information-extraction module."),
            ("SUPPORTING", "[7]", "Integration of large vision language models … (DisasTeller)",
             "Nature Communications, 2026", "a working multi-agent vision-language system.",
             "damage assessment and automated reporting.")])
notes(s, "My primary baseline is the systematic review by Muthukumar et al., because it covers all phases and AI "
         "approaches. The ACL survey supports the language-model part, and the DisasTeller paper shows how "
         "vision-language agents can automate damage assessment and reporting. Reviews 2 to 5 were then used for "
         "early-warning, flood and wildfire details.")

# 9. System architecture
s = d.content("06  ·  System architecture", "From raw signals to decisions in four stages")
d.subtitle(s, "End-to-end AI pipeline for disaster management, with a human-validated feedback loop [1]")
cols = [("Data sources", INK, P["ic_i"], [("satellite", "Satellite / UAV imagery"), ("sensor", "IoT sensors: rain, river, seismic"),
                                         ("comment", "Social media & news"), ("db", "Government & historical data")]),
        ("AI processing", PRI, P["ic_p"], [("cogs", "Cleaning & data fusion"), ("brain", "ML / DL: CNN, LSTM, ViT"),
                                           ("comment", "NLP / LLM: BERT, NER"), ("route", "Optimization / RL")]),
        ("Decisions", ACC, P["ic_a"], [("chart", "Risk prediction"), ("house", "Damage assessment"),
                                              ("search", "Information extraction"), ("truck", "Resource allocation")]),
        ("Outputs", GOOD, "g", [("bell", "Early warnings & alerts"), ("map", "Damage maps"), ("route", "Evacuation routes"),
                                ("file", "Situation reports")])]
for k, (head, col, ic_key, items) in enumerate(cols):
    x = 0.6 + k * 2.27
    w = 2.0
    box(s, x, 1.85, w, 4.0, bg=P["card"], radius=0.12)
    box(s, x + 0.15, 2.0, 0.36, 0.36, bg=col, shape="oval", paras=str(k + 1), size=12, bold=True, color=WHITE, margin=0)
    text(s, x + 0.6, 1.98, w - 0.65, 0.4, head, size=13.5, bold=True, color=col, anchor="m", font=HEAD)
    for i, (ic, t) in enumerate(items):
        y = 2.55 + i * 0.8
        box(s, x + 0.12, y, w - 0.24, 0.68, bg=WHITE, line=P["line"], lw=0.75, radius=0.08)
        d.icon(s, ic, x + 0.22, y + 0.18, 0.32, ic_key)
        text(s, x + 0.62, y, w - 0.8, 0.68, t, size=11.5, color=TXT, anchor="m")
    if k < 3:
        box(s, x + w + 0.045, 3.7, 0.18, 0.3, bg=P["line"], shape="chevron")
path(s, [(8.41, 5.85), (8.41, 6.45), (1.6, 6.45), (1.6, 5.85)], ACC, 1.75, dash=True)
box(s, 3.25, 6.29, 3.5, 0.32, bg=WHITE, line=ACC, radius=0.16,
    paras="feedback & continuous learning  ·  human validation", size=10.5, bold=True, color=ACC, margin=0.02)
notes(s, "This is the overall system. Data comes from satellites and drones, IoT sensors, social media and government "
         "databases. The AI layer cleans and fuses it, then applies deep learning, NLP and optimization models. The "
         "decision-support layer predicts risk, assesses damage, extracts information and allocates resources. Outputs "
         "are warnings, damage maps, evacuation routes and reports. A feedback loop with human validation keeps "
         "improving the models.")

# 10. Algorithm 1 — early warning
s = d.content("07  ·  Algorithms studied", "Early warning: learning from time-series data")
d.subtitle(s, "Algorithm 1 — LSTM / Transformer flood forecasting from historical and live signals [4], [8]")
box(s, 0.6, 1.95, 1.45, 0.78, bg=P["soft"], paras=[[("Historical", {"bold": True, "color": INK})], "rainfall, river level"],
    size=10.5, color=MUT)
box(s, 0.6, 2.9, 1.45, 0.78, bg=P["soft"], paras=[[("Real-time IoT", {"bold": True, "color": INK})], "sensors, weather"],
    size=10.5, color=MUT)
box(s, 2.3, 2.37, 1.35, 0.88, bg=WHITE, line=P["line"], lw=1.25, paras=[[("Preprocess", {"bold": True, "color": INK})],
                                                                     "normalize, windows"], size=10.5, color=MUT)
box(s, 3.9, 2.2, 1.4, 1.22, bg=INK, paras=[[("LSTM /", {"bold": True, "size": 14})], [("Transformer", {"bold": True, "size": 14})],
                                           "sequence model"], size=10.5, color=WHITE)
box(s, 5.55, 2.37, 1.35, 0.88, bg=WHITE, line=P["line"], lw=1.25, paras=[[("Flood risk ŷ", {"bold": True, "color": INK})],
                                                                      "next 6–24 h"], size=10.5, color=MUT)
box(s, 7.1, 2.26, 1.15, 1.1, bg=AMBER, shape="diamond", paras="ŷ > τ ?", size=13, bold=True, color=INK)
box(s, 8.45, 2.37, 0.95, 0.88, bg=ACC, paras=[[("Issue", {"bold": True})], [("alert", {"bold": True})]], size=13,
    color=WHITE)
arrow(s, 2.05, 2.34, 2.3, 2.62, MUT, 1.5)
arrow(s, 2.05, 3.29, 2.3, 3.0, MUT, 1.5)
for x1, x2 in ((3.65, 3.9), (5.3, 5.55), (6.9, 7.1), (8.25, 8.45)):
    arrow(s, x1, 2.81, x2, 2.81, MUT, 1.75)
text(s, 8.2, 2.45, 0.4, 0.25, "yes", size=9.5, color=MUT)
box(s, 0.6, 4.0, 4.3, 2.8, bg=P["card"], radius=0.12)
text(s, 0.82, 4.15, 3.9, 0.3, "WHY LSTM?", size=10, bold=True, color=PRI, spc=160)
text(s, 0.82, 4.55, 3.95, 2.2, [
    "Gated memory cells keep long-term patterns, e.g. days of rainfall [8]",
    "Forget, input and output gates decide what to keep",
    "Robust to noisy, irregular sensor sequences",
    "Transformers use attention for long-range links"], size=13.5, color=TXT, bullet="•", bullet_color=ACC,
     after=7)
d.code(s, 5.1, 4.0, 4.3, 2.8, [
    "Input: series X_t, threshold τ",
    "X ← Normalize(X_t); make windows",
    "h_t ← LSTM(X, h_(t-1))",
    "ŷ_(t+1) ← Predict(h_t)   # risk",
    "if ŷ_(t+1) > τ then",
    "    IssueAlert(region, ŷ_(t+1))",
    "return ŷ_(t+1), alert"], size=11.5)
notes(s, "For early warning, the model takes historical and real-time readings such as rainfall and river level. After "
         "normalisation the data is split into time windows and fed to an LSTM or Transformer. The LSTM's gates let it "
         "remember long-term patterns like several days of rain. It predicts the flood risk for the next hours; if the "
         "prediction crosses a threshold tau, an alert is issued for that region.")

# 11. Algorithm 2 — damage assessment
s = d.content("07  ·  Algorithms studied", "Damage assessment: comparing before and after")
d.subtitle(s, "Algorithm 2 — CNN / ViT segmentation of satellite and UAV imagery [3], [7]")
for k, (lab, key) in enumerate((("Pre-disaster image", P["ic_p"]), ("Post-disaster image", "r"))):
    y = 1.9 + k * 1.0
    box(s, 0.6, y, 1.6, 0.88, bg=P["soft"], radius=0.1)
    d.icon(s, "house", 0.72, y + 0.2, 0.48, key)
    text(s, 1.27, y, 0.9, 0.88, lab, size=10.5, color=INK, anchor="m", bold=True)
box(s, 2.45, 2.3, 1.35, 1.05, bg=WHITE, line=P["line"], lw=1.25,
    paras=[[("Align &", {"bold": True, "color": INK})], [("preprocess", {"bold": True, "color": INK})], "co-registration"],
    size=10.5, color=MUT)
box(s, 4.05, 2.2, 1.45, 1.25, bg=INK, paras=[[("CNN / ViT", {"bold": True, "size": 14})], "semantic segmentation"],
    size=10.5, color=WHITE)
arrow(s, 2.2, 2.34, 2.45, 2.65, MUT, 1.5)
arrow(s, 2.2, 3.34, 2.45, 3.0, MUT, 1.5)
arrow(s, 3.8, 2.82, 4.05, 2.82, MUT, 1.75)
arrow(s, 5.5, 2.82, 5.78, 2.82, MUT, 1.75)
grid = ["00012", "01123", "01233", "00122", "00011"]
for r, row in enumerate(grid):
    for c, v in enumerate(row):
        box(s, 5.8 + c * 0.29, 1.9 + r * 0.29, 0.27, 0.27, bg=DMG[int(v)][1], shape="rect")
text(s, 5.8, 3.38, 1.43, 0.28, "Damage map", size=11, bold=True, color=INK, align="c")
for i, (lab, col) in enumerate(DMG):
    box(s, 7.6, 2.0 + i * 0.36, 0.22, 0.22, bg=col, shape="rect")
    text(s, 7.92, 1.95 + i * 0.36, 1.5, 0.32, lab, size=11.5, color=TXT, anchor="m")
box(s, 0.6, 4.0, 4.3, 2.8, bg=P["card"], radius=0.12)
text(s, 0.82, 4.15, 3.9, 0.3, "STEPS", size=10, bold=True, color=PRI, spc=160)
steps = ["Input pre- and post-event images", "Align and normalise both images",
         "CNN/ViT labels each pixel or building", "Generate the damage map", "Overlay on GIS maps for responders"]
for i, st in enumerate(steps):
    y = 4.5 + i * 0.45
    box(s, 0.82, y + 0.05, 0.3, 0.3, bg=PRI, shape="oval", paras=str(i + 1), size=10.5, bold=True, color=WHITE, margin=0)
    text(s, 1.25, y, 3.55, 0.4, st, size=13, color=TXT, anchor="m")
box(s, 5.1, 4.0, 4.3, 2.8, bg=INK, radius=0.12)
text(s, 5.32, 4.15, 3.9, 0.3, "EXTENSION · DISASTELLER [7]", size=10, bold=True, color=ACC, spc=160)
text(s, 5.32, 4.48, 3.9, 0.55, "Four specialised vision-language agents collaborate on post-disaster images.",
     size=12.5, color=WHITE)
for i in range(4):
    d.icon_circle(s, "robot", 5.42 + i * 0.98, 5.1, 0.5, bg=PRI if i % 2 == 0 else ACC)
for i, o in enumerate(["Damage assessment", "Alerts", "Emergency reports", "Resource & recovery plans"]):
    x = 5.32 + (i % 2) * 2.0
    y = 5.75 + (i // 2) * 0.48
    box(s, x, y, 1.9, 0.4, bg=P["dark_line"], radius=0.2, paras=o, size=10.5, color=WHITE, margin=0.02)
notes(s, "For damage assessment, the system takes satellite or drone images from before and after the event. After "
         "aligning them, a CNN or Vision Transformer performs semantic segmentation and labels each building or "
         "region: no damage, minor, major or destroyed. The result is a damage map overlaid on GIS for responders. "
         "DisasTeller extends this with four vision-language agents that also produce alerts, emergency reports and "
         "resource and recovery plans.")

# 12. Algorithm 3 — NLP extraction & RL evacuation
s = d.content("07  ·  Algorithms studied", "From crisis messages and roads to action")
d.subtitle(s, "Algorithm 3 — NLP information extraction [6] and reinforcement-learning evacuation routing")
text(s, 0.6, 1.88, 6, 0.3, "CRISIS INFORMATION EXTRACTION", size=10, bold=True, color=PRI, spc=160)
for k, msg in enumerate(("“Road blocked near the bridge, need rescue!”", "“Help needed in Wardha, water rising”")):
    box(s, 0.6, 2.28 + k * 0.78, 2.7, 0.66, bg=P["soft"], radius=0.18, paras=[[(msg, {"italic": True})]], size=11.5,
        color=INK, align="l", margin=0.14)
box(s, 3.6, 2.42, 1.55, 1.0, bg=INK, paras=[[("NLP model", {"bold": True, "size": 13.5})], "BERT / LLM + NER"],
    size=10.5, color=WHITE)
arrow(s, 3.3, 2.61, 3.6, 2.78, MUT, 1.5)
arrow(s, 3.3, 3.39, 3.6, 3.1, MUT, 1.5)
arrow(s, 5.15, 2.92, 5.45, 2.92, MUT, 1.75)
for i, (k_, v) in enumerate((("Location", "Wardha"), ("Event", "Flood"), ("Need", "Rescue"), ("Severity", "High"))):
    y = 2.25 + i * 0.36
    box(s, 5.45, y, 3.95, 0.32, bg=P["card"] if i % 2 == 0 else WHITE, shape="rect")
    text(s, 5.6, y, 1.4, 0.32, k_, size=11.5, bold=True, color=MUT, anchor="m")
    text(s, 7.05, y, 2.2, 0.32, v, size=12, bold=True, color=BAD if k_ == "Severity" else INK, anchor="m")
line(s, 0.6, 3.85, 9.4, 3.85, P["line"], 0.75)
text(s, 0.6, 4.0, 6, 0.3, "EVACUATION ROUTING  ·  REINFORCEMENT LEARNING", size=10, bold=True, color=PRI, spc=160)
box(s, 0.6, 4.75, 1.85, 1.2, bg=ACC, paras=[[("Agent", {"bold": True, "size": 15})], "policy π", "PPO / DQN"],
    size=11, color=WHITE)
box(s, 3.2, 4.75, 1.85, 1.2, bg=PRI, paras=[[("Environment", {"bold": True, "size": 15})], "road network,",
                                            "hazard map"], size=11, color=WHITE)
path(s, [(1.525, 4.75), (1.525, 4.5), (4.125, 4.5), (4.125, 4.75)], INK, 1.5)
text(s, 1.6, 4.27, 2.45, 0.22, "action: choose next road", size=10.5, color=INK, align="c")
path(s, [(4.125, 5.95), (4.125, 6.2), (1.525, 6.2), (1.525, 5.95)], GOOD, 1.5)
text(s, 0.6, 6.27, 4.45, 0.5, [[("state  ", {"bold": True}), ("location, congestion, hazard", {})],
                               [("reward  ", {"bold": True}), ("+ safety, − travel time", {})]], size=10.5, color=GOOD,
     align="c", after=0)
d.code(s, 5.45, 4.4, 3.95, 2.4, [
    "Input: road graph G, hazard map H",
    "s ← (loc, congestion, hazard)",
    "a ← π(s)            # next road",
    "r ← R(safety, time)",
    "update π with PPO / DQN",
    "return safest route"], size=11)
notes(s, "During a disaster people post messages like these. An NLP model such as BERT or an LLM with named entity "
         "recognition extracts structured fields - location, event, need and severity - so responders can prioritise. "
         "For evacuation, reinforcement learning treats routing as a sequential decision problem: the agent observes "
         "the state - location, congestion and hazard - chooses the next road, and gets a reward for safety and speed. "
         "Algorithms like PPO or DQN learn the best evacuation policy.")

# 13. Features / advantages / disadvantages
s = d.content("08  ·  Features, advantages & disadvantages", "Faster and wider, but only as good as its data")
d.three_columns(s, [
    ("Features", PRI, "star", [("Data fusion", "satellite, sensor and text data"), ("Real-time", "continuous monitoring"),
                               ("Prediction", "forecasts risk in advance"), ("Auto mapping", "damage maps from imagery"),
                               ("Decision support", "routes, resources, reports")]),
    ("Advantages", GOOD, "check", [("Earlier warnings", "more lead time to evacuate"),
                                   ("Faster assessment", "quicker than ground surveys"),
                                   ("Better allocation", "relief reaches need first"),
                                   ("Wide coverage", "large or unreachable areas"),
                                   ("Scalable", "works 24×7 at scale")]),
    ("Disadvantages", BAD, "warn", [("Data scarcity", "rare events, imbalanced data"),
                                    ("Generalization", "may fail in new regions"),
                                    ("Black box", "low trust without explanation [2]"),
                                    ("Infrastructure", "power / network may fail"),
                                    ("Misinformation", "false posts; privacy risks")]),
])
notes(s, "Key features are data fusion, real-time monitoring, prediction, automatic mapping and decision support. "
         "Advantages include more lead time, faster assessment and better use of resources. But there are real "
         "limitations: data on rare disasters is scarce, models may not transfer to new regions, black-box outputs "
         "reduce trust, infrastructure can fail during the disaster itself, and social media contains misinformation.")

# 14. Applications
s = d.content("09  ·  Applications", "AI across hazards and response tasks")
d.app_grid(s, [
    ("water", "Flood forecasting", "River-level and rainfall prediction for early warnings [4]."),
    ("fire", "Wildfire detection", "AIoT sensors and cameras detect fires early [5]."),
    ("quake", "Earthquake damage", "Satellite / UAV imagery maps collapsed buildings [3]."),
    ("cyclone", "Cyclone tracking", "Forecasting track and intensity to plan evacuations."),
    ("comment", "Crisis informatics", "LLMs classify social-media posts and help requests [6]."),
    ("truck", "Relief logistics", "Optimised routing of supplies, shelters and rescue teams."),
])
notes(s, "Applications include flood forecasting, wildfire detection with AI-enabled IoT, earthquake damage mapping, "
         "cyclone tracking, crisis informatics using language models, and relief logistics.")

# 15. Analysis / comparison
s = d.content("10  ·  Analysis & comparison", "AI shortens every step from signal to action")
rows = [["Aspect", "Traditional approach", "AI-based approach", "Benefit"],
        ["Early warning", "Manual monitoring, fixed thresholds", "ML/DL forecasts on live sensor data", "More lead time"],
        ["Damage assessment", "Ground surveys (days)", "Satellite/UAV + CNN/ViT maps (hours)", "Faster response"],
        ["Information", "Phone calls, manual reports", "NLP/LLM triage of social media", "Situational awareness"],
        ["Resource allocation", "Static, pre-planned routes", "Optimization / RL adapts live", "Efficient use"],
        ["Reporting", "Manual situation reports", "Automated reports, e.g. [7]", "Quick, consistent"]]
d.comparison_table(s, rows, [1.85, 2.35, 2.6, 2.0], y=1.7, row_h=0.66, hl_col=2)
d.insight(s, 5.95, "Key insight", "AI supports — it does not replace — human decision-makers; outputs must be "
          "explainable and trusted before authorities act on them [2].", h=0.85)
notes(s, "Comparing traditional and AI-based approaches: AI gives earlier warnings, maps damage in hours instead of "
         "days, triages social media automatically, adapts routes as conditions change and generates reports quickly. "
         "But AI should support human decision-makers, and its outputs must be explainable and trusted.")

# 16. Conclusion
s = d.conclusion("AI strengthens the whole disaster cycle", [
    "AI supports every phase of the disaster-management cycle.",
    "Time-series models warn early; CNN/ViT models map damage quickly.",
    "NLP/LLMs turn crisis messages into structured, actionable data.",
    "Optimization and RL improve evacuation and relief logistics."],
    ["Multimodal models fusing satellite, sensor and text data",
     "Explainable, trustworthy AI for critical decisions [2]",
     "Edge AI that keeps working when networks fail",
     "Collaboration of government, research and industry"],
    "Earlier detection, faster assessment, smarter response — with humans in the loop")
notes(s, "To conclude, AI can strengthen early detection, damage assessment, information extraction and resource "
         "allocation. Future work should focus on multimodal models, explainability, edge deployment and close "
         "collaboration with disaster-management authorities.")

# 17. References (IEEE format)
refs = [
    "S. Muthukumar et al., “A systematic review of artificial intelligence frameworks for holistic disaster "
    "management,” Discover Artificial Intelligence, vol. 6, Art. no. 308, 2026, doi: 10.1007/s44163-026-01020-w.",
    "“A systematic review of trustworthy artificial intelligence applications in natural disasters,” Computers & "
    "Electrical Engineering, vol. 118, pt. B, Art. no. 109409, 2024, doi: 10.1016/j.compeleceng.2024.109409.",
    "Akhyar et al., “Deep artificial intelligence applications for natural disaster management systems: A "
    "methodological review,” Ecological Indicators, vol. 163, Art. no. 112067, 2024, doi: 10.1016/j.ecolind.2024.112067.",
    "“Artificial intelligence for flood risk management: A comprehensive state-of-the-art review and future "
    "directions,” Int. J. Disaster Risk Reduction, vol. 117, Art. no. 105110, 2025, doi: 10.1016/j.ijdrr.2024.105110.",
    "“Survey of AI-Enabled IoT for Wildfire Prediction, Detection, and Post-Operations,” IEEE Access, vol. 14, "
    "pp. 9819–9837, 2026, doi: 10.1109/ACCESS.2026.3654863.",
    "Z. Lei et al., “Harnessing Large Language Models for Disaster Management: A Survey,” in Findings of the "
    "Association for Computational Linguistics: ACL 2025, 2025, pp. 14528–14551.",
    "Z. Chen et al., “Integration of large vision language models for efficient post-disaster damage assessment "
    "and reporting,” Nature Communications, 2026. [Online]. Available: https://www.nature.com/articles/s41467-025-68216-z",
    "S. Hochreiter and J. Schmidhuber, “Long Short-Term Memory,” Neural Computation, vol. 9, no. 8, "
    "pp. 1735–1780, 1997.",
]
s = d.references("References", refs, 1, size=13)
notes(s, "References in IEEE format; numbers in square brackets on the slides point to this list.")

# 18. Closing
s = d.closing(motif, "Vedika Dandade  ·  Roll No. B344")
notes(s, "Thank you. I am happy to take questions.")

d.save(OUT)
print("saved", OUT, len(d.prs.slides))
