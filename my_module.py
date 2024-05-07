# This function displays basic details of the dataset
def knowYourData(df):
  ''' Enter a dataframe '''
  print('Shape: ', df.shape)
  print('Duplicates count: ', df.duplicated().sum())
  print('Columns:')
  print(list(df.columns))
# This function removes punctuations and integers from a given sentence.
def remove_punctuations_and_integers(text):
    ''' Enter texts '''
    punc= list(string.punctuation)
    new_text= []
    result = ''
    for t in text.split():
        if t.isnumeric()==False:
            new_text.append(t)
    new_text= ' '.join(new_text)
    for i in new_text:
        if i not in punc:
            result += i
    return result