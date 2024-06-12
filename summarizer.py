import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import defaultdict
from string import punctuation

# Load the necessary NLTK data
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Define a function to preprocess the text
def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Join the tokens back into a string
    text = ' '.join(tokens)

    return text

# Define a function to calculate the sentence scores
def calculate_sentence_scores(text):
    # Tokenize the text
    sentences = sent_tokenize(text)

    # Calculate the sentence scores
    sentence_scores = defaultdict(int)
    for sentence in sentences:
        for word in word_tokenize(sentence):
            if word in punctuation:
                continue
            sentence_scores[sentence] += 1

    return sentence_scores

# Define a function to generate the summary
def generate_summary(text, num_sentences):
    # Preprocess the text
    text = preprocess_text(text)

    # Calculate the sentence scores
    sentence_scores = calculate_sentence_scores(text)

    # Sort the sentences by their scores
    sorted_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)

    # Select the top sentences
    summary = ' '.join([sentence for sentence, score in sorted_sentences[:num_sentences]])

    return summary

# Load a text
with open('free-copyright-notice.txt', 'r') as file:
    text = file.read()

# Generate the summary
summary = generate_summary(text, 5)

print('Summary:')
print(summary)