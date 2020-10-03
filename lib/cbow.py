import sys
import vector as ve
import layer_naive as ln

# TO BE 10e-2
global SET_CENTI
SET_CENTI = 0.01

#CBOW : Continuous Bag-Of-Words
class CBOW:
    def __init__(self, vocab_size, hidden_size):
        V, H = vocab_size, hidden_size

        # Init weight factors
        W_in = ve.random.randn(V, H) * SET_CENTI
        W_out = ve.random.randn(H, V) * SET_CENTI

        # Create layer
        self.in_layer0 = ln.MatMul(W_in)
        self.in_layer1 = ln.MatMul(W_in)
        self.out_layer = ln.MatMul(W_out)
        self.loss_layer = ln.SoftmaxWithLoss()

        layers = [self.in_layer0, self.in_layer1, self.out_layer]
        self.params, self.grads = [], []
        for layer in layers:
            self.params += layer.params
            self.grads += layer.grads
        
        self.word_vecs = W_in

    def forward(self, contexts, target):
        h0 = self.in_layer0.forward(contexts[0])
        h1 = self.in_lyaer1.forward(contexts[1])
        h = (h0 + h1) * 0.5   #calculate average between h0 and h1
        score = self.out_layer.forward(h)
        loss = self.loss_layer.forward(score, target)

        return loss

    def backward(self, dout=1):
        ds = self.loss_layer.backward(dout)
        da = self.out_layer.backward(ds)
        da = da * 0.5
        self.in_layer0.backward(da)
        self.in_layer1.backward(da)

        return None
