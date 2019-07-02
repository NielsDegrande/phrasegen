# PhraseGen

PhraseGen example to illustrate some DevOps concepts.

Run on production server using:
```bash
sudo docker run --rm --name phrasegen phrasegen --theme {specify_theme}
```

Run locally by:
```bash
pip install -e .
phrasegen --theme {specify_theme}
```

To install the development packages locally:
```bash
pip install -e .[dev]
```
