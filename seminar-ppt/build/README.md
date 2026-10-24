# Building the seminar decks

Both decks are generated with python-pptx on the BIT Seminar-I template's 4:3 canvas
(`../template/`), reusing its institute logo and header banner, and follow the template's
section order. Each deck has its own, deliberately different design system:

- `utkarsh_design.py` — "neon night" (dark glow backgrounds, glass panels, gradients, mono labels)
  for `agentic_ai.py`
- `vedika_design.py` — "hazard signage" (white, amber/charcoal blocks, all-sans) for `disaster_ai.py`

`design.py` provides the shared text/shape primitives. Diagrams are native, editable shapes.

```bash
node render_icons.js <node_modules with react, react-dom, react-icons, sharp> <icon dir>
python3 make_backgrounds.py <bg dir>          # glow backgrounds for the Agentic AI deck
T=../template/Seminar-I_PPT_Template2025-26.pptx
python3 agentic_ai.py  $T <icon dir> <bg dir> out_agentic.pptx
python3 disaster_ai.py $T <icon dir> out_disaster.pptx
```
