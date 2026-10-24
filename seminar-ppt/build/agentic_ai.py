"""Seminar-I deck: Agentic AI (Utkarsh Kale, B342) — "neon night" design, template-compliant structure.

Slide map (Seminar-I template order): Title · Index · Introduction · Objectives · Literature Review ·
Literature Survey (tabular, 2 slides) · Baseline Papers · System Architecture + 2 algorithm slides ·
Features/Advantages/Disadvantages · Applications · Analysis/Comparison · Conclusion · References (2) · Thank you.
"""
import math
import sys

from utkarsh_design import *  # noqa: F401,F403

TEMPLATE, ICONS, BGS, OUT = sys.argv[1:5]
d = UDeck(TEMPLATE, ICONS, BGS, "agentic_ai  ·  utkarsh_kale  ·  B342", total=18)


def thank_you_orbit(s):
    d.orbit(s, 7.7, 3.3, r=1.25)


# 1. Title (template fields: Title · Delivered By · Name · Department · Under Supervision of)
s = d._slide("bg_cover.jpg")
d.institution_card(s)
label(s, 0.6, 2.0, 5.0, "SEMINAR-I  ·  2025–26")
t(s, 0.6, 2.3, 5.6, 0.95, [[("Agentic ", {}), ("AI", {"color": CYAN})]], size=52, bold=True, anchor="m")
t(s, 0.6, 3.3, 5.3, 1.0, "Autonomous LLM Agents for Planning, Reasoning, Coordination and Task Execution", size=17,
  color=MUTED)
d.orbit(s, 7.75, 3.4, r=1.25)
for k, (lab, name, l2, l3) in enumerate((
        ("DELIVERED BY:", "Utkarsh Kale", "Roll No. B342  ·  Third Year, Semester V",
         "Department of Computer Engineering, Bajaj Institute of Technology, Wardha."),
        ("UNDER SUPERVISION OF:", "Name of Faculty", "Designation of faculty",
         "Computer Engineering Department, BIT, Wardha"))):
    x = 0.6 + k * 4.5
    glass(s, x, 5.2, 4.3, 1.75)
    label(s, x + 0.22, 5.32, 3.9, lab, color=PINK if k else CYAN)
    t(s, x + 0.22, 5.62, 3.9, 0.42, name, size=19, bold=True)
    t(s, x + 0.22, 6.04, 3.9, 0.3, l2, size=12, color=MUTED)
    t(s, x + 0.22, 6.32, 3.9, 0.55, l3, size=11, color=MUTED)
notes(s, "Good morning. My seminar topic is Agentic AI: autonomous agents built on large language models that can "
         "plan, reason, coordinate with other agents and execute tasks. I will cover how these systems work, the main "
         "algorithms, applications, and their limitations.")

# 2. Index
s = d.slide("// index", "Index")
idx = [("Introduction", "origins and inspiration"), ("Objectives", "of the seminar topic"),
       ("Literature Review", "methods and algorithms studied"), ("Literature Survey", "in tabular form"),
       ("Baseline Papers", "selected for seminar work"), ("System Architecture", "and algorithms studied"),
       ("Features", "advantages / disadvantages"), ("Applications", "where agents are used"),
       ("Analysis / Comparison", "with other tools and technologies"), ("Conclusion", "main ideas and future scope"),
       ("References", "IEEE format")]
for col, chunk in enumerate((idx[:6], idx[6:])):
    x = 0.75 + col * 4.55
    n = len(chunk)
    line(s, x + 0.17, 1.82, x + 0.17, 1.82 + (n - 1) * 0.86, EDGE, 1.5)
    for i, (head, sub) in enumerate(chunk):
        k = col * 6 + i + 1
        y = 1.65 + i * 0.86
        grad_box(s, x, y, 0.34, 0.34, shape="oval", paras=f"{k:02d}", size=9, bold=True, font=MONO, angle=45,
                 margin=0)
        t(s, x + 0.55, y - 0.08, 3.7, 0.34, head, size=16, bold=True)
        t(s, x + 0.55, y + 0.26, 3.7, 0.3, sub, size=11.5, color=MUTED, font=MONO)
notes(s, "This is the flow of my presentation, following the Seminar-I template.")

# 3. Introduction
s = d.slide("// 01 · introduction — origins & inspiration", "Introduction: From Chatbots to Agents")
glass(s, 0.6, 1.6, 8.8, 0.95)
d.icon_orb(s, "robot", 0.8, 1.75, 0.65)
t(s, 1.65, 1.6, 7.6, 0.95, [[("Agentic AI ", {"bold": True, "color": CYAN}),
                             ("— LLM-based systems that pursue goals autonomously: they plan, use tools, remember "
                              "context and verify results with limited human supervision [1], [2].", {})]],
  size=14, anchor="m")
label(s, 0.6, 2.82, 5, "BACKGROUND & HISTORY")
grad_box(s, 0.8, 3.6, 8.4, 0.05, shape="rect", radius=0)
miles = [("Pre-2020", "Rule-based and RL agents in narrow tasks"),
         ("2020–22", "LLMs as text generators (GPT-3, ChatGPT)"),
         ("2022–23", "Reasoning + tool use: Chain-of-Thought, ReAct [12]"),
         ("2023–24", "Multi-agent frameworks (AutoGen, CrewAI)"),
         ("2024–26", "Open protocols MCP, A2A; production agents [6]")]
for i, (yr, desc) in enumerate(miles):
    cx = 1.3 + i * 1.85
    t(s, cx - 0.85, 3.17, 1.7, 0.32, yr, size=13, bold=True, color=CYAN if i == 4 else VIOLET, align="c", font=MONO)
    box(s, cx - 0.12, 3.505, 0.24, 0.24, bg=CYAN if i == 4 else VIOLET, shape="oval")
    t(s, cx - 0.88, 3.85, 1.76, 0.85, desc, size=11.5, color=MUTED, align="c")
label(s, 0.6, 4.85, 6, "INSPIRATION — WHY DO WE NEED AGENTS?")
needs = [("layers", "Real tasks are multi-step", "Research, coding and booking need many dependent steps."),
         ("globe", "Models need live data", "Tools give access to the web, code, databases and APIs."),
         ("check", "Results must be verified", "Feedback loops let an agent catch and fix its own errors.")]
for i, (ic, head, body) in enumerate(needs):
    x = 0.6 + i * 3.0
    glass(s, x, 5.2, 2.8, 1.6)
    d.icon_orb(s, ic, x + 0.18, 5.36, 0.5)
    t(s, x + 0.8, 5.33, 1.92, 0.55, head, size=13.5, bold=True, anchor="m")
    t(s, x + 0.18, 5.97, 2.5, 0.8, body, size=12.5, color=MUTED)
notes(s, "Classic LLM use is prompt-response: you ask, it answers once. Agentic AI turns the model into the brain of a "
         "loop: it breaks a goal into steps, calls tools such as web search or a code interpreter, stores what it "
         "learns, and checks its own output. Historically this grew from narrow rule-based agents, to LLMs in 2020-22, "
         "to reasoning-and-acting methods like ReAct, to multi-agent frameworks, and now to open protocols like MCP "
         "and A2A.")

# 4. Objectives — hub
s = d.slide("// 02 · objectives of the seminar topic", "Objectives")
cx, cy = 5.0, 4.05
objs = [((0.6, 1.65), "Architecture", "How LLM agents plan, remember, use tools and self-critique."),
        ((6.35, 1.65), "Coordination", "Centralized, hierarchical and decentralized multi-agent patterns."),
        ((0.6, 3.5), "Memory & context", "Short- and long-term memory for long-horizon tasks."),
        ((6.35, 3.5), "Applications", "Real agent systems in software, research, security, robotics."),
        ((3.475, 5.45), "Challenges", "Reliability, safety, evaluation and cost; future directions.")]
for (x, y), _, _ in objs:
    line(s, cx, cy, x + 1.525, y + 0.65, EDGE, 1.5)
box(s, cx - 1.1, cy - 1.1, 2.2, 2.2, bg=DEEP, shape="oval", alpha=25)
grad_box(s, cx - 0.85, cy - 0.85, 1.7, 1.7, shape="oval", angle=45,
         paras=[[("GOAL", {"font": MONO, "size": 10, "bold": True})],
                [("Understand reliable autonomous agents", {"bold": True})]], size=12.5, margin=0.12)
for i, ((x, y), head, desc) in enumerate(objs):
    glass(s, x, y, 3.05, 1.3)
    t(s, x + 0.2, y + 0.12, 0.6, 0.35, f"{i + 1:02d}", size=13, bold=True, color=CYAN, font=MONO)
    t(s, x + 0.75, y + 0.1, 2.2, 0.38, head, size=14.5, bold=True)
    t(s, x + 0.2, y + 0.52, 2.7, 0.75, desc, size=12, color=MUTED)
notes(s, "By the end of this seminar I aim to explain the internal architecture of an agent, compare ways of "
         "coordinating several agents, explain memory management, show real applications, and critically discuss the "
         "open challenges. Together they answer one question: how do we build reliable autonomous agents?")

# 5. Literature review
s = d.slide("// 03 · literature review — methods & algorithms studied", "Literature Review")
stats = [("12", "sources studied, 2022–2026", CYAN), ("6", "IEEE journal & conference papers", VIOLET),
         ("5", "arXiv, ACL and ICLR papers", VIOLET), ("1", "industry engineering report", PINK)]
for i, (n, lab, col) in enumerate(stats):
    y = 1.65 + i * 1.05
    glass(s, 0.6, y, 2.5, 0.92)
    t(s, 0.75, y, 0.85, 0.92, n, size=28, bold=True, color=col, font=MONO, anchor="m")
    t(s, 1.55, y, 1.48, 0.92, lab, size=11.5, color=MUTED, anchor="m")
themes = [("book", "Surveys & taxonomies", "[1] [2] [3]", "Agent = perception + planning + memory + action."),
          ("cogs", "Frameworks & runtime", "[4] [10]", "Blueprint vs runtime; hybrid multi-agent designs."),
          ("db", "Memory", "[5]", "Learn when to store, retrieve, summarize, discard."),
          ("plug", "Protocols", "[6]", "MCP for tools; A2A for agent-to-agent messages."),
          ("shield", "Security & testing", "[7] [8]", "Prompt injection and tool abuse need fuzzing."),
          ("robot", "Planning & multi-agent", "[9] [11] [12]", "ReAct loops, replanning, orchestrator-workers.")]
for i, (ic, ti, refs, body) in enumerate(themes):
    x = 3.3 + (i % 2) * 3.05
    y = 1.65 + (i // 2) * 1.38
    glass(s, x, y, 2.95, 1.25)
    d.icon(s, ic, x + 0.17, y + 0.17, 0.34, CYAN if i % 2 == 0 else VIOLET)
    t(s, x + 0.62, y + 0.1, 2.25, 0.32, ti, size=13, bold=True)
    t(s, x + 0.62, y + 0.42, 2.25, 0.25, refs, size=10, color=VIOLET, font=MONO, bold=True)
    t(s, x + 0.17, y + 0.72, 2.7, 0.5, body, size=11.5, color=MUTED)
grad_box(s, 0.6, 5.95, 8.8, 0.8, align="l", margin=0.2, anchor="m",
         paras=[[("My interpretation:  ", {"bold": True}),
                 ("reliability depends on orchestration, memory, coordination, evaluation and safeguards — not on "
                  "model capability alone.", {})]], size=13.5)
notes(s, "I studied twelve sources: six IEEE papers, five arXiv, ACL and ICLR papers, and one industry engineering "
         "report. I grouped them into six themes, each feeding one part of the architecture. The IEEE ICOIN 2026 "
         "survey was my architectural starting point. My own interpretation: a strong model is not enough - "
         "orchestration, memory and checking matter just as much.")

# 6-7. Literature survey in tabular form (template columns)
lit = [
    ("A Survey on LLM Agents: Architecture, Applications, and Challenges", "IEEE ICOIN, 2026",
     "Surveys agent architecture — memory, planning, tool use, control flows — plus evaluation, reliability, scalability."),
    ("Agentic AI: Architectures, Taxonomies, and Evaluation of LLM Agents",
     "V. Arunkumar, G. R. Gangadharan, R. Buyya · arXiv, 2026",
     "Taxonomy of perception, planning, action, tools and collaboration; evaluation methods and failure modes."),
    ("From Prompt-Response to Goal-Directed Systems", "M. Alenezi · arXiv, 2026",
     "Evolution of agent software architecture: typed tool interfaces, multi-agent topologies, governance."),
    ("The Auton Agentic AI Framework", "S. Cao et al. · arXiv, 2026",
     "Separates the cognitive blueprint from runtime execution; covers memory, MCP, safety, runtime optimization."),
    ("Agentic Memory (AgeMem)", "Y. Yu et al. · ACL, 2026",
     "Unified long/short-term memory: the agent learns when to store, retrieve, update, summarize or discard."),
    ("MCP and A2A Protocol for Scalable Agentic AI Systems", "IEEE ICICDS, 2026",
     "MCP gives standardized tool/data access; A2A enables communication and coordination between agents."),
    ("LLM-Based Intelligent Agents for Cybersecurity", "IEEE Access, 2026",
     "Tool-using agents for automated vulnerability discovery; discusses reliability, cost and ethics."),
    ("A Survey of Fuzzing Techniques for LLM Agents", "IEEE BDAI, 2026",
     "Agent security testing: indirect prompt injection, planning hallucination and tool abuse."),
    ("GLaMP: Grounded LM-Based Multiagent System", "IEEE Trans. Industrial Electronics, 2026",
     "VLM + LLM planning with symbolic grounding and failure-aware replanning for long-horizon robot tasks."),
    ("Beyond Single-Framework Architectures", "IEEE Access, 2026",
     "Evaluates CrewAI, AutoGen and LangChain; proposes a hybrid design (results on its own benchmark)."),
]
for part in (0, 1):
    s = d.slide("// 03 · literature survey in tabular form", f"Literature Survey in Tabular Form ({part + 1}/2)")
    rows = [["Sr. No", "Details of Papers", "Work reported"]]
    for i, (ti, v, w) in enumerate(lit[part * 5:(part + 1) * 5], part * 5 + 1):
        rows.append([str(i), [[(ti, {"bold": True})], [(v, {"size": 10.5, "color": MUTED})]], w])
    d.table(s, rows, [0.8, 4.0, 4.0], y=1.55, row_h=0.95, num_col=True)
    notes(s, "This table summarises each paper and what it reports. " +
          ("The first five cover the overall architecture, taxonomy, software evolution, runtime framework and memory."
           if part == 0 else
           "These five cover protocols, security, fuzzing, grounded robotic planning and a comparison of agent frameworks."))

# 8. Baseline papers
s = d.slide("// 04 · baseline papers", "Baseline Papers Selected for Seminar Work")
glass(s, 0.6, 1.6, 8.8, 2.45, edge=CYAN)
label(s, 0.85, 1.72, 3, "PRIMARY BASELINE", color=PINK)
t(s, 0.85, 2.1, 1.4, 0.9, "[1]", size=44, bold=True, color=CYAN, font=MONO, anchor="m")
t(s, 2.3, 1.98, 6.9, 0.45, "A Survey on LLM Agents: Architecture, Applications, and Challenges", size=17, bold=True)
t(s, 2.3, 2.45, 6.9, 0.3, "IEEE ICOIN, 2026", size=12, italic=True, color=MUTED)
for k, (lab, body) in enumerate((("WHY SELECTED", "Broad, recent view of agent architecture — the starting point."),
                                 ("USED FOR", "Overall architecture: planning, memory, tools, control flow."))):
    x = 2.3 + k * 3.5
    label(s, x, 2.95, 3.3, lab, color=VIOLET, size=9.5)
    t(s, x, 3.23, 3.3, 0.75, body, size=12.5)
sup = [("[2]", "Agentic AI: Architectures, Taxonomies, and Evaluation of LLM Agents", "arXiv, 2026",
        "clear taxonomy and evaluation dimensions.", "agent types, failure modes, evaluation."),
       ("[6]", "MCP and A2A Protocol for Scalable Agentic AI Systems", "IEEE ICICDS, 2026",
        "explains how agents connect to tools and each other.", "the interoperability layer.")]
for k, (ref, ti, venue, why, used) in enumerate(sup):
    x = 0.6 + k * 4.5
    glass(s, x, 4.25, 4.3, 2.5)
    label(s, x + 0.22, 4.38, 2.5, "SUPPORTING", color=VIOLET)
    t(s, x + 3.1, 4.28, 1.0, 0.45, ref, size=22, bold=True, color=CYAN, font=MONO, align="r")
    t(s, x + 0.22, 4.7, 3.85, 0.65, ti, size=13.5, bold=True)
    t(s, x + 0.22, 5.35, 3.85, 0.28, venue, size=11, italic=True, color=MUTED)
    t(s, x + 0.22, 5.7, 3.85, 1.0, [[("Why: ", {"bold": True, "color": CYAN}), (why, {})],
                                     [("Used for: ", {"bold": True, "color": CYAN}), (used, {})]], size=12, after=4)
notes(s, "I selected the ICOIN 2026 survey as my primary baseline because it covers the full agent architecture. The "
         "taxonomy paper by Arunkumar, Gangadharan and Buyya helped me classify agents and their failure modes, and the "
         "MCP/A2A paper explains the interoperability layer. Focused papers 4, 5 and 7 to 10 then supplied the runtime, "
         "memory, security and multi-agent details.")

# 9. System architecture
s = d.slide("// 05 · system architecture / algorithms studied", "System Architecture",
            "Hierarchical multi-agent design: plan → orchestrate → act through tools → verify [1], [6], [11]")
glass(s, 0.5, 3.15, 1.2, 1.0, edge=CYAN)
d.icon(s, "user", 0.94, 3.25, 0.32, CYAN)
t(s, 0.5, 3.6, 1.2, 0.45, "User goal", size=12, bold=True, align="c")
glass(s, 1.95, 2.75, 1.5, 1.8)
label(s, 1.95, 2.88, 1.5, "PLANNER", color=VIOLET, size=10, align="c")
t(s, 2.05, 3.2, 1.3, 1.25, ["understand goal", "decompose", "task graph"], size=11.5, color=MUTED, align="c",
  after=6)
ocx, ocy = 5.15, 3.65
workers = [((3.75, 1.75), "Research agent"), ((5.6, 1.75), "Coding agent"), ((3.75, 5.0), "Testing agent"),
           ((5.6, 5.0), "Critique agent")]
for (x, y), _ in workers:
    line(s, ocx, ocy, x + 0.65, y + 0.275, VIOLET, 1.25, dash=True, alpha=70)
box(s, ocx - 0.95, ocy - 0.95, 1.9, 1.9, bg=DEEP, shape="oval", alpha=28)
grad_box(s, ocx - 0.72, ocy - 0.72, 1.44, 1.44, shape="oval", angle=45,
         paras=[[("Orchestrator", {"bold": True})], "agent"], size=12.5, margin=0.02)
for (x, y), lab in workers:
    glass(s, x, y, 1.3, 0.55, edge=VIOLET)
    t(s, x, y, 1.3, 0.55, lab, size=11, bold=True, align="c", anchor="m")
t(s, 4.85, 2.45, 0.6, 0.26, "A2A", size=10, bold=True, color=PINK, font=MONO, align="c")
glass(s, 7.05, 2.3, 1.4, 2.75)
label(s, 7.05, 2.42, 1.4, "TOOLS", size=10, align="c")
for i, (ic, lab) in enumerate((("search", "Web search"), ("terminal", "Code exec"), ("db", "APIs / DB"),
                               ("file", "Files"))):
    y = 2.8 + i * 0.55
    d.icon(s, ic, 7.17, y + 0.06, 0.28, CYAN)
    t(s, 7.52, y, 0.9, 0.4, lab, size=11, color=MUTED, anchor="m")
grad_box(s, 8.65, 3.15, 0.85, 1.0, paras=[[("Output", {"bold": True})]], size=12, angle=45, margin=0.02)
arrow(s, 1.7, 3.65, 1.95, 3.65, MUTED, 1.75)
arrow(s, 3.45, 3.65, ocx - 0.72, 3.65, MUTED, 1.75)
arrow(s, ocx + 0.72, 3.65, 7.05, 3.65, CYAN, 1.75, head="both")
t(s, 6.0, 3.32, 0.9, 0.28, "MCP", size=10, bold=True, color=CYAN, font=MONO, align="c")
arrow(s, 8.45, 3.65, 8.65, 3.65, MUTED, 1.75)
glass(s, 3.6, 5.85, 4.85, 0.62)
d.icon(s, "db", 3.75, 5.99, 0.32, VIOLET)
t(s, 4.2, 5.85, 4.2, 0.62, [[("Memory  ", {"bold": True, "color": VIOLET}),
                             ("short-term · long-term (vector DB) · shared", {"color": MUTED})]], size=11.5, anchor="m")
arrow(s, ocx, ocy + 0.72, ocx, 5.85, VIOLET, 1.5, head="both")
path(s, [(9.075, 4.15), (9.075, 6.75), (2.7, 6.75), (2.7, 4.55)], PINK, 1.5, dash=True)
box(s, 2.95, 6.62, 1.55, 0.27, bg=BG, line=PINK, lw=1, radius=0.13, paras="verify → replan", size=9.5, bold=True,
    color=PINK, font=MONO, margin=0.01)
notes(s, "This is the overall architecture. The user gives a goal; the planner understands it, decomposes it and builds a "
         "task graph. The orchestrator agent assigns subtasks to specialised worker agents - research, coding, testing "
         "and critique - which talk to each other through A2A and reach external tools through MCP. A memory layer "
         "keeps short-term, long-term and shared context. The output is verified, and on failure the system replans.")

# 10. Algorithms studied (1/2) — ReAct
s = d.slide("// 05 · algorithms studied (1/2)", "ReAct: Reason + Act Loop",
            "Interleaves reasoning (thought) with tool actions and observations until the goal is met [12]")
cx, cy, r = 2.75, 4.25, 1.55
box(s, cx - r, cy - r, 2 * r, 2 * r, shape="oval", line=CYAN, lw=2, line_alpha=55)
for phi in (-45, 45, 135, 225):
    a = math.radians(phi)
    px, py = cx + r * math.cos(a), cy + r * math.sin(a)
    tri = box(s, px - 0.11, py - 0.11, 0.22, 0.22, bg=CYAN, shape="rect")
    tri._element.spPr.find(qn("a:prstGeom")).set("prst", "triangle")
    tri.rotation = phi + 180
glass(s, cx - 0.6, cy - 0.6, 1.2, 1.2, radius=0.6)
t(s, cx - 0.6, cy - 0.6, 1.2, 1.2, [[("goal G", {"bold": True, "color": TEXT})], "history H"], size=11, color=MUTED,
  font=MONO, align="c", anchor="m", after=0)
nodes = [((cx, cy - r), "Thought", "reason about next step", "grad"), ((cx + r, cy), "Action", "call a tool", CYAN),
         ((cx, cy + r), "Observation", "read tool result", "pink"), ((cx - r, cy), "Update", "add (r, a, o) to H", VIOLET)]
for (nx, ny), ti, sub, sty in nodes:
    paras = [[(ti, {"bold": True, "size": 13.5})], [(sub, {"size": 10, "color": TEXT})]]
    if sty == "grad":
        grad_box(s, nx - 0.78, ny - 0.33, 1.56, 0.66, paras=paras, angle=0, margin=0.02)
    elif sty == "pink":
        grad_box(s, nx - 0.78, ny - 0.33, 1.56, 0.66, paras=paras, c1="BE185D", c2=DEEP, margin=0.02)
    else:
        b_ = glass(s, nx - 0.78, ny - 0.33, 1.56, 0.66, bg=PANEL2, edge=sty, alpha=None)
        fill(b_.text_frame, paras, 13, TEXT, align="c", font=BODY)
d.code(s, 5.3, 1.75, 4.1, 3.3, [
    "Input: goal G, environment E",
    "H ← ∅                 # history",
    "while not Done(G) do",
    "  r ← LLM_Reason(G, H) # thought",
    "  a ← Select_Tool(r)   # action",
    "  o ← Execute(a, E)    # observe",
    "  H ← H ∪ {(r, a, o)}",
    "  if Need_Replan(o):",
    "      G ← Update(G, o)",
    "return FinalAnswer(G, H)"], size=11, title="react_loop.algo")
glass(s, 5.3, 5.2, 4.1, 1.55)
label(s, 5.5, 5.3, 3.5, "EXAMPLE", color=PINK, size=9.5)
t(s, 5.5, 5.58, 3.75, 1.15, [[("“What is the weather in Wardha?”", {"bold": True, "italic": True})],
                             [("Thought: needs live data → Action: weather_api(\"Wardha\") → Observation: 31 °C, "
                               "clear → Answer", {"color": MUTED})]], size=12, after=3)
notes(s, "ReAct, proposed by Yao et al., is the core loop inside most agents. At each step the model first produces a "
         "Thought - its reasoning about what to do. It then picks an Action, usually a tool call, and reads the "
         "Observation. These go into the history so the next step is better informed. The loop stops when the goal is "
         "met. In the example the agent realises it needs live data and calls a weather tool.")

# 11. Algorithms studied (2/2) — planning, coordination, memory
s = d.slide("// 05 · algorithms studied (2/2)", "Planning, Coordination & Memory",
            "Task decomposition into a task graph, multi-agent coordination and context management [5], [9]")
label(s, 0.6, 1.68, 8, "TASK DECOMPOSITION  —  example goal: a research report")
grad_box(s, 0.6, 2.25, 1.25, 0.85, paras=[[("Goal", {"bold": True})], "research report"], size=11.5, angle=45)
tasks = [((2.15, 2.0), "t1  Search news", "research agent"), ((2.15, 2.78), "t2  Search papers", "research agent"),
         ((4.05, 2.39), "t3  Analyse data", "coding agent"), ((5.85, 2.39), "t4  Draft report", "writer agent"),
         ((7.65, 2.39), "t5  Review & fix", "critique agent")]
for (x, y), ti, ag in tasks:
    glass(s, x, y, 1.6 if x < 7 else 1.75, 0.62, edge=VIOLET)
    t(s, x, y + 0.03, 1.6 if x < 7 else 1.75, 0.58, [[(ti, {"bold": True})], [(ag, {"color": CYAN, "size": 9.5,
                                                                                    "font": MONO})]],
      size=11.5, align="c", anchor="m", after=0)
arrow(s, 1.85, 2.55, 2.15, 2.31, MUTED, 1.5)
arrow(s, 1.85, 2.8, 2.15, 3.09, MUTED, 1.5)
arrow(s, 3.75, 2.31, 4.05, 2.6, MUTED, 1.5)
arrow(s, 3.75, 3.09, 4.05, 2.8, MUTED, 1.5)
arrow(s, 5.65, 2.7, 5.85, 2.7, MUTED, 1.5)
arrow(s, 7.45, 2.7, 7.65, 2.7, MUTED, 1.5)
label(s, 0.6, 3.68, 5, "COORDINATION PATTERNS")
pats = [("Centralized", "+ simple control", "− bottleneck"), ("Hierarchical", "+ scales well", "− more delay"),
        ("Decentralized", "+ no single point", "− hard to sync")]
for i, (ti, pro, con) in enumerate(pats):
    x = 0.6 + i * 1.78
    glass(s, x, 4.0, 1.68, 2.75)
    t(s, x, 4.08, 1.68, 0.32, ti, size=12.5, bold=True, align="c")
    mx, my = x + 0.84, 4.95
    if i == 0:
        pts = [(mx - 0.5, my + 0.35), (mx, my + 0.45), (mx + 0.5, my + 0.35)]
        for px, py in pts:
            line(s, mx, my - 0.12, px, py, EDGE, 1.5)
        grad_box(s, mx - 0.15, my - 0.3, 0.3, 0.3, shape="oval", angle=45)
        for px, py in pts:
            box(s, px - 0.1, py - 0.1, 0.2, 0.2, bg=CYAN, shape="oval")
    elif i == 1:
        lv1 = [(mx - 0.35, my + 0.05), (mx + 0.35, my + 0.05)]
        lv2 = [(mx - 0.55, my + 0.45), (mx - 0.18, my + 0.45), (mx + 0.18, my + 0.45), (mx + 0.55, my + 0.45)]
        for px, py in lv1:
            line(s, mx, my - 0.28, px, py, EDGE, 1.5)
        for k, (px, py) in enumerate(lv2):
            line(s, *lv1[k // 2], px, py, EDGE, 1.5)
        grad_box(s, mx - 0.13, my - 0.4, 0.26, 0.26, shape="oval", angle=45)
        for px, py in lv1:
            box(s, px - 0.1, py - 0.1, 0.2, 0.2, bg=VIOLET, shape="oval")
        for px, py in lv2:
            box(s, px - 0.07, py - 0.07, 0.14, 0.14, bg=CYAN, shape="oval")
    else:
        pts = [(mx - 0.4, my - 0.25), (mx + 0.4, my - 0.25), (mx + 0.4, my + 0.35), (mx - 0.4, my + 0.35)]
        for a_ in range(4):
            for b2 in range(a_ + 1, 4):
                line(s, *pts[a_], *pts[b2], EDGE, 1.5)
        for px, py in pts:
            box(s, px - 0.1, py - 0.1, 0.2, 0.2, bg=CYAN, shape="oval")
    t(s, x + 0.08, 5.65, 1.52, 1.0, [[(pro, {"color": GREEN, "bold": True})], [(con, {"color": RED, "bold": True})]],
      size=11, align="c", after=3)
label(s, 6.05, 3.68, 3.4, "CONTEXT MANAGEMENT [5]")
d.code(s, 6.05, 4.0, 3.35, 2.75, ["st  ← recent(k)", "lt  ← retrieve(G, vecDB)", "ctx ← merge(st, lt)",
                                  "if too_long(ctx):", "  ctx ← summarize(ctx)", "return ctx   # to LLM"],
       size=10.5, title="memory.algo")
notes(s, "For complex goals the planner asks the LLM for a plan and decomposes it into subtasks with dependencies - a "
         "task graph. Independent tasks such as the two searches run in parallel. Each subtask goes to a specialised "
         "agent. Agents can be coordinated centrally, hierarchically or in a decentralized way, each with trade-offs. "
         "Finally, context management keeps the prompt lean: it merges recent turns with retrieved long-term memory "
         "and summarises when the context gets too long, as studied in the AgeMem paper.")

# 12. Features / advantages / disadvantages
s = d.slide("// 06 · features / advantages / disadvantages", "Features, Advantages & Disadvantages")
cols = [("Features", CYAN, (DEEP, "0891B2"), "star", None,
         [("Autonomy", "pursues a goal over many steps"), ("Planning", "breaks goals into subtasks"),
          ("Tool use", "web, code, APIs, databases"), ("Memory", "short- and long-term context"),
          ("Reflection", "verifies and replans")]),
        ("Advantages", GREEN, ("047857", "10B981"), "check", "check",
         [("Complex tasks", "handles multi-step workflows"), ("Specialisation", "agents work in parallel"),
          ("Live data", "external tools and sources"), ("Productivity", "less repetitive human effort"),
          ("Interoperable", "MCP / A2A ease scaling [6]")]),
        ("Disadvantages", RED, ("9F1239", "F43F5E"), "warn", "times",
         [("Error chains", "mistakes compound over steps"), ("Security", "prompt injection, tool abuse [8]"),
          ("Cost", "many LLM calls, higher latency"), ("Evaluation", "hard to test reliably [2]"),
          ("Oversight", "still needs human checks")])]
for k, (head, col, (c1, c2), ic, mark, items) in enumerate(cols):
    x = 0.6 + k * 3.0
    glass(s, x, 1.6, 2.8, 5.2)
    d.icon_orb(s, ic, x + 0.2, 1.78, 0.5, c1, c2)
    t(s, x + 0.85, 1.78, 1.85, 0.5, head, size=17, bold=True, color=col, anchor="m")
    for i, (lead, rest) in enumerate(items):
        y = 2.5 + i * 0.84
        if mark:
            d.icon(s, mark, x + 0.22, y + 0.12, 0.24, col)
        else:
            box(s, x + 0.28, y + 0.19, 0.12, 0.12, bg=col, shape="oval")
        t(s, x + 0.6, y, 2.1, 0.78, [[(lead, {"bold": True})], [(rest, {"size": 11.5, "color": MUTED})]], size=13.5,
          after=0)
        if i < 4:
            line(s, x + 0.2, y + 0.8, x + 2.6, y + 0.8, EDGE, 0.75)
notes(s, "Key features are autonomy, planning, tool use, memory and reflection. The advantages follow: agents handle "
         "complex workflows, specialise and parallelise, and use live data. The disadvantages are important: one wrong "
         "step can cascade, external content can inject malicious instructions, multi-agent systems are costly, and "
         "reliable evaluation is still an open problem.")

# 13. Applications — hub & spoke
s = d.slide("// 07 · applications", "Applications", "Where agentic AI is already deployed")
cx, cy, rx, ry = 5.0, 4.25, 3.2, 1.95
apps = [(-90, "code", "Software engineering", "Agents write, test and debug code."),
        (-30, "search", "Research assistants", "Parallel search agents compile reports [11]."),
        (30, "bug", "Cybersecurity", "Vulnerability discovery and testing [7]."),
        (90, "robot", "Industrial robotics", "Long-horizon planning, replanning [9]."),
        (150, "cogs", "Business workflows", "Tickets, data entry and reporting."),
        (210, "user", "Personal assistants", "Email, scheduling, travel via tools.")]
pos = []
for ang, *_ in apps:
    a = math.radians(ang)
    pos.append((cx + rx * math.cos(a), cy + ry * math.sin(a)))
for px, py in pos:
    line(s, cx, cy, px, py, EDGE, 1.5)
box(s, cx - 1.0, cy - 1.0, 2.0, 2.0, bg=DEEP, shape="oval", alpha=28)
grad_box(s, cx - 0.68, cy - 0.68, 1.36, 1.36, shape="oval", angle=45, paras=[[("Agentic", {"bold": True})],
                                                                             [("AI", {"bold": True})]], size=14)
for (px, py), (ang, ic, ti, desc) in zip(pos, apps):
    x, y = px - 1.35, py - 0.5
    glass(s, x, y, 2.7, 1.0)
    d.icon_orb(s, ic, x + 0.15, y + 0.2, 0.6, *((DEEP, "0891B2") if ang % 60 else ("BE185D", DEEP)))
    t(s, x + 0.85, y + 0.08, 1.8, 0.38, ti, size=13, bold=True, anchor="m")
    t(s, x + 0.85, y + 0.46, 1.8, 0.52, desc, size=10.5, color=MUTED)
notes(s, "Agentic AI is already used in software engineering, where agents write and test code; in research, where "
         "Anthropic describes an orchestrator that runs several search agents in parallel; in cybersecurity for "
         "vulnerability discovery; in industrial robotics for long-horizon planning such as GLaMP; and in business and "
         "personal productivity.")

# 14. Analysis / comparison
s = d.slide("// 08 · analysis / comparison", "Analysis / Comparison",
            "Agentic approach vs other technologies and tools — and its benefits")
rows = [["Aspect", "Single LLM", "Single agent (ReAct)", "Multi-agent system"],
        ["Task type", "One-shot answers", "Multi-step tasks", "Large, parallel, multi-skill"],
        ["Tools", "None", "Yes", "Specialised per agent"],
        ["Memory", "Prompt window only", "Short + long-term", "Per-agent + shared"],
        ["Error handling", "User re-prompts", "Self-reflection loop", "Critique agents + verification"],
        ["Cost / latency", "Low", "Medium", "High — many LLM calls [11]"]]
d.table(s, rows, [1.7, 2.2, 2.3, 2.6], y=1.65, header_h=0.42, row_h=0.42, size=11.5, hl_col=3)
label(s, 0.6, 4.35, 8, "AGENT FRAMEWORKS COMPARED [10]")
fws = [("CrewAI", "role-based agent crews", "quick team-of-roles prototypes"),
       ("AutoGen", "agents collaborate by conversation", "dialogue-driven problem solving"),
       ("LangChain / LangGraph", "graph-based, stateful workflows", "controlled production pipelines")]
for i, (n, style, best) in enumerate(fws):
    x = 0.6 + i * 3.0
    glass(s, x, 4.68, 2.8, 1.25)
    t(s, x + 0.18, 4.75, 2.5, 0.35, n, size=13.5, bold=True, color=CYAN)
    t(s, x + 0.18, 5.1, 2.5, 0.3, style, size=11.5, color=TEXT)
    t(s, x + 0.18, 5.42, 2.5, 0.45, [[("best for: ", {"color": VIOLET, "bold": True}), (best, {"color": MUTED})]],
      size=11)
grad_box(s, 0.6, 6.1, 8.8, 0.68, align="l", margin=0.2, anchor="m", paras=[
    [("Benefit:  ", {"bold": True}), ("agents turn a model that answers into a system that acts, verifies and scales — "
                                     "start simple, add agents only when needed.", {})]], size=12.5)
notes(s, "Comparing three levels: a single LLM is cheap but cannot act; a single agent with ReAct and tools handles "
         "multi-step tasks; a multi-agent system handles large parallel work but costs more. Among frameworks, CrewAI "
         "organises agents as role-based crews, AutoGen as conversations between agents, and LangGraph as stateful "
         "graphs. Paper 10 compares CrewAI, AutoGen and LangChain and proposes a hybrid; its numbers apply to its own "
         "benchmark. The main benefit is moving from answering to acting and verifying.")

# 15. Conclusion
s = d.slide("// 09 · conclusion", "Conclusion")
grad_box(s, 0.6, 1.6, 8.8, 1.05, align="l", margin=0.25, anchor="m", paras=[
    [("Reliability is a system property: ", {"bold": True}),
     ("orchestration, memory, coordination, evaluation and safeguards matter as much as the model.", {})]], size=15)
label(s, 0.6, 2.88, 6, "MAIN IDEAS & RESULTS")
ideas = ["Agentic AI moves LLMs from answering prompts to completing goals.",
         "ReAct loops, task decomposition and memory are the core building blocks.",
         "Multi-agent designs add specialisation and parallelism — at higher cost.",
         "MCP and A2A make tools and agents interoperable."]
for i, it in enumerate(ideas):
    x = 0.6 + (i % 2) * 4.5
    y = 3.2 + (i // 2) * 1.05
    glass(s, x, y, 4.3, 0.92)
    t(s, x + 0.18, y, 0.55, 0.92, f"{i + 1:02d}", size=15, bold=True, color=CYAN, font=MONO, anchor="m")
    t(s, x + 0.75, y, 3.45, 0.92, it, size=13, anchor="m")
label(s, 0.6, 5.42, 6, "FUTURE SCOPE", color=PINK)
fut = ["Learned long-term memory [5]", "Standard reliability benchmarks [2]", "Prompt-injection defences [8]",
       "Domain agents: security, robotics [7], [9]"]
for i, f_ in enumerate(fut):
    x = 0.6 + i * 2.24
    glass(s, x, 5.75, 2.08, 1.0, edge=PINK)
    d.icon(s, "arrowr", x + 0.15, 5.98, 0.24, PINK)
    t(s, x + 0.48, 5.75, 1.55, 1.0, f_, size=11.5, anchor="m")
notes(s, "To conclude: agentic AI is a shift from prompt-response to goal-directed systems. Its building blocks are the "
         "ReAct loop, planning, memory and tools; multi-agent systems add specialisation; MCP and A2A connect "
         "everything. Future work is in learned memory, standard evaluation, security and domain-specific agents. My "
         "main conclusion is that reliability comes from the whole system design, not just a bigger model.")

# 16-17. References (IEEE format)
refs = [
    "“A Survey on LLM Agents: Architecture, Applications, and Challenges,” in Proc. Int. Conf. Information "
    "Networking (ICOIN), IEEE, 2026. [Online]. Available: https://ieeexplore.ieee.org/document/11480623/",
    "V. Arunkumar, G. R. Gangadharan, and R. Buyya, “Agentic Artificial Intelligence (AI): Architectures, "
    "Taxonomies, and Evaluation of Large Language Model Agents,” arXiv:2601.12560, 2026.",
    "M. Alenezi, “From Prompt-Response to Goal-Directed Systems: The Evolution of Agentic AI Software "
    "Architecture,” arXiv:2602.10479, 2026.",
    "S. Cao et al., “The Auton Agentic AI Framework,” arXiv:2602.23720, 2026.",
    "Y. Yu et al., “Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for Large "
    "Language Model Agents,” in Proc. 64th Annu. Meeting Assoc. Comput. Linguistics (ACL), 2026.",
    "“Model Context Protocol (MCP) and Agent-to-Agent (A2A) Protocol for Scalable Agentic AI Systems,” in Proc. "
    "IEEE ICICDS, 2026. [Online]. Available: https://ieeexplore.ieee.org/document/11604962/",
    "“LLM-Based Intelligent Agents for Cybersecurity: A Tutorial and Survey of Automated Vulnerability "
    "Discovery,” IEEE Access, 2026. [Online]. Available: https://ieeexplore.ieee.org/document/11580353/",
    "“A Survey of Fuzzing Techniques for Large Language Model Agents: Challenges, Methods, and Future "
    "Directions,” in Proc. IEEE BDAI, 2026. [Online]. Available: https://ieeexplore.ieee.org/document/11655176/",
    "“GLaMP: A Grounded Language Model-Based Multiagent System for Long-Horizon Robotic Task Planning in "
    "Industrial Settings,” IEEE Trans. Ind. Electron., 2026. [Online]. Available: "
    "https://ieeexplore.ieee.org/document/11641677/",
    "“Beyond Single-Framework Architectures: A Systematic Evaluation and Hybrid Design for Scalable Multi-Agent "
    "Coordination,” IEEE Access, 2026. [Online]. Available: https://ieeexplore.ieee.org/document/11481053/",
    "Anthropic, “How we built our multi-agent research system,” Anthropic Engineering Blog, Jun. 2025. [Online]. "
    "Available: https://www.anthropic.com/engineering/multi-agent-research-system",
    "S. Yao et al., “ReAct: Synergizing Reasoning and Acting in Language Models,” in Proc. Int. Conf. Learning "
    "Representations (ICLR), 2023, arXiv:2210.03629.",
]
for part in (0, 1):
    s = d.slide("// 10 · references", f"References ({part + 1}/2)", "IEEE format — [n] on the slides refers to this list")
    paras = [{"runs": [(f"[{i}]\t", {"bold": True, "color": CYAN, "font": MONO}), (r, {})]}
             for i, r in enumerate(refs[part * 6:(part + 1) * 6], part * 6 + 1)]
    tb = t(s, 0.6, 1.75, 8.8, 5.1, paras, size=13, after=11)
    for p in tb.text_frame.paragraphs:
        pPr = p._p.get_or_add_pPr()
        pPr.set("marL", str(int(Inches(0.55))))
        pPr.set("indent", str(-int(Inches(0.55))))
    notes(s, "References in IEEE format; numbers in square brackets on the slides point to this list." +
          (" Reference 11 is an industry engineering report, not a peer-reviewed paper." if part else ""))

# 18. Thank you
s = d._slide("bg_cover.jpg")
d.institution_card(s)
label(s, 0.6, 2.2, 5, "SEMINAR-I  ·  2025–26")
t(s, 0.6, 2.5, 5.6, 1.1, [[("Thank ", {}), ("you", {"color": CYAN})]], size=56, bold=True, anchor="m")
t(s, 0.6, 3.6, 5.6, 0.5, "Questions & discussion", size=20, color=MUTED)
thank_you_orbit(s)
glass(s, 0.6, 5.35, 8.8, 1.2)
t(s, 0.85, 5.45, 8.3, 0.45, "Utkarsh Kale  ·  Roll No. B342", size=19, bold=True)
t(s, 0.85, 5.92, 8.3, 0.5, "Department of Computer Engineering, Bajaj Institute of Technology, Wardha", size=12.5,
  color=MUTED)
notes(s, "Thank you. I am happy to take questions.")

d.save(OUT)
print("saved", OUT, len(d.prs.slides))
