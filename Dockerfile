FROM python:latest

COPY setup.py README.md requirements.txt requirements_dev.txt /home/phrasegen/
COPY phrasegen/ /home/phrasegen/phrasegen/

WORKDIR /home/phrasegen/

RUN pip install .

ENTRYPOINT ["phrasegen"]
CMD ["--help"]
