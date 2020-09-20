# Epidey Live Search: Relevant research-articles at your fingertips


[![Jina](https://github.com/jina-ai/jina/blob/master/.github/badges/jina-badge.svg?raw=true "We fully commit to open-source")](https://get.jina.ai)

[![](epidey-demo.gif)]()

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

**Table of Contents**

- [Use toy data](#use-toy-data)
- Download full research abstract dataset
- [Install](#install)
- [Run](#run)
- [View in Browser](#view-in-browser)
- [License](#license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Use toy data

As the project was built upon the multisearch-lyrics example provided by Jina, the example can be run on the toy-data initially provided by them. 
This data is ready to use with this example by simply switching to `input_fn` within your `index` function.

```python
# for index
def index():
    """ Please switch the input function for whichever data-set you want to test for """
    f = Flow.load_config('flows/index.yml')

    with f:
        f.index(input_fn, batch_size=8) # the input_fn refers to lyrics toy-data ingestion
```

## Download full research dataset

If you want to use the an actual research dataset which is what the project is meant to be based on, you can download it from kaggle (https://www.kaggle.com/nikhilmittal/research-paper-abstracts).

1. Download the `archive.zip` file
2. Unzip and copy the `data_input.csv` to the `toy-data` folder
3. Switch to `input_fn_research` within your `index` function:

```python
# for index
def index():
    """ Please switch the input function for whichever data-set you want to test for """
    f = Flow.load_config('flows/index.yml')

    with f:
        f.index(input_fn_research, batch_size=8) # the input_fn_research refers to research toy-data ingestion
```

## Install

```bash
pip install -r requirements.txt
```

## Run

| Command                | Description                  |
| :--------------------- | :--------------------------- |
| `python app.py index`  | To index files/data          |
| `python app.py search` | To run query on the index    |
| `python app.py dryrun` | Sanity check on the topology |

<!--
## Run as a Docker Container

To build the docker image
```bash
docker build -t jinaai/hub.app.multires_lyrics_search:0.0.1 .
```

To mount local directory and run:
```bash
docker run -v "$(pwd)/j:/workspace" jinaai/hub.app.multires_lyrics_search:0.0.1
```

To query
```bash
docker run -p 65481:65481 -e "JINA_PORT=65481" jinaai/hub.app.multires_lyrics_search:0.0.1 search
``` -->

## View in Browser

```bash
cd static
python -m http.server
```

Open `http://0.0.0.0:8000/` in your browser.

## License

Copyright (c) 2020 Han Xiao. All rights reserved.
