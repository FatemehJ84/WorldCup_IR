class SearchEngine:
    def __init__(self, index, documents, dataframe):
        self.index = index
        self.documents = documents
        self.df= dataframe

    def search(self, query,tfidf): 
        words = query.lower().split()
        result = set()
        for word in words:
            posting = self.index.get_postings(word)
            result.update(posting.keys())
        return self.ranking(result,words,tfidf)

    def get_documents(self, term):
        posting =self.index.get_postings(term.lower())
        return set(posting.keys())
    
    def and_search(self, term1, term2):
        docs1 =self.get_documents(term1)
        docs2 =self.get_documents(term2)
        return sorted(docs1&docs2)
    
    def or_search(self, term1, term2):
        docs1 =self.get_documents(term1)
        docs2 =self.get_documents(term2)
        return sorted(docs1 | docs2)
    
    def not_search(self, term):
        docs =self.get_documents(term)
        all_docs =set(self.documents.keys())
        return sorted(all_docs-docs)
    
    def A_not_B_search(self, term1, term2):
        docs1 =self.get_documents(term1)
        docs2 =self.get_documents(term2)
        return sorted(docs1-docs2)
    
    def boolean_search(self, query,tfidf):
        tokens =query.split()
        if len(tokens)!=3:
            print("Invalid Boolean Query")
            return [] 
        elif len(tokens)==3:
            term1 =tokens[0]
            operator =tokens[1].lower()
            term2 =tokens[2]
            if operator == "and":
                docs= self.and_search(term1,term2)
                return self.ranking(docs,[term1,term2],tfidf)
            elif operator == "or":
                docs= self.or_search(term1,term2)
                return self.ranking(docs,[term1,term2],tfidf)
            elif operator == "not":
                docs= self.A_not_B_search(term1,term2)
                return self.ranking(docs,[term1],tfidf)
            else:
                print("Unknown Operator")
                return []
        
    

    def ranking(self, documents, terms, tfidf):
        scores ={}
        for doc_id in documents:
            score =0
            for term in terms:
                posting =self.index.get_postings(term)
                if doc_id in posting:
                    score+=tfidf.get_weight(term,doc_id)
            scores[doc_id]=score
        return sorted(
            scores.items(),
            key=lambda x: x[1],
            reverse=True
        )
    
        
    def print_results(self, results):
        if len(results) == 0:
            print("No Results Found :(")
            return
        print(f"\nFound {len(results)} result(s)\n")
        for rank, (doc_id,score) in enumerate(results,start=1):
            row = self.df.iloc[doc_id]
            print("="*70)
            print(f"Rank    : #{rank}")
            print(f"DocID   : {doc_id}")
            print(f"Match   : {row['home_team']} vs {row['away_team']}")
            print(f"Date    : {row['Date']}")
            print(f"Stage   : {row['Round']}")
            print(f"Venue   : {row['Venue']}")
            print(f"Host    : {row['Host']}")
            print(f"Referee : {row['Referee']}")
            print(f"Score   : {row['Score']}")
            print(f"TF-IDF  : {score:.4f}")
            print("-"*70)
            preview = " ".join(self.documents[doc_id][:35])
            print("Preview:")
            print(preview)
            print()
            