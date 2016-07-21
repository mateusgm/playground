import re
import warnings
from itertools import combinations

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import scipy.sparse as sps
import pandas as pd

import sklearn.feature_extraction
import sklearn.preprocessing
import sklearn.cross_validation
import sklearn.metrics
import sklearn.feature_selection

import sklearn.ensemble
import sklearn.naive_bayes
import sklearn.svm
import sklearn.tree
import sklearn.linear_model

# figure size

#%matplotlib inline
plt.rcParams['figure.figsize'] = 12, 9

    
# feature selection

def remove_outliers(y, x=None, std=3):
    indexes = abs(y - y.mean()) < std*y.std()
    if x is not None:
        return y[indexes], x[indexes]
    return y[indexes]

def one_hot_encode(data, categorical=None):
    if categorical is None:
        categorical = data.columns
        
    data.loc[:,categorical] = data[categorical].applymap(str)
    data_dict = data.to_dict(orient='record')
    
    vec = sklearn.feature_extraction.DictVectorizer()
    new_x = vec.fit_transform(data_dict)
    
    new_x.columns = vec.get_feature_names()
    new_x.index   = data.index
    return new_x
    

def feature_importance(X, y, names=None, pvalues=False, chi2=False, f_class=False):
    rfc = sklearn.ensemble.RandomForestClassifier(max_depth=7, n_estimators=500)
    rfc.fit(X, y)
    rfc_std = np.std([tree.feature_importances_ for tree in rfc.estimators_], axis=0)
    
    names = X.columns if names is None else names
    ranking = pd.DataFrame(list(zip(names, rfc.feature_importances_, rfc_std)),
                           columns=['features', 'gini', 'std'])
    
    if not sps.issparse(X):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            rlr = sklearn.linear_model.RandomizedLasso()
            rlr.fit(X,y)
            ranking['stability'] = sklearn.preprocessing.MinMaxScaler().fit_transform(rlr.scores_)
    
    if chi2:
        chi2 = sklearn.feature_selection.SelectKBest(sklearn.feature_selection.chi2, k='all')
        chi2.fit(X, y)
        ranking['chi2'] = sklearn.preprocessing.MinMaxScaler().fit_transform(chi2.scores_)
    
    if f_class:
        f_classif = sklearn.feature_selection.SelectKBest(sklearn.feature_selection.f_classif, k='all')
        f_classif.fit(X, y)
        ranking['f_classif'] = sklearn.preprocessing.MinMaxScaler().fit_transform(f_classif.scores_)

    return ranking.sort_values(by='gini', ascending=False)

def feature_group(table, x):
    return re.match('([\w_]+)=?', table['features'][x]).groups()[0]

# visualization

def plot_curve(data, x='X axis', y='Y axis', title='My chart', roc=False):
    plt.figure()
    for label, data in data.items():
        plt.plot(data[0], data[1], label=label)
    if roc:
        plt.plot([0, 1], [0, 1], 'k--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
    plt.xlabel(x)
    plt.ylabel(y)
    plt.title(title)
    plt.legend(loc="lower right")
    return plt

    
# model performance

def evaluate(X, y, model, scoring='roc_auc'):
    scores = sklearn.cross_validation.cross_val_score(model, X, y, cv=5, scoring=scoring, n_jobs=-1)
    print("%s: %f +- %f" % (model.__class__.__name__, scores.mean(), scores.std()*2))

def roc_score(X_train, y_train, X_test, y_test, model):
    model.fit(X_train, y_train)
    
    predict_method = 'predict_proba' if hasattr(model, 'predict_proba') else 'predict'
    y_scores = getattr(model, predict_method)(X_test)
    y_scores = y_scores[:,1] if len(y_scores.shape) == 2 else y_scores
    
    fpr, tpr, p = sklearn.metrics.roc_curve(y_test, y_scores)
    roc_auc_scr = sklearn.metrics.auc(fpr, tpr)
    return roc_auc_scr, fpr, tpr, p

def roc_curve(X, y, models, seed=42, test_size=.2):
    X_train, X_test, y_train, y_test = sklearn.cross_validation.train_test_split(
        X, y, test_size=test_size, random_state=seed
    )
    data = dict()
    for m in range(len(models)):
        scr, fpr, tpr, prb = roc_score(X_train, y_train, X_test, y_test, models[m])
        name = '%s_%d (%0.4f)' % (models[m].__class__.__name__, m, scr)
        data[name] = [ fpr, tpr, prb, scr ]
        verbose and print("  " + name)
    return plot_curve(data, x='False Positive Rate', y='True Positive Rate', title='ROC curve', roc=True)

def learning_curvex(X, y, model, steps=50, seed=42):
    print("asd")
    max_perc = 85
    learning_x = [ int(X.shape[0] * (s+1)* max_perc / steps / 100.0) for s in range(steps-1) ]
    data = dict(
        train = [ np.array(learning_x), [] ],
        test  = [ np.array(learning_x), [] ],        
    )
    name = model.__class__.__name__
    for i in learning_x:
        X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=i, random_state=seed)
        roc_train, _, _, _ = roc_score(X_train, y_train, X_train, y_train, model)
        roc_test, _, _, _  = roc_score(X_train, y_train, X_test, y_test,  model)
        data['train'][1] = np.append(data['train'][1], roc_train)
        data['test'][1]  = np.append(data['test'][1], roc_test)
    return plot_curve(data, x='Trainning set size', y='Score', title='Learning curve') 

    
# deployment 

def explode_combinations(data, features, feature_i=0):
    values = data[features[feature_i]].unique()
    if feature_i + 1 == len(features):
        return [ np.array([v]) for v in values ]
    
    others = explode_combinations(data, features, feature_i+1)
    print("Feature %s: %d" % ( features[feature_i+1], len(others)))
    partial = []
    for v in values:
        for o in others:
            row = np.append(o, v)
            partial.append(row)
    return partial


def formula( model, features ):
    coefs = model.coef_ if hasattr(model, 'coef_') else model.feature_importances_
    intercept = model.intercept_ if hasattr(model, 'intercept_') else "tree"
    lst = zip( np.array([coefs]).flatten(), features )
    lst = sorted( lst,  key = lambda x: -np.abs(x[0]) )
    lst = [ "%.3f  %s" % (c, name) for c, name in lst ]
    return "%s\n  %s" % ( str(intercept), "\n  ".join(lst) )


# IO

def load(csv, n=None):
    # sys.stdin
    data = pd.read_csv(csv, sep='\t', encoding='utf-8')
    data.columns = [ re.match('.*\.(.*)', c).groups()[0] for c in data.columns ]
    return data.sample(n=n) if n else data

def hc():
    from pyspark.sql import HiveContext
    return HiveContext(sc)
    
def overwritePartition( table_name, partition, data ) :
    toHadoop = data if isinstance(data, pyspark.sql.DataFrame) else hc.createDataFrame(data)
    toHadoop.registerTempTable("toHadoop")
    hc().sql("INSERT OVERWRITE TABLE %s PARTITION (%s) SELECT * FROM toHadoop" % (table_name, partition))
    
def createTable( table_name, data ):
    toHadoop = data if isinstance(data, pyspark.sql.DataFrame) else hc.createDataFrame(data)
    toHadoop.registerTempTable("toHadoop")
    hc().sql("DROP TABLE IF EXISTS %s" % (table_name))
    hc().sql("CREATE TABLE %s STORED as TEXTFILE AS SELECT * FROM toHadoop" % (table_name))

