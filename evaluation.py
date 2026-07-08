class Evaluation:
    def __init__(self, engine, tfidf):
        self.engine = engine
        self.tfidf = tfidf

        self.queries =[
            "messi",
            "argentina final",
            "mbappe goal",
            "brazil semifinals",
            "ronaldo portugal",
            "morocco quarterfinals",
            "20221210", #تاریخ دوتا از مسابقات
            "penalty miss",
            "argentina AND france",
            "matches in lusail"
        ]
    
        self.relevent ={
            "messi":[0,3,7,15,27,43,56,78,91,107],
            "argentina final":[0,128,500,552,656,946],
            "mbappe goal":[],
            "brazil semifinals":[131,387,735,798,831,322,914,451],
            "ronaldo portugal":[126,50,16,145,35,314,79,95,224,108],
            "morocco quarterfinals":[4],
            "20221210":[4,5],
            "penalty miss":[5,86,103,122,199],
            "argentina AND france":[0,78,685],
            "matches in lusail":[0,3,7,9,18,26,35,43,51,56]
        }

    def retrieve(self, query):
        if " AND " in query or " OR " in query or " NOT " in query:
            results = self.engine.boolean_search(query, self.tfidf)
        else:
            results = self.engine.search(query, self.tfidf)
        return [doc_id for doc_id, score in results]


    def precision(self,retrieved,relevant):
        if len(retrieved)==0:
            return 0
        relevant_retrieved=0
        for doc in retrieved:
            if doc in relevant:
                relevant_retrieved+=1
        return relevant_retrieved/len(retrieved)
    
    def recall(self,retrieved,relevant):
        if len(relevant)==0:
            return 0
        relevant_retrieved=0
        for doc in retrieved:
            if doc in relevant:
                relevant_retrieved+=1
        return relevant_retrieved/len(relevant)
    
    def evaluate_query(self,query):
        retrieved=self.retrieve(query)
        relevant=self.relevant[query]
        p=self.precision(retrieved,relevant)
        r=self.recall(retrieved,relevant)
        print(query)
        print("Precision =",round(p,3))
        print("Recall =",round(r,3))

    def evaluate_all(self):
        total_p=0
        total_r=0
        for query in self.queries:
            retrieved=self.retrieve(query)
            relevant=self.relevent[query]
            p=self.precision(retrieved,relevant)
            r=self.recall(retrieved,relevant)
            total_p+=p
            total_r+=r
            print("="*60)
            print(query)
            print("Precision :",round(p,3))
            print("Recall :",round(r,3))
        print("="*60)
        print("Average Precision :",round(total_p/len(self.queries),3))
        print("Average Recall :",round(total_r/len(self.queries),3))