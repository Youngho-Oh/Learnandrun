import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from corpus import corpus as cp
from lib import vector as np
from lib.util import create_co_matrix

text = 'You say boodbye and I say hello.'
corpus, word_to_id, id_to_word = cp.preprocess(text)

vocab_size = len(word_to_id)

print vocab_size
print text
print corpus
print word_to_id
print id_to_word
C = create_co_matrix(corpus, vocab_size)

print "<C-matrix>"
print C
#c0 = np.arange(C.get_origin_list()[word_to_id['you']])
#c1 = np.arange(C.get_origin_list()[word_to_id['i']])
#print(cp.cos_similarity(c0, c1))

print "<COS SIMILARITY>"
print cp.most_similar('you', word_to_id, id_to_word, C)

W = cp.ppmi(C)
print "<PPMI>"
print W
