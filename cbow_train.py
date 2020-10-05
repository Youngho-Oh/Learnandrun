import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from lib import perceptron as pe
from lib import vector as np
from lib import layer as la
from lib import loss as lo
from lib import layer_naive as ln
from lib import optimizer as op
from lib import cbow
from lib import util
from corpus import corpus


window_size = 1
hidden_size = 5
batch_size = 3
max_epoch = 1000

text = 'You say goodbye and I say hello'
corpus, word_to_id, id_to_word = corpus.preprocess(text)

vocab_size = len(word_to_id)
#TODO
contexts, target = util.create_contexts_target(corpus, window_size)
#target = convert_one_hot(target, vocab_size)
#contexts = covert_one_hot(contexts, vocab_size)

#model = cw.CBOW(vocab_size, hidden_size)
#optimizer = op.Adam()
#trainer = Trainer(model, optimizer)

#trainer.fit(contexts, target, max_epoch, batch_size)
