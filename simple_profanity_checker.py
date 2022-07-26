# I hadnt intendended to use any Profanity laibraries
import re
import pandas as pd

def read_text():
    text_file = open('fileName.txt: path_to_the_twiter_text_file', 'r')
    sentences = [line.split('\n') for line in text_file.readlines()]
    check_proficenty(contents)
    preprocessed_sentence = []
    labels = []
    for line in sentences:
        preprocessed_sentence.append(preprocess_sentence(line))
        target = check_proficenty(preprocess_sentence(line))
        labels.append(target)

    data = pd.DataFrame({'textlines':[], 'preprocessed_textlines': [], 'labels': []})
    data['textlines'] = sentences
    data['preprocessed_textlines'] = preprocessed_sentence
    data['labels'] = labels
    text_file.close()
    return data

def preprocess_sentence(sent):
    '''Function to preprocess sentences'''
    sent = sent.lower() # lower casing
    sent = re.sub("'", '', sent) # remove the quotation marks if any
    sent = ''.join(ch for ch in sent if ch not in exclude)
    sent = sent.translate(remove_digits) # remove the digits
    sent = sent.strip()
    sent = re.sub(" +", " ", sent) # remove extra spaces
    return sent

def check_proficenty(text):
    racial_slur_wordfile = open('fileName.txt: path_to_the_racial_slur_wordfile', 'r')
    racial_slur_words = racial_slur_wordfile.read()
    for word in text.split('\n').strip():
        if word in racial_slur_words:
            return 'Yes'
        return 'No'
