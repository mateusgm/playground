## Entry/Mid Level Positions

*  What is a P-Value ? - I expect candidates to know how to explain to me what P-Value is and what P-Value means (even at 4am...)
*  What is Regularization? Which problem does Regularization tries to solve?
*  How you can fit non-linear relations between X (say, Age) and Y (say, Income) into a Linear Model? - I also expect candidates to show me mathematically the marginal effect of X on Y based on their proposed solution.
*  What is the probability to get the sum 2 if I have 2 equally weighted dice? Now with 4? 7?
*  What is the Gradient Descent Method (the intuition is mostly enough)?
*  Which Clustering methods are you familiar with?
*  Which libraries for Analytics/DS you are familiar in Python? (0ne or two questions)
*  Describe a Data Science project that you led/participated.
*  What is an eigenvalue? (linear algebra)
*  I usually ask a question for evaluation familiarity with Bayes Law ("I have two Coins..")
*  Time Series: if you have a data-set with 100 observations for each Xi, and 3 lag-effect variables of X1, how many predictions will you have if you will run any simple linear regression?

## More Advanced Level Positions

*  What is Regularization? What is the difference in the outcome (coefficients) between the L1 and L2 norms? (usually I ask them to draw the geometric shape of the functions, just to make sure)
*  How do you fit a non-linear relation between X (age) and Y (income) in a Linear Model? Other methods?
*  What is Box-Cox transformation?
*  What is Multicollinearity ? How can we solve it?
*  Does the Gradient Descent method always converge to the same point?
*  Is it necessary that the Gradient Descent Method will always find the global minima? (I also expect candidates in this level to guide me through the intuition and some math behind the method)
*  Clustering is also a common question in this case - I usually ask: 
*  How do you find the optimal k (k*) in K-Mean? (I expect candidates to know at least 2 methods)
*  Sometimes, I ask about NLP (Natural Language Process) - general questions.
*  Sometimes, I ask questions in Combinatorics.
*  Sometimes, I'm presenting a "consulting type of job" and I give candidates few minutes to guide me through a solution: Say I'm the CEO of a famous a News-Paper company, which has 5 different Magazine, How would you - as a Data Scientist - recommend to me (the CEO) a method to recommend a Magazine to a reader? (In this question, I evaluate knowledge in DS methods as well as ability to explain and communicate the process/outcome to a senior non-technical manager) 

1. Regression (the short answer here is to know everything) (Always)
- p-values, interpretation of coefficients, interaction coefficients
- know how factor variables are dummy coded, coefficient interpretation
- linear regression assumptions
- residual analysis, adding non-linear terms
- difference between L1 and L2 penalization, when you would use each one
- how to deal with highly correlated variables
- walk me through how you would approach building a regression model to predict Y given you have data X
- how do you choose the right number of predictors
- logistic regression

2. General predictive modeling (Always)
- train/test/validate sets, cross-validation, parameter selection, predictor selection, etc.

3. Random Forrest (Always)
- how a tree is grown
- purpose of growing a forrest
- purpose of selecting a subset of variables at each split
- pruning
- variable importance
- knowing gbm here is also a plus

4. Matrix Factorization (Rare)
- pca, when do you use it? how are the components ordered?
- read up on how factorization was used in netflix competition
- i've never been asked about factor analysis, but it is great to know and makes other related questions easier

5. K-means clustering (often)
- what is the loss function? when does it converge?
- know the algorithm iteration steps
- how do you choose the right number of clusters?
- is the optimization convex?

6. Standard Stats (Often)
- t-test
- z-scores
- chi-square test
- know covariance and correlation equations

7. Time Series (Rare)
- p,d,q parameters and how you choose them
- unit root and box test


Data exploration
How do you summarize the distribution of your data?
How do you handle outliers or data points that skew data?
What assumptions can you make? Why and when? (i.e When is it safe to assume "normal")

Confidence intervals
How they are constructed
Why you standardize
How to interpret

Sampling
Why and when?
How do you calculate needed sample size? [Power analysis is advanced]
Limitations
Bootstrapping and resampling?

Biases
When you sample, what bias are you inflicting?
How do you control for biases?
What are some of the first things that come to mind when I do X in terms of biasing your data?

Modeling
Can you build a simple linear model?
How do you select features?
How do you evaluate a model?

Experimentation 
How do test new concepts or hypotheses in....insert domain X? i.e. How would evaluate whether or not consumers like the webpage redesign or new food being served?
How do you create test and control groups?
How do you control for external factors?
How do you evaluate results?



https://alyaabbott.wordpress.com/2014/10/01/how-to-ace-a-data-science-interview/
https://medium.com/rants-on-machine-learning/interview-questions-for-data-scientist-positions-5ad3c5d5b8bd#.amhg27jvi
https://medium.com/rants-on-machine-learning/interview-questions-for-data-scientist-positions-part-ii-ac294c2c7241#.iq2rvnmkg
http://rpubs.com/JDAHAN/172473
http://www.edureka.co/blog/frequently-asked-data-science-interview-questions?utm_source=quora&utm_medium=social-media-sg&utm_campaign=data-science-interview