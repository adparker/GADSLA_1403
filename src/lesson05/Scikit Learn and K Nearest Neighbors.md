
# Installing Scikit Learn

Scikit Learn is an open source machine learning library for Python. It has
libraries for classification, regression and numerous clustering algorithms.

Install instructions are [here](http://scikit-learn.org/stable/install.html).

The easiest way is to use the Python package managers (pip or easy_install). You
can do either:

```bash
pip install -U scikit-learn
```

or

```bash
easy_install -U scikit-learn
```

# Now let's take a look at the Iris data set. 

Scikit comes with a few "well known" toy data sets. You can learn more about
them here: [Scikit Datasets](http://scikit-
learn.org/stable/datasets/index.html#datasets)

For this exercise, we're going to use the Iris dataset, whose background you can
learn about in the [Wikipedia article
here](http://en.wikipedia.org/wiki/Iris_flower_data_set).

> The data set consists of 50 samples from each of three species of Iris (Iris
setosa, Iris virginica and Iris versicolor). Four features were measured from
each sample: the length and the width of the sepals and petals, in centimetres.
Based on the combination of these four features, Fisher developed a linear
discriminant model to distinguish the species from each other.

Parts of an Iris plant:
![Parts of an Iris plant](http://w3.uniroma1.it/chemo/image/iris-flower.jpg)

|Iris setosa|Iris virginica|Iris versicolor|
|-----------|--------------|---------------|
|![Picture of Iris
setosa](http://farm9.staticflickr.com/8367/8589345220_7c8bec1d3b_n.jpg "Iris
setosa")|![Picture of Iris virginica](http://upload.wikimedia.org/wikipedia/comm
ons/thumb/9/9f/Iris_virginica.jpg/295px-Iris_virginica.jpg "Iris
virginica")|![Picture of Iris versicolor](http://upload.wikimedia.org/wikipedia/
commons/thumb/c/cd/Iris_versicolor_FWS.jpg/300px-Iris_versicolor_FWS.jpg "Iris
versicolor")|



    from pprint import pprint
    from sklearn import datasets
    iris = datasets.load_iris()
    print(iris.DESCR)

    Iris Plants Database
    
    Notes
    -----
    Data Set Characteristics:
        :Number of Instances: 150 (50 in each of three classes)
        :Number of Attributes: 4 numeric, predictive attributes and the class
        :Attribute Information:
            - sepal length in cm
            - sepal width in cm
            - petal length in cm
            - petal width in cm
            - class:
                    - Iris-Setosa
                    - Iris-Versicolour
                    - Iris-Virginica
        :Summary Statistics:
        ============== ==== ==== ======= ===== ====================
                        Min  Max   Mean    SD   Class Correlation
        ============== ==== ==== ======= ===== ====================
        sepal length:   4.3  7.9   5.84   0.83    0.7826
        sepal width:    2.0  4.4   3.05   0.43   -0.4194
        petal length:   1.0  6.9   3.76   1.76    0.9490  (high!)
        petal width:    0.1  2.5   1.20  0.76     0.9565  (high!)
        ============== ==== ==== ======= ===== ====================
        :Missing Attribute Values: None
        :Class Distribution: 33.3% for each of 3 classes.
        :Creator: R.A. Fisher
        :Donor: Michael Marshall (MARSHALL%PLU@io.arc.nasa.gov)
        :Date: July, 1988
    
    This is a copy of UCI ML iris datasets.
    http://archive.ics.uci.edu/ml/datasets/Iris
    
    The famous Iris database, first used by Sir R.A Fisher
    
    This is perhaps the best known database to be found in the
    pattern recognition literature.  Fisher's paper is a classic in the field and
    is referenced frequently to this day.  (See Duda & Hart, for example.)  The
    data set contains 3 classes of 50 instances each, where each class refers to a
    type of iris plant.  One class is linearly separable from the other 2; the
    latter are NOT linearly separable from each other.
    
    References
    ----------
       - Fisher,R.A. "The use of multiple measurements in taxonomic problems"
         Annual Eugenics, 7, Part II, 179-188 (1936); also in "Contributions to
         Mathematical Statistics" (John Wiley, NY, 1950).
       - Duda,R.O., & Hart,P.E. (1973) Pattern Classification and Scene Analysis.
         (Q327.D83) John Wiley & Sons.  ISBN 0-471-22361-1.  See page 218.
       - Dasarathy, B.V. (1980) "Nosing Around the Neighborhood: A New System
         Structure and Classification Rule for Recognition in Partially Exposed
         Environments".  IEEE Transactions on Pattern Analysis and Machine
         Intelligence, Vol. PAMI-2, No. 1, 67-71.
       - Gates, G.W. (1972) "The Reduced Nearest Neighbor Rule".  IEEE Transactions
         on Information Theory, May 1972, 431-433.
       - See also: 1988 MLC Proceedings, 54-64.  Cheeseman et al"s AUTOCLASS II
         conceptual clustering system finds 3 classes in the data.
       - Many, many more ...
    


Let's take a closer look at `iris`.


    iris.keys()




    ['target_names', 'data', 'target', 'DESCR', 'feature_names']



`iris.feature` describes the data columns. Looks like the data are measurements
of sepal and petal length and width measurements in centimeters. One row per
observation.


    iris.feature_names




    ['sepal length (cm)',
     'sepal width (cm)',
     'petal length (cm)',
     'petal width (cm)']



`iris.data` contains the raw measurements.


    iris.data




    array([[ 5.1,  3.5,  1.4,  0.2],
           [ 4.9,  3. ,  1.4,  0.2],
           [ 4.7,  3.2,  1.3,  0.2],
           [ 4.6,  3.1,  1.5,  0.2],
           [ 5. ,  3.6,  1.4,  0.2],
           [ 5.4,  3.9,  1.7,  0.4],
           [ 4.6,  3.4,  1.4,  0.3],
           [ 5. ,  3.4,  1.5,  0.2],
           [ 4.4,  2.9,  1.4,  0.2],
           [ 4.9,  3.1,  1.5,  0.1],
           [ 5.4,  3.7,  1.5,  0.2],
           [ 4.8,  3.4,  1.6,  0.2],
           [ 4.8,  3. ,  1.4,  0.1],
           [ 4.3,  3. ,  1.1,  0.1],
           [ 5.8,  4. ,  1.2,  0.2],
           [ 5.7,  4.4,  1.5,  0.4],
           [ 5.4,  3.9,  1.3,  0.4],
           [ 5.1,  3.5,  1.4,  0.3],
           [ 5.7,  3.8,  1.7,  0.3],
           [ 5.1,  3.8,  1.5,  0.3],
           [ 5.4,  3.4,  1.7,  0.2],
           [ 5.1,  3.7,  1.5,  0.4],
           [ 4.6,  3.6,  1. ,  0.2],
           [ 5.1,  3.3,  1.7,  0.5],
           [ 4.8,  3.4,  1.9,  0.2],
           [ 5. ,  3. ,  1.6,  0.2],
           [ 5. ,  3.4,  1.6,  0.4],
           [ 5.2,  3.5,  1.5,  0.2],
           [ 5.2,  3.4,  1.4,  0.2],
           [ 4.7,  3.2,  1.6,  0.2],
           [ 4.8,  3.1,  1.6,  0.2],
           [ 5.4,  3.4,  1.5,  0.4],
           [ 5.2,  4.1,  1.5,  0.1],
           [ 5.5,  4.2,  1.4,  0.2],
           [ 4.9,  3.1,  1.5,  0.1],
           [ 5. ,  3.2,  1.2,  0.2],
           [ 5.5,  3.5,  1.3,  0.2],
           [ 4.9,  3.1,  1.5,  0.1],
           [ 4.4,  3. ,  1.3,  0.2],
           [ 5.1,  3.4,  1.5,  0.2],
           [ 5. ,  3.5,  1.3,  0.3],
           [ 4.5,  2.3,  1.3,  0.3],
           [ 4.4,  3.2,  1.3,  0.2],
           [ 5. ,  3.5,  1.6,  0.6],
           [ 5.1,  3.8,  1.9,  0.4],
           [ 4.8,  3. ,  1.4,  0.3],
           [ 5.1,  3.8,  1.6,  0.2],
           [ 4.6,  3.2,  1.4,  0.2],
           [ 5.3,  3.7,  1.5,  0.2],
           [ 5. ,  3.3,  1.4,  0.2],
           [ 7. ,  3.2,  4.7,  1.4],
           [ 6.4,  3.2,  4.5,  1.5],
           [ 6.9,  3.1,  4.9,  1.5],
           [ 5.5,  2.3,  4. ,  1.3],
           [ 6.5,  2.8,  4.6,  1.5],
           [ 5.7,  2.8,  4.5,  1.3],
           [ 6.3,  3.3,  4.7,  1.6],
           [ 4.9,  2.4,  3.3,  1. ],
           [ 6.6,  2.9,  4.6,  1.3],
           [ 5.2,  2.7,  3.9,  1.4],
           [ 5. ,  2. ,  3.5,  1. ],
           [ 5.9,  3. ,  4.2,  1.5],
           [ 6. ,  2.2,  4. ,  1. ],
           [ 6.1,  2.9,  4.7,  1.4],
           [ 5.6,  2.9,  3.6,  1.3],
           [ 6.7,  3.1,  4.4,  1.4],
           [ 5.6,  3. ,  4.5,  1.5],
           [ 5.8,  2.7,  4.1,  1. ],
           [ 6.2,  2.2,  4.5,  1.5],
           [ 5.6,  2.5,  3.9,  1.1],
           [ 5.9,  3.2,  4.8,  1.8],
           [ 6.1,  2.8,  4. ,  1.3],
           [ 6.3,  2.5,  4.9,  1.5],
           [ 6.1,  2.8,  4.7,  1.2],
           [ 6.4,  2.9,  4.3,  1.3],
           [ 6.6,  3. ,  4.4,  1.4],
           [ 6.8,  2.8,  4.8,  1.4],
           [ 6.7,  3. ,  5. ,  1.7],
           [ 6. ,  2.9,  4.5,  1.5],
           [ 5.7,  2.6,  3.5,  1. ],
           [ 5.5,  2.4,  3.8,  1.1],
           [ 5.5,  2.4,  3.7,  1. ],
           [ 5.8,  2.7,  3.9,  1.2],
           [ 6. ,  2.7,  5.1,  1.6],
           [ 5.4,  3. ,  4.5,  1.5],
           [ 6. ,  3.4,  4.5,  1.6],
           [ 6.7,  3.1,  4.7,  1.5],
           [ 6.3,  2.3,  4.4,  1.3],
           [ 5.6,  3. ,  4.1,  1.3],
           [ 5.5,  2.5,  4. ,  1.3],
           [ 5.5,  2.6,  4.4,  1.2],
           [ 6.1,  3. ,  4.6,  1.4],
           [ 5.8,  2.6,  4. ,  1.2],
           [ 5. ,  2.3,  3.3,  1. ],
           [ 5.6,  2.7,  4.2,  1.3],
           [ 5.7,  3. ,  4.2,  1.2],
           [ 5.7,  2.9,  4.2,  1.3],
           [ 6.2,  2.9,  4.3,  1.3],
           [ 5.1,  2.5,  3. ,  1.1],
           [ 5.7,  2.8,  4.1,  1.3],
           [ 6.3,  3.3,  6. ,  2.5],
           [ 5.8,  2.7,  5.1,  1.9],
           [ 7.1,  3. ,  5.9,  2.1],
           [ 6.3,  2.9,  5.6,  1.8],
           [ 6.5,  3. ,  5.8,  2.2],
           [ 7.6,  3. ,  6.6,  2.1],
           [ 4.9,  2.5,  4.5,  1.7],
           [ 7.3,  2.9,  6.3,  1.8],
           [ 6.7,  2.5,  5.8,  1.8],
           [ 7.2,  3.6,  6.1,  2.5],
           [ 6.5,  3.2,  5.1,  2. ],
           [ 6.4,  2.7,  5.3,  1.9],
           [ 6.8,  3. ,  5.5,  2.1],
           [ 5.7,  2.5,  5. ,  2. ],
           [ 5.8,  2.8,  5.1,  2.4],
           [ 6.4,  3.2,  5.3,  2.3],
           [ 6.5,  3. ,  5.5,  1.8],
           [ 7.7,  3.8,  6.7,  2.2],
           [ 7.7,  2.6,  6.9,  2.3],
           [ 6. ,  2.2,  5. ,  1.5],
           [ 6.9,  3.2,  5.7,  2.3],
           [ 5.6,  2.8,  4.9,  2. ],
           [ 7.7,  2.8,  6.7,  2. ],
           [ 6.3,  2.7,  4.9,  1.8],
           [ 6.7,  3.3,  5.7,  2.1],
           [ 7.2,  3.2,  6. ,  1.8],
           [ 6.2,  2.8,  4.8,  1.8],
           [ 6.1,  3. ,  4.9,  1.8],
           [ 6.4,  2.8,  5.6,  2.1],
           [ 7.2,  3. ,  5.8,  1.6],
           [ 7.4,  2.8,  6.1,  1.9],
           [ 7.9,  3.8,  6.4,  2. ],
           [ 6.4,  2.8,  5.6,  2.2],
           [ 6.3,  2.8,  5.1,  1.5],
           [ 6.1,  2.6,  5.6,  1.4],
           [ 7.7,  3. ,  6.1,  2.3],
           [ 6.3,  3.4,  5.6,  2.4],
           [ 6.4,  3.1,  5.5,  1.8],
           [ 6. ,  3. ,  4.8,  1.8],
           [ 6.9,  3.1,  5.4,  2.1],
           [ 6.7,  3.1,  5.6,  2.4],
           [ 6.9,  3.1,  5.1,  2.3],
           [ 5.8,  2.7,  5.1,  1.9],
           [ 6.8,  3.2,  5.9,  2.3],
           [ 6.7,  3.3,  5.7,  2.5],
           [ 6.7,  3. ,  5.2,  2.3],
           [ 6.3,  2.5,  5. ,  1.9],
           [ 6.5,  3. ,  5.2,  2. ],
           [ 6.2,  3.4,  5.4,  2.3],
           [ 5.9,  3. ,  5.1,  1.8]])



Corresponding to each row in `iris.data` is a label of the Iris species. This is
represented by an array of integers.


    iris.target




    array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
           0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
           1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
           2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
           2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2])



Each integer is an indix into `iris.target_names` which looks like this:


    iris.target_names




    array(['setosa', 'versicolor', 'virginica'], 
          dtype='|S10')



So putting it all together, the first row in data is:


    iris.data[0]




    array([ 5.1,  3.5,  1.4,  0.2])



Which is means that the following measurements and were made:

|sepal length (cm)|sepal width (cm)|petal length (cm)|petal width(cm)|
|-----------------|----------------|-----------------|---------------|
|5.1|3.5|1.4|0.2|

And this plant was determined to be of species **setosa**.


    iris.target_names[iris.target[0]]




    'setosa'



# Nearest Neighbors

Our task is to classify a plant into one of three categories based on the length
and width of the sepals and petals. We'll say that $X$ is our *independent
variable* which consists of measurements, and $y$ is our dependent variable,
which is the Iris species. We want to use $X$ to predict $y$.

To do this, we will use **Nearest neigbors**. This means that for a *new*
$X_{test}$ will find $X$'s in our *training set* that are in the *neighborhood*
of $X_{test}$ in order to determine the value of $y$.

What are the details and variations on this main idea?
How do we define the *neighborbood* of k?
*I'm showing you the code to create the following graph. Don't worry too much
about the details right now.*



    import pylab as pl
    
    cm = pl.cm.get_cmap('RdYlBu')
    
    X = iris.data[:, :2]  # we only take the first two features.
    Y = iris.target
    
    x_min, x_max = X[:, 0].min() - .5, X[:, 0].max() + .5
    y_min, y_max = X[:, 1].min() - .5, X[:, 1].max() + .5
    
    pl.figure(2, figsize=(8, 6))
    pl.clf()
    
    # Plot the training points
    pl.scatter(X[:, 0], X[:, 1], c=Y, cmap=cm)
    
    pl.title('Iris Sepel Measurements')
    pl.xlabel('Sepal length (cm)')
    pl.ylabel('Sepal width (cm)')
    
    pl.xlim(x_min, x_max)
    pl.ylim(y_min, y_max)
    pl.legend(loc=0, scatterpoints=1)
    
    pl.show()



![png](Scikit%20Learn%20and%20K%20Nearest%20Neighbors_files/Scikit%20Learn%20and%20K%20Nearest%20Neighbors_21_0.png)


Here's a visualization of the data using *1-Nearest Neigbor*.
**If you don't have ipython, but using regular python instead, then comment out
the 6th line that says `%matplotlib inline`.**
For now you, you don't have to understand every line. Although later, you should
go back and take a look at the code.


    import numpy as np
    import pylab as pl
    from matplotlib.colors import ListedColormap
    from sklearn import neighbors, datasets
    
    ## Comment out this line if you don't have **ipython**
    %matplotlib inline
    
    n_neighbors = 1
    
    # import some data to play with
    iris = datasets.load_iris()
    X = iris.data[:, :2]  # we only take the first two features. We could
                          # avoid this ugly slicing by using a two-dim dataset
    y = iris.target
    
    h = .02  # step size in the mesh
    
    # Create color maps
    cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
    weights = 'uniform'
    
    for n_neighbors in xrange(1,10,3):
        # we create an instance of Neighbours Classifier and fit the data.
        clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
        clf.fit(X, y)
    
        # Plot the decision boundary. For that, we will assign a color to each
        # point in the mesh [x_min, m_max]x[y_min, y_max].
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                             np.arange(y_min, y_max, h))
        Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    
        # Put the result into a color plot
        Z = Z.reshape(xx.shape)
        pl.figure()
        pl.pcolormesh(xx, yy, Z, cmap=cmap_light)
    
        # Plot also the training points
        pl.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
        pl.xlim(xx.min(), xx.max())
        pl.ylim(yy.min(), yy.max())
        pl.title("3-Class classification (k = %i)"
                 % (n_neighbors))
    
    pl.show()


![png](Scikit%20Learn%20and%20K%20Nearest%20Neighbors_files/Scikit%20Learn%20and%20K%20Nearest%20Neighbors_23_0.png)



![png](Scikit%20Learn%20and%20K%20Nearest%20Neighbors_files/Scikit%20Learn%20and%20K%20Nearest%20Neighbors_23_1.png)



![png](Scikit%20Learn%20and%20K%20Nearest%20Neighbors_files/Scikit%20Learn%20and%20K%20Nearest%20Neighbors_23_2.png)


That's just plotting against the sepal measurements. Remember, we also have
petal width and length measurements.

## Using k-Nearest Neighbors for Prediction

Starting fresh, here's code to use k-Nearest Neighbors for modeling and
predicting the Iris data. We first load the observed data (the petal and sepal
measurements) into $X$, and the labeled data into $y$.


    from sklearn import datasets
    from sklearn import neighbors
    iris = datasets.load_iris()
    X = iris.data
    y = iris.target

Next, we instantiate a k-Nearest Neighbors model (using 1 neighbor) and *fit* it
to our data.


    knn = neighbors.KNeighborsClassifier(n_neighbors=1)
    knn.fit(X, y)




    KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
               n_neighbors=1, p=2, weights='uniform')



Now we can ask the model to make some predictions. For example:
> What kind of iris has 3cm x 5cm sepal and 4cm x 2cm petal?


    print iris.target_names[knn.predict([[3, 5, 4, 2]])]

    ['virginica']


All supervised estimators in `scikit-learn` share this interface of `fit(X, y)`
and `predict(X)`.

## Cross Validation

One problem is that we used *all* of our data to train our classifier. How do we
get a sense for how well the classifier will perform in practice? More
specifically, how do get a handle on expected **Out-of-Sample Error** (OOS
Error)?

We'll use **Cross Validation**, where we randomly split our data into *training*
and *validation* sets.

The following code will use 60% of the data for training (`X_train` and
`y_train`), and 40% for testing (`X_test` and `y_test`). Then it prints out the
predicted answers versus the actual answers.


    from sklearn.cross_validation import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.4, random_state=0)
    knn = neighbors.KNeighborsClassifier(n_neighbors=1)
    knn.fit(X_train, y_train)
    predicted = knn.predict(X_test)
    print predicted
    print y_test

    [2 1 0 2 0 2 0 1 1 1 2 1 1 1 1 0 1 1 0 0 2 1 0 0 2 0 0 1 1 0 2 1 0 2 2 1 0
     2 1 1 2 0 2 0 0 1 2 2 1 2 1 2 1 1 1 1 1 2 1 2]
    [2 1 0 2 0 2 0 1 1 1 2 1 1 1 1 0 1 1 0 0 2 1 0 0 2 0 0 1 1 0 2 1 0 2 2 1 0
     1 1 1 2 0 2 0 0 1 2 2 2 2 1 2 1 1 2 2 2 2 1 2]


## Confusion Matrix

Well, that's a bit hard to read. `sklearn` has some nice tools to help us
understand how well the model is performing.

The first tool is `metrics.confusion_report(y_test, predicted)`. More info
[here](http://scikit-learn.org/stable/auto_examples/plot_confusion_matrix.html)


    from sklearn import metrics
    print metrics.confusion_matrix(y_test, predicted)

    [[16  0  0]
     [ 0 22  1]
     [ 0  4 17]]


In the **confusion matrix**, the rows indicate the true label, and the columns
indicate the predicted label. At a glance, the diagonals represent those cases
where the model correctly predicted the label, and the off-diagonals are cases
where it mis-predicted. For example:

- Row 0 shows that it got all 16 cases correct when the answer was "0".
- Row 1 shows that it got 22 correct, and 1 wrong (predicting label "2" when the
answer was label "1").
- Row 2 shows that it got 17 correct, and 4 wrong (predicting label "1" when the
answer was label "2").

## Classification Report

We can also construct a *classification report*, which includes *precision*,
*recall* and *f1-scores*.


    print metrics.classification_report(y_test, predicted, target_names=iris.target_names)

                 precision    recall  f1-score   support
    
         setosa       1.00      1.00      1.00        16
     versicolor       0.85      0.96      0.90        23
      virginica       0.94      0.81      0.87        21
    
    avg / total       0.92      0.92      0.92        60
    


### Precision and Recall

Precision of a label is defined as

$$\frac{\text{True positive}}{\text{Test outcome positive}}$$

In other words, given the predictor says it's a certain label, what percent of
time is it correct? How *precise* is it?

Recall of a label is defined as

$$\frac{\text{True positive}}{\text{Condition positive}}$$

And can be thought of as, given that it's truly a particular label, what percent
of time will the predictor be correct? How well does it *recall*?

### F1-score

The F1-socre is defined as the harmonic mean of precision and recall. You get
get more info [here](http://en.wikipedia.org/wiki/F1_score).

$$F_1 = 2 \cdot \frac{\text{precision} \cdot \text{recall}}{\text{precision} +
\text{recall}}$$


    print metrics.f1_score(y_test, predicted)

    0.91601255887


### k-Fold Cross Validation

You can perform **k-Fold Cross Validation** and have the F1-score output for
each iteration. Here's how to do a 5-Fold Cross Validation and print out the
mean and standard-deviation of the F1 scores.


    from sklearn.cross_validation import cross_val_score
    scores = cross_val_score(knn, iris.data, iris.target, cv=5, scoring='f1')
    print("F1: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    F1: 0.95 (+/- 0.07)


This result is an array that indicaters the F1 score for each iteration of the
5-Fold Cross Validation.

Compare this to a k-Nearest Neighbor model that uses the seven nearest negibors:


    knn7 = neighbors.KNeighborsClassifier(n_neighbors=7)
    scores7 = cross_val_score(knn7, iris.data, iris.target, cv=5, scoring='f1')
    print("F1: %0.2f (+/- %0.2f)" % (scores7.mean(), scores7.std() * 2))

    F1: 0.96 (+/- 0.05)


We are now getting into the realm of **Model Evaluation**, which we will save
for another day! :)
