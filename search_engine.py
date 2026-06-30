class SearchEngine:
    def __init__(self, index, documents, dataframe):
        self.index = index
        self.documents = documents
        self.df= dataframe

    def search(self, query): 
        words = query.lower().split()
        result = set()
        for word in words:
            posting = self.index.get_postings(word)
            result.update(posting.keys())
        return sorted(result)

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
    
    def boolean_search(self, query):
        tokens =query.split()
        if len(tokens)==2:
            operator= tokens[0]
            term1= tokens[1].lower()
            if  operator == "not":
                return self.not_search(term1)
            else:
                print("Invalid Boolean Query")
                return [] 
        elif len(tokens)==3:
            term1 =tokens[0]
            operator =tokens[1].lower()
            term2 =tokens[2]
            if operator == "and":
                return self.and_search(term1,term2)
            elif operator == "or":
                return self.or_search(term1,term2)
            elif operator == "not":
                return self.A_not_B_search(term1,term2)
            else:
                print("Unknown Operator")
                return []
        else:
            len(tokens)!=3
            print("Invalid Boolean Query")
            return []
        
    
        
    def print_results(self, results):
        if len(results) == 0:
            print("No Results Found :(")
            return
        print(f"\nFound {len(results)} result(s)\n")
        for i,doc_id in enumerate(results,start=1):
            row = self.df.iloc[doc_id]
            print("="*70)
            print(f"Result #{i}")
            print(f"DocID   : {doc_id}")
            print(f"Match   : {row['home_team']} vs {row['away_team']}")
            print(f"Date    : {row['Date']}")
            print(f"Stage   : {row['Round']}")
            print(f"Venue   : {row['Venue']}")
            print(f"Host    : {row['Host']}")
            print(f"Referee : {row['Referee']}")
            print(f"Score   : {row['Score']}")
            print("-"*70)
            preview = " ".join(self.documents[doc_id][:35])
            print("Preview:")
            print(preview)
            print()