import re
import string
import unicodedata
import nltk
from nltk.tokenize import ToktokTokenizer

class Text_processing:

    '''
    Class created to apply pre-processing functions, in order to clean the dataset text.

    '''

    def __init__(self, largs, run_all=False):
        '''

        Class initializer:
        
        :param largs (List): List of the text sequences to be processed.
        :param run_all (Bool): It determines if the text from the list of sequences should be subject to all the pre-processing functions or not.
        '''
        self.largs=largs
        if type(self.largs) is not list:
            self.largs=[self.largs]
        if run_all:
            self.pre_processing()

    def get_processed_text(self):
        '''
        Function that returns the processed text.
        '''
        return self.largs

    def pre_processing(self):
        '''
        Text processing function. Calls the relevant functions to clean the text from the dataset.
        '''
        self.to_lowercase() 
        self.remove_punctuation()
        self.remove_special_characters_and_accented_characters()
        self.remove_extra_whitespace_tabs()
        self.stemming_phrases()
        self.remove_stopwords()

    def to_lowercase(self):
        '''
        Function to convert all characters from the sequences to lowercase.
        '''
        for i in range(len(self.largs)):
            self.largs[i]=self.largs[i].lower()
        return self.largs

    def remove_punctuation(self):
        '''
        Function to remove all punctuation characters from the sequences.
        '''
        
        for i in range(len(self.largs)):
            self.largs[i] = ''.join([c for c in self.largs[i] if c not in string.punctuation])
        return self.largs

    def remove_special_characters_and_accented_characters(self):
        '''
        Function to remove all special characters (not included in 'pattern') from the sequences.
        '''
        pattern = r'[^a-zA-z\"\'\s]'
        for i in range(len(self.largs)):
            self.largs[i] = re.sub(pattern, '', self.largs[i])
            self.largs[i] = unicodedata.normalize('NFKD', self.largs[i]).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        return self.largs

    def remove_extra_whitespace_tabs(self):
        '''
        Function to remove extra whitespaces from the sequences.
        '''
        pattern = r'^\s*|\s\s*'
        for i in range(len(self.largs)):
            self.largs[i] = re.sub(pattern, ' ', self.largs[i]).strip()
        return self.largs

    def stemming_phrases(self):
        '''
        Stemming is the process of reducing inflected/derived words to their word stem, base or root form.
        The stem need not be identical to original word. 
        This particular function mainly relies on chopping-off ‘s’, ‘es’, ‘ed’, ‘ing’, ‘ly’ etc from the end of the words and sometimes the conversion is not desirable.         
        '''
        stemmer = nltk.porter.PorterStemmer()
        for i in range(len(self.largs)):
            self.largs[i] = ' '.join([stemmer.stem(word) for word in self.largs[i].split()])
        return self.largs

    def remove_stopwords(self):
        '''
        Function to remove stopwords from the sequences, using nltk.corpus.
        Stopwords are often added to sentences to make them grammatically correct, for example, words such as a, is, an, the, and etc. 
        These stopwords carry minimal to no importance and are available plenty on open texts, articles, comments etc. 
        These should be removed so machine learning algorithms can better focus on words which define the meaning/idea of the text. 
        '''
        tokenizer = ToktokTokenizer()
        stopword_list = nltk.corpus.stopwords.words('english')
        for i in range(len(self.largs)):
            tokens = tokenizer.tokenize(self.largs[i])
            tokens = [token.strip() for token in tokens]
            # check in lowercase
            t = [token for token in tokens if token.lower() not in stopword_list]
            self.largs[i] = ' '.join(t)
        return self.largs

if __name__ == '__main__':
    texts=['The PAST cant hurt you anymore, un##$less you LET it.','There IS NO cert$$$ainty, only opportunity.','BENEATH THIS MASK THERES AN IDEA','studying','study','studied']
    var_one = Text_processing(texts, run_all=True)
    print(var_one.get_processed_text())
    # ['past cannot hurt anymore unless let', 'certainty opportunity', 'beneath mask idea'] sem stemming
    # ['past cannot hurt anymor unless let', 'certainti onli opportun', 'beneath thi mask idea'] com stemming

