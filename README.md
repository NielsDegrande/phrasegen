# PhraseGen

PhraseGen example to illustrate some DevOps concepts.

Run as Docker container on production server (or Kubernetes cluster) using:
```bash
sudo docker run --rm --name phrasegen phrasegen --theme {specify_theme}
```

Run locally by:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install .
phrasegen --theme {specify_theme}
```

Run locally for development ("editable" install) by:
```bash
tox -e dev
phrasegen --theme {specify_theme}
python -m phrasegen --theme {specify_theme} # Alternative.
```
_Tox will create an editable install (similar to pip install -e .), which will add the project folder to sys.path, create a symbolic link from site-packages to the project folder, and generate egg-info._
_Alternative with -m relies on \_\_main\_\_.py. Note that -m allows to find modules (with '.' path) to be found without adding the project folder to sys.path (in case of no editable install)._


To package (software or binary distribution), e.g. for PyPi:
```bash
python setup.py sdist bdist_wheel
```
