### Insurance Premium Prediction:
 
To give people an estimate of how much they need based on their individual health situation. After that, customers can work with any health insurance carrier and its plans and perks while keeping the projected cost from our study in mind. I am considering variables as age, sex, BMI, number of children, smoking habits and living region to predict the premium. This can assist a person in concentrating on the health side of an insurance policy rather than the ineffective part.

**Data source**: https://www.kaggle.com/noordeen/insurance-premium-prediction

#### Approach: 
1. Loading the dataset using Pandas and performed basic checks like the data type of each column and having any missing values.
2. Performed Exploratory data analysis:
- Visualized each predictor or independent feature with the target feature and found that there's a direct proportionality between cement and the target feature while there's an inverse proportionality between water and the target feature.
- To get even more better insights, plotted both Pearson and Spearman correlations, which showed the same results as above.
- the distribution of the target feature, expenses which was in Normal distribution with a very little right skewness.
- Checked for the presence of outliers in all the columns
3. Experimenting with various ML algorithms
- First, tried with Linear regression models, ridge and lasso regression approached. Performance metrics are calculated for all the approaches. The test RMSE score is little bit lesser compared to other approaches. Then, performed a residual analysis and the model satisfied all the assumptions of linear regression.
- Next, tried with various tree based models, performed hyper parameter tuning using the GridSearchCV and found the best hyperparameters for each model. Then, picked the top most features as per the feature importance by an each model. Models, evaluated on both the training and testing data and recorded the performance metrics.
- Based on the performance metrics of both the linear and the tree based models, XGBoost regressor performed the best, followed by the random forest regressor.
4.Deployment: Deployed the XGBoost regressor model using Flask, which works in the backend part while for the frontend UI Web page, used HTML5.

At each step in both development and deployment parts, logging operation is performed which are stored in log folder.

So, now we can find the insurance premium quickly by just passing the mentioned details as an input to the web application.

#### Web Deployment
Deployed on web using Streamlit url: https://matindra-insurance-premium-prediction-project-app-crn16z.streamlit.app/

## Setup
Create a conda environment
```
conda create -p venv python==3.7 -y
```

activate conda environment
```
conda activate venv/
```

To install requirement file
```
pip install -r requirements.txt
```

* Add files to git  `git add .` or  `git add <file_name>`    
* To check the git status  `git status`    
* To check all version maintained by git  `git log`    
* To create version/commit all changes by git  `git commit -m "message"`    
* To send version/changes to github  `git push origin main`    


## Project Pipeline
1. [Data Ingestion](#1-data-ingestion)
2. [Data Validation](#2-data-validation)
3. [Data Transformation](#3-data-transformation)
4. [Model Training](#4-model-training)
5. [Model Evaluation](#5-model-evaluation)
6. [Model Deployement](#6-model-deployement)

### 1. Data Ingestion: 
* Data ingestion is the process in which unstructured data is extracted from one or multiple sources and then prepared for training machine learning models.

### 2. Data Validation:
* Data validation is an integral part of ML pipeline. It is checking the quality of source data before training a new mode
* It focuses on checking that the statistics of the new data are as expected (e.g. feature distribution, number of categories, etc). 

### 3. Data Transformation 
* Data transformation is the process of converting raw data into a format or structure that would be more suitable for model building.
* It is an imperative step in feature engineering that facilitates discovering insights.

### 4. Model Training
* Model training in machine learning is the process in which a machine learning (ML) algorithm is fed with sufficient training data to learn from.

### 5. Model Evaluation
* Model evaluation is the process of using different evaluation metrics to understand a machine learning model’s performance, as well as its strengths and weaknesses.
* Model evaluation is important to assess the efficacy of a model during initial research phases, and it also plays a role in model monitoring.

### 6. Model Deployement
* Deployment is the method by which we integrate a machine learning model into production environment to make practical business decisions based on data. 


<p align="left">
  <img src="https://lh5.googleusercontent.com/49NljwFVuPL1zR5z6rrBsLh8fEQBDTLCmG9Z9xScq1sLWdtR89KhtKS702hUDN566WIE42eems8Fb_y0jbb6N7Cv-noJ_W3pt7JDlblCE_0POna1AUAZ6aSNERqPC9nfMFrXL8g"/>

#### Tools and Technologies used

![Tools](https://user-images.githubusercontent.com/69260855/142414506-f21e3ea1-5956-418e-903d-9835c32f3708.png)

#### High Level Design: 
URL: https://drive.google.com/file/d/1orDqgXQWhve7WrxedtcOCJZffYveSzHe/view

#### Low Level Design: 
URL: https://drive.google.com/file/d/1SSx30MvTk1KpUAPQ_KJKSjlJTCqLCSjc/view

#### Architecture: 
URL: https://drive.google.com/file/d/1xBthUq0hCnkScHCdNGjUGu-AFJTalZZ0/view

#### Detailed Project report: 
URL: https://drive.google.com/file/d/1dzPu4exm8wOFKNVR26tZ8AuFKOTNkD7j/view

#### Wireframe document: 
URL: https://drive.google.com/file/d/1zEqb--Vpy4Mekkvmq7IcF41WiaMqIJww/view?usp=share_link

#### Demo video: 
URL: https://drive.google.com/


#### Author:
- ##### Matindra Malik (Linkedin: https://www.linkedin.com/in/matindra/)
