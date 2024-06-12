# Text Summarizer Tool for Legal Documents

## Project Description
The Text Summarizer Tool for Legal Documents is a Python-based application designed to automatically summarize legal texts. Using natural language processing (NLP) techniques, the tool extracts key sentences to generate concise summaries, making it easier to grasp the main points of lengthy legal documents.

## Features
- Preprocesses text by tokenizing, removing stop words, and lemmatizing.
- Scores sentences based on word frequency to determine their importance.
- Generates a summary by selecting the top-ranked sentences.
- Easy to use with any legal text file.

## Requirements
- Python 3.x
- NLTK (Natural Language Toolkit)

## Installation
1. Ensure you have Python 3.x installed.
2. Install NLTK by running:
   ```bash
   pip install nltk
   ```

## How to Run the Project
1. Download or clone the project files to your local machine.
2. Ensure you have a text file named `free-copyright-notice.txt` in the project directory, or modify the code to load a different file.
3. Open a terminal or command prompt and navigate to the directory containing the `text_summarizer.py` file.
4. Run the script by typing:
   ```bash
   python text_summarizer.py
   ```
5. The summary of the text will be displayed on the screen.

## Code Explanation
The script for the Text Summarizer Tool for Legal Documents consists of the following steps:

1. **Import Libraries:**
   ```python
   import nltk
   from nltk.tokenize import sent_tokenize, word_tokenize
   from nltk.corpus import stopwords
   from nltk.stem import WordNetLemmatizer
   from collections import defaultdict
   from string import punctuation
   ```

2. **Load NLTK Data:**
   ```python
   nltk.download('punkt')
   nltk.download('wordnet')
   nltk.download('stopwords')
   ```

3. **Preprocess the Text:**
   - Tokenize the text into words.
   - Remove stop words.
   - Lemmatize the tokens to their base form.
   - Join the tokens back into a string.
   ```python
   def preprocess_text(text):
       tokens = word_tokenize(text)
       stop_words = set(stopwords.words('english'))
       tokens = [token for token in tokens if token not in stop_words]
       lemmatizer = WordNetLemmatizer()
       tokens = [lemmatizer.lemmatize(token) for token in tokens]
       text = ' '.join(tokens)
       return text
   ```

4. **Calculate Sentence Scores:**
   - Tokenize the text into sentences.
   - Score each sentence based on the frequency of its words.
   ```python
   def calculate_sentence_scores(text):
       sentences = sent_tokenize(text)
       sentence_scores = defaultdict(int)
       for sentence in sentences:
           for word in word_tokenize(sentence):
               if word in punctuation:
                   continue
               sentence_scores[sentence] += 1
       return sentence_scores
   ```

5. **Generate the Summary:**
   - Preprocess the text.
   - Calculate the scores for each sentence.
   - Sort sentences by their scores and select the top sentences.
   ```python
   def generate_summary(text, num_sentences):
       text = preprocess_text(text)
       sentence_scores = calculate_sentence_scores(text)
       sorted_sentences = sorted(sentence_scores.items(), key=lambda x: x[1], reverse=True)
       summary = ' '.join([sentence for sentence, score in sorted_sentences[:num_sentences]])
       return summary
   ```

6. **Load the Text and Generate the Summary:**
   ```python
   with open('free-copyright-notice.txt', 'r') as file:
       text = file.read()

   summary = generate_summary(text, 5)
   print('Summary:')
   print(summary)
   ```

## Example Output
```bash
Summary:
[Summary of the first 5 most important sentences of the legal document]
```

## Notes
- Ensure the input text file is in the same directory as the script, or adjust the file path accordingly.
- Modify the `num_sentences` parameter in the `generate_summary` function to change the length of the summary.

## License
This project is open-source and available under the MIT License. Feel free to use, modify, and distribute the code.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, please submit a pull request or open an issue.

## Contact
For any questions or further assistance, please contact the project maintainer at omkarkadle@gmail.com.

---

Simplify and understand lengthy legal documents with the Text Summarizer Tool for Legal Documents!
