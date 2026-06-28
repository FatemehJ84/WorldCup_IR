import re
import string
import nltk

from nltk.corpus import stopwords

nltk.download("stopwords")

class Preprocessor:
    def __init__(self):
        self.stop_words =set(stopwords.words("english"))

    #lowercase
    def lowercase(self,text):
        return text.lower()
    
    #حذف علائم نگارشی
    def remove_punctuation(self, text):
        return text.translate(str.maketrans("", "", string.punctuation))
    
    #حذف فاصله های اضافی
    def remove_extra_spaces(self, text):
        return re.sub(r"\s+", " ", text).strip()
    
    #tokenization
    def tokenize(self, text):
        return re.findall(r"\b\w+\b", text)
    
    #deleting stop words
    def remove_stopwords(self, tokens):
        result = []
        for token in tokens:
            if token not in self.stop_words:
                result.append(token)
        return result
    
    def preprocess(self, text):
        text = self.lowercase(text)
        text = self.remove_punctuation(text)
        text = self.remove_extra_spaces(text)
        tokens = self.tokenize(text)
        tokens = self.remove_stopwords(tokens)
        return tokens