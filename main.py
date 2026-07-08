import sys

from preprocessing import Preprocessor
sys.stdout.reconfigure(encoding='utf-8')
from doc_builder import DocumentBuilder
from inverted_index import InvertedIndex
from search_engine import SearchEngine
from TF_IDF import TF_IDF
from controller import Controller
from evaluation import Evaluation

builder = DocumentBuilder("data/matches_1930_2022.csv")

builder.load_dataset()
docs = builder.build_documents()
pre = Preprocessor()
processed_docs = {}
for doc_id,text in docs.items():
    processed_docs[doc_id]=pre.preprocess(text)
index = InvertedIndex()
index.build(processed_docs)
tfidf = TF_IDF(index, processed_docs)
tfidf.calculate_weights()

engine = SearchEngine(index, processed_docs,builder.df)
evaluation=Evaluation(engine,tfidf)

# evaluation.evaluate_all()

controller = Controller(engine, tfidf)
controller.choose("argentina final")
