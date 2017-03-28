## other 1

1. What is the curse of higher dimensionality? What is the difference between density-sparse data and dimensionally-sparse data? What does "higher dimensionality" imply when applying textbook clustering algorithms developed for low dimension metric spaces to, say, numerical text analysis? Think of using cluster density to identify "good" clusters.
2. Probability space: How do you compare probabilities? Probability space is often referred to as a "vector space", is it? Define addition on this space? Is ds^2 = dp^2 a good metric on probability space? How would you construct a metric on probability space, so you can start doing complicated things like L2 norm etc.?
3. Regression: What is regression? What are the principal choices involved? What is linear about linear regression?
4. Logistic regression: Explain Logistic Regression to an economist, biologist or physical scientist. You can use the "formula" if you want. Motivate the "formula".
5. What does the score distribution for logistic regression look like? How would I track it?
6. How should logistic regression scores be calibrated? What are the dangers of over-fitting in calibration?
7. Certain third party data providers (DP1, DP2 ...) will identify cookie_ids as belonging to a specific demographic segment, say DP1_S1 = F35-44. To test the accuracy of this assignment, random samples of cookie_ids in these segments are measured against an industry standard source of "ground truth". This will yield data like "40% of the cookie_ids that DP1 identifies as in S1 are actually (according to "ground truth") in F35-44" and "30% of the cookie_ids that DP2 identifies as in S5 are actually (according to "ground truth") in F35-44". Given the above, what is the probability that a cookie_id that is in both DP1_S1 and DP2_S5 will be found to be in F35-44 according to the industry standard source of ground truth?
8. The x and y are two random variables and their standard errors are known. How can you calculate/estimate the standard error in f(x,y)? If you want, specifically, in f(x,y) = y/x. How would you do this if you had all the data (x_i, y_i)?
9. Why should the test and the control group be of the same size in an "A/B" test?

## other 2

What is the biggest data set that you have processed and how did you process it? What was the result?
Tell me two success stories about your analytic or computer science projects? How was the lift (or success) measured?
How do you optimize a web crawler to run much faster, extract better information and summarize data to produce cleaner databases?
What is probabilistic merging (AKA fuzzy merging)? Is it easier to handle with SQL or other languages? And which languages would you choose for semi-structured text data reconciliation?
State any 3 positive and negative aspects about your favorite statistical software.
You are about to send one million email (marketing campaign). How do you optimize delivery and its response? Can both of these be done separately?
How would you turn unstructured data into structured data? Is it really necessary? Is it okay to store data as flat text files rather than in an SQL-powered RDBMS?
In terms of access speed (assuming both fit within RAM) is it better to have 100 small hash tables or one big hash table in memory? What do you think about in-database analytics?
Can you perform logistic regression with Excel? If yes, how can it be done? Would the result be good?
Give examples of data that does not have a Gaussian distribution, or log-normal. Also give examples of data that has a very chaotic distribution?
How can you prove that one improvement you’ve brought to an algorithm is really an improvement over not doing anything? How familiar are you with A/B testing?
What is sensitivity analysis? Is it better to have low sensitivity and low predictive power? How do you perform good cross-validation? What do you think about the idea of injecting noise in your data set to test the sensitivity of your models?
Compare logistic regression with decision trees and neural networks. How have these technologies improved over the last 15 years?
What is root cause analysis? How to identify a cause Vs a correlation? Give examples.
How to detect the best rule set for a fraud detection scoring technology? How do you deal with rule redundancy, rule discovery and the combinatorial nature of the problem? Can an approximate solution to the rule set problem be okay? How would you find an okay approximate solution? What factors will help you decide that it is good enough and stop looking for a better one?
Which tools do you use for visualization? What do you think of Tableau, R and SAS? (for graphs). How to efficiently represent 5 dimension in a chart or in a video?
Which is better: Too many false positives or too many false negatives?
Have you used any of the following: Time series models, Cross-correlations with time lags, Correlograms, Spectral analysis, Signal processing and filtering techniques? If yes, in which context?
What is the computational complexity of a good and fast clustering algorithm? What is a good clustering algorithm? How do you determine the number of clusters? How would you perform clustering in one million unique keywords, assuming you have 10 million data points and each one consists of two keywords and a metric measuring how similar these two keywords are? How would you create this 10 million data points table in the first place?


# models

What type of problem does the model try to solve?
Is it prone to over-fitting? If so – what can be done about this?
Does the model make any important assumptions about the data? When might these be unrealistic? How do we examine the data to test whether these assumptions are satisfied?
Does the model have convergence problems? Does it have a random component or will the same training data always generate the same model? How do we deal with random effects in training?
What types of data (numerical, categorical etc…) can the model handle?
Can the model handle missing data? What could we do if we find missing fields in our data?
How interpretable is the model?
What alternative models might we use for the same type of problem that this one attempts to solve, and how does it compare to those?
Can we update the model without retraining it from the beginning?
How fast is prediction compared to other models? How fast is training compared to other models?
Does the model have any meta-parameters and thus require tuning? How do we do this?

(Deeper machine learning questions)

What is the EM algorithm? Give a couple of applications
What is deep learning and what are some of the main characteristics that distinguish it from traditional machine learning
What is linear in a generalized linear model?
What is a probabilistic graphical model? What is the difference between Markov networks and Bayesian networks?
Give an example of an application of non-negative matrix factorization
On what type of ensemble technique is a random forest based? What particular limitation does it try to address?
What methods for dimensionality reduction do you know and how do they compare with each other?
What are some good ways for performing feature selection that do not involve exhaustive search?
How would you evaluate the quality of the clusters that are generated by a run of K-means?

(Tools and research)

Do you have any research experience in machine learning or a related field? Do you have any publications?
What tools and environments have you used to train and assess models?
Do you have experience with Spark ML or another platform for building machine learning models using very large datasets?


Why do we need/want the bias term?
Why do we call it GLM when it's clearly non-linear? (somewhat tricky question, to be asked somewhat humorously---but extremely revealing.)
How are neural nets related to Fourier transforms? What are Fourier transforms, for that matter?