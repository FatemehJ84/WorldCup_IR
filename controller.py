class Controller:
    def __init__(self, engine, tfidf):
        self.engine = engine
        self.tfidf = tfidf

    def choose(self, query):
        # Boolean Search
        if " AND " in query or " OR " in query or " NOT " in query:
            results=self.engine.boolean_search(query,self.tfidf)
            self.engine.print_results(results)
        # normal search
        else:
            results=self.engine.search(query, self.tfidf)
            self.engine.print_results(results)