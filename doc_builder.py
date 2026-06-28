import pandas as pd


class DocumentBuilder:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.df = None
        self.documents ={}

    def load_dataset(self):
        self.df = pd.read_csv(self.csv_path)
        print("Dataset Loaded")
        print("Matches:", len(self.df))
        return self.df
    
    def build_documents(self):
        for index, row in self.df.iterrows():
            text = ""
            for column in self.df.columns:
                value = row[column]
                if pd.isna(value):
                    continue
                text += f"{column} : {value}\n"
            self.documents[index] = text
        return self.documents
    
    def save_documents(self, output_file):
        with open(output_file, "w", encoding="utf-8") as f:
            for doc_id, document in self.documents.items():
                f.write(f"========== Document {doc_id} ==========\n")
                f.write(document)
                f.write("\n\n")