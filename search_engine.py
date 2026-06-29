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