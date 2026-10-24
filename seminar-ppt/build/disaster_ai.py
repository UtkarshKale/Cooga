"""Seminar-I deck: AI in Disaster Management (Vedika Dandade, B344) — "hazard signage" design."""
import sys

from vedika_design import *  # noqa: F401,F403

TEMPLATE, ICONS, OUT = sys.argv[1:4]
d = VDeck(TEMPLATE, ICONS, "AI in Disaster Management   |   Vedika Dandade, B344")
HAZARDS = [("water", "Flood"), ("fire", "Wildfire"), ("quake", "Earthquake"), ("cyclone", "Cyclone")]
DMG = [("No damage", GREEN), ("Minor", "F6D365"), ("Major", AMBER), ("Destroyed", RED)]

# 1. Cover
s = d.cover("AI in Disaster Management", "SEMINAR-I   |   2025–26", HAZARDS,
            info=[("Presented by", "Vedika Dandade", "Roll No. B344  |  Third Year, Semester V"),
                  ("Under the guidance of", "Name of Faculty", "Designation of faculty")])
notes(s, "Good morning. My seminar topic is AI in Disaster Management: how artificial intelligence helps predict "
         "disasters, assess damage, extract critical information and plan the response.")

# 2. Contents
s = d.slide("00", "Contents", "Seminar flow, following the Seminar-I template")
items = ["Introduction", "Objectives", "Literature Review", "Literature Survey", "Baseline Papers",
         "System Architecture", "Algorithms Studied", "Features, Advantages & Disadvantages", "Applications",
         "Analysis & Comparison", "Conclusion & Future Scope", "References"]
for i, it in enumerate(items):
    col, row = i % 3, i // 3
    x = 0.6 + col * 3.0
    y = 1.6 + row * 1.3
    b(s, x, y, 2.8, 1.12, bg=CHAR if i in (5, 6) else GRAY)
    t(s, x + 0.18, y + 0.1, 1.0, 0.45, f"{i + 1:02d}", size=20, bold=True, color=AMBER if i in (5, 6) else BLUE)
    t(s, x + 0.18, y + 0.55, 2.5, 0.5, it, size=13.5, bold=True, color=WHITE if i in (5, 6) else CHAR)
notes(s, "This is the flow of my presentation. Sections 6 and 7 - the system architecture and the algorithms - are "
         "the technical core.")

# 3. Introduction
s = d.slide("01", "Introduction", "Disasters move fast — data and AI can now move faster")
intro = [("house", AMBER, CHAR, "Background",
          "Floods, cyclones, earthquakes, wildfires and landslides cause loss of life, infrastructure damage and "
          "economic setbacks."),
         ("clock", RED, WHITE, "Problem",
          "Traditional disaster management relies on manual surveys and delayed reports, which slows decisions."),
         ("lightbulb", BLUE, WHITE, "Inspiration",
          "Satellites, IoT sensors and social media now give real-time data; AI turns it into early, actionable "
          "insight [1].")]
for i, (ic, bg, fg, head, body) in enumerate(intro):
    x = 0.6 + i * 3.0
    d.icon_tile(s, ic, x, 1.55, 0.55, bg=bg, fg=fg)
    t(s, x + 0.7, 1.55, 2.1, 0.55, head, size=16, bold=True, anchor="m")
    t(s, x, 2.25, 2.75, 1.5, body, size=13, color=MUTED)
t(s, 0.6, 3.95, 8.8, 0.3, "THE DISASTER MANAGEMENT CYCLE — WHERE AI HELPS", size=10.5, bold=True, spc=100)
phases = [("Mitigation", CHAR, WHITE, "Risk and hazard mapping"),
          ("Preparedness", BLUE, WHITE, "Early warning and forecasting"),
          ("Response", RED, WHITE, "Damage assessment and information extraction"),
          ("Recovery", GREEN, WHITE, "Recovery planning and reports")]
for i, (ph, bg, fg, role) in enumerate(phases):
    x = 0.6 + i * 2.17
    b(s, x, 4.35, 2.3, 0.8, bg=bg, shape="chevron", paras=ph, size=13.5, bold=True, color=fg)
    t(s, x + 0.25, 5.3, 1.85, 0.85, role, size=12.5, color=CHAR, align="c")
path(s, [(9.15, 6.2), (9.15, 6.5), (0.85, 6.5), (0.85, 6.2)], MUTED, 1.25)
t(s, 3.5, 6.52, 3.0, 0.28, "the cycle repeats for the next event", size=10, italic=True, color=MUTED, align="c")
notes(s, "Disasters such as floods, cyclones and earthquakes cause huge losses every year. Traditional management "
         "depends on manual surveys and delayed information. Today satellites, drones, IoT sensors and social media "
         "give data in real time, and AI can process it quickly. The disaster management cycle has four phases - "
         "mitigation, preparedness, response and recovery - and AI has a role in each of them.")

# 4. Objectives
s = d.slide("02", "Objectives", "What this seminar aims to achieve")
objs = [("sync", "Disaster lifecycle", "Understand the role of AI in mitigation, preparedness, response and recovery."),
        ("brain", "AI techniques", "Study ML, deep learning, computer vision, NLP and spatio-temporal analysis."),
        ("water", "Applications", "Explore flood prediction, wildfire detection, damage assessment and crisis information."),
        ("sitemap", "System design", "Analyse an end-to-end AI-based disaster management pipeline."),
        ("balance", "Challenges", "Identify issues in data, generalization, interpretability and fairness.")]
for i, (ic, head, desc) in enumerate(objs):
    x = 0.6 + (i % 3) * 3.0
    y = 1.55 + (i // 3) * 2.62
    b(s, x, y, 2.8, 2.45, bg=GRAY)
    t(s, x + 0.2, y + 0.12, 1.0, 0.6, str(i + 1), size=32, bold=True, color=AMBER)
    d.icon(s, ic, x + 2.2, y + 0.25, 0.4, CHAR)
    t(s, x + 0.2, y + 0.85, 2.45, 0.4, head, size=15, bold=True)
    t(s, x + 0.2, y + 1.27, 2.45, 1.1, desc, size=12.5, color=MUTED)
b(s, 6.6, 4.17, 2.8, 2.45, bg=CHAR)
t(s, 6.8, 4.35, 2.4, 0.3, "EXPECTED OUTCOME", size=10.5, bold=True, color=AMBER, spc=100)
t(s, 6.8, 4.75, 2.45, 1.75, "A clear picture of how AI makes disaster response earlier, faster and smarter — and "
  "where it still falls short.", size=13.5, color=WHITE)
notes(s, "My objectives are to understand where AI fits in each phase of disaster management, study the main AI "
         "techniques, explore real applications, analyse a complete system pipeline, and discuss the challenges.")

# 5. Literature review
s = d.slide("03", "Literature Review", "Peer-reviewed reviews and surveys (2024–2026), grouped into four themes")
themes = [("book", "Reviews & frameworks", ["1", "2"],
           "Map AI methods to every disaster phase (96 studies in [1]); stress trustworthy, explainable deployment [2]."),
          ("layers", "Hazard-specific deep learning", ["3", "4", "5"],
           "CNNs, LSTMs and AIoT for floods, earthquakes and wildfires: prediction, detection and damage assessment."),
          ("comment", "Large language models", ["6"],
           "LLMs across disaster phases: classifying crisis messages, extracting information, generating reports."),
          ("eye", "Vision-language agents", ["7"],
           "DisasTeller: four specialised agents turn post-disaster imagery into assessments, alerts and plans.")]
for i, (ic, name, refs, desc) in enumerate(themes):
    y = 1.55 + i * 1.1
    b(s, 0.6, y, 2.6, 0.95, bg=CHAR)
    d.icon(s, ic, 0.78, y + 0.29, 0.38, AMBER)
    t(s, 1.28, y, 1.85, 0.95, name, size=13, bold=True, color=WHITE, anchor="m")
    b(s, 3.2, y, 6.2, 0.95, bg=GRAY)
    t(s, 3.4, y, 4.6, 0.95, desc, size=12.5, anchor="m")
    for k, r in enumerate(refs):
        b(s, 8.15 + k * 0.42, y + 0.3, 0.36, 0.34, bg=AMBER, paras=f"[{r}]", size=10, bold=True, margin=0)
d.key_block(s, 6.05, "Key finding", "AI helps most when several data sources are fused and its outputs are "
            "trustworthy enough for responders to act on.")
notes(s, "I grouped the literature into four themes. Systematic reviews give the overall map - the Muthukumar review "
         "alone synthesises 96 studies. Hazard-specific papers cover floods, earthquakes and wildfires. The ACL survey "
         "covers large language models, and the Nature Communications paper presents DisasTeller, a multi-agent "
         "vision-language system for damage assessment and reporting.")

# 6-7. Literature survey tables
lit = [
    ("A systematic review of AI frameworks for holistic disaster management",
     "S. Muthukumar et al., Discover Artificial Intelligence, 2026",
     "Synthesises 96 peer-reviewed studies; maps AI approaches to each disaster-management phase."),
    ("A systematic review of trustworthy AI applications in natural disasters",
     "Computers & Electrical Engineering, 2024",
     "Reviews AI for prediction, risk assessment, early warning and evacuation, focusing on trustworthy deployment."),
    ("Deep AI applications for natural disaster management systems: a methodological review",
     "Akhyar et al., Ecological Indicators, 2024",
     "Reviews deep-learning applications for forest fires, earthquakes and floods."),
    ("AI for flood risk management: a comprehensive state-of-the-art review", "Int. J. Disaster Risk Reduction, 2025",
     "Reviews ML/DL models, input data and applications in flood-risk management."),
    ("Survey of AI-Enabled IoT for Wildfire Prediction, Detection, and Post-Operations", "IEEE Access, 2026",
     "AIoT for wildfire prediction, real-time detection, damage assessment and recovery."),
    ("Harnessing Large Language Models for Disaster Management: A Survey", "Z. Lei et al., Findings of ACL, 2025",
     "Taxonomy of LLM uses across disaster phases; datasets, use cases and open challenges."),
    ("Integration of large vision language models for post-disaster damage assessment and reporting",
     "Z. Chen et al., Nature Communications, 2026",
     "DisasTeller: four vision-language agents for assessment, alerts, emergency reports, resource allocation and "
     "recovery planning."),
]
for part, chunk in enumerate((lit[:4], lit[4:])):
    s = d.slide("04", f"Literature Survey ({part + 1}/2)", "Papers studied and the work each one reports")
    start = 1 if part == 0 else 5
    rows = [["Sr. No", "Details of paper", "Work reported"]]
    for i, (ti, v, w) in enumerate(chunk, start):
        rows.append([str(i), [[(ti, {"bold": True})], [(v, {"size": 10.5, "color": MUTED})]], w])
    d.table(s, rows, [0.8, 4.1, 3.9], y=1.5, row_h=1.15, num_col=True)
    notes(s, "This table summarises each paper and what it reports. " +
          ("The first four are broad reviews and hazard-specific reviews for floods, fires and earthquakes."
           if part == 0 else
           "These cover AIoT for wildfires, large language models, and the DisasTeller vision-language system."))

# 8. Baseline papers
s = d.slide("05", "Baseline Papers", "Three papers selected as the foundation of this seminar")
base = [("[1]", "PRIMARY BASELINE", True, "A systematic review of AI frameworks for holistic disaster management",
         "Discover Artificial Intelligence, 2026", "Most comprehensive recent review: 96 studies across all phases.",
         "Overall structure (phases × AI techniques) and the system pipeline."),
        ("[6]", "SUPPORTING", False, "Harnessing Large Language Models for Disaster Management: A Survey",
         "Findings of ACL, 2025", "Broad survey of LLMs in disaster management.",
         "The NLP / LLM information-extraction module."),
        ("[7]", "SUPPORTING", False, "Integration of large vision language models … (DisasTeller)",
         "Nature Communications, 2026", "A working multi-agent vision-language system.",
         "Damage assessment and automated reporting.")]
for i, (ref, tag, primary, ti, venue, why, used) in enumerate(base):
    x = 0.6 + i * 3.0
    b(s, x, 1.55, 2.8, 1.05, bg=CHAR if primary else AMBER)
    t(s, x + 0.2, 1.62, 1.2, 0.6, ref, size=28, bold=True, color=AMBER if primary else CHAR)
    t(s, x + 0.2, 2.2, 2.5, 0.3, tag, size=10, bold=True, color=WHITE if primary else CHAR, spc=100)
    b(s, x, 2.6, 2.8, 4.15, bg=GRAY)
    t(s, x + 0.2, 2.75, 2.45, 1.15, ti, size=13.5, bold=True)
    t(s, x + 0.2, 3.9, 2.45, 0.3, venue, size=11, italic=True, color=MUTED)
    t(s, x + 0.2, 4.35, 2.45, 0.25, "WHY SELECTED", size=9.5, bold=True, color=BLUE, spc=100)
    t(s, x + 0.2, 4.62, 2.45, 0.9, why, size=12.5)
    t(s, x + 0.2, 5.5, 2.45, 0.25, "USED FOR", size=9.5, bold=True, color=BLUE, spc=100)
    t(s, x + 0.2, 5.77, 2.45, 0.9, used, size=12.5)
notes(s, "My primary baseline is the systematic review by Muthukumar et al., because it covers all phases and AI "
         "approaches. The ACL survey supports the language-model part, and the DisasTeller paper shows how "
         "vision-language agents can automate damage assessment and reporting. Reviews 2 to 5 were used for "
         "early-warning, flood and wildfire details.")

# 9. System architecture — swimlanes
s = d.slide("06", "System Architecture", "Four-layer AI pipeline from raw data to decisions, with continuous feedback [1]")
lanes = [("1", "Data sources", CHAR, WHITE, [("satellite", "Satellite / UAV imagery"), ("sensor", "IoT sensors"),
                                             ("comment", "Social media & news"), ("db", "Government data")]),
         ("2", "AI processing", BLUE, WHITE, [("cogs", "Cleaning & fusion"), ("brain", "CNN / LSTM / ViT"),
                                              ("comment", "NLP / LLM, NER"), ("route", "Optimization / RL")]),
         ("3", "Decisions", AMBER, CHAR, [("chart", "Risk prediction"), ("house", "Damage assessment"),
                                          ("search", "Info extraction"), ("truck", "Resource allocation")]),
         ("4", "Outputs", GREEN, WHITE, [("bell", "Early warnings"), ("map", "Damage maps"), ("route", "Evacuation routes"),
                                         ("file", "Situation reports")])]
for i, (n, name, bg, fg, chips) in enumerate(lanes):
    y = 1.5 + i * 1.2
    b(s, 0.6, y, 1.9, 1.0, bg=bg)
    t(s, 0.75, y + 0.1, 0.5, 0.4, n, size=20, bold=True, color=fg if bg != CHAR else AMBER)
    t(s, 0.75, y + 0.52, 1.7, 0.4, name, size=13, bold=True, color=fg)
    for j, (ic, lab) in enumerate(chips):
        x = 2.65 + j * 1.55
        b(s, x, y, 1.45, 1.0, bg=GRAY)
        d.icon(s, ic, x + 0.56, y + 0.1, 0.33, CHAR if bg == AMBER else bg)
        t(s, x + 0.05, y + 0.48, 1.35, 0.5, lab, size=10.5, align="c", anchor="m")
    if i < 3:
        arrow(s, 1.55, y + 1.0, 1.55, y + 1.2, MUTED, 1.75)
path(s, [(8.85, 5.6), (9.25, 5.6), (9.25, 2.0), (8.85, 2.0)], RED, 1.75, dash=True)
d.icon(s, "sync", 0.6, 6.33, 0.3, RED)
t(s, 1.0, 6.3, 8.4, 0.36, [[("Feedback & continuous learning: ", {"bold": True, "color": RED}),
                            ("model updates and human validation flow back into data collection.", {})]],
  size=12, anchor="m")
notes(s, "This is the overall system, shown as four layers. Data comes from satellites and drones, IoT sensors, social "
         "media and government databases. The AI layer cleans and fuses it, then applies deep learning, NLP and "
         "optimization models. The decision layer predicts risk, assesses damage, extracts information and allocates "
         "resources. Outputs are warnings, damage maps, evacuation routes and reports. The feedback loop with human "
         "validation keeps improving the models.")

# 10. Algorithm 1 — early warning (vertical flow)
s = d.slide("07", "Algorithm 1: Early Warning (LSTM)", "Forecasting floods from historical and real-time time-series data [4], [8]")
b(s, 0.6, 1.5, 1.45, 0.7, bg=GRAY, paras=[[("Historical", {"bold": True})], "rainfall, river level"], size=10.5)
b(s, 2.15, 1.5, 1.45, 0.7, bg=GRAY, paras=[[("Live IoT", {"bold": True})], "sensors, weather"], size=10.5)
b(s, 0.6, 2.45, 3.0, 0.5, bg=WHITE, line=GRAY2, lw=1.25, paras="Preprocess: normalize, sliding windows", size=11.5)
b(s, 0.6, 3.2, 3.0, 0.75, bg=CHAR, paras=[[("LSTM / Transformer", {"bold": True, "size": 14})], "sequence model"],
  size=10.5, color=WHITE)
b(s, 0.6, 4.2, 3.0, 0.5, bg=WHITE, line=GRAY2, lw=1.25, paras="Flood risk ŷ for the next 6–24 h", size=11.5)
b(s, 1.35, 4.95, 1.5, 0.8, bg=AMBER, shape="diamond", paras="ŷ > τ ?", size=13, bold=True)
b(s, 0.6, 6.05, 3.0, 0.55, bg=RED, paras="Issue alert to the region", size=12.5, bold=True, color=WHITE)
arrow(s, 1.325, 2.2, 1.6, 2.45, MUTED, 1.5)
arrow(s, 2.875, 2.2, 2.6, 2.45, MUTED, 1.5)
for y1, y2 in ((2.95, 3.2), (3.95, 4.2), (4.7, 4.95), (5.75, 6.05)):
    arrow(s, 2.1, y1, 2.1, y2, MUTED, 1.5)
t(s, 2.2, 5.75, 0.5, 0.28, "yes", size=10, color=MUTED)
path(s, [(2.85, 5.35), (3.45, 5.35), (3.45, 4.45), (3.6, 4.45)], MUTED, 1.25, head=None)
t(s, 2.95, 5.38, 0.8, 0.28, "no: keep monitoring", size=9, color=MUTED)
b(s, 4.0, 1.5, 5.4, 2.45, bg=GRAY)
t(s, 4.2, 1.62, 5.0, 0.35, "Why LSTM?", size=15, bold=True)
t(s, 4.2, 2.02, 5.0, 1.85, ["Gated memory cells keep long-term patterns, e.g. days of rainfall [8]",
                            "Forget, input and output gates decide what to keep",
                            "Robust to noisy, irregular sensor sequences",
                            "Transformers use attention for long-range links"],
  size=13, bullet="■", bullet_color=AMBER, after=5)
d.code(s, 4.0, 4.15, 5.4, 2.6, [
    "Input: series X_t, threshold τ",
    "X ← Normalize(X_t); make windows",
    "h_t ← LSTM(X, h_(t-1))",
    "ŷ_(t+1) ← Predict(h_t)        # risk",
    "if ŷ_(t+1) > τ then",
    "    IssueAlert(region, ŷ_(t+1))",
    "return ŷ_(t+1), alert"])
notes(s, "For early warning, the model takes historical and real-time readings such as rainfall and river level. After "
         "normalisation the data is split into time windows and fed to an LSTM or Transformer. The LSTM's gates let it "
         "remember long-term patterns like several days of rain. It predicts the flood risk for the next hours; if the "
         "prediction crosses the threshold tau, an alert is issued, otherwise monitoring continues.")

# 11. Algorithm 2 — damage assessment
s = d.slide("07", "Algorithm 2: Damage Assessment", "CNN / ViT segmentation of pre- and post-disaster satellite and UAV images [3], [7]")
for k, (lab, col) in enumerate((("Pre-disaster image", BLUE), ("Post-disaster image", RED))):
    y = 1.55 + k * 1.0
    b(s, 0.6, y, 1.65, 0.85, bg=GRAY)
    d.icon(s, "house", 0.72, y + 0.18, 0.48, col)
    t(s, 1.27, y, 0.95, 0.85, lab, size=10.5, bold=True, anchor="m")
b(s, 2.5, 1.95, 1.35, 1.05, bg=WHITE, line=GRAY2, lw=1.25,
  paras=[[("Align &", {"bold": True})], [("preprocess", {"bold": True})], "co-registration"], size=10.5)
b(s, 4.1, 1.85, 1.45, 1.25, bg=CHAR, paras=[[("CNN / ViT", {"bold": True, "size": 14})], "semantic segmentation"],
  size=10.5, color=WHITE)
arrow(s, 2.25, 1.98, 2.5, 2.3, MUTED, 1.5)
arrow(s, 2.25, 2.98, 2.5, 2.65, MUTED, 1.5)
arrow(s, 3.85, 2.47, 4.1, 2.47, MUTED, 1.75)
arrow(s, 5.55, 2.47, 5.8, 2.47, MUTED, 1.75)
grid = ["00012", "01123", "01233", "00122", "00011"]
for r, row in enumerate(grid):
    for c, v in enumerate(row):
        b(s, 5.82 + c * 0.29, 1.55 + r * 0.29, 0.27, 0.27, bg=DMG[int(v)][1])
t(s, 5.82, 3.03, 1.43, 0.28, "Damage map", size=11, bold=True, align="c")
for i, (lab, col) in enumerate(DMG):
    b(s, 7.6, 1.65 + i * 0.38, 0.24, 0.24, bg=col)
    t(s, 7.95, 1.6 + i * 0.38, 1.45, 0.34, lab, size=11.5, anchor="m")
t(s, 0.6, 3.6, 4.3, 0.3, "STEPS", size=10.5, bold=True, color=BLUE, spc=100)
steps = ["Input pre- and post-event images", "Align and normalise both images",
         "CNN/ViT labels each pixel or building", "Generate the damage map", "Overlay on GIS maps for responders"]
for i, st in enumerate(steps):
    y = 3.98 + i * 0.55
    b(s, 0.6, y, 0.4, 0.4, bg=AMBER, paras=str(i + 1), size=12, bold=True, margin=0)
    t(s, 1.15, y - 0.03, 3.7, 0.46, st, size=13, anchor="m")
b(s, 5.1, 3.6, 4.3, 3.15, bg=CHAR)
t(s, 5.3, 3.75, 3.9, 0.3, "EXTENSION: DISASTELLER [7]", size=10.5, bold=True, color=AMBER, spc=100)
t(s, 5.3, 4.08, 3.9, 0.55, "Four specialised vision-language agents work together on post-disaster images.",
  size=12.5, color=WHITE)
for i in range(4):
    d.icon_tile(s, "robot", 5.35 + i * 0.98, 4.75, 0.55, bg=AMBER, fg=CHAR)
for i, o in enumerate(["Damage assessment", "Alerts", "Emergency reports", "Resource & recovery plans"]):
    x = 5.3 + (i % 2) * 2.0
    y = 5.55 + (i // 2) * 0.55
    b(s, x, y, 1.9, 0.45, bg="3A4046", paras=o, size=10.5, color=WHITE, margin=0.02)
notes(s, "For damage assessment, the system takes satellite or drone images from before and after the event. After "
         "aligning them, a CNN or Vision Transformer performs semantic segmentation and labels each building or "
         "region: no damage, minor, major or destroyed. The result is a damage map overlaid on GIS for responders. "
         "DisasTeller extends this with four vision-language agents that also produce alerts, emergency reports and "
         "resource and recovery plans.")

# 12. Algorithm 3 — crisis info & evacuation (left / right split)
s = d.slide("07", "Algorithm 3: Crisis Info & Evacuation", "NLP extraction of crisis messages [6] and reinforcement-learning evacuation routing")
t(s, 0.6, 1.5, 4.3, 0.3, "CRISIS INFORMATION EXTRACTION", size=10.5, bold=True, color=BLUE, spc=100)
for k, msg in enumerate(("“Road blocked near the bridge, need rescue!”", "“Help needed in Wardha, water rising”")):
    b(s, 0.6 + k * 0.3, 1.9 + k * 0.7, 3.95, 0.55, bg=GRAY, shape="callout", paras=[[(msg, {"italic": True})]],
      size=12, align="l", margin=0.12)
b(s, 1.45, 3.45, 2.6, 0.7, bg=CHAR, paras=[[("NLP model", {"bold": True, "size": 14})], "BERT / LLM + NER"],
  size=10.5, color=WHITE)
arrow(s, 2.75, 3.2, 2.75, 3.45, MUTED, 1.5)
arrow(s, 2.75, 4.15, 2.75, 4.4, MUTED, 1.5)
d.table(s, [["Field", "Extracted value"], ["Location", "Wardha"], ["Event", "Flood"], ["Need", "Rescue"],
            ["Severity", [[("High", {"bold": True, "color": RED})]]]], [1.7, 2.6], y=4.4, header_h=0.36, row_h=0.36)
line(s, 4.95, 1.5, 4.95, 6.75, GRAY2, 1.0)
t(s, 5.2, 1.5, 4.2, 0.3, "EVACUATION ROUTING (RL)", size=10.5, bold=True, color=BLUE, spc=100)
b(s, 5.2, 2.2, 1.8, 1.0, bg=AMBER, paras=[[("Agent", {"bold": True, "size": 15})], "policy π (PPO / DQN)"], size=10.5)
b(s, 7.6, 2.2, 1.8, 1.0, bg=BLUE, paras=[[("Environment", {"bold": True, "size": 14})], "roads + hazard map"],
  size=10.5, color=WHITE)
arrow(s, 7.0, 2.45, 7.6, 2.45, CHAR, 1.5)
arrow(s, 7.6, 2.95, 7.0, 2.95, GREEN, 1.5)
t(s, 5.2, 1.9, 4.2, 0.28, "action a: choose the next road →", size=10.5, color=CHAR, align="r")
t(s, 5.2, 3.25, 4.2, 0.5, [[("← state s: ", {"bold": True}), ("location, congestion, hazard", {})],
                           [("← reward r: ", {"bold": True}), ("+ safety, − travel time", {})]], size=10.5,
  color=GREEN, after=0)
d.code(s, 5.2, 4.0, 4.2, 2.75, [
    "Input: road graph G, hazard map H",
    "s ← (loc, congestion, hazard)",
    "a ← π(s)          # next road",
    "r ← R(safety, time)",
    "update π with PPO / DQN",
    "return safest route"], size=11)
notes(s, "During a disaster people post messages like these. An NLP model such as BERT or an LLM with named entity "
         "recognition extracts structured fields - location, event, need and severity - so responders can prioritise. "
         "For evacuation, reinforcement learning treats routing as a sequence of decisions: the agent observes the "
         "state - location, congestion and hazard - chooses the next road, and gets a reward for safety and speed. "
         "Algorithms like PPO or DQN learn the best evacuation policy.")

# 13. Features / advantages / disadvantages
s = d.slide("08", "Features, Advantages & Disadvantages", "Faster and wider — but only as good as its data")
t(s, 0.6, 1.45, 4, 0.3, "KEY FEATURES", size=10.5, bold=True, color=BLUE, spc=100)
feats = [("layers", "Data fusion", "satellite, sensor, text"), ("clock", "Real-time", "continuous monitoring"),
         ("chart", "Prediction", "forecasts risk early"), ("map", "Auto mapping", "damage from imagery"),
         ("sitemap", "Decision support", "routes, resources")]
for i, (ic, lead, rest) in enumerate(feats):
    x = 0.6 + i * 1.785
    b(s, x, 1.8, 1.66, 1.35, bg=GRAY)
    d.icon_tile(s, ic, x + 0.15, 1.92, 0.42)
    t(s, x + 0.15, 2.42, 1.45, 0.7, [[(lead, {"bold": True})], [(rest, {"size": 10.5, "color": MUTED})]],
      size=12.5, after=0)
for k, (head, col, ic, rows) in enumerate((
        ("Advantages", GREEN, "check", [("Earlier warnings", "more lead time to evacuate"),
                                        ("Faster assessment", "quicker than ground surveys"),
                                        ("Better allocation", "relief reaches need first"),
                                        ("Wide coverage", "large or unreachable areas"),
                                        ("Scalable", "works 24×7 at scale")]),
        ("Disadvantages", RED, "times", [("Data scarcity", "rare events, imbalanced data"),
                                         ("Generalization", "may fail in new regions"),
                                         ("Black box", "low trust without explanation [2]"),
                                         ("Infrastructure", "power / network may fail"),
                                         ("Misinformation", "false posts; privacy risks")]))):
    x = 0.6 + k * 4.5
    b(s, x, 3.4, 4.3, 0.5, bg=col, paras=head, size=14, bold=True, color=WHITE, align="l", margin=0.15)
    for i, (lead, rest) in enumerate(rows):
        y = 4.0 + i * 0.55
        d.icon(s, ic, x + 0.05, y + 0.1, 0.27, col)
        t(s, x + 0.45, y, 3.85, 0.48, [[(lead + "  ", {"bold": True}), (rest, {"color": MUTED})]], size=12.5,
          anchor="m")
notes(s, "Key features are data fusion, real-time monitoring, prediction, automatic mapping and decision support. "
         "Advantages include more lead time, faster assessment and better use of resources. But there are real "
         "limitations: data on rare disasters is scarce, models may not transfer to new regions, black-box outputs "
         "reduce trust, infrastructure can fail during the disaster itself, and social media contains misinformation.")

# 14. Applications
s = d.slide("09", "Applications", "AI across hazards and response tasks")
apps = [("water", "Flood forecasting", "River-level and rainfall prediction for early warnings [4]."),
        ("fire", "Wildfire detection", "AIoT sensors and cameras detect fires early [5]."),
        ("quake", "Earthquake damage", "Satellite / UAV imagery maps collapsed buildings [3]."),
        ("cyclone", "Cyclone tracking", "Forecasting track and intensity to plan evacuations."),
        ("comment", "Crisis informatics", "LLMs classify social-media posts and help requests [6]."),
        ("truck", "Relief logistics", "Optimised routing of supplies, shelters and rescue teams.")]
for i, (ic, ti, desc) in enumerate(apps):
    x = 0.6 + (i % 3) * 3.0
    y = 1.5 + (i // 3) * 2.65
    b(s, x, y, 2.8, 2.45, bg=WHITE, line=GRAY2, lw=1.25)
    d.icon_tile(s, ic, x + 0.2, y + 0.2, 0.72, bg=AMBER if i % 2 == 0 else CHAR, fg=CHAR if i % 2 == 0 else AMBER)
    t(s, x + 0.2, y + 1.05, 2.45, 0.4, ti, size=15, bold=True)
    t(s, x + 0.2, y + 1.47, 2.45, 0.9, desc, size=12.5, color=MUTED)
notes(s, "Applications include flood forecasting, wildfire detection with AI-enabled IoT, earthquake damage mapping, "
         "cyclone tracking, crisis informatics using language models, and relief logistics.")

# 15. Analysis / comparison
s = d.slide("10", "Analysis & Comparison", "Traditional vs AI-based disaster management")
rows = [["Aspect", "Traditional approach", "AI-based approach", "Benefit"],
        ["Early warning", "Manual monitoring, fixed thresholds", "ML/DL forecasts on live sensor data", "More lead time"],
        ["Damage assessment", "Ground surveys (days)", "Satellite/UAV + CNN/ViT maps (hours)", "Faster response"],
        ["Information", "Phone calls, manual reports", "NLP/LLM triage of social media", "Situational awareness"],
        ["Resource allocation", "Static, pre-planned routes", "Optimization / RL adapts live", "Efficient use"],
        ["Reporting", "Manual situation reports", "Automated reports, e.g. [7]", "Quick, consistent"]]
d.table(s, rows, [1.9, 2.35, 2.55, 2.0], y=1.5, header_h=0.5, row_h=0.72, hl_col=2, size=12.5)
d.key_block(s, 5.95, "Key insight", "AI supports — it does not replace — human decision-makers; outputs must be "
            "explainable and trusted before authorities act on them [2].", h=0.85, dark=True)
notes(s, "Comparing traditional and AI-based approaches: AI gives earlier warnings, maps damage in hours instead of "
         "days, triages social media automatically, adapts routes as conditions change and generates reports quickly. "
         "But AI should support human decision-makers, and its outputs must be explainable and trusted.")

# 16. Conclusion
s = d.slide("11", "Conclusion & Future Scope", "AI strengthens the whole disaster-management cycle")
t(s, 0.6, 1.5, 4.2, 0.35, "Key takeaways", size=16, bold=True)
for i, it in enumerate(["AI supports every phase of the disaster-management cycle.",
                        "Time-series models warn early; CNN/ViT models map damage quickly.",
                        "NLP/LLMs turn crisis messages into structured, actionable data.",
                        "Optimization and RL improve evacuation and relief logistics."]):
    y = 2.0 + i * 0.9
    b(s, 0.6, y + 0.12, 0.42, 0.42, bg=AMBER, paras=str(i + 1), size=13, bold=True, margin=0)
    t(s, 1.18, y, 3.6, 0.7, it, size=13.5, anchor="m")
b(s, 5.1, 1.5, 4.3, 4.15, bg=CHAR)
t(s, 5.35, 1.65, 3.9, 0.35, "Future scope", size=16, bold=True, color=AMBER)
for i, it in enumerate(["Multimodal models fusing satellite, sensor and text data",
                        "Explainable, trustworthy AI for critical decisions [2]",
                        "Edge AI that keeps working when networks fail",
                        "Collaboration of government, research and industry"]):
    y = 2.15 + i * 0.85
    d.icon(s, "arrowr", 5.35, y + 0.2, 0.26, AMBER)
    t(s, 5.75, y, 3.5, 0.7, it, size=13, color=WHITE, anchor="m")
b(s, 0.6, 5.9, 8.8, 0.85, bg=AMBER, paras="Earlier detection  •  faster assessment  •  smarter response  — with humans in the loop",
  size=15, bold=True)
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
s = d.slide("12", "References", "IEEE format; bracketed numbers on the slides refer to this list")
for i, r in enumerate(refs):
    y = 1.45 + i * 0.66
    b(s, 0.6, y + 0.04, 0.42, 0.34, bg=AMBER if i % 2 == 0 else GRAY, paras=str(i + 1), size=11, bold=True, margin=0)
    t(s, 1.18, y, 8.2, 0.64, r, size=11.5)
notes(s, "References in IEEE format; numbers in square brackets on the slides point to this list.")

# 18. Thank you
s = d.cover("Thank you", "SEMINAR-I   |   2025–26", HAZARDS, title_size=48, extra="Questions & discussion", extra_y=3.3)
t(s, 0.6, 5.5, 8.8, 0.45, "Vedika Dandade   |   Roll No. B344", size=20, bold=True)
t(s, 0.6, 6.0, 8.8, 0.35, "Department of Computer Engineering, Bajaj Institute of Technology, Wardha", size=12.5,
  color=MUTED)
notes(s, "Thank you. I am happy to take questions.")

d.save(OUT)
print("saved", OUT, len(d.prs.slides))
