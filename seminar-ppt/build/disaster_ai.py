"""Seminar-I deck: AI in Disaster Management (Vedika Dandade, B344)."""
import sys

from common import *  # noqa: F401,F403

TEMPLATE, ICONS, OUT = sys.argv[1:4]
d = Deck(TEMPLATE, ICONS)
ACC = ORANGE

# 1. Title
s = title_slide(d, ["AI in Disaster Management"], "Vedika Dandade",
                "Roll No.: B344  |  Third Year (Semester V)", title_size=30)
notes(s, "Good morning. My seminar topic is AI in Disaster Management: how artificial intelligence helps "
         "predict disasters, assess damage, extract critical information and plan the response.")

# 2. Index
s = index_slide(d, ["Introduction", "Objectives", "Literature Review", "Literature Survey (Tabular Form)",
                    "Baseline Papers Selected", "System Architecture / Algorithms Studied",
                    "Features / Advantages / Disadvantages", "Applications", "Analysis / Comparison",
                    "Conclusion & Future Scope", "References"])
notes(s, "This is the flow of the presentation, following the seminar template.")

# 3. Introduction
s = d.content_slide("Introduction")
blocks = [("house", "Background", NAVY,
           "Floods, cyclones, earthquakes, wildfires and landslides cause loss of life, damage to "
           "infrastructure and economic setbacks."),
          ("clock", "Problem", RED,
           "Traditional disaster management relies on manual surveys and delayed reports, which slows "
           "decisions."),
          ("lightbulb", "Inspiration", ACC,
           "Satellites, IoT sensors and social media now give real-time data; AI turns it into early, "
           "actionable insight [1].")]
for i, (ic, head, col, body) in enumerate(blocks):
    y = 1.35 + i * 1.8
    box(s, 0.4, y, 4.55, 1.62, fill=PALE)
    d.icon_circle(s, ic, 0.55, y + 0.17, 0.55, fill=col)
    text(s, 1.25, y + 0.17, 3.5, 0.55, head, size=17, bold=True, color=col, anchor="m")
    text(s, 0.55, y + 0.8, 4.3, 0.8, body, size=14)
text(s, 5.15, 1.25, 4.5, 0.4, "Disaster management cycle", size=16, bold=True, color=NAVY, align="c")
cx, cy = 7.4, 4.15
box(s, cx - 0.62, cy - 0.62, 1.24, 1.24, fill=ACC, shape="oval",
    paras=[[("AI", {"bold": True, "size": 22})], "support"], size=12, color=WHITE)
phases = [((cx, cy - 1.75), "Mitigation", "risk mapping", NAVY),
          ((cx + 1.45, cy), "Preparedness", "early warning", BLUE),
          ((cx, cy + 1.75), "Response", "damage & info extraction", RED),
          ((cx - 1.45, cy), "Recovery", "planning & reports", GREEN)]
for (nx, ny), t, sub, col in phases:
    box(s, nx - 0.8, ny - 0.45, 1.6, 0.9, fill=col, paras=[[(t, {"bold": True, "size": 14})], sub],
        size=11, color=WHITE)
for (x1, y1, x2, y2) in ((cx + 0.8, cy - 1.6, cx + 1.3, cy - 0.45), (cx + 1.3, cy + 0.45, cx + 0.8, cy + 1.6),
                         (cx - 0.8, cy + 1.6, cx - 1.3, cy + 0.45), (cx - 1.3, cy - 0.45, cx - 0.8, cy - 1.6)):
    arrow(s, x1, y1, x2, y2, MUTED, 2)
notes(s, "Disasters such as floods, cyclones and earthquakes cause huge losses every year. Traditional "
         "management depends on manual surveys and delayed information. Today we have satellite and drone "
         "imagery, IoT sensors and social media giving data in real time. AI can process this data quickly. "
         "The diagram shows the disaster management cycle - mitigation, preparedness, response and recovery - "
         "and AI can support every phase.")

# 4. Objectives
s = d.content_slide("Objectives")
numbered_rows(d, s, [
    ("Disaster lifecycle", "Understand the role of AI in mitigation, preparedness, response and recovery.", "sync"),
    ("AI techniques", "Study ML, deep learning, computer vision, NLP and spatio-temporal analysis for disasters.", "brain"),
    ("Applications", "Explore flood prediction, wildfire detection, damage assessment and crisis information.", "water"),
    ("System design", "Analyse an end-to-end AI-based disaster management pipeline.", "sitemap"),
    ("Challenges", "Identify issues in data, generalization, interpretability and fairness; suggest future directions.", "balance"),
], circ=NAVY, icon_color="o")
notes(s, "My objectives are to understand where AI fits in each phase of disaster management, study the main AI "
         "techniques, explore real applications, analyse a complete system pipeline, and discuss challenges.")

# 5. Literature review overview
s = d.content_slide("Literature Review")
text(s, 0.5, 1.2, 9.0, 0.5, "Peer-reviewed reviews and surveys (2024–2026) were grouped into four themes.",
     size=14, color=MUTED, italic=True)
cards = [("book", "Reviews & Frameworks", "[1], [2]",
          "Map AI methods to every disaster phase (96 studies in [1]); stress trustworthy, explainable deployment [2]."),
         ("layers", "Hazard-Specific Deep Learning", "[3], [4], [5]",
          "CNNs, LSTMs and AIoT for floods, earthquakes and wildfires: prediction, detection and damage assessment."),
         ("comment", "Large Language Models", "[6]",
          "LLMs across disaster phases: classifying crisis messages, extracting information, generating reports."),
         ("eye", "Vision-Language Agents", "[7]",
          "DisasTeller: four specialised agents turn post-disaster imagery into assessments, alerts and plans.")]
for i, (ic, t, r, b) in enumerate(cards):
    theme_card(d, s, 0.5 + (i % 2) * 4.6, 1.75 + (i // 2) * 2.15, 4.4, 2.0, ic, t, r, b,
               circ=NAVY if i in (0, 3) else ACC, size=15)
box(s, 0.5, 6.12, 9.0, 0.68, fill=LIGHT, margin=0.12, paras=[[
    ("Common finding: ", {"bold": True, "color": NAVY}),
    ("AI helps most when several data sources are fused and outputs are trustworthy enough for "
     "responders to act on.", {})]], size=14)
notes(s, "I grouped the literature into four themes. Systematic reviews give the overall map - the Muthukumar "
         "review alone synthesises 96 studies. Hazard-specific papers cover floods, earthquakes and wildfires. "
         "The ACL survey covers large language models, and the Nature Communications paper presents DisasTeller, "
         "a multi-agent vision-language system for damage assessment and reporting.")

# 6-7. Literature survey tables
lit = [
    ("A systematic review of AI frameworks for holistic disaster management",
     "S. Muthukumar et al. — Discover Artificial Intelligence, 2026",
     "Synthesises 96 peer-reviewed studies; maps AI approaches to each disaster-management phase."),
    ("A systematic review of trustworthy AI applications in natural disasters",
     "Computers & Electrical Engineering, 2024",
     "Reviews AI for prediction, risk assessment, early warning and evacuation, with focus on trustworthy deployment."),
    ("Deep AI applications for natural disaster management systems: A methodological review",
     "Akhyar et al. — Ecological Indicators, 2024",
     "Reviews deep-learning applications for forest fires, earthquakes and floods."),
    ("AI for flood risk management: A comprehensive state-of-the-art review",
     "Int. J. Disaster Risk Reduction, 2025",
     "Reviews ML/DL models, input data and applications in flood-risk management."),
    ("Survey of AI-Enabled IoT for Wildfire Prediction, Detection, and Post-Operations", "IEEE Access, 2026",
     "AIoT for wildfire prediction, real-time detection, damage assessment and recovery."),
    ("Harnessing Large Language Models for Disaster Management: A Survey", "Z. Lei et al. — Findings of ACL, 2025",
     "Taxonomy of LLM uses across disaster phases; datasets, use cases and open challenges."),
    ("Integration of large vision language models for post-disaster damage assessment and reporting",
     "Z. Chen et al. — Nature Communications, 2026",
     "DisasTeller: four vision-language agents for assessment, alerts, emergency reports, resource allocation "
     "and recovery planning."),
]
for part, chunk in enumerate((lit[:4], lit[4:])):
    s = d.content_slide(f"Literature Survey in Tabular Form ({part + 1}/2)", size=26)
    rows = [["Sr. No", "Details of Paper", "Work Reported"]]
    start = 1 if part == 0 else 5
    for i, (t, v, w) in enumerate(chunk, start):
        rows.append([str(i), [[(t, {"bold": True})], [(v, {"size": 11, "color": MUTED})]], w])
    table(s, 0.45, 1.3, [0.75, 4.1, 4.25], rows, size=13, row_h=1.15, col_align=["c", "l", "l"])
    notes(s, "This table summarises each paper and what it reports. " +
          ("The first four are broad reviews and hazard-specific reviews for floods, fires and earthquakes."
           if part == 0 else
           "These cover AIoT for wildfires, large language models, and the DisasTeller vision-language system."))

# 8. Baseline papers
s = d.content_slide("Baseline Papers Selected for Seminar Work", size=26)
base = [("PRIMARY BASELINE", NAVY, "[1] A systematic review of AI frameworks for holistic disaster management",
         "Discover AI, 2026", "Most comprehensive recent review (96 studies) across all disaster phases.",
         "Overall structure: phases × AI techniques; system pipeline."),
        ("SUPPORTING", ACC, "[6] Harnessing Large Language Models for Disaster Management: A Survey",
         "Findings of ACL, 2025", "Broad survey of LLM use in disaster management.",
         "NLP / LLM crisis-information extraction module."),
        ("SUPPORTING", ACC, "[7] Integration of large vision language models … (DisasTeller)",
         "Nature Communications, 2026", "Shows a working multi-agent vision-language system.",
         "Damage assessment and automated reporting.")]
for i, (tag, col, t, v, why, used) in enumerate(base):
    x = 0.5 + i * 3.075
    box(s, x, 1.35, 2.85, 4.5, fill=PALE)
    box(s, x, 1.35, 2.85, 0.5, fill=col, paras=tag, size=13, bold=True, color=WHITE)
    text(s, x + 0.15, 1.95, 2.55, 1.25, t, size=14, bold=True, color=NAVY)
    text(s, x + 0.15, 3.2, 2.55, 0.32, v, size=12, italic=True, color=MUTED)
    text(s, x + 0.15, 3.6, 2.55, 1.15, [[("Why selected: ", {"bold": True, "color": col}), (why, {})]], size=13)
    text(s, x + 0.15, 4.75, 2.55, 1.05, [[("Used for: ", {"bold": True, "color": col}), (used, {})]], size=13)
text(s, 0.5, 6.05, 9.0, 0.7, "Reviews [2]–[5] were then used for early-warning, flood and wildfire details.",
     size=14, italic=True, color=MUTED, align="c", anchor="m")
notes(s, "My primary baseline is the systematic review by Muthukumar et al., because it covers all phases and "
         "AI approaches. The ACL survey supports the language-model part, and the DisasTeller paper shows how "
         "vision-language agents can automate damage assessment and reporting.")

# 9. System architecture
s = d.content_slide("System Architecture")
text(s, 0.5, 1.08, 9.0, 0.35, "End-to-end AI pipeline: from raw data to disaster-management decisions [1]",
     size=13, italic=True, color=MUTED, align="c")
cols = [("Data Sources", NAVY, "n", [("satellite", "Satellite / UAV imagery"), ("sensor", "IoT sensors: rain, river, seismic"),
                                     ("comment", "Social media & news"), ("db", "Government & historical data")]),
        ("AI Processing", BLUE, "b", [("cogs", "Preprocessing: cleaning, fusion"), ("brain", "ML / DL: CNN, LSTM, ViT"),
                                      ("comment", "NLP / LLM: BERT, NER"), ("route", "Optimization / RL")]),
        ("Decision Support", ACC, "o", [("chart", "Risk prediction"), ("house", "Damage assessment"),
                                        ("search", "Information extraction"), ("truck", "Resource allocation")]),
        ("Outputs", GREEN, "g", [("bell", "Early warnings"), ("map", "Damage maps"), ("route", "Evacuation routes"),
                                 ("file", "Situation reports")])]
xs = (0.3, 2.75, 5.2, 7.65)
cw = 2.05
for x, (head, col, ic_c, items) in zip(xs, cols):
    box(s, x, 1.55, cw, 4.15, fill=PALE, line=col, lw=1.25)
    box(s, x, 1.55, cw, 0.5, fill=col, paras=head, size=14, bold=True, color=WHITE)
    for i, (ic, t) in enumerate(items):
        y = 2.2 + i * 0.86
        box(s, x + 0.1, y, cw - 0.2, 0.74, fill=WHITE, line=LIGHT, lw=0.75)
        d.icon(s, ic, x + 0.2, y + 0.19, 0.36, ic_c)
        text(s, x + 0.62, y + 0.02, cw - 0.78, 0.7, t, size=12, anchor="m")
for x in (2.35, 4.8, 7.25):
    box(s, x + 0.02, 3.4, 0.36, 0.5, fill=MUTED, shape="rarrow")
box(s, 1.9, 6.05, 6.2, 0.6, fill=NAVY, paras=[[("Feedback & continuous learning: ", {"bold": True}),
                                               ("model updates · human validation", {})]],
    size=13, color=WHITE)
polyline(s, [(8.67, 5.7), (8.67, 6.35), (8.1, 6.35)], NAVY, 2)
polyline(s, [(1.9, 6.35), (1.33, 6.35), (1.33, 5.7)], NAVY, 2)
notes(s, "This is the overall system. Data comes from satellites and drones, IoT sensors, social media and "
         "government databases. The AI layer cleans and fuses it, then applies deep learning, NLP and "
         "optimization models. The decision-support layer predicts risk, assesses damage, extracts information "
         "and allocates resources. Outputs are warnings, damage maps, evacuation routes and reports. A feedback "
         "loop with human validation keeps improving the models.")

# 10. Algorithm 1: early warning (LSTM)
s = d.content_slide("Algorithm 1: Early Warning (LSTM)", size=26)
text(s, 0.5, 1.08, 9.0, 0.35, "Learns patterns in historical and real-time time-series data to predict floods [4], [8]",
     size=13, italic=True, color=MUTED, align="c")
box(s, 0.3, 1.6, 1.55, 0.8, fill=BLUE, paras=[[("Historical", {"bold": True})], "rainfall, river level"],
    size=11, color=WHITE)
box(s, 0.3, 2.6, 1.55, 0.8, fill=BLUE, paras=[[("Real-time IoT", {"bold": True})], "sensors, weather feeds"],
    size=11, color=WHITE)
box(s, 2.1, 2.05, 1.4, 0.9, fill=WHITE, line=NAVY, paras=[[("Preprocess", {"bold": True})], "normalize, windows"],
    size=11)
box(s, 3.75, 1.85, 1.4, 1.3, fill=NAVY, paras=[[("LSTM /", {"bold": True, "size": 14})],
                                               [("Transformer", {"bold": True, "size": 14})], "sequence model"],
    size=11, color=WHITE)
box(s, 5.4, 2.05, 1.45, 0.9, fill=WHITE, line=NAVY, paras=[[("Flood risk", {"bold": True})], "next 6–24 h"],
    size=11)
box(s, 7.0, 1.95, 1.3, 1.1, fill=GOLD, shape="diamond", paras="ŷ > τ ?", size=14, bold=True)
box(s, 8.5, 2.05, 1.2, 0.9, fill=ACC, paras=[[("Issue", {"bold": True})], [("alert", {"bold": True})]],
    size=13, color=WHITE)
arrow(s, 1.85, 2.0, 2.1, 2.35, MUTED, 1.5)
arrow(s, 1.85, 3.0, 2.1, 2.65, MUTED, 1.5)
for x1, x2 in ((3.5, 3.75), (5.15, 5.4), (6.85, 7.0), (8.3, 8.5)):
    arrow(s, x1, 2.5, x2, 2.5, MUTED, 1.75)
text(s, 8.25, 2.15, 0.4, 0.25, "yes", size=10, color=MUTED)
box(s, 0.4, 3.75, 4.3, 3.0, fill=PALE)
text(s, 0.55, 3.82, 4.0, 0.4, "Why LSTM?", size=15, bold=True, color=NAVY)
text(s, 0.55, 4.25, 4.05, 2.45, [
    "Gated memory cells keep long-term patterns, e.g. days of rainfall [8]",
    "Forget, input and output gates decide what to keep",
    "Handles noisy, irregular sensor sequences",
    "Transformers use attention for long-range links"], size=15, bullet=True, after=10)
code_box(s, 4.95, 3.75, 4.65, 3.0, [
    "Input: series X_t, threshold τ",
    "X ← Normalize(X_t); make windows",
    "h_t ← LSTM(X, h_(t-1))",
    "ŷ_(t+1) ← Predict(h_t)",
    "if ŷ_(t+1) > τ then",
    "    IssueAlert(region, ŷ_(t+1))",
    "return ŷ_(t+1), alert"], title="Pseudocode", size=12)
notes(s, "For early warning, the model takes historical and real-time readings such as rainfall and river level. "
         "After normalisation the data is split into time windows and fed to an LSTM or Transformer. The LSTM's "
         "gates let it remember long-term patterns like several days of rain. It predicts the flood risk for the "
         "next hours; if the prediction crosses a threshold, an alert is issued for that region.")

# 11. Algorithm 2: damage assessment
s = d.content_slide("Algorithm 2: Damage Assessment (CNN/ViT)", size=26)
text(s, 0.5, 1.08, 9.0, 0.35, "Compares pre- and post-disaster satellite/UAV images to classify damage [3], [7]",
     size=13, italic=True, color=MUTED, align="c")
for k, (lab, ic, col) in enumerate((("Pre-disaster image", "house", "b"), ("Post-disaster image", "house", "r"))):
    y = 1.5 + k * 1.05
    box(s, 0.3, y, 1.75, 0.95, fill=LIGHT, line=BLUE)
    d.icon(s, "house", 0.45, y + 0.2, 0.55, col)
    text(s, 1.0, y + 0.05, 1.0, 0.85, lab, size=11, anchor="m")
box(s, 2.35, 1.95, 1.45, 1.1, fill=WHITE, line=NAVY, paras=[[("Align &", {"bold": True})],
                                                            [("preprocess", {"bold": True})], "co-registration"], size=11)
box(s, 4.1, 1.8, 1.55, 1.4, fill=NAVY, paras=[[("CNN / ViT", {"bold": True, "size": 14})], "semantic",
                                              "segmentation"], size=11, color=WHITE)
arrow(s, 2.05, 1.98, 2.35, 2.35, MUTED, 1.5)
arrow(s, 2.05, 3.03, 2.35, 2.75, MUTED, 1.5)
arrow(s, 3.8, 2.5, 4.1, 2.5, MUTED, 1.75)
arrow(s, 5.65, 2.5, 5.95, 2.5, MUTED, 1.75)
DMG = [("No damage", "9BBB59"), ("Minor", GOLD), ("Major", "F79646"), ("Destroyed", RED)]
grid = ["00012", "01123", "01233", "00122", "00011"]
for r, row in enumerate(grid):
    for c, v in enumerate(row):
        box(s, 5.95 + c * 0.3, 1.55 + r * 0.3, 0.28, 0.28, fill=DMG[int(v)][1], shape="rect")
text(s, 5.95, 3.08, 1.5, 0.3, "Damage map", size=12, bold=True, color=NAVY, align="c")
for i, (lab, col) in enumerate(DMG):
    box(s, 7.75, 1.65 + i * 0.4, 0.25, 0.25, fill=col, shape="rect")
    text(s, 8.08, 1.6 + i * 0.4, 1.5, 0.35, lab, size=12, anchor="m")
box(s, 0.4, 3.65, 4.4, 3.1, fill=PALE)
text(s, 0.55, 3.72, 4.1, 0.4, "Steps", size=15, bold=True, color=NAVY)
steps = ["Input pre- and post-event images", "Align and normalise both images",
         "CNN/ViT labels each pixel or building", "Generate the damage map",
         "Overlay on GIS maps for responders"]
for i, st in enumerate(steps):
    y = 4.2 + i * 0.5
    box(s, 0.6, y + 0.04, 0.36, 0.36, fill=ACC, shape="oval", paras=str(i + 1), size=12, bold=True, color=WHITE,
        margin=0)
    text(s, 1.1, y, 3.6, 0.44, st, size=14, anchor="m")
box(s, 5.05, 3.65, 4.55, 3.1, fill=PALE)
text(s, 5.2, 3.72, 4.3, 0.4, "Extension: DisasTeller [7]", size=15, bold=True, color=NAVY)
text(s, 5.2, 4.12, 4.3, 0.6, "Four specialised vision-language agents work together on post-disaster images:",
     size=13)
for i in range(4):
    d.icon_circle(s, "robot", 5.35 + i * 1.05, 4.8, 0.55, fill=NAVY if i % 2 == 0 else BLUE)
outs = ["Damage assessment", "Alerts", "Emergency reports", "Resource & recovery plans"]
for i, o in enumerate(outs):
    x = 5.2 + (i % 2) * 2.17
    y = 5.55 + (i // 2) * 0.55
    box(s, x, y, 2.07, 0.45, fill=WHITE, line=ACC, paras=o, size=12, color=INK)
notes(s, "For damage assessment, the system takes satellite or drone images from before and after the event. "
         "After aligning them, a CNN or Vision Transformer performs semantic segmentation and labels each "
         "building or region: no damage, minor, major or destroyed. The result is a damage map overlaid on GIS "
         "for responders. DisasTeller extends this with four vision-language agents that also produce alerts, "
         "emergency reports and resource and recovery plans.")

# 12. Algorithm 3: NLP extraction & evacuation RL
s = d.content_slide("Algorithm 3: Crisis Info & Evacuation", size=26)
text(s, 0.4, 1.12, 9.2, 0.38, "Crisis information extraction (NLP / LLM) [6]", size=16, bold=True, color=NAVY)
for k, msg in enumerate(("“Road blocked near the bridge, need rescue!”", "“Help needed in Wardha, water rising”")):
    box(s, 0.4, 1.6 + k * 0.9, 2.75, 0.75, fill=LIGHT, line=BLUE, paras=[[(msg, {"italic": True})]], size=12,
        align="l", margin=0.1)
box(s, 3.55, 1.85, 1.7, 1.15, fill=NAVY, paras=[[("NLP model", {"bold": True, "size": 14})],
                                                "BERT / LLM + NER"], size=11, color=WHITE)
arrow(s, 3.15, 1.98, 3.55, 2.25, MUTED, 1.5)
arrow(s, 3.15, 2.88, 3.55, 2.6, MUTED, 1.5)
arrow(s, 5.25, 2.42, 5.6, 2.42, MUTED, 1.75)
table(s, 5.6, 1.6, [1.55, 2.4], [["Field", "Extracted value"], ["Location", "Wardha"], ["Event", "Flood"],
                                 ["Need", "Rescue"], ["Severity", "High"]],
      size=12, header_size=12, row_h=0.33, header_h=0.33, first_col_bold=True)
line(s, 0.4, 3.6, 9.6, 3.6, LIGHT, 1.5)
text(s, 0.4, 3.7, 9.2, 0.38, "Evacuation routing (Reinforcement Learning)", size=16, bold=True, color=NAVY)
box(s, 0.5, 4.5, 1.9, 1.3, fill=ACC, paras=[[("Agent", {"bold": True, "size": 15})], "policy π", "(PPO / DQN)"],
    size=12, color=WHITE)
box(s, 3.4, 4.5, 1.9, 1.3, fill=BLUE, paras=[[("Environment", {"bold": True, "size": 15})], "road network,",
                                             "hazard map"], size=12, color=WHITE)
polyline(s, [(1.45, 4.5), (1.45, 4.2), (4.35, 4.2), (4.35, 4.5)], NAVY, 1.75)
text(s, 1.6, 4.17, 2.6, 0.3, "action: choose next road", size=12, color=NAVY, align="c", anchor="b")
polyline(s, [(4.35, 5.8), (4.35, 6.15), (1.45, 6.15), (1.45, 5.8)], GREEN, 1.75)
text(s, 1.3, 6.2, 3.2, 0.55, [[("state: ", {"bold": True}), ("location, congestion, hazard", {})],
                              [("reward: ", {"bold": True}), ("+ safety, − travel time", {})]],
     size=12, color=GREEN, align="c", after=0)
code_box(s, 5.6, 4.15, 4.0, 2.6, [
    "Input: road graph G, hazard map H",
    "s ← (loc, congestion, hazard)",
    "a ← π(s)        # next road",
    "r ← R(safety, time)",
    "update π with PPO / DQN",
    "return optimal evacuation route"], title="Pseudocode", size=12)
notes(s, "During a disaster people post messages like these. An NLP model such as BERT or an LLM with named "
         "entity recognition extracts structured fields - location, event, need and severity - so responders can "
         "prioritise. For evacuation, reinforcement learning treats routing as a game: the agent observes the "
         "state - location, congestion and hazard - chooses the next road, and gets a reward for safety and "
         "speed. Algorithms like PPO or DQN learn the best evacuation policy.")

# 13. Features / advantages / disadvantages
s = d.content_slide("Features / Advantages / Disadvantages", size=26)
three_columns(d, s, [
    ("Features", NAVY, "star", [("Data fusion", "satellite, sensor and text data"),
                                ("Real-time", "continuous monitoring"),
                                ("Prediction", "forecasts risk in advance"),
                                ("Auto mapping", "damage maps from imagery"),
                                ("Decision support", "routes, resources, reports")]),
    ("Advantages", GREEN, "check", [("Earlier warnings", "more lead time to evacuate"),
                                    ("Faster assessment", "quicker than ground surveys"),
                                    ("Better allocation", "relief reaches need first"),
                                    ("Wide coverage", "large or unreachable areas"),
                                    ("Scalable", "works 24×7 at scale")]),
    ("Disadvantages", RED, "warn", [("Data scarcity", "rare events, imbalanced data"),
                                    ("Generalization", "may fail in new regions"),
                                    ("Black box", "low trust without explanation [2]"),
                                    ("Infrastructure", "power/network may fail"),
                                    ("Misinformation", "false posts; privacy risks")]),
])
notes(s, "Key features are data fusion, real-time monitoring, prediction, automatic mapping and decision "
         "support. Advantages include more lead time, faster assessment and better use of resources. "
         "But there are real limitations: data on rare disasters is scarce, models may not transfer to new "
         "regions, black-box outputs reduce trust, infrastructure can fail during the disaster itself, and "
         "social media contains misinformation.")

# 14. Applications
s = d.content_slide("Applications")
app_grid(d, s, [
    ("water", "Flood Forecasting", "River-level and rainfall prediction for early warnings [4]."),
    ("fire", "Wildfire Detection", "AIoT sensors and cameras detect fires early [5]."),
    ("quake", "Earthquake Damage", "Satellite/UAV imagery maps collapsed buildings [3]."),
    ("cyclone", "Cyclone Tracking", "Forecasting track and intensity to plan evacuations."),
    ("comment", "Crisis Informatics", "LLMs classify social-media posts and help requests [6]."),
    ("truck", "Relief Logistics", "Optimised routing of supplies, shelters and rescue teams."),
], circ=ACC)
notes(s, "Applications include flood forecasting, wildfire detection with AI-enabled IoT, earthquake damage "
         "mapping, cyclone tracking, crisis informatics using language models, and relief logistics.")

# 15. Analysis / comparison
s = d.content_slide("Analysis / Comparison")
rows = [["Aspect", "Traditional approach", "AI-based approach", "Benefit"],
        ["Early warning", "Manual monitoring, fixed thresholds", "ML/DL forecasts on live sensor data", "More lead time"],
        ["Damage assessment", "Ground surveys (days)", "Satellite/UAV + CNN/ViT maps (hours)", "Faster response"],
        ["Information", "Phone calls, manual reports", "NLP/LLM triage of social media", "Situational awareness"],
        ["Resource allocation", "Static, pre-planned routes", "Optimization / RL adapts live", "Efficient use"],
        ["Reporting", "Manual situation reports", "Automated reports, e.g. [7]", "Quick, consistent"]]
table(s, 0.45, 1.3, [1.85, 2.4, 2.75, 2.1], rows, size=13, header_size=13, row_h=0.72, first_col_bold=True)
box(s, 0.45, 5.75, 9.1, 1.0, fill=PALE, align="l", anchor="m", margin=0.14, paras=[
    [("Key insight: ", {"bold": True, "color": NAVY}),
     ("AI supports — it does not replace — human decision-makers. Trustworthy, explainable outputs are "
      "essential before authorities act on them [2].", {})]], size=14)
notes(s, "Comparing traditional and AI-based approaches: AI gives earlier warnings, maps damage in hours instead "
         "of days, triages social media automatically, adapts routes as conditions change and generates reports "
         "quickly. But AI should support human decision-makers, and its outputs must be explainable and trusted.")

# 16. Conclusion
conclusion_slide(d, [
    "AI strengthens every phase of the disaster-management cycle.",
    "Time-series models give early warnings; CNN/ViT models map damage quickly.",
    "NLP/LLMs turn crisis messages into structured, actionable data.",
    "Optimization and RL improve evacuation and relief logistics."],
    ["Multimodal models fusing satellite, sensor and text data",
     "Explainable, trustworthy AI for critical decisions [2]",
     "Edge AI that keeps working when networks fail",
     "Collaboration of government, research and industry"],
    "AI enables earlier detection, faster assessment and smarter response — with humans in the loop")
notes(d.prs.slides[-1], "To conclude, AI can strengthen early detection, damage assessment, information "
      "extraction and resource allocation. Future work should focus on multimodal models, explainability, edge "
      "deployment and close collaboration with disaster-management authorities.")

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
s = references_slide(d, refs, 1, size=13)
notes(s, "References in IEEE format; numbers in square brackets on the slides point to this list.")

# 18. Thank you
s = thank_you_slide(d, "Vedika Dandade  |  Roll No.: B344")
notes(s, "Thank you. I am happy to take questions.")

d.save(OUT)
print("saved", OUT, len(d.prs.slides))
