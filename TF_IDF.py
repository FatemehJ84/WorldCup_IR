import math

class TF_IDF:
    def __init__(self, index, documents):
        self.index = index
        self.documents = documents
        self.N = len(documents)
        self.idf ={}
        self.weights ={}

    def calculate_idf(self):
        for term, posting in self.index.index.items():
            df =len(posting)
            print('df:  {}'.format(df))
            self.idf[term] =math.log(self.N/df)
            print("idf[]:  {}".format(self.idf[term]))


    def calculate_weights(self):
        self.calculate_idf()
        for term, posting in self.index.index.items():
            self.weights[term] = {}
            print("har kalameh:")
            for doc_id, info in posting.items():
                tf =info["tf"]
                print(tf)
                self.weights[term][doc_id] = tf*self.idf[term]
                print("wazn:  {}".format(self.weights[term][doc_id] ))


    def get_weight(self, term, doc_id):
        if term not in self.weights:
            return 0
        return self.weights[term].get(doc_id,0)