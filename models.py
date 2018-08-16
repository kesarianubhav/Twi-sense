from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from gensim import models


class Models(object):

    def __init__(self, Model, preprocessed=True):
        self.model_type = Model
        self.preprocessed = preprocessed
