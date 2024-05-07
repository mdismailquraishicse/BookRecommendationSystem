from nltk.stem import SnowballStemmer
import string
# This function displays basic details of the dataset
def knowYourData(df):
  ''' Enter a dataframe '''
  print('Shape: ', df.shape)
  print('Duplicates count: ', df.duplicated().sum())
  print('Columns:')
  print(list(df.columns))
# This function removes punctuations and integers from a given sentence.
def remove_punctuations(text):
    ''' Enter texts '''
    punc= list(string.punctuation)
    result = ''
    for i in text:
        if i not in punc:
            result += i
    return result.lower()
# This function removes integers
def removeIntegers(text):
    result= []
    text= text.split()
    for t in text:
        if t.isnumeric() == False:
            result.append(t)
    return ' '.join(result)
# This function is used for stemming
def stemming(text):
    ''' Enter texts '''
    result = []
    ss= SnowballStemmer(language='english')
    for t in text.split():
        result.append(ss.stem(t))
    return ' '.join(result)