# Donald Trump NLP #

Natural language processing with Trump Tweets and Speeches.

# Setting up your environment #

Use [conda](http://conda.pydata.org/docs/index.html).

Run `conda env create -f environment.yml` to create a python environment called `lant-nlp` complete with:

- [ipython](https://ipython.org/)
- [python-twitter](https://github.com/bear/python-twitter)
- [spacy](https://spacy.io/)

# Scraping tweets #

Set the following environment variables in your shell (and make sure your python process inherits them):

- `CONSUMER_KEY` (your twitter consumer API key)
- `CONSUMER_SECRET` (your twitter consumer API secret)
- `ACCESS_TOKEN` (your twitter access token)
- `ACCESS_SECRET` (your twitter access secret)

Then run `scripts/scrape_tweets.py`.

The most recent 200 tweets are already available in json form in `scripts/trump_tweets.json`


