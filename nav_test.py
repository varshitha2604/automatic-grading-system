from sklearn.naive_bayes import GaussianNB
import pandas as pd
import pickle

# Step 1: Load and Inspect the Dataset
df = pd.read_csv('finaldataset.csv')
print(df.head())
print(df.columns)

# Ensure necessary columns exist
assert 'keyword' in df.columns
assert 'grammar' in df.columns
assert 'qst' in df.columns
assert 'class' in df.columns

# Step 2: Fit and Save the Model
X = df[['keyword', 'grammar', 'qst']]
y = df['class']

clf = GaussianNB()
clf.fit(X, y)

with open('nav_test.pickle', 'wb') as pickle_out:
    pickle.dump(clf, pickle_out)

# Step 3: Load and Use the Model for Prediction
with open('nav_test.pickle', 'rb') as pickle_in:
    clf = pickle.load(pickle_in)

def predict(k, g, q):
    predicted = clf.predict([[k, g, q]])
    accuracy = clf.predict_proba([[k, g, q]])
    print("class[1-9] : " + str(predicted))
    return predicted

# Example prediction
print(predict(1, 2, 3))


