import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import string

def summarize(text, summary_length=5):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Tokenize the text into words and remove stop words and punctuation
    stop_words = set(stopwords.words('english') + list(string.punctuation))
    words = word_tokenize(text.lower())
    words = [word for word in words if word not in stop_words]
    
    # Calculate word frequencies
    word_frequencies = {}
    for word in words:
        if word in word_frequencies:
            word_frequencies[word] += 1
        else:
            word_frequencies[word] = 1
    
    # Calculate sentence scores
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequencies[word]
                else:
                    sentence_scores[sentence] += word_frequencies[word]
    
    # Get the highest scoring sentences for the summary
    summary_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:summary_length]
    
    # Combine the summary sentences
    summary = ' '.join(summary_sentences)
    return summary

if __name__ == "__main__":
    # Read the input text file
    with open('input.txt', 'r') as file:
        text = file.read()
    
    # Generate the summary
    summary = summarize(text)
    
    # Print the summary
    print("Summary:")
    print(summary)
