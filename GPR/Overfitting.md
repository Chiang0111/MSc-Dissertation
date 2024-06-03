# Overfitting

### Definition of overfitting
Overfitting, is the process of overlearning the training data and becoming unable to successfully predict or discriminate between data that is not part of the training data.

Example: 

<img width="523" alt="截圖 2024-06-03 中午12 41 32" src="https://github.com/Chiang0111/MSc-Dissertation/assets/149504305/5d0e5ba9-b2a7-4628-9148-405d83bb78db"> 

Green line = Result of overfitting, Black line = Normal classification model

However, if a new data comes in (yellow dots), it will cause classification error, because the accuracy of the green line model is very high in the training data, but the error rate will increase under the new data classification.

Method of detecting the occurrence of Overfitting conditions:
All the Training data chap into two parts, one is Training Set and Validate Set, Training Set is really take the data to training, and Validate Set is to verify the Model in the training data outside the data is feasible. 

Check is the model is overfitting or not by using scikit-learn, Method link:
https://scikit-learn.org/stable/auto_examples/model_selection/plot_underfitting_overfitting.html

### Reason of Overfitting and solutions
1. Obtaining more information
2. Reducing parameters or features or reducing the number of neural layers.
3. In the case of the same parameters and the same amount of data, regularisation can be used.
4. In the case of the same parameters and the same amount of data, you can use Dropout.
