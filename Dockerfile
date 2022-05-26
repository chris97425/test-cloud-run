FROM python:3.8-buster
COPY api.py api.py
RUN pip3 install -U pip
RUN pip3 install fastapi uvicorn nltk
RUN python -m nltk.downloader vader_lexicon
CMD uvicorn api:app --host 0.0.0.0 --port $PORT
