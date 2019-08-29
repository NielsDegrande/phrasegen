FROM python:3.7

COPY requirements.txt /home/phrasegen/
COPY phrasegen/ /home/phrasegen/phrasegen/

WORKDIR /home/phrasegen/

RUN pip install .

ENTRYPOINT ["phrasegen"]
CMD ["--help"]
