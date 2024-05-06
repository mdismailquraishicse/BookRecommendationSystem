def knowYourData(df):
  print('Shape: ', df.shape)
  print('Duplicates count: ', df.duplicated().sum())
  print('Columns:')
  print(list(df.columns))