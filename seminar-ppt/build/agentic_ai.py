"""Seminar-I deck: Agentic AI (Utkarsh Kale, B342) — redesigned."""
import sys

from design import *  # noqa: F401,F403

TEMPLATE, ICONS, OUT = sys.argv[1:4]
P = AGENTIC
d = Deck(TEMPLATE, ICONS, P, "Agentic AI  ·  Utkarsh Kale (B342)")
INK, PRI, ACC, MUT, TXT = P["ink"], P["primary"], P["accent"], P["muted"], P["text"]


def motif(deck, s):
    """Agent network: nodes and links, central node in the accent colour."""
    nodes = [(7.25, 2.25, .26), (8.65, 2.05, .2), (9.3, 2.95, .3), (8.0, 3.25, .46), (7.05, 3.95, .22),
             (8.6, 4.15, .3), (9.25, 4.85, .2), (7.65, 4.9, .28), (6.85, 2.95, .16)]
    edges = [(0, 1), (0, 3), (1, 2), (1, 3), (2, 5), (3, 4), (3, 5), (4, 7), (5, 6), (5, 7), (2, 6), (8, 0), (8, 4)]
    for a, b in edges:
        line(s, nodes[a][0], nodes[a][1], nodes[b][0], nodes[b][1], P["on_dark"], 1.25, alpha=45)
    for i, (x, y, r) in enumerate(nodes):
        if i == 3:
            box(s, x - r * .8, y - r * .8, r * 1.6, r * 1.6, bg=ACC, shape="oval", alpha=25)
        box(s, x - r / 2, y - r / 2, r, r, bg=ACC if i == 3 else PRI, shape="oval", alpha=None if i == 3 else 85)


# 1. Cover
s = d.cover("Seminar-I  ·  2025–26", "Agentic AI",
            "Autonomous LLM agents for planning, reasoning, coordination and task execution", motif,
            info=[("Presented by", "Utkarsh Kale", "Roll No. B342  ·  Third Year, Semester V"),
                  ("Under the guidance of", "Name of Faculty", "Designation of faculty")], title_size=44)
notes(s, "Good morning. My seminar topic is Agentic AI: autonomous agents built on large language models "
         "that can plan, reason, coordinate with other agents and execute tasks. I will cover how these systems "
         "work, the main algorithms, applications, and their limitations.")

# 2. Agenda
s = d.agenda(["Introduction", "Objectives", "Literature review", "Literature survey", "Baseline papers",
              "System architecture", "Algorithms studied", "Features & trade-offs", "Applications",
              "Analysis & comparison", "Conclusion & future scope", "References"])
notes(s, "This is the flow of the presentation, following the seminar template.")

# 3. Introduction
s = d.content("01  ·  Introduction", "From chatbots to autonomous agents")
chips = [("LLM", INK, WHITE), ("+", None, MUT), ("Planning", P["soft"], PRI), ("+", None, MUT),
         ("Memory", P["soft"], PRI), ("+", None, MUT), ("Tools", P["soft"], PRI), ("+", None, MUT),
         ("Feedback", P["soft"], PRI), ("=", None, MUT), ("Agent", ACC, WHITE)]
x = 0.75
for t, bg, col in chips:
    w = 1.12 if bg else 0.32
    if bg:
        box(s, x, 1.62, w, 0.62, bg=bg, radius=0.31, paras=t, size=15, bold=True, color=col)
    else:
        text(s, x, 1.62, w, 0.62, t, size=20, bold=True, color=col, align="c", anchor="m")
    x += w
text(s, 0.6, 2.36, 8.8, 0.35, "An agent wraps a language model in a loop that plans, acts through tools, remembers "
     "and checks its own work [1], [2].", size=13, italic=True, color=MUT, align="c")
text(s, 0.6, 2.95, 5, 0.3, "HOW WE GOT HERE", size=10, bold=True, color=PRI, spc=160)
line(s, 0.8, 3.72, 9.2, 3.72, P["line"], 2.25)
miles = [("Pre-2020", "Rule-based and RL agents in narrow tasks"),
         ("2020–22", "LLMs as text generators (GPT-3, ChatGPT)"),
         ("2022–23", "Reasoning + tool use (Chain-of-Thought, ReAct [12])"),
         ("2023–24", "Multi-agent frameworks (AutoGen, CrewAI)"),
         ("2024–26", "Open protocols (MCP, A2A) and production agents [6]")]
for i, (yr, desc) in enumerate(miles):
    cx = 1.3 + i * 1.85
    last = i == len(miles) - 1
    text(s, cx - 0.85, 3.25, 1.7, 0.32, yr, size=14, bold=True, font=HEAD, color=ACC if last else PRI, align="c")
    box(s, cx - 0.11, 3.61, 0.22, 0.22, bg=ACC if last else PRI, shape="oval")
    text(s, cx - 0.88, 3.95, 1.76, 0.85, desc, size=12, color=TXT, align="c")
text(s, 0.6, 4.95, 5, 0.3, "WHY WE NEED AGENTS", size=10, bold=True, color=PRI, spc=160)
needs = [("layers", "Real tasks are multi-step", "Research, coding and booking need many dependent steps, not one reply."),
         ("globe", "Models need live data", "Tools give access to the web, code execution, databases and APIs."),
         ("check", "Results must be verified", "Feedback loops let an agent detect and correct its own errors.")]
for i, (ic, head, body) in enumerate(needs):
    x = 0.6 + i * 3.0
    d.icon_circle(s, ic, x, 5.35, 0.5, bg=PRI)
    text(s, x + 0.62, 5.35, 2.2, 0.5, head, size=14, bold=True, color=INK, anchor="m")
    text(s, x, 5.95, 2.75, 0.85, body, size=13, color=MUT)
notes(s, "Classic LLM use is prompt-response: you ask, it answers once. Agentic AI turns the model into the brain "
         "of a loop: it breaks a goal into steps, calls tools such as web search or a code interpreter, stores what "
         "it learns, and checks its own output. The idea grew from reasoning techniques such as Chain-of-Thought and "
         "ReAct in 2022, to multi-agent frameworks in 2023-24, and now open protocols like MCP and A2A that let "
         "agents connect to tools and to each other.")

# 4. Objectives
s = d.content("02  ·  Objectives", "What this seminar sets out to do")
d.numbered_rows(s, [
    ("Architecture", "Study how autonomous LLM agents work: planning, memory, tool use and self-critique.", "brain"),
    ("Coordination", "Compare centralized, hierarchical and decentralized multi-agent patterns.", "users"),
    ("Memory & context", "Understand short- and long-term memory management for long-horizon tasks.", "db"),
    ("Applications", "Explore real agent systems in software, research, cybersecurity and robotics.", "cogs"),
    ("Challenges", "Identify issues in reliability, safety, evaluation and cost; suggest future directions.", "shield"),
])
notes(s, "By the end of this seminar I aim to explain the internal architecture of an agent, compare ways of "
         "coordinating several agents, explain memory management, show real applications, and critically discuss "
         "the open challenges.")

# 5. Literature review
s = d.content("03  ·  Literature review", "Six research threads shape modern agents")
d.subtitle(s, "Sources from 2022–2026: IEEE surveys, arXiv preprints, ACL papers and engineering reports, grouped by theme.")
cards = [("book", "Surveys & taxonomies", "[1] [2] [3]",
          "Agent = perception + planning + memory + action; a shift to goal-directed systems."),
         ("cogs", "Frameworks & runtime", "[4] [10]",
          "Separate the agent's blueprint from its execution; hybrid frameworks scale coordination."),
         ("db", "Memory", "[5]", "Agents learn when to store, retrieve, summarize or discard memory (AgeMem)."),
         ("plug", "Protocols", "[6]", "MCP standardizes tool and data access; A2A standardizes agent-to-agent messaging."),
         ("shield", "Security & testing", "[7] [8]",
          "Prompt injection, planning hallucination and tool abuse need fuzzing and guardrails."),
         ("robot", "Planning & multi-agent", "[9] [11] [12]",
          "ReAct loops, grounded planning with replanning, orchestrator-worker agents.")]
for i, (ic, t, r, b) in enumerate(cards):
    d.theme_card(s, 0.6 + (i % 3) * 3.025, 1.85 + (i // 3) * 2.05, 2.75, 1.9, ic, t, r, b, alt=(i % 3 == 1))
d.insight(s, 6.05, "Common finding", "reliability depends on orchestration, memory, coordination, evaluation and "
          "safeguards — not on model capability alone.")
notes(s, "I did not rely on a single paper. The IEEE ICOIN 2026 survey was my architectural starting point; I then "
         "used focused papers on memory, protocols, evaluation, security and multi-agent systems. The common message "
         "is that a strong model is not enough: how the agent is orchestrated, what it remembers, and how it is "
         "checked matter just as much.")

# 6-7. Literature survey tables
lit = [
    ("A Survey on LLM Agents: Architecture, Applications, and Challenges", "IEEE ICOIN, 2026",
     "Surveys agent architecture — memory, planning, tool use, control flows — plus evaluation, reliability and scalability."),
    ("Agentic AI: Architectures, Taxonomies, and Evaluation of LLM Agents",
     "V. Arunkumar, G. R. Gangadharan, R. Buyya · arXiv, 2026",
     "Taxonomy of perception, planning, action, tools and collaboration; evaluation methods and failure modes."),
    ("From Prompt-Response to Goal-Directed Systems", "M. Alenezi · arXiv, 2026",
     "Evolution of agent software architecture: typed tool interfaces, multi-agent topologies, governance, observability."),
    ("The Auton Agentic AI Framework", "S. Cao et al. · arXiv, 2026",
     "Separates the cognitive blueprint from runtime execution; covers memory, MCP, safety and runtime optimization."),
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
    s = d.content("04  ·  Literature survey", f"Literature survey in tabular form ({part + 1}/2)")
    rows = [(f"{i:02d}", t, v, w) for i, (t, v, w) in enumerate(lit[part * 5:(part + 1) * 5], part * 5 + 1)]
    d.lit_table(s, rows, row_h=0.98)
    notes(s, "This table summarises each paper and what it contributes. " +
          ("The first five cover the overall architecture, taxonomy, software evolution, runtime framework and memory."
           if part == 0 else
           "These five cover protocols, security, fuzzing, grounded robotic planning and a comparison of agent frameworks."))

# 8. Baseline papers
s = d.content("05  ·  Baseline papers", "Three papers anchor this seminar")
d.baseline(s, ("PRIMARY BASELINE", "[1]", "A Survey on LLM Agents: Architecture, Applications, and Challenges",
               "IEEE ICOIN, 2026", "Broad, recent view of agent architecture — the starting point of this seminar.",
               "Overall architecture: planning, memory, tools and control flow."),
           [("SUPPORTING", "[2]", "Agentic AI: Architectures, Taxonomies, and Evaluation of LLM Agents", "arXiv, 2026",
             "clear taxonomy and evaluation dimensions.", "agent types, failure modes, evaluation."),
            ("SUPPORTING", "[6]", "MCP and A2A Protocol for Scalable Agentic AI Systems", "IEEE ICICDS, 2026",
             "explains how agents connect to tools and each other.", "the interoperability layer.")])
notes(s, "I selected the ICOIN 2026 survey as my primary baseline because it covers the full agent architecture. "
         "The taxonomy paper by Arunkumar, Gangadharan and Buyya helped me classify agents and their failure modes, "
         "and the MCP/A2A paper explains the interoperability layer. Focused papers 4, 5 and 7 to 10 were then used "
         "for runtime, memory, security and multi-agent details.")

# 9. System architecture
s = d.content("06  ·  System architecture", "A hierarchical multi-agent architecture")
d.subtitle(s, "Goal → plan → coordinated specialist agents → tools → verified output, backed by shared memory [1], [11]")
box(s, 0.45, 2.75, 1.15, 1.2, bg=INK, paras=[[("User goal", {"bold": True, "size": 14})], "task / objective"],
    size=11, color=WHITE)
box(s, 1.8, 1.85, 1.55, 3.05, bg=P["soft"], radius=0.12)
text(s, 1.8, 1.95, 1.55, 0.25, "PLANNING", size=9.5, bold=True, color=PRI, align="c", spc=140)
for i, t in enumerate(["Understand goal", "Decompose into subtasks", "Build task graph"]):
    box(s, 1.92, 2.3 + i * 0.86, 1.31, 0.64, bg=WHITE, line=P["line"], paras=t, size=11, color=TXT)
    if i < 2:
        arrow(s, 2.575, 2.94 + i * 0.86, 2.575, 3.16 + i * 0.86, PRI, 1.25)
box(s, 3.55, 1.85, 3.35, 3.05, bg=P["soft"], radius=0.12)
text(s, 3.55, 1.95, 3.35, 0.25, "MULTI-AGENT SYSTEM", size=9.5, bold=True, color=PRI, align="c", spc=140)
box(s, 3.7, 2.3, 3.05, 0.72, bg=PRI, paras=[[("Manager / orchestrator agent", {"bold": True})],
                                            "assigns · monitors · replans"], size=11.5, color=WHITE)
for i, t in enumerate(["Research agent", "Coding agent", "Testing agent", "Critique agent"]):
    x = 3.7 + (i % 2) * 1.6
    y = 3.35 + (i // 2) * 0.75
    box(s, x, y, 1.45, 0.6, bg=WHITE, line=PRI, lw=1.25, paras=t, size=11, bold=True, color=PRI)
line(s, 5.225, 3.02, 5.225, 3.18, PRI, 1.25)
line(s, 4.425, 3.18, 6.025, 3.18, PRI, 1.25)
arrow(s, 4.425, 3.18, 4.425, 3.35, PRI, 1.25)
arrow(s, 6.025, 3.18, 6.025, 3.35, PRI, 1.25)
box(s, 7.1, 1.85, 1.3, 3.05, bg=P["soft"], radius=0.12)
text(s, 7.1, 1.95, 1.3, 0.25, "TOOLS", size=9.5, bold=True, color=PRI, align="c", spc=140)
for i, (ic, t) in enumerate([("search", "Web search"), ("terminal", "Code exec"), ("db", "APIs / DB"), ("file", "Files")]):
    y = 2.35 + i * 0.6
    d.icon(s, ic, 7.22, y + 0.07, 0.28, P["ic_p"])
    text(s, 7.58, y, 0.82, 0.42, t, size=11, color=TXT, anchor="m")
box(s, 8.6, 2.75, 0.95, 1.2, bg=ACC, paras=[[("Output", {"bold": True, "size": 13})], "answer / artifacts"],
    size=10.5, color=WHITE)
for x1, x2 in ((1.6, 1.8), (3.35, 3.55), (6.9, 7.1), (8.4, 8.6)):
    arrow(s, x1, 3.35, x2, 3.35, MUT, 1.75, head="both" if x1 == 6.9 else "end")
box(s, 1.8, 5.1, 6.6, 0.95, bg=P["soft"], radius=0.12)
text(s, 1.92, 5.1, 1.2, 0.95, "MEMORY", size=9.5, bold=True, color=PRI, anchor="m", spc=140)
for i, (a, b) in enumerate([("Short-term", "recent steps"), ("Long-term", "vector store / DB"), ("Shared", "multi-agent context")]):
    box(s, 3.05 + i * 1.8, 5.22, 1.68, 0.71, bg=WHITE, line=P["line"], paras=[[(a, {"bold": True, "color": INK})], b],
        size=11, color=MUT)
arrow(s, 5.225, 4.9, 5.225, 5.1, PRI, 1.75, head="both")
path(s, [(9.07, 3.95), (9.07, 6.5), (1.02, 6.5), (1.02, 3.95)], ACC, 1.75, dash=True)
box(s, 3.6, 6.34, 3.0, 0.32, bg=WHITE, line=ACC, radius=0.16, paras="feedback  ·  verification  ·  replanning",
    size=10.5, bold=True, color=ACC, margin=0.02)
notes(s, "This is the overall architecture. The user gives a goal. The planner understands it, breaks it into subtasks "
         "and builds a task graph. A manager agent assigns subtasks to specialised worker agents - research, coding, "
         "testing and critique - which call external tools such as web search, code execution, APIs and files. A "
         "memory layer stores short-term, long-term and shared context. Finally the output goes through feedback and "
         "verification; if it fails, the system replans.")

# 10. Algorithm 1 — ReAct
s = d.content("07  ·  Algorithms studied", "ReAct: think, act, observe, repeat")
d.subtitle(s, "Algorithm 1 — reasoning and acting interleaved in a single loop [12]")
cx, cy = 2.75, 4.2
box(s, cx - 0.62, cy - 0.5, 1.24, 1.0, bg=P["soft"], shape="oval",
    paras=[[("Goal G", {"bold": True})], "history H"], size=12, color=PRI)
nodes = [((cx, cy - 1.6), "Thought", "reason about next step", INK, WHITE),
         ((cx + 1.62, cy), "Action", "call a tool", PRI, WHITE),
         ((cx, cy + 1.6), "Observation", "read tool result", ACC, WHITE),
         ((cx - 1.62, cy), "Update", "add (r, a, o) to H", WHITE, PRI)]
for (nx, ny), t, sub, bg, col in nodes:
    box(s, nx - 0.76, ny - 0.38, 1.52, 0.76, bg=bg, line=PRI if bg == WHITE else None, lw=1.5,
        paras=[[(t, {"bold": True, "size": 14})], sub], size=10.5, color=col)
for (x1, y1, x2, y2) in ((cx + 0.76, cy - 1.45, cx + 1.4, cy - 0.38), (cx + 1.4, cy + 0.38, cx + 0.76, cy + 1.45),
                         (cx - 0.76, cy + 1.45, cx - 1.4, cy + 0.38), (cx - 1.4, cy - 0.38, cx - 0.76, cy - 1.45)):
    arrow(s, x1, y1, x2, y2, MUT, 1.75)
d.code(s, 5.35, 1.9, 4.05, 3.35, [
    "Input: goal G, environment E",
    "H ← ∅                  # history",
    "while not Done(G) do",
    "  r ← LLM_Reason(G, H)  # thought",
    "  a ← Select_Tool(r)    # action",
    "  o ← Execute(a, E)     # observe",
    "  H ← H ∪ {(r, a, o)}",
    "  if Need_Replan(o):",
    "      G ← Update(G, o)",
    "return FinalAnswer(G, H)"], size=11.5)
box(s, 5.35, 5.42, 4.05, 1.35, bg=P["card"], radius=0.12)
text(s, 5.57, 5.52, 3.7, 0.25, "EXAMPLE", size=9.5, bold=True, color=PRI, spc=160)
text(s, 5.57, 5.8, 3.7, 0.95, [[("“What is the weather in Wardha?”", {"italic": True, "color": INK, "bold": True})],
                               "Thought: needs live data → Action: weather_api(\"Wardha\") → Observation: 31 °C, clear → Answer"],
     size=12, color=TXT, after=3)
notes(s, "ReAct, proposed by Yao et al., is the core loop inside most agents. At each step the model first produces a "
         "Thought - its reasoning about what to do. It then picks an Action, usually a tool call, and reads the "
         "Observation that comes back. These are added to the history so the next step is better informed. The loop "
         "stops when the goal is met. The example shows the agent deciding it needs live data and calling a weather tool.")

# 11. Algorithm 2 — planning & coordination
s = d.content("07  ·  Algorithms studied", "Planning turns goals into a task graph")
d.subtitle(s, "Algorithm 2 — task decomposition and multi-agent coordination (example goal: a research report)")
box(s, 0.6, 2.15, 1.3, 1.0, bg=INK, paras=[[("Goal", {"bold": True, "size": 14})], "research report"], size=11,
    color=WHITE)
tasks = [((2.2, 1.85), "t1  Search news", "research agent"), ((2.2, 2.75), "t2  Search papers", "research agent"),
         ((4.05, 2.3), "t3  Analyse data", "coding agent"), ((5.85, 2.3), "t4  Draft report", "writer agent"),
         ((7.65, 2.3), "t5  Review & fix", "critique agent")]
for (x, y), t, a in tasks:
    box(s, x, y, 1.6, 0.72, bg=WHITE, line=P["line"], lw=1.25,
        paras=[[(t, {"bold": True, "color": INK})], [(a, {"italic": True, "color": ACC, "size": 10.5})]], size=12)
arrow(s, 1.9, 2.5, 2.2, 2.21, MUT, 1.5)
arrow(s, 1.9, 2.8, 2.2, 3.11, MUT, 1.5)
arrow(s, 3.8, 2.21, 4.05, 2.55, MUT, 1.5)
arrow(s, 3.8, 3.11, 4.05, 2.86, MUT, 1.5)
arrow(s, 5.65, 2.66, 5.85, 2.66, MUT, 1.5)
arrow(s, 7.45, 2.66, 7.65, 2.66, MUT, 1.5)
text(s, 0.6, 3.68, 8.8, 0.3, "P ← LLM_Plan(G);  T ← Decompose(P);  assign agents;  merge results", size=11.5,
     font=MONO, color=MUT, align="c")
text(s, 0.6, 4.15, 5, 0.3, "COORDINATION PATTERNS", size=10, bold=True, color=PRI, spc=160)
pats = [("Centralized", "One orchestrator assigns all work", "+ simple control", "− single bottleneck"),
        ("Hierarchical", "Managers delegate to sub-teams", "+ scales to big tasks", "− more delay"),
        ("Decentralized", "Peers negotiate directly", "+ no single point of failure", "− hard to coordinate")]
for i, (t, desc, pro, con) in enumerate(pats):
    x = 0.6 + i * 3.025
    box(s, x, 4.5, 2.75, 2.3, bg=P["card"], radius=0.12)
    text(s, x, 4.6, 2.75, 0.32, t, size=14, bold=True, color=INK, align="c", font=HEAD)
    mx, my = x + 1.375, 5.35
    if i == 0:
        pts = [(mx - 0.75, my + 0.32), (mx, my + 0.42), (mx + 0.75, my + 0.32)]
        for px, py in pts:
            line(s, mx, my - 0.15, px, py, P["line"], 1.5)
        box(s, mx - 0.17, my - 0.36, 0.34, 0.34, bg=INK, shape="oval")
        for px, py in pts:
            box(s, px - 0.12, py - 0.12, 0.24, 0.24, bg=PRI, shape="oval")
    elif i == 1:
        lv1 = [(mx - 0.55, my + 0.05), (mx + 0.55, my + 0.05)]
        lv2 = [(mx - 0.85, my + 0.45), (mx - 0.28, my + 0.45), (mx + 0.28, my + 0.45), (mx + 0.85, my + 0.45)]
        for px, py in lv1:
            line(s, mx, my - 0.3, px, py, P["line"], 1.5)
        for k, (px, py) in enumerate(lv2):
            line(s, *lv1[k // 2], px, py, P["line"], 1.5)
        box(s, mx - 0.15, my - 0.45, 0.3, 0.3, bg=INK, shape="oval")
        for px, py in lv1:
            box(s, px - 0.12, py - 0.12, 0.24, 0.24, bg=PRI, shape="oval")
        for px, py in lv2:
            box(s, px - 0.09, py - 0.09, 0.18, 0.18, bg=ACC, shape="oval")
    else:
        pts = [(mx - 0.55, my - 0.3), (mx + 0.55, my - 0.3), (mx + 0.55, my + 0.35), (mx - 0.55, my + 0.35)]
        for a in range(4):
            for b in range(a + 1, 4):
                line(s, *pts[a], *pts[b], P["line"], 1.5)
        for px, py in pts:
            box(s, px - 0.12, py - 0.12, 0.24, 0.24, bg=PRI, shape="oval")
    text(s, x + 0.1, 5.92, 2.55, 0.85, [[(desc, {"color": TXT})], [(pro, {"color": GOOD, "bold": True})],
                                        [(con, {"color": BAD, "bold": True})]], size=12, align="c", after=1)
notes(s, "For complex goals, the planner asks the LLM for a plan and decomposes it into subtasks with dependencies - a "
         "task graph. Independent tasks such as the two searches run in parallel; dependent ones wait. Each subtask "
         "goes to a specialised agent and the manager combines the results. Agents can be coordinated centrally, "
         "hierarchically or in a decentralized way: centralized is simplest but creates a bottleneck, hierarchical "
         "scales better, decentralized is robust but harder to keep consistent.")

# 12. Algorithm 3 — memory & protocols
s = d.content("07  ·  Algorithms studied", "Memory and protocols keep agents scalable")
d.subtitle(s, "Algorithm 3 — context management [5] and MCP / A2A interoperability [6]")
text(s, 0.6, 1.9, 4.2, 0.3, "CONTEXT MANAGEMENT", size=10, bold=True, color=PRI, spc=160)
box(s, 0.6, 2.3, 2.0, 0.72, bg=PRI, paras=[[("Short-term", {"bold": True})], "recent k turns"], size=11.5, color=WHITE)
box(s, 2.8, 2.3, 2.0, 0.72, bg=PRI, paras=[[("Long-term", {"bold": True})], "vector DB retrieval"], size=11.5, color=WHITE)
box(s, 1.45, 3.28, 2.5, 0.48, bg=WHITE, line=P["line"], lw=1.25, paras="Merge into context", size=12, bold=True, color=INK)
arrow(s, 1.6, 3.02, 2.0, 3.28, MUT, 1.5)
arrow(s, 3.8, 3.02, 3.4, 3.28, MUT, 1.5)
box(s, 1.65, 3.98, 2.1, 0.92, bg=AMBER, shape="diamond", paras="Too long?", size=12, bold=True, color=INK)
arrow(s, 2.7, 3.76, 2.7, 3.98, MUT, 1.5)
box(s, 1.45, 5.15, 2.5, 0.5, bg=WHITE, line=ACC, lw=1.25, paras="Summarize / prune old items", size=11.5, color=INK)
arrow(s, 2.7, 4.9, 2.7, 5.15, MUT, 1.5)
text(s, 2.78, 4.88, 0.5, 0.25, "yes", size=10, color=MUT)
box(s, 1.45, 5.9, 2.5, 0.55, bg=INK, paras="Context sent to LLM", size=12.5, bold=True, color=WHITE)
arrow(s, 2.7, 5.65, 2.7, 5.9, MUT, 1.5)
path(s, [(1.65, 4.44), (0.85, 4.44), (0.85, 6.17), (1.45, 6.17)], MUT, 1.5)
text(s, 0.9, 4.16, 0.5, 0.25, "no", size=10, color=MUT)
line(s, 5.0, 1.95, 5.0, 6.75, P["line"], 1.0)
text(s, 5.2, 1.9, 4.2, 0.3, "MCP & A2A PROTOCOLS", size=10, bold=True, color=PRI, spc=160)
box(s, 5.2, 2.35, 1.55, 0.62, bg=INK, paras="Agent A", size=13, bold=True, color=WHITE)
box(s, 7.85, 2.35, 1.55, 0.62, bg=INK, paras="Agent B", size=13, bold=True, color=WHITE)
arrow(s, 6.75, 2.66, 7.85, 2.66, ACC, 2.25, head="both")
box(s, 6.95, 2.47, 0.7, 0.36, bg=WHITE, line=ACC, radius=0.18, paras="A2A", size=11, bold=True, color=ACC, margin=0.01)
for x, labels in ((5.2, ("Database", "GitHub")), (7.85, ("Files", "Web API"))):
    for k, lab in enumerate(labels):
        bx = x + k * 0.82 - 0.05
        box(s, bx, 3.65, 0.78, 0.46, bg=P["soft"], paras=lab, size=10.5, color=INK)
        arrow(s, x + 0.775, 2.97, bx + 0.39, 3.65, PRI, 1.25)
    box(s, x + 0.47, 3.15, 0.62, 0.3, bg=WHITE, line=PRI, radius=0.15, paras="MCP", size=10.5, bold=True, color=PRI,
        margin=0.01)
for k, (t, col, body, eg) in enumerate((
        ("MCP", PRI, "Standard way for an agent to discover and call tools and data (agent ↔ tool).",
         "e.g. query a database or GitHub through an MCP server"),
        ("A2A", ACC, "Standard way for agents to delegate tasks and share results (agent ↔ agent).",
         "e.g. a planner hands a coding task to a coding agent"))):
    x = 5.2 + k * 2.15
    box(s, x, 4.4, 2.05, 2.35, bg=P["card"], radius=0.12)
    text(s, x + 0.15, 4.5, 1.75, 0.4, t, size=18, bold=True, font=HEAD, color=col)
    text(s, x + 0.15, 4.92, 1.8, 1.8, [body, [(eg, {"italic": True, "color": MUT, "size": 11})]], size=12,
         color=TXT, after=6)
notes(s, "Agents work over long tasks, so the context window fills up. The memory algorithm combines recent interactions "
         "with relevant items retrieved from long-term storage such as a vector database; if the context is too long "
         "it summarises or prunes old items. AgeMem goes further by letting the agent learn these memory operations. "
         "On the right: MCP is a standard for connecting an agent to tools and data; A2A is a standard for agents "
         "talking to other agents. Together they make large agent systems interoperable.")

# 13. Features / advantages / disadvantages
s = d.content("08  ·  Features, advantages & disadvantages", "Powerful, but not free of trade-offs")
d.three_columns(s, [
    ("Features", PRI, "star", [("Autonomy", "pursues a goal over many steps"), ("Planning", "breaks goals into subtasks"),
                               ("Tool use", "web, code, APIs, databases"), ("Memory", "short- and long-term context"),
                               ("Reflection", "verifies and replans")]),
    ("Advantages", GOOD, "check", [("Complex tasks", "handles multi-step workflows"),
                                   ("Specialisation", "agents work in parallel"),
                                   ("Live data", "external tools and sources"),
                                   ("Productivity", "less repetitive human effort"),
                                   ("Interoperable", "MCP / A2A ease scaling [6]")]),
    ("Disadvantages", BAD, "warn", [("Error chains", "mistakes compound over steps"),
                                    ("Security", "prompt injection, tool abuse [8]"),
                                    ("Cost", "many LLM calls, higher latency"),
                                    ("Evaluation", "hard to test reliably [2]"),
                                    ("Oversight", "still needs human checks")]),
])
notes(s, "Key features are autonomy, planning, tool use, memory and reflection. The advantages follow: agents handle "
         "complex workflows, specialise and parallelise, and use live data. The disadvantages are important: one wrong "
         "step can cascade, external content can inject malicious instructions, multi-agent systems use many model "
         "calls so they are costly, and reliable evaluation is still an open problem.")

# 14. Applications
s = d.content("09  ·  Applications", "Where agents are already at work")
d.app_grid(s, [
    ("code", "Software engineering", "Coding agents write, run, test and debug code in a loop."),
    ("search", "Research assistants", "An orchestrator runs parallel search agents to compile reports [11]."),
    ("bug", "Cybersecurity", "Agents discover vulnerabilities and run security tests [7]."),
    ("robot", "Industrial robotics", "Long-horizon task planning with failure-aware replanning [9]."),
    ("cogs", "Business workflows", "Automating support tickets, data entry and reporting."),
    ("user", "Personal assistants", "Email, scheduling and travel booking through tools."),
])
notes(s, "Agentic AI is already used in software engineering, where agents write and test code; in research, where "
         "Anthropic describes an orchestrator that runs several search agents in parallel; in cybersecurity for "
         "vulnerability discovery; in industrial robotics for long-horizon planning such as GLaMP; and in business "
         "and personal productivity.")

# 15. Analysis / comparison
s = d.content("10  ·  Analysis & comparison", "More autonomy: more capability, more cost")
text(s, 2.4, 1.55, 7.0, 0.28, "more autonomy  ·  more capability  ·  more cost", size=11, italic=True, color=MUT,
     align="r")
arrow(s, 2.4, 1.9, 9.4, 1.9, ACC, 2.0)
rows = [["Aspect", "Single LLM", "Single agent (ReAct + tools)", "Multi-agent system"],
        ["Task type", "One-shot answers", "Multi-step tasks", "Large, parallel, multi-skill tasks"],
        ["Tools", "None", "Yes", "Specialised tools per agent"],
        ["Memory", "Prompt window only", "Short + long-term", "Per-agent + shared"],
        ["Error handling", "User re-prompts", "Self-reflection loop", "Critique agents + verification"],
        ["Cost / latency", "Low", "Medium", "High — many LLM calls [11]"],
        ["Main risk", "Hallucination", "Tool misuse, loops", "Coordination failures"]]
d.comparison_table(s, rows, [1.75, 2.1, 2.45, 2.5], y=2.1, row_h=0.5, hl_col=3)
box(s, 0.6, 5.85, 4.3, 0.95, bg=P["card"], radius=0.12, align="l", margin=0.18, paras=[
    [("Framework study [10]  ", {"bold": True, "color": PRI}),
     ("CrewAI, AutoGen and LangChain suit different workloads; a hybrid is proposed (its own benchmark).", {})]],
    size=12, color=TXT)
box(s, 5.1, 5.85, 4.3, 0.95, bg=INK, radius=0.12, align="l", margin=0.18, paras=[
    [("Design rule  ", {"bold": True, "color": ACC}),
     ("use the simplest design that works; add agents only for parallelism or specialisation.", {})]],
    size=12, color=WHITE)
notes(s, "Comparing three levels: a single LLM is cheap but cannot act; a single agent with ReAct and tools handles "
         "multi-step tasks; a multi-agent system handles large parallel work but costs more and can fail in "
         "coordination. The framework study compares CrewAI, AutoGen and LangChain and proposes a hybrid; its numbers "
         "apply to its own benchmark. The practical rule is to start simple.")

# 16. Conclusion
s = d.conclusion("Reliability is a system property, not a model property", [
    "Agentic AI moves LLMs from answering prompts to completing goals.",
    "ReAct loops, task decomposition and memory are the core building blocks.",
    "Multi-agent designs add specialisation and parallelism — at higher cost.",
    "MCP and A2A make tools and agents interoperable."],
    ["Learned long-term memory management [5]",
     "Standard benchmarks for agent reliability [2]",
     "Stronger defences against prompt injection [8]",
     "Domain agents in software, security and robotics [7], [9]"],
    "Reliable agents = orchestration + memory + coordination + evaluation + safeguards")
notes(s, "To conclude: agentic AI is a shift from prompt-response to goal-directed systems. Its building blocks are the "
         "ReAct loop, planning, memory and tools; multi-agent systems add specialisation. Future work is in learned "
         "memory, standard evaluation, security, and domain-specific agents. My main conclusion is that reliability "
         "comes from the whole system design, not just a bigger model.")

# 17-18. References (IEEE format)
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
s = d.references("References (1/2)", refs[:6], 1)
notes(s, "References in IEEE format; numbers in square brackets on the slides point to this list.")
s = d.references("References (2/2)", refs[6:], 7)
notes(s, "References continued. [11] is an industry engineering report, not a peer-reviewed paper.")

# 19. Closing
s = d.closing(motif, "Utkarsh Kale  ·  Roll No. B342")
notes(s, "Thank you. I am happy to take questions.")

d.save(OUT)
print("saved", OUT, len(d.prs.slides))
