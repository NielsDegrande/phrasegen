FROM python:3.7

COPY requirements.txt /home/phrasegen/
COPY phrasegen/ /home/phrasegen/phrasegen/

WORKDIR /home/phrasegen/

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/home/phrasegen/phrasegen/__main__.py"]
CMD ["--help"]
