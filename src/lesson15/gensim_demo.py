# First install gensim:
# pip install --upgrade gensim

import string
import logging
import nltk
from gensim import corpora, models, similarities
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Getting our documents
categories = ['alt.atheism', 
              'soc.religion.christian', 
              'comp.graphics', 
              'sci.med']
twenty_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)
# documents is just a list of strings.
# Just get the first 200 documents (out of ~2500 documents)
documents = twenty_train.data[:200]
# documents = twenty_train.data

# remove common words and tokenize
# you will have to run nltk.download()
lame = ['from', 'subject', 'nntp', 'posting', 'host', 'organization', 'lines', 're', 'nntp-posting-host']
stoplist = nltk.corpus.stopwords.words('english') + lame + list(string.punctuation) + ['--', "''", '``', "'s", "n't", '...']

def is_good_word(word):
	return len(word) > 3 and word not in stoplist

# texts is the document turned into a list of words.
texts = [[word for word in nltk.word_tokenize(document.lower()) if is_good_word(word)] for document in documents]

# remove words that appear only once
all_tokens = sum(texts, [])
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
texts = [[word for word in text if word not in tokens_once] for text in texts]

# Creating a dictionary to map words to integers.
dictionary = corpora.Dictionary(texts)

# print(dictionary.token2id).items()[:10]
# new_doc = "Human computer interaction"
# new_vec = dictionary.doc2bow(new_doc.lower().split())
# print(new_vec)

# Vectorize: turn each document (list-of-words) into a vectorized bag-of-words.
corpus = [dictionary.doc2bow(text) for text in texts]

# Transformations, from one vector representation to another.
# E.g. bag-of-words to Tf-IDF
tfidf = models.TfidfModel(corpus) # step 1 -- initialize a model. This learns document frequencies.

# You can transform a vectorized bag-of-words:
# doc_bow = [(0, 1), (1, 1)]
# print(tfidf[doc_bow])

# You can also transform a whole corpus.
# Note that corpus_tfidf is actually an iterator over corpus
# that performs the transformation at the last-minute.
corpus_tfidf = tfidf[corpus]  # step 2 -- use the model to transform bunch of vectors.

# type(corpus_tfidf)


#### LSI
# Now let's try Latent Sementic Analysis (LSA) to transform documents into 2D space.
lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=20) # initialize an LSI transformation
corpus_lsi = lsi[corpus_tfidf] # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi

# It's easy to see what words contribute to the two dimensions.
# This is kind of like PCA.
# print lsi.print_topics(2)

#### LDA
lda = models.LdaModel(corpus, id2word=dictionary, num_topics=20, passes=20, iterations=500)

#### Similarity queries
doc = "jesus pope"

#### vector bag-of-words
vec_bow = dictionary.doc2bow(doc.lower().split())

vec_lsi = lsi[vec_bow] # convert the query to LSI space
print vec_lsi

vec_lda = lda[vec_bow] # convert the query to LDA space
print vec_lda

##### Initializing query structures:

# Uses cosine measure
index = similarities.MatrixSimilarity(lda[corpus]) # Transform corpus to LDA space

sims = index[vec_lda] # perform a similarity query against the corpus
sims_sorted = sorted(enumerate(sims), key=lambda item: -item[1])
print(sims_sorted)

