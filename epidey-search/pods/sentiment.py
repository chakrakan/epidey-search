from nltk.sentiment.vader import SentimentIntensityAnalyzer
from jina.executors.crafters import BaseCrafter
import nltk

nltk.download('vader_lexicon')
nltk.download('punkt')


class SentimentAnalyzer(BaseCrafter):

    def craft(self, text: str, *args, **kwargs):
        sid = SentimentIntensityAnalyzer()
        scores = sid.polarity_scores(text)
        # sentiment = self.calculate_sentiment()
        # doc.meta_info["sentiment"] = sentiment
        for key in sorted(scores):
            print('{0}: {1}, '.format(key, scores[key]), end='')

        return dict(weight=1., text=text, meta_info=str(scores['compound']).encode('utf8'))
