from nltk.classify import NaiveBayesClassifier
from nltk.classify.util import accuracy
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize


sentiment_dict = {}

with open('data/AFINN-111.txt') as f:
    for line in f:
        word, score = line.split('\t')
        sentiment_dict[word] = int(score)


def print_sentiment_score(s):
    words = word_tokenize(s.lower())
    print(sum(sentiment_dict.get(word, 0) for word in words))


# positive
print_sentiment_score('I like this project.')
print_sentiment_score('Students love to to go school.')
# negitive
print_sentiment_score("You're wrong!")
print_sentiment_score('This event is terrible.')


print_sentiment_score('a tour de force of modern cinema.')  # doesn't work with new word
print_sentiment_score("Nice book! Though it is lack of advanced topics. It's still good for beginners.")  # doesn't work with complex sentence



def format_sentence(sentence):
    return {word: True for word in word_tokenize(sentence)}


pos_data = []
with open('data/rt-polaritydata/rt-polaritydata/rt-polarity.pos', encoding='latin-1') as f:
    for line in f:
        pos_data.append([format_sentence(line), 'pos'])


neg_data = []
with open('data/rt-polaritydata/rt-polaritydata/rt-polarity.neg', encoding='latin-1') as f:
    for line in f:
        neg_data.append([format_sentence(line), 'neg'])

threshold = round(len(neg_data) * 0.75)
training_data = pos_data[:threshold] + neg_data[:threshold]
testing_data = pos_data[threshold:] + neg_data[threshold:]

model = NaiveBayesClassifier.train(training_data)

print(model.classify(format_sentence('this is a nice article')))
print(model.classify(format_sentence('this is a bad article')))
print(accuracy(model, testing_data))  # 77% accuracy

print(model.classify(format_sentence('a tour de force of modern cinema.')))
