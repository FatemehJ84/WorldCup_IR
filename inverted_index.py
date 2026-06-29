from collections import defaultdict


class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(dict)

    def build(self, documents):
        for doc_id, tokens in documents.items():
            for position, term in enumerate(tokens):
                if doc_id not in self.index[term]:
                    self.index[term][doc_id] ={
                        "tf":0,
                        "positions":[]
                    }
                self.index[term][doc_id]["tf"] +=1
                self.index[term][doc_id]["positions"].append(position)

    def get_postings(self, term):
        return self.index.get(term,{})
    
    def print_index(self, limit=20):
        counter = 0
        for term, posting in self.index.items():
            print(term,"->",posting)
            counter +=1
            if counter >=limit:
                break