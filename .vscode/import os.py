import os
import re
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn

# Initialize NLTK components
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Define constants
DOC_PATTERN = r'.*\.txt'
DOC_PATH = 'path/to/documents'
STOPWORDS = set(nltk.corpus.stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

# Preprocess text
def preprocess_text(text):
    # Remove non-alphanumeric characters and convert to lowercase
    text = re.sub(r'[^a-z0-9\s]', '', text.lower())
    # Tokenize text and remove stopwords
    tokens = nltk.word_tokenize(text)
    tokens = [t for t in tokens if t not in STOPWORDS]
    # Lemmatize tokens
    tokens = [lemmatizer.lemmatize(t, get_wordnet_pos(t)) for t in tokens]
    return tokens

# Get WordNet part of speech for lemmatization
def get_wordnet_pos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {'J': wn.ADJ,
                'N': wn.NOUN,
                'V': wn.VERB,
                'R': wn.ADV}
    return tag_dict.get(tag, wn.NOUN)

# Index documents
def index_documents(docs_path):
    index = {}
    for doc_name in os.listdir(docs_path):
        if re.match(DOC_PATTERN, doc_name):
            doc_path = os.path.join(docs_path, doc_name)
            with open(doc_path, 'r') as f:
                text = f.read()
                words = preprocess_text(text)
                for word in words:
                    if word not in index:
                        index[word] = set()
                    index[word].add(doc_name)
    return index

# Search documents
def search_documents(query, index):
    query_words = preprocess_text(query)
    result = set(index[query_words[0]])
    for word in query_words[1:]:
        result = result.intersection(index.get(word, set()))
    return result

# Main function
def main():
    index = index_documents(DOC_PATH)
    while True:
        query = input('Enter your query (type "exit" to quit): ')
        if query == 'exit':
            break
        result = search_documents(query, index)
        print('Results:')
        if len(result) == 0:
            print('No documents found')
        else:
            for doc_name in result:
                print(doc_name)

if __name__ == '__main__':
    main()
