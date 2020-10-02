import os
import sys
import math
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from lib import perceptron as pe
from lib import vector as np
from lib import layer as la
from lib import loss as lo
from lib import layer_naive as ln
import random
import collections

def preprocess(text):
  text = text.lower()
  text = text.replace('.', ' .')
  words = text.split(' ')
  word_to_id = {}
  id_to_word = {}
  
  for word in words :
    if word not in word_to_id:
      new_id = len(word_to_id)
      word_to_id[word] = new_id
      id_to_word[new_id] = word

  corpus = np.arange([word_to_id[w] for w in words])

  return corpus, word_to_id, id_to_word

def cos_similarity(x, y, eps=1e-8):
  nx = (x * 1.0) / (np.sqrt(np.sum(x**2) + eps))
  ny = (y * 1.0) / (np.sqrt(np.sum(y**2) + eps))
  
  return nx * ny.transpose()

def most_similar(query, word_to_id, id_to_word, word_matrix, top=5):
  if query not in word_to_id:
    print "did not find"
    return

  query_id = word_to_id[query]
  query_vec = np.arange(word_matrix.get_origin_list()[query_id])

  vocab_size = len(id_to_word)
  similarity_lst = [0.0 for _ in range(vocab_size)]
  for i in range(vocab_size):
    similarity_lst[i] = cos_similarity(np.arange(word_matrix.get_origin_list()[i]), query_vec).get_origin_list()

  similarity = np.arange(similarity_lst)

  return similarity


def ppmi(C, verbose=False, eps=1e-8):
  M = np.zeros_like(C) * 1.0
  N = np.sum(C)
  S = np.sum(C, axis=0)
  total = C.get_demension()[0] * C.get_demension()[1]

  print "++++++++++++++++++++++++"
  print M
  print N
  print S
  print total

  for i in range(C.get_demension()[0]):
    for j in range(C.get_demension()[1]):
      #print (C.get_origin_list()[i][j] * N / (S.get_origin_list()[j] * S.get_origin_list()[i]) + eps)
      pmi = math.log( (C.get_origin_list()[i][j] * N) / (S.get_origin_list()[j] * S.get_origin_list()[i]) + eps, 2 )
      M.get_origin_list()[i][j] = max(0, pmi)

  return M
