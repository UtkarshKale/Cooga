# Building the seminar decks

Both decks are generated from the BIT Seminar-I template (`../template/`) with python-pptx.
Every slide is a clone of a template slide, so the template's header banner, logo, title
styling and slide numbers are kept; diagrams are native, editable PowerPoint shapes.

```bash
# icons (one-time): needs react, react-dom, react-icons, sharp in some node_modules dir
node render_icons.js <node_modules dir> <icon out dir>

python3 agentic_ai.py  ../template/Seminar-I_PPT_Template2025-26.pptx <icon dir> out_agentic.pptx
python3 disaster_ai.py ../template/Seminar-I_PPT_Template2025-26.pptx <icon dir> out_disaster.pptx
```
