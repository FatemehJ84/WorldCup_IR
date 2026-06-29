import sys

from preprocessing import Preprocessor
sys.stdout.reconfigure(encoding='utf-8')
from doc_builder import DocumentBuilder

builder = DocumentBuilder("data/matches_1930_2022.csv")

builder.load_dataset()
#hey check for the edit
docs = builder.build_documents()

pre = Preprocessor()

tokens = pre.preprocess(docs[0])
print(tokens[:100])