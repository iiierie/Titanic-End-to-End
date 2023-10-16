# Titanic - End To End

---

## LifeCycle of a ML Project

1. **Problem Definition**( figure out the goals and objectives of what you are trying to solve)
    1. In our case, it’s to **draw the insights about death of people** in the titanic disaster incident based on his/her age, sex, ticket class, socio-economic background and other features and finally, **to be able to make prediction** if a certain person would survive or die.
2. **Data Collection**
    1. sources of data can be anything like csv, from API, web scraping ,directly from Database using SQL.
    2. in our case, we got it from Kaggle and the file type is csv so we can use pandas read_csv .
3. **EDA**
    1. **Import** all needed libraries
    2. **load** and **explore** the data
        1. understand given training data
            - note down all the basic initial observations on training data
        2. understand given test data
            - note down all the basic initial observations on test data
            - Is test data behaviour same as training data?
            - What are the differences?
    3. **Clean the data**
        1. check for **duplicated** rows and delete them
        2. check for any **outliers** [box plot] [use **IQR**] 
        3. work on **missing values**, check how many missing and decide whether to ***drop*** or to ***fill with mean, median*** or ***create a model with training data and fill with predictions***
    4. **Feature Binning** 
        1. binning means creating class groups  categories of continuous data
        2. note: encoding only needed before we train the model cause model only undstands numbers
    5. **Data Visualization with clean and processed data**
        1. might as well drop unnecessary features carefully selecting
        2. search for **correlation** among features
            - create **heatmaps**, **correlation matrix**
            - explore data further by Univariate EDA     (count plot of all features)
            - multivariate EDA
    6. Note all the **insights and conclusions** about each important feature seperately and neatly
    7. **Feature Encoding and Engineering**
        1. select important features
        2. encode the features
        3. train , test, validation split
4. **Modelling**
    1. check which classification model works the best
    2. check the test scores for each classification model
    3. implement whichever gives high accuracy
    4. generate pickle file or submission file as necessary
5. **Deploy** the model 

---

- encoding
    
    pclass :1, 2,3
    
    **encoded** sex : {male: 1, female :0}
    
    **encoded** age:{teenager:5, adult:0, elderly adult : 2, child : 1, young : 6, old:4, infant :3}
    
    sibsp: 0,1,2,3,4,5,6,7,8
    
    parch = 0,1,2,3,4,5,6
    
    **encoded** embarked :{S:2, C:0, B:1}
    
    **encoded** fare_bin:{1,2,3,4,5}
    
    fare: mini : -1,  q1:7.9104, q2:14.4542, q3 = 31.0, maxi = 512.3292
    
    fare_range = [1,2,3,4,5]
    fare_bins = [mini,q1,q2,q3,maxi,np.inf]
    
    train_df['Fare_Bin'] = pd.cut(train_df['Fare'], bins = fare_bins, labels = fare_range)
    
    #train_test split
    X = train_df[['Pclass','Sex_Labels','Age_Labels','Embarked_Labels','Fare_Bin','SibSp','Parch']].values
    y = train_df[['Survived']].values
    
- building flask app steps
    - ✔️first, create a html webpage that accepts ['Pclass','Sex_Labels','Age_Labels','Embarked_Labels','Fare_Bin','SibSp','Parch'] and predict button
    - second, create a flask app and incorporate model, link the html with the model’s prediction
        - important: in the html, get it in human readable form like for fare, give bin range but in flask while passing it to the model , pass the corresponding binned or encoded value.
-
