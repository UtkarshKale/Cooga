# Building the seminar decks

Both decks are generated with python-pptx on the BIT Seminar-I template's 4:3 canvas
(`../template/`), reusing its institute logo and header banner. `design.py` holds the shared
design system (palettes, cover, agenda, content frame, cards, tables, code panels); each
deck script holds its content. Diagrams are native, editable PowerPoint shapes.

```bash
# icons (one-time): needs react, react-dom, react-icons, sharp in some node_modules dir
node render_icons.js <node_modules dir> <icon out dir>

python3 agentic_ai.py  ../template/Seminar-I_PPT_Template2025-26.pptx <icon dir> out_agentic.pptx
python3 disaster_ai.py ../template/Seminar-I_PPT_Template2025-26.pptx <icon dir> out_disaster.pptx
```
