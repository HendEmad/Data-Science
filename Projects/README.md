# Data:
### 1. train data:

![Screenshot (1947)](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/bb284c9c-633b-491e-8b05-5b77c15623c9)
### 2. test data:

![Screenshot (1948)](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/04483889-ef84-4c9a-9d0e-1433dc93310e)

# Data exploration:
The aim of this step is to explore the data statistics and check the issues need to be solved in the processing. Here, there are 6 issues need to be checked:
1. Missing values
2. Duplications
3. Classes balancing
4. Correlation
   
   ![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/847fbd36-e436-42ea-84d2-0b2ed69f02f4)
   
5. Multicollinearity
6. Distribution
   ![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/b2e46f13-e300-4a62-b46f-7f18a33a3aeb)
   
   ![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/020e64db-c51e-41ea-a883-61e5c6d154d2)

# Exploratory data analysis:
The aim of this step is to understand the data and the relations between its features more. In addition to checing the outliers and delete them.
### Relations between the data features:
1. Internal memory vs. price range:
   
   ![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/f1146f72-fad8-421f-bf25-cef45348e05c)
   
2. Phones with 3G support percentage:
   
   ![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/a262d3a3-7354-47d2-9527-c0db9d481f1b)
   
3. Phones with 4G support percentage:
   
   ![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/f7a407e3-df70-49b4-9369-7398484ed414)
   
4. Battery power vs Price Range:
   
   ![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/874e2ba5-a94e-4b27-9798-6a3e4e6d439d)
   
5. No of Phones vs Camera megapixels of front and primary camera:

   ![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/40e3679f-cc15-41df-80ca-760e13df55ea)

6. Talk time vs Price range:

   ![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/1b28b768-d03b-4177-9242-c02b60620e8b)

### Insights:
1. As the internal memory of the mobile increases, the price range tends to increase as well, as this makes sense.
2. However, the overlapping of price ranges for the same internal memory space suggests that internal memory alone is not a good predictor of proce range.
3. The majority of phones with 3G support is clear with approximately 75% of phones.
4. `three_g` feature may be an improtant feature in predicting the price range of the phones.
5. The higher percentage of 4G support indicates that the 4G technology is widely used.
6. As the median battery power increases, the price range increases. This suggests that the `battery_power` is an important feature.
7. The variability in battery power among the lower price ranges (0&1) and the higher price ranges (2&3) may be due to the other features effect.
8. The front camera megapixels are generally lower than the primary camera megapixels, this makes sense.
9. The front camera distibution is more skewed towards thelower end of the range, indicating that many phones have lower quality front cameras.
10. The primary camera distribution is moreevenly distributed across the range, indicating that there is a wider variety of primary camera qualities among phones on the dataset, suggesting that the `pc` feature. may be more important than `fc` feature.
11. The mean talk time values for each price range class is clear, but the confidence intervals are quite wide, indicating that there is a lot of variablility in the dataset.

### Outliers detection and deletion
![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/f00921c3-8a86-4068-a1c8-414634e9edcf)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/eabc1714-5348-4024-ae42-2f6fc16fd74e)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/4ef502b5-5474-43e4-9cfa-8a3cb58712a1)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/065e9f2b-896f-48c6-861a-085c6ebba1cb)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/429741a6-a79a-4607-8153-ef8af62e9b24)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/2ecc8866-c622-4c36-aa98-19b335351356)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/14bc792e-f107-4cbf-ab05-3c30e6e129a5)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/6eee8b6a-7990-4775-9175-d7984c7a5cdd)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/b10d0317-3efc-4a1e-87eb-c8bbf81aeec3)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/c975f891-3129-4a5c-bc36-e88d81b23aba)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/cb01a8df-2565-4b46-9a43-a0efaad5214f)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/f8120e81-f7c6-409f-9521-75324a7fc59f)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/20863577-37a6-4dff-b523-8d4e4d90702e)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/927be447-1911-4bd0-815e-8c2fde04f5f4)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/9fca944a-d432-4498-a0d2-8c57681785ae)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/b742ae3d-8f47-4e1d-bcdd-3a43174b078d)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/3b9bfc66-0372-4411-a10c-7b75926474e7)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/a1218bd6-6f49-4a75-b672-789595a0292a)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/abbedebf-1d5f-400b-b029-c902921da2f5)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/bcc1f459-6e76-4132-8551-65d2d05004d3)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/bbfeab7a-61e8-4123-9669-0542fde92672)

# Data transformation and feature engineering:
- Applying BoxCox transformation to convert the skewed features into normal distribution form.
- Scaling the features.
### After applying BoxCox transformation:
![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/96b274e9-0c33-4755-ad78-e506c28bf183)

# Feature selection and cross validations:
- Creating 5 classifiers and applying the cross validation using k-fold cross validation technique to select the most related features to the target variable.
### Classifiers performance:
***1. Confusion matrix:***

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/66c3d163-419f-4c1c-917f-eaf875c639d8)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/1ee8a695-1847-4433-85dd-f186b22d0726)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/78250060-7ee4-4bdd-ba73-833c3df706ad)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/37827044-4b50-4c73-96a1-8ba455420714)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/24f23c2b-dbd2-41b2-8581-4d3154d63cc6)

***2. Precision, recall, and f1 score:***

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/e0951f26-4cef-4d88-8f43-3fe4f5ae4e6b)

# Model implementation and hyperparameters tuning:
The aim of this step is to tune hyperparameters of the best models according to the performance to choose the best values of them
### Results of multinomial logistic regression model on the validation set, after balancing the classes using SMOTE technique; to avoid biasing:
![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/f4017655-5333-4a51-b290-8e08072b9976)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/fc84a6c8-97dc-4849-bd3e-0f252f92675a)

### Results of multi-class svm model on the validation set:
![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/1168ade9-4353-4d75-993b-49dcb93c0b09)

![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/f40084b8-1961-4fb8-8a45-2268f8525002)

# Predicting the test data price range result
![image](https://github.com/HendEmad/Mobile_price_prediction/assets/91827137/70e289e4-cd59-45ff-95fd-8f2230da3d5e)
