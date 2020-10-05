FROM jinaai/jina:0.6.3

COPY . /workspace
WORKDIR /workspace

RUN apt-get update && pip install -r requirements.txt

RUN python app.py search

ENTRYPOINT ["python", "app.py", "search"]