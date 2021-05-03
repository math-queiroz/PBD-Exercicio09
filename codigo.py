import random

def scalar_multiply (escalar, vetor):
    return [escalar * i for i in vetor]

def vector_sum (vetores):
    res = vetores[0]
    for vetor in vetores[1:]:
        res = [res[i] + vetor[i] for i in range(len(vetor))]
    return res

def vector_mean (vetores):
    return scalar_multiply(1 / len(vetores), vector_sum(vetores))

def dot (v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares (v):
    return dot (v, v)

def vector_subtract (v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]

def squared_distance (v, w):
    return sum_of_squares(vector_subtract(v, w))

class Kmeans:
    def __init__(self, k, means = None):
        self.k = k
        self.means = means
        self.points = []

    def classify(self, ponto):
        return min(range(self.k), key = lambda i: squared_distance(ponto, self.means[i]))

    def train (self, pontos):
        self.means = random.sample(pontos, self.k)
        assignments = None
        while True:
            new_assignments = list(map (self.classify, pontos))
            if new_assignments == assignments:
                return
            assignments = new_assignments
            self.points.clear()
            for i in range(self.k):
                i_points = [p for p, a in zip(pontos, assignments) if a == i]
                self.points.append(i_points)
                if i_points:
                    self.means[i] = vector_mean(i_points)

    def exibir_colecao(self):
        for i in range(self.k):
            print(f'Centroid {self.means[i]}: {self.points[i]}')

    
def test_k_means():
    dados = [[1], [2], [3], [6], [7], [10], [11]]
    kmeans = Kmeans(3, [[11], [10], [3]])
    kmeans.train(dados)
    kmeans.exibir_colecao()

test_k_means()