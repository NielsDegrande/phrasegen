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
_Running pip install -e . will add the project folder to sys.path, create a symbolic link from site-packages to the project folder, as well as generate egg-info._

Alternatively:
```bash
pip install -r requirements.txt
python -m phrasegen --theme {specify_theme}
```
_Using -m approach allows to find modules without adding it to sys.path_

To install the development packages locally:
```bash
pip install -e ".[dev]"
```

To package (software or binary distribution), e.g. for PyPi:
```bash
python setup.py sdist bdist_wheel
```
