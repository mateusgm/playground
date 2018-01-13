
# coding: utf-8

# In[1]:

get_ipython().magic('load_ext autoreload')
get_ipython().magic('autoreload 2')

import sys
sys.path.insert(0,'..')

import pandas as pd
import numpy as np

from helper import *
from itertools import combinations
from sklearn import *


# In[3]:


def add_combinations(X, degrees):
    print("Adding combinations of %d features" % ( degrees ))
    combs = combinations(range(X.columns.size), degrees)
    dt = pd.DataFrame()
    for features_i in combs:
        feature_vals = [ hash(tuple(v)) for v in X.ix[:,features_i].values ]
        feature_name = "comb_" +  '_'.join([str(x) for x in features_i])
        dt[feature_name] = feature_vals
        print('.', end="")
    print("")
    return dt

def prepare(X):
    x2 = add_combinations(X, 2)
    x3 = add_combinations(X, 3)
    X = pd.concat([X, x2, x3], axis=1)
    print("Added combinations: ", X.shape)
    return X


# In[5]:

SEED = 42

# loading data

test  = pd.read_csv("./test.csv")
train = pd.read_csv("./train.csv")

features = train.columns[~train.columns.isin(['ACTION', 'MGR_ID'])]
X, y, X_test = train[features], train.ACTION, test[features]


# In[ ]:

FEATURES    = X.columns
categorical = X.columns

X_train = prepare(X)
ranking_0 = feature_importance(X_train, y)

X_train = one_hot_encode(X_train)
ranking_1 = feature_importance(X_train, y)


# In[ ]:

ranking_0


# In[ ]:

ranking_1.groupby(lambda x: feature_group(ranking_1, x), axis=0).sum().sort_values(by='importances', ascending=False)


# In[ ]:


models = [
    ensemble.RandomForestClassifier( n_estimators=100, max_depth=7 ),
    linear_model.LogisticRegression(penalty='l2', C=1),
    linear_model.LogisticRegression(penalty='l1', C=1),
    naive_bayes.MultinomialNB(),
]

for m in models:
    evaluate(X_enc, y, m)
    
evaluate(X_enc, y, ensemble.VotingClassifier(
    estimators=[ ( m.__class__.__name__, m ) for m in models ],
    voting='soft'
))


# In[ ]:

ranking_1 = feature_importance(X_enc, y)
ranking_0


# In[ ]:


# hyperparameter optimization

params = { "C": np.logspace(-4, 4, 15, base=2) }
p = GridSearchCV(model, param_distributions=params, scoring='roc_auc', n_jobs=-1).fit(X, y)

print("Found best params: ", p)

# predicting

model = LogisticRegression(C=p.best_params_.C)
model = model.train(X, y)
predictions = model.predic_proba(X_test)[:,1]

export = pd.DataFrame({ "id": test.id, "ACTION": predictions })
export.to_csv("./predictions.csv", index=False)

print "Done!"

# evaluation

scores = cross_val_score(model, X, y, cv=cv, scoring='roc_auc', n_jobs=-1)
print "Final score: %f +- %f" % (i, scores.mean(), scores.std()*2)

