FROM python:3.7

COPY main.py requirements.txt /home/phrasegen/
COPY phrasegen/*.py /home/phrasegen/phrasegen/

WORKDIR /home/phrasegen/

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/home/phrasegen/main.py]
