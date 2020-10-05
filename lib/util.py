import vector as np

def im2col(input_data, filter_h, filter_w, stride=1, pad=0):
  """ Trasnmake from several images to 2-demension matrix
  
  Parameters
  ---------
  input_data : 4-demension matrix input data(num of images, num of channels, height, width)
  filter_h : height of filter
  filter_w : width of filter
  stride : stride
  pad : padding

  Returns
  ---------
  col : 2-demension matrix
  """

  N = input_data.get_demension()[0]
  C = input_data.get_demension()[1]
  H = input_data.get_demension()[2]
  W = input_data.get_demension()[3]
  out_h = ((H + 2 * pad - filter_h) / stride) + 1
  out_w = ((W + 2 * pad - filter_w) / stride) + 1


def create_co_matrix(corpus, vocab_size, window_size=1):
  corpus_lst = corpus.get_origin_list()
  corpus_size = len(corpus_lst)
  co_matrix = np.arange([0 for _ in range(vocab_size * vocab_size)]).reshape(vocab_size, vocab_size)

  for idx, word_id in enumerate(corpus_lst):
    for i in range(1, window_size + 1):
      left_idx = idx - 1
      right_idx = idx + 1

      if left_idx >= 0:
        left_word_id = corpus_lst[left_idx]
        co_matrix.get_origin_list()[word_id][left_word_id] += 1

      if right_idx < corpus_size:
        right_word_id = corpus_lst[right_idx]
        co_matrix.get_origin_list()[word_id][right_word_id] += 1

  return co_matrix

def create_contexts_target(corpus, window_size=1):
    corpus_lst = corpus.get_origin_list()
    target = corpus_lst[window_size:-window_size]
    contexts = []

    for idx in range(window_size, len(corpus_lst)-window_size):
        cs = []
        for t in range(-window_size, window_size+1):
            if t == 0 :
                continue
            cs.append(corpus_lst[idx+1])
        contexts.append(cs)

    return np.arange(contexts), np.arange(target) 
