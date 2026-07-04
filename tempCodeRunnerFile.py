engine = SearchEngine(index, processed_docs,builder.df)
# controller = Controller(engine, tfidf)

# while True:
#     query = input("\nSearch : ")
#     if query.lower()=="exit":
#         print("Good Bye!")
#         break
#     controller.choose(query)