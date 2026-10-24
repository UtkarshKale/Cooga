"""Seminar-I deck: Agentic AI (Utkarsh Kale, B342)."""
import sys

from common import *  # noqa: F401,F403

TEMPLATE, ICONS, OUT = sys.argv[1:4]
d = Deck(TEMPLATE, ICONS)
ACC = TEAL

# 1. Title
s = title_slide(d, ["Agentic AI: Autonomous LLM Agents for Planning,",
                    "Reasoning, Coordination and Task Execution"],
                "Utkarsh Kale", "Roll No.: B342  |  Third Year (Semester V)")
notes(s, "Good morning. My seminar topic is Agentic AI: autonomous agents built on large language "
         "models that can plan, reason, coordinate with other agents and execute tasks. "
         "I will cover how these systems work, the main algorithms, applications, and their limitations.")

# 2. Index
s = index_slide(d, ["Introduction", "Objectives", "Literature Review", "Literature Survey (Tabular Form)",
                    "Baseline Papers Selected", "System Architecture / Algorithms Studied",
                    "Features / Advantages / Disadvantages", "Applications", "Analysis / Comparison",
                    "Conclusion & Future Scope", "References"])
notes(s, "This is the flow of the presentation, following the seminar template.")

# 3. Introduction
s = d.content_slide("Introduction")
box(s, 0.5, 1.25, 9.0, 0.82, fill=PALE, align="l", anchor="m", margin=0.15, paras=[[
    ("Agentic AI: ", {"bold": True, "color": NAVY}),
    ("LLM-based systems that pursue a goal on their own — they plan, use tools, remember "
     "context and check their results with limited human supervision [1], [2].", {})]], size=15)
text(s, 0.5, 2.22, 9.0, 0.4, "Evolution: from chatbots to agents", size=16, bold=True, color=NAVY)
line(s, 0.75, 3.1, 9.25, 3.1, BLUE, 2.5)
miles = [("Pre-2020", "Rule-based and RL agents in narrow tasks"),
         ("2020–22", "LLMs as text generators (GPT-3, ChatGPT)"),
         ("2022–23", "Reasoning + tool use (Chain-of-Thought, ReAct [12])"),
         ("2023–24", "Multi-agent frameworks (AutoGen, CrewAI)"),
         ("2024–26", "Open protocols (MCP, A2A) and production agents [6]")]
for i, (yr, desc) in enumerate(miles):
    cx = 1.3 + i * 1.85
    text(s, cx - 0.85, 2.62, 1.7, 0.35, yr, size=14, bold=True, color=NAVY if i < 4 else ACC, align="c")
    box(s, cx - 0.14, 2.96, 0.28, 0.28, fill=NAVY if i < 4 else ACC, shape="oval")
    text(s, cx - 0.86, 3.32, 1.72, 1.0, desc, size=12, align="c", color=INK)
text(s, 0.5, 4.4, 9.0, 0.4, "Inspiration — why we need agents", size=16, bold=True, color=NAVY)
needs = [("layers", "Real tasks are multi-step",
          "Research, coding and booking need many dependent steps, not one reply."),
         ("globe", "Models need live data",
          "Tools give access to the web, code execution, databases and APIs."),
         ("check", "Results must be verified",
          "Feedback loops let an agent detect and correct its own errors.")]
for i, (ic, head, body) in enumerate(needs):
    x = 0.5 + i * 3.075
    box(s, x, 4.85, 2.85, 1.9, fill=PALE)
    d.icon_circle(s, ic, x + 0.15, 5.0, 0.52, fill=ACC)
    text(s, x + 0.75, 4.97, 2.0, 0.58, head, size=14, bold=True, color=NAVY, anchor="m")
    text(s, x + 0.15, 5.6, 2.55, 1.1, body, size=14)
notes(s, "Classic LLM use is prompt-response: you ask, it answers once. Agentic AI turns the model into "
         "the 'brain' of a loop: it breaks a goal into steps, calls tools such as web search or a code "
         "interpreter, stores what it learns, and checks its own output. The idea grew from reasoning "
         "techniques such as Chain-of-Thought and ReAct in 2022, to multi-agent frameworks in 2023-24, "
         "and now open protocols like MCP and A2A that let agents connect to tools and to each other.")

# 4. Objectives
s = d.content_slide("Objectives")
numbered_rows(d, s, [
    ("Architecture", "Study how autonomous LLM agents work: planning, memory, tool use and self-critique.", "brain"),
    ("Coordination", "Analyse multi-agent patterns (centralized, hierarchical, decentralized) and their trade-offs.", "users"),
    ("Memory & context", "Understand short- and long-term memory management for long-horizon tasks.", "db"),
    ("Applications", "Explore real agent systems in software, research, cybersecurity and robotics.", "cogs"),
    ("Challenges", "Identify issues in reliability, safety, evaluation and cost; suggest future directions.", "shield"),
], circ=NAVY)
notes(s, "By the end of this seminar I aim to explain the internal architecture of an agent, compare ways "
         "of coordinating several agents, explain memory management, show real applications, and "
         "critically discuss the open challenges.")

# 5. Literature review overview
s = d.content_slide("Literature Review")
text(s, 0.5, 1.2, 9.0, 0.5, "Sources (2022–2026) were grouped into six themes; each theme fed one part "
     "of the architecture studied.", size=14, color=MUTED, italic=True)
cards = [("book", "Surveys & Taxonomies", "[1], [2], [3]",
          "Agent = perception + planning + memory + action; shift from prompt-response to goal-directed systems."),
         ("cogs", "Frameworks & Runtime", "[4], [10]",
          "Separate the agent's blueprint from its execution; hybrid frameworks for scalable coordination."),
         ("db", "Memory", "[5]",
          "Agents learn when to store, retrieve, summarize or discard memory (AgeMem)."),
         ("plug", "Protocols", "[6]",
          "MCP standardizes tool and data access; A2A standardizes agent-to-agent messaging."),
         ("shield", "Security & Testing", "[7], [8]",
          "Prompt injection, planning hallucination and tool abuse need fuzzing and guardrails."),
         ("robot", "Planning & Multi-Agent", "[9], [11], [12]",
          "ReAct loops, grounded planning with replanning, orchestrator-worker research agents.")]
for i, (ic, t, r, b) in enumerate(cards):
    theme_card(d, s, 0.5 + (i % 3) * 3.075, 1.75 + (i // 3) * 2.15, 2.85, 2.0, ic, t, r, b,
               circ=NAVY if i % 2 == 0 else ACC)
box(s, 0.5, 6.12, 9.0, 0.68, fill=LIGHT, margin=0.12, paras=[[
    ("Common finding: ", {"bold": True, "color": NAVY}),
    ("reliability depends on orchestration, memory, coordination, evaluation and safeguards — "
     "not on model capability alone.", {})]], size=14)
notes(s, "I did not rely on a single paper. The IEEE ICOIN 2026 survey was my architectural starting point; "
         "I then used focused papers on memory, protocols, evaluation, security and multi-agent systems. "
         "The common message across all of them is that a strong model is not enough: how the agent is "
         "orchestrated, what it remembers, and how it is checked matter just as much.")

# 6-7. Literature survey tables
lit = [
    ("A Survey on LLM Agents: Architecture, Applications, and Challenges", "IEEE ICOIN, 2026",
     "Surveys agent architecture: memory, planning, tool use and control flows; discusses evaluation, reliability and scalability."),
    ("Agentic AI: Architectures, Taxonomies, and Evaluation of LLM Agents",
     "V. Arunkumar, G. R. Gangadharan, R. Buyya — arXiv, 2026",
     "Taxonomy of perception, planning, action, tools and collaboration; catalogues evaluation methods and failure modes."),
    ("From Prompt-Response to Goal-Directed Systems", "M. Alenezi — arXiv, 2026",
     "Evolution of agent software architecture: typed tool interfaces, multi-agent topologies, governance, observability."),
    ("The Auton Agentic AI Framework", "S. Cao et al. — arXiv, 2026",
     "Separates the cognitive blueprint from runtime execution; covers memory, MCP, safety and runtime optimization."),
    ("Agentic Memory (AgeMem)", "Y. Yu et al. — ACL, 2026",
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
    s = d.content_slide(f"Literature Survey in Tabular Form ({part + 1}/2)", size=26)
    rows = [["Sr. No", "Details of Paper", "Work Reported"]]
    for i, (t, v, w) in enumerate(lit[part * 5:(part + 1) * 5], part * 5 + 1):
        rows.append([str(i), [[(t, {"bold": True})], [(v, {"size": 11, "color": MUTED})]], w])
    table(s, 0.45, 1.3, [0.75, 3.85, 4.5], rows, size=13, row_h=0.95, col_align=["c", "l", "l"])
    notes(s, "This table summarises each paper and what it contributes. " +
          ("The first five cover the overall architecture, taxonomy, software evolution, runtime framework and memory."
           if part == 0 else
           "These five cover protocols, security, fuzzing, grounded robotic planning and a comparison of agent frameworks."))

# 8. Baseline papers
s = d.content_slide("Baseline Papers Selected for Seminar Work", size=26)
base = [("PRIMARY BASELINE", NAVY, "[1] A Survey on LLM Agents: Architecture, Applications, and Challenges",
         "IEEE ICOIN 2026", "Broad, recent view of agent architecture — the starting point of this seminar.",
         "Overall architecture: planning, memory, tools and control flow."),
        ("SUPPORTING", ACC, "[2] Agentic AI: Architectures, Taxonomies, and Evaluation of LLM Agents",
         "arXiv 2026", "Clear taxonomy and evaluation dimensions.",
         "Comparing agent types, failure modes and evaluation."),
        ("SUPPORTING", ACC, "[6] MCP and A2A Protocol for Scalable Agentic AI Systems",
         "IEEE ICICDS 2026", "Explains how agents connect to tools and to each other.",
         "Interoperability layer of the architecture.")]
for i, (tag, col, t, v, why, used) in enumerate(base):
    x = 0.5 + i * 3.075
    box(s, x, 1.35, 2.85, 4.5, fill=PALE)
    box(s, x, 1.35, 2.85, 0.5, fill=col, paras=tag, size=13, bold=True, color=WHITE)
    text(s, x + 0.15, 1.95, 2.55, 1.25, t, size=14, bold=True, color=NAVY)
    text(s, x + 0.15, 3.2, 2.55, 0.32, v, size=12, italic=True, color=MUTED)
    text(s, x + 0.15, 3.6, 2.55, 1.15, [[("Why selected: ", {"bold": True, "color": col}), (why, {})]], size=13)
    text(s, x + 0.15, 4.75, 2.55, 1.05, [[("Used for: ", {"bold": True, "color": col}), (used, {})]], size=13)
text(s, 0.5, 6.05, 9.0, 0.7, "Focused papers [4], [5], [7]–[10] were then used for runtime, memory, "
     "security and multi-agent details.", size=14, italic=True, color=MUTED, align="c", anchor="m")
notes(s, "I selected the ICOIN 2026 survey as my primary baseline because it covers the full agent "
         "architecture. The taxonomy paper by Arunkumar, Gangadharan and Buyya helped me classify agents "
         "and their failure modes, and the MCP/A2A paper explains the interoperability layer.")

# 9. System architecture
s = d.content_slide("System Architecture")
text(s, 0.5, 1.08, 9.0, 0.35, "Hierarchical multi-agent architecture for autonomous task execution [1], [11]",
     size=13, italic=True, color=MUTED, align="c")
box(s, 0.3, 2.45, 1.3, 1.3, fill=BLUE, paras=[[("User Goal", {"bold": True, "size": 14})], "task / objective"],
    size=11, color=WHITE)
# planning group
box(s, 1.8, 1.55, 1.6, 3.05, fill=PALE, line=BLUE)
text(s, 1.8, 1.58, 1.6, 0.35, "Planning", size=13, bold=True, color=NAVY, align="c")
for i, t in enumerate(["Understand goal", "Decompose into subtasks", "Build task graph"]):
    box(s, 1.92, 2.0 + i * 0.86, 1.36, 0.62, fill=WHITE, line=BLUE, paras=t, size=11)
    if i < 2:
        arrow(s, 2.6, 2.62 + i * 0.86, 2.6, 2.86 + i * 0.86, BLUE, 1.25)
# multi-agent group
box(s, 3.6, 1.55, 3.3, 3.05, fill=PALE, line=BLUE)
text(s, 3.6, 1.58, 3.3, 0.35, "Multi-Agent System", size=13, bold=True, color=NAVY, align="c")
box(s, 3.75, 1.98, 3.0, 0.7, fill=NAVY, paras=[[("Manager / Orchestrator Agent", {"bold": True})],
                                               "assigns · monitors · replans"], size=11, color=WHITE)
workers = ["Research Agent", "Coding Agent", "Testing Agent", "Critique Agent"]
for i, t in enumerate(workers):
    x = 3.75 + (i % 2) * 1.55
    y = 3.05 + (i // 2) * 0.72
    box(s, x, y, 1.45, 0.58, fill=WHITE, line=ACC, lw=1.25, paras=t, size=11, bold=True, color=ACC)
line(s, 5.25, 2.68, 5.25, 2.88, NAVY, 1.25)
line(s, 4.47, 2.88, 6.03, 2.88, NAVY, 1.25)
arrow(s, 4.47, 2.88, 4.47, 3.05, NAVY, 1.25)
arrow(s, 6.03, 2.88, 6.03, 3.05, NAVY, 1.25)
# tools group
box(s, 7.1, 1.55, 1.3, 3.05, fill=PALE, line=BLUE)
text(s, 7.1, 1.58, 1.3, 0.55, "Tools & Environment", size=12, bold=True, color=NAVY, align="c")
for i, (ic, t) in enumerate([("search", "Web search"), ("terminal", "Code exec"), ("db", "APIs / DB"),
                             ("file", "Files")]):
    y = 2.2 + i * 0.58
    d.icon(s, ic, 7.2, y + 0.06, 0.3, "n")
    text(s, 7.55, y, 0.85, 0.42, t, size=11, anchor="m")
box(s, 8.6, 2.45, 1.1, 1.3, fill=ACC, paras=[[("Output", {"bold": True, "size": 13})], "answer / artifacts"],
    size=11, color=WHITE)
for x1, x2 in ((1.6, 1.8), (3.4, 3.6), (6.9, 7.1), (8.4, 8.6)):
    arrow(s, x1, 3.1, x2, 3.1, MUTED, 2, head="both" if x1 == 6.9 else "end")
# memory layer
box(s, 1.8, 4.85, 6.6, 1.0, fill=LIGHT, line=BLUE)
text(s, 1.85, 4.87, 1.3, 0.95, "Memory Layer", size=13, bold=True, color=NAVY, anchor="m", align="c")
for i, (a, b) in enumerate([("Short-term", "conversation, recent steps"), ("Long-term", "vector store, external DB"),
                            ("Shared", "multi-agent context")]):
    box(s, 3.2 + i * 1.75, 4.98, 1.62, 0.74, fill=WHITE, line=BLUE,
        paras=[[(a, {"bold": True})], b], size=11)
arrow(s, 5.25, 4.6, 5.25, 4.85, NAVY, 2, head="both")
# feedback loop
box(s, 1.8, 6.1, 6.6, 0.55, fill=ORANGE, paras="Feedback · Verification · Replanning", size=14, bold=True,
    color=WHITE)
polyline(s, [(9.15, 3.75), (9.15, 6.37), (8.4, 6.37)], ORANGE, 2)
polyline(s, [(1.8, 6.37), (0.95, 6.37), (0.95, 3.75)], ORANGE, 2)
notes(s, "This is the overall architecture. The user gives a goal. The planner understands it, breaks it "
         "into subtasks and builds a task graph. A manager agent assigns subtasks to specialised worker "
         "agents - research, coding, testing and critique - which call external tools such as web search, "
         "code execution, APIs and files. A memory layer stores short-term, long-term and shared context. "
         "Finally the output goes through feedback and verification; if it fails, the system replans.")

# 10. Algorithm 1: ReAct
s = d.content_slide("Algorithm 1: ReAct Reasoning–Acting Loop", size=26)
text(s, 0.5, 1.08, 9.0, 0.35, "Interleaves reasoning (Thought) with actions (tool calls) and observations [12]",
     size=13, italic=True, color=MUTED, align="c")
cx, cy = 2.75, 3.95
box(s, cx - 0.6, cy - 0.45, 1.2, 0.9, fill=LIGHT, shape="oval",
    paras=[[("Goal G", {"bold": True})], "history H"], size=12, color=NAVY)
nodes = [((cx, cy - 1.55), "Thought", "reason about next step", NAVY),
         ((cx + 1.65, cy), "Action", "call a tool", BLUE),
         ((cx, cy + 1.55), "Observation", "read tool result", ACC),
         ((cx - 1.65, cy), "Update", "add (r, a, o) to H", ORANGE)]
for (nx, ny), t, sub, col in nodes:
    box(s, nx - 0.78, ny - 0.4, 1.56, 0.8, fill=col, paras=[[(t, {"bold": True, "size": 14})], sub],
        size=11, color=WHITE)
for (x1, y1, x2, y2) in ((cx + 0.78, cy - 1.45, cx + 1.45, cy - 0.4), (cx + 1.45, cy + 0.4, cx + 0.78, cy + 1.45),
                         (cx - 0.78, cy + 1.45, cx - 1.45, cy + 0.4), (cx - 1.45, cy - 0.4, cx - 0.78, cy - 1.45)):
    arrow(s, x1, y1, x2, y2, MUTED, 2)
code_box(s, 5.3, 1.55, 4.35, 3.55, [
    "Input: goal G, environment E",
    "H ← ∅                  # history",
    "while not Done(G) do",
    "  r ← LLM_Reason(G, H)  # Thought",
    "  a ← Select_Tool(r)    # Action",
    "  o ← Execute(a, E)     # Observe",
    "  H ← H ∪ {(r, a, o)}",
    "  if Need_Replan(o):",
    "      G ← Update(G, o)",
    "return FinalAnswer(G, H)"], title="Pseudocode", size=12)
box(s, 5.3, 5.3, 4.35, 1.45, fill=PALE, align="l", anchor="m", margin=0.12, paras=[
    [("Example: ", {"bold": True, "color": NAVY}), ("“What is the weather in Wardha?”", {"italic": True})],
    "Thought: needs live data → Action: weather_api(\"Wardha\") → Observation: 31 °C, clear → Answer"],
    size=13, after=3)
notes(s, "ReAct, proposed by Yao et al., is the core loop inside most agents. At each step the model "
         "first produces a Thought - its reasoning about what to do. It then picks an Action, usually a "
         "tool call, and reads the Observation that comes back. The thought, action and observation are "
         "added to the history so the next step is better informed. The loop stops when the goal is met. "
         "The example shows how the agent decides it needs live data and calls a weather tool.")

# 11. Algorithm 2: planning & coordination
s = d.content_slide("Algorithm 2: Planning & Coordination", size=26)
text(s, 0.5, 1.12, 9.0, 0.35, "Task decomposition into a task graph (example goal: market-research report)",
     size=14, bold=True, color=NAVY)
box(s, 0.4, 1.95, 1.45, 1.05, fill=BLUE, paras=[[("Goal", {"bold": True})], "research report"],
    size=12, color=WHITE)
tasks = [((2.15, 1.6), "t1: Search news", "Research agent"), ((2.15, 2.62), "t2: Search papers", "Research agent"),
         ((4.1, 2.11), "t3: Analyse data", "Coding agent"), ((6.0, 2.11), "t4: Draft report", "Writer agent"),
         ((7.9, 2.11), "t5: Review & fix", "Critique agent")]
for (x, y), t, a in tasks:
    box(s, x, y, 1.65, 0.78, fill=WHITE, line=NAVY, paras=[[(t, {"bold": True})],
                                                           [(a, {"italic": True, "color": ACC, "size": 11})]],
        size=12)
arrow(s, 1.85, 2.3, 2.15, 1.99, MUTED, 1.5)
arrow(s, 1.85, 2.65, 2.15, 3.01, MUTED, 1.5)
arrow(s, 3.8, 1.99, 4.1, 2.35, MUTED, 1.5)
arrow(s, 3.8, 3.01, 4.1, 2.75, MUTED, 1.5)
arrow(s, 5.75, 2.5, 6.0, 2.5, MUTED, 1.5)
arrow(s, 7.65, 2.5, 7.9, 2.5, MUTED, 1.5)
text(s, 0.4, 3.5, 9.2, 0.35, [[("P ← LLM_Plan(G); T ← Decompose(P); assign agents; merge results", {})]],
     size=12, font=MONO_FONT, color=INK, align="c")
text(s, 0.5, 3.95, 9.0, 0.4, "Coordination patterns", size=16, bold=True, color=NAVY)
pats = [("Centralized", "One orchestrator assigns all work", "+ simple control", "− single bottleneck"),
        ("Hierarchical", "Managers delegate to sub-teams", "+ scales to big tasks", "− more delay"),
        ("Decentralized", "Peers negotiate directly", "+ robust, no single point", "− hard to coordinate")]
for i, (t, desc, pro, con) in enumerate(pats):
    x = 0.5 + i * 3.075
    box(s, x, 4.4, 2.85, 2.4, fill=PALE)
    text(s, x + 0.1, 4.45, 2.65, 0.35, t, size=14, bold=True, color=NAVY, align="c")
    mx, my = x + 1.425, 5.3  # mini diagram centre
    if i == 0:
        pts = [(mx - 0.8, my + 0.3), (mx, my + 0.42), (mx + 0.8, my + 0.3)]
        for px, py in pts:
            line(s, mx, my - 0.15, px, py, MUTED, 1.25)
        box(s, mx - 0.18, my - 0.38, 0.36, 0.36, fill=NAVY, shape="oval")
        for px, py in pts:
            box(s, px - 0.13, py - 0.13, 0.26, 0.26, fill=ACC, shape="oval")
    elif i == 1:
        lv1 = [(mx - 0.6, my + 0.05), (mx + 0.6, my + 0.05)]
        lv2 = [(mx - 0.9, my + 0.45), (mx - 0.3, my + 0.45), (mx + 0.3, my + 0.45), (mx + 0.9, my + 0.45)]
        for px, py in lv1:
            line(s, mx, my - 0.3, px, py, MUTED, 1.25)
        for k, (px, py) in enumerate(lv2):
            line(s, *lv1[k // 2], px, py, MUTED, 1.25)
        box(s, mx - 0.16, my - 0.46, 0.32, 0.32, fill=NAVY, shape="oval")
        for px, py in lv1:
            box(s, px - 0.13, py - 0.13, 0.26, 0.26, fill=BLUE, shape="oval")
        for px, py in lv2:
            box(s, px - 0.1, py - 0.1, 0.2, 0.2, fill=ACC, shape="oval")
    else:
        pts = [(mx - 0.55, my - 0.3), (mx + 0.55, my - 0.3), (mx + 0.55, my + 0.35), (mx - 0.55, my + 0.35)]
        for a in range(4):
            for b in range(a + 1, 4):
                line(s, *pts[a], *pts[b], MUTED, 1.25)
        for px, py in pts:
            box(s, px - 0.13, py - 0.13, 0.26, 0.26, fill=ACC, shape="oval")
    text(s, x + 0.12, 5.85, 2.61, 0.95, [desc, [(pro, {"color": GREEN, "bold": True})],
                                         [(con, {"color": RED, "bold": True})]], size=12, align="c", after=1)
notes(s, "For complex goals, the planner asks the LLM for a plan and decomposes it into subtasks with "
         "dependencies - a task graph. Independent tasks such as the two searches run in parallel; dependent "
         "ones wait. Each subtask goes to a specialised agent and the manager combines the results. "
         "Agents can be coordinated centrally, hierarchically or in a decentralized way: centralized is "
         "simplest but creates a bottleneck, hierarchical scales better, decentralized is robust but harder "
         "to keep consistent.")

# 12. Algorithm 3: memory & protocols
s = d.content_slide("Algorithm 3: Memory & Interoperability", size=26)
text(s, 0.4, 1.12, 4.4, 0.38, "Context management [5]", size=16, bold=True, color=NAVY)
box(s, 0.4, 1.6, 2.05, 0.78, fill=BLUE, paras=[[("Short-term", {"bold": True})], "recent k turns"], size=12,
    color=WHITE)
box(s, 2.65, 1.6, 2.05, 0.78, fill=BLUE, paras=[[("Long-term", {"bold": True})], "retrieve from vector DB"],
    size=12, color=WHITE)
box(s, 1.3, 2.68, 2.5, 0.5, fill=WHITE, line=NAVY, paras="Merge into context", size=12, bold=True)
arrow(s, 1.42, 2.38, 1.9, 2.68, MUTED, 1.5)
arrow(s, 3.68, 2.38, 3.2, 2.68, MUTED, 1.5)
box(s, 1.5, 3.42, 2.1, 0.95, fill=GOLD, shape="diamond", paras="Too long?", size=12, bold=True)
arrow(s, 2.55, 3.18, 2.55, 3.42, MUTED, 1.5)
box(s, 1.3, 4.65, 2.5, 0.55, fill=WHITE, line=ORANGE, paras="Summarize / prune old items", size=12)
arrow(s, 2.55, 4.37, 2.55, 4.65, MUTED, 1.5)
text(s, 2.6, 4.33, 0.6, 0.3, "yes", size=11, color=MUTED)
box(s, 1.3, 5.5, 2.5, 0.6, fill=NAVY, paras="Context sent to LLM", size=13, bold=True, color=WHITE)
arrow(s, 2.55, 5.2, 2.55, 5.5, MUTED, 1.5)
polyline(s, [(1.5, 3.9), (0.75, 3.9), (0.75, 5.8), (1.3, 5.8)], MUTED, 1.5)
text(s, 0.8, 3.6, 0.6, 0.3, "no", size=11, color=MUTED)
text(s, 0.4, 6.25, 4.4, 0.55, "AgeMem: the agent learns when to store, retrieve, update, summarize or discard.",
     size=12, italic=True, color=MUTED)
line(s, 5.0, 1.2, 5.0, 6.75, LIGHT, 1.5)
text(s, 5.2, 1.12, 4.4, 0.38, "MCP & A2A protocols [6]", size=16, bold=True, color=NAVY)
box(s, 5.25, 1.75, 1.55, 0.65, fill=NAVY, paras="Agent A", size=13, bold=True, color=WHITE)
box(s, 8.0, 1.75, 1.55, 0.65, fill=NAVY, paras="Agent B", size=13, bold=True, color=WHITE)
arrow(s, 6.8, 2.08, 8.0, 2.08, ACC, 2.5, head="both")
text(s, 6.8, 1.5, 1.2, 0.3, "A2A", size=13, bold=True, color=ACC, align="c")
for x, labels in ((5.25, ("Database", "GitHub")), (8.0, ("Files", "Web API"))):
    for k, lab in enumerate(labels):
        bx = x + k * 0.82 - 0.05
        box(s, bx, 3.2, 0.78, 0.5, fill=LIGHT, paras=lab, size=11)
        arrow(s, x + 0.775, 2.4, bx + 0.39, 3.2, BLUE, 1.5)
    box(s, x + 0.47, 2.62, 0.6, 0.3, fill=WHITE, line=BLUE, lw=1, paras="MCP", size=11, bold=True, color=BLUE,
        margin=0.01)
for k, (t, col, body, eg) in enumerate((
        ("MCP", BLUE, "Standard way for an agent to discover and call tools and data (agent ↔ tool).",
         "e.g. query a database or GitHub through an MCP server"),
        ("A2A", ACC, "Standard way for agents to delegate tasks and share results (agent ↔ agent).",
         "e.g. a planner agent hands a coding task to a coding agent"))):
    x = 5.2 + k * 2.25
    box(s, x, 4.05, 2.15, 2.7, fill=PALE)
    text(s, x + 0.1, 4.12, 1.95, 0.42, t, size=18, bold=True, color=col, align="c")
    text(s, x + 0.12, 4.58, 1.91, 2.1, [body, [(eg, {"italic": True, "color": MUTED, "size": 12})]],
         size=13, align="c", after=6)
notes(s, "Agents work over long tasks, so the context window fills up. The memory algorithm combines recent "
         "interactions with relevant items retrieved from long-term storage such as a vector database; if the "
         "context is too long it summarises or prunes old items. AgeMem goes further by letting the agent learn "
         "these memory operations. On the right: MCP is a standard for connecting an agent to tools and data; "
         "A2A is a standard for agents talking to other agents. Together they make large agent systems interoperable.")

# 13. Features / advantages / disadvantages
s = d.content_slide("Features / Advantages / Disadvantages", size=26)
three_columns(d, s, [
    ("Features", NAVY, "star", [("Autonomy", "pursues a goal over many steps"),
                                ("Planning", "breaks goals into subtasks"),
                                ("Tool use", "web, code, APIs, databases"),
                                ("Memory", "short- and long-term context"),
                                ("Reflection", "verifies and replans")]),
    ("Advantages", GREEN, "check", [("Complex tasks", "handles multi-step workflows"),
                                    ("Specialisation", "agents work in parallel"),
                                    ("Live data", "external tools and sources"),
                                    ("Productivity", "less repetitive human effort"),
                                    ("Interoperable", "MCP / A2A ease scaling [6]")]),
    ("Disadvantages", RED, "warn", [("Error chains", "mistakes compound over steps"),
                                    ("Security", "prompt injection, tool abuse [8]"),
                                    ("Cost", "many LLM calls, higher latency"),
                                    ("Evaluation", "hard to test reliably [2]"),
                                    ("Oversight", "still needs human checks")]),
])
notes(s, "Key features are autonomy, planning, tool use, memory and reflection. The advantages follow: agents "
         "handle complex workflows, specialise and parallelise, and use live data. The disadvantages are "
         "important: one wrong step can cascade, external content can inject malicious instructions, multi-agent "
         "systems use many model calls so they are costly, and reliable evaluation is still an open problem.")

# 14. Applications
s = d.content_slide("Applications")
app_grid(d, s, [
    ("code", "Software Engineering", "Coding agents write, run, test and debug code in a loop."),
    ("search", "Research Assistants", "Orchestrator + parallel search agents compile reports [11]."),
    ("bug", "Cybersecurity", "Agents discover vulnerabilities and run security tests [7]."),
    ("robot", "Industrial Robotics", "Long-horizon task planning with failure-aware replanning [9]."),
    ("cogs", "Business Workflows", "Automating support tickets, data entry and reporting."),
    ("user", "Personal Assistants", "Email, scheduling and travel booking through tools."),
], circ=NAVY)
notes(s, "Agentic AI is already used in software engineering, where agents write and test code; in research, "
         "where Anthropic describes an orchestrator that runs several search agents in parallel; in "
         "cybersecurity for vulnerability discovery; in industrial robotics for long-horizon planning such as "
         "GLaMP; and in business and personal productivity.")

# 15. Analysis / comparison
s = d.content_slide("Analysis / Comparison")
rows = [["Aspect", "Single LLM (prompt-response)", "Single Agent (ReAct + tools)", "Multi-Agent System"],
        ["Task type", "One-shot answers", "Multi-step tasks", "Large, parallel, multi-skill tasks"],
        ["Tools", "None", "Yes", "Specialised tools per agent"],
        ["Memory", "Prompt window only", "Short + long-term", "Per-agent + shared"],
        ["Error handling", "User re-prompts", "Self-reflection loop", "Critique agents + verification"],
        ["Cost / latency", "Low", "Medium", "High (many LLM calls) [11]"],
        ["Main risk", "Hallucination", "Tool misuse, loops", "Coordination failures"]]
table(s, 0.45, 1.3, [1.55, 2.4, 2.45, 2.7], rows, size=13, header_size=13, row_h=0.6, first_col_bold=True)
box(s, 0.45, 5.75, 9.1, 1.05, fill=PALE, align="l", anchor="m", margin=0.14, paras=[
    [("Framework study [10]: ", {"bold": True, "color": NAVY}),
     ("CrewAI, AutoGen and LangChain each suit different workloads; a hybrid design is proposed "
      "(gains reported on its own benchmark).", {})],
    [("Design rule: ", {"bold": True, "color": ACC}),
     ("use the simplest design that works — add agents only for parallelism or specialisation.", {})]],
    size=13, after=4)
notes(s, "Comparing three levels: a single LLM is cheap but cannot act; a single agent with ReAct and tools "
         "handles multi-step tasks; a multi-agent system handles large parallel work but costs more and can fail "
         "in coordination. The framework study compares CrewAI, AutoGen and LangChain and proposes a hybrid; its "
         "numbers apply to its own benchmark. The practical rule is to start simple.")

# 16. Conclusion
conclusion_slide(d, [
    "Agentic AI moves LLMs from answering prompts to completing goals.",
    "ReAct loops, task decomposition and memory are the core building blocks.",
    "Multi-agent designs add specialisation and parallelism — at higher cost.",
    "MCP and A2A make tools and agents interoperable."],
    ["Learned long-term memory management [5]",
     "Standard benchmarks for agent reliability [2]",
     "Stronger defences against prompt injection [8]",
     "Domain agents: software, security, robotics [7], [9]"],
    "Reliable agents = orchestration + memory + coordination + evaluation + safeguards")
notes(d.prs.slides[-1], "To conclude: agentic AI is a shift from prompt-response to goal-directed systems. Its "
      "building blocks are the ReAct loop, planning, memory and tools; multi-agent systems add specialisation. "
      "Future work is in learned memory, standard evaluation, security, and domain-specific agents. My main "
      "conclusion is that reliability comes from the whole system design, not just a bigger model.")

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
s = references_slide(d, refs[:6], 1)
notes(s, "References in IEEE format; numbers in square brackets on the slides point to this list.")
s = references_slide(d, refs[6:], 7)
notes(s, "References continued. [11] is an industry engineering report, not a peer-reviewed paper.")

# 19. Thank you
s = thank_you_slide(d, "Utkarsh Kale  |  Roll No.: B342")
notes(s, "Thank you. I am happy to take questions.")

d.save(OUT)
print("saved", OUT, len(d.prs.slides))
