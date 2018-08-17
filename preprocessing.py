from gensim.models import Word2Vec
from gensim.test.utils import common_texts, get_tmpfile
from gensim.models import KeyedVectors
import numpy as np
# import numpy as
from constants import hyperparams
import gensim
# path = get_tmpfile('word2vec.model')

# model = Word2Vec(common_texts, size=hyperparams[
#                  'embed_size'], window=hyperparams['window'], workers=4)

# model.save("word2vec.model")
# model = Word2Vec.load("word2vec.model")


print(model.wv['computer'])
