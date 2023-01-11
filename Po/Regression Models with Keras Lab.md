# Regression Models with Keras Lab
UID: 202212261305
Tags: #🌱 
Links: [[Regression Models with Keras]]

----
## Python file
```python
import pandas as pd
import numpy as np
import keras # Uses TensorFlow backend
from keras.models import Sequential
from keras.layers import Dense

concrete_data = pd.read_csv('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DL0101EN/labs/data/concrete_data.csv')
concrete_data.head() # inspect headers in Jupyter
concrete_data.shape #(1030, 9)
concrete_data.describe() # check for missing data
concrete_data.isnull().sum() # outputs heaers of the CSV and 0 for number of isnull() --> the data is clean

## ---- Pre-processing: Splitting the data into targets and determinants
concrete_data_columns = concrete_data.columns

predictors = concrete_data[concrete_data_columns[concrete_data_columns != 'Strength']] # all columns except Strength
target = concrete_data['Strength'] # Strength column. Strength is the target variable

predictors.head() 
target.head()

# Normalizing data: Find difference from mean and divide by standard deviation
predictors_norm = (predictors - predictors.mean()) / predictors.std()
predictors_norm.head()

n_cols = predictors_norm.shape[1] # number of predictors

## ------ Building a network
# define regression model
def regression_model():
    # create model
    model = Sequential()
    model.add(Dense(50, activation='relu', input_shape=(n_cols,))) # Input layer takes shape of CSV header, has 50 nodes in hidden layer 1
    model.add(Dense(50, activation='relu')) # Hidden layer 2 of another 50 nodes
    model.add(Dense(1)) # Output layer
    
    # compile model
    model.compile(optimizer='adam', loss='mean_squared_error') # Adam is an alternative to gradient descent, advantage is that learning rate doesn't have to be predefined
    return model

# build the model
model = regression_model()

# fit the model: traning using 100 epochs
model.fit(predictors_norm, target, validation_split=0.3, epochs=100, verbose=2)
```

## Output
```terminal
2022-12-26 04:03:49.137874: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
2022-12-26 04:03:49.144395: I tensorflow/core/platform/profile_utils/cpu_utils.cc:94] CPU Frequency: 2095145000 Hz
2022-12-26 04:03:49.145271: I tensorflow/compiler/xla/service/service.cc:168] XLA service 0x55a1cf591730 executing computations on platform Host. Devices:
2022-12-26 04:03:49.145336: I tensorflow/compiler/xla/service/service.cc:175]   StreamExecutor device (0): <undefined>, <undefined>
2022-12-26 04:03:49.398546: W tensorflow/compiler/jit/mark_for_compilation_pass.cc:1412] (One-time warning): Not using XLA:CPU for cluster because envvar TF_XLA_FLAGS=--tf_xla_cpu_global_jit was not set.  If you want XLA:CPU, either set that envvar, or use experimental_jit_scope to enable XLA:CPU.  To confirm that XLA is active, pass --vmodule=xla_compilation_cache=1 (as a proper command-line flag, not via TF_XLA_FLAGS) or set the envvar XLA_FLAGS=--xla_hlo_profile.

 - 1s - loss: 1629.8291 - val_loss: 1128.1850
Epoch 2/100
 - 0s - loss: 1491.9495 - val_loss: 1007.5891
Epoch 3/100
 - 0s - loss: 1266.8107 - val_loss: 818.6939
Epoch 4/100
 - 0s - loss: 940.4477 - val_loss: 582.9469
Epoch 5/100
 - 0s - loss: 579.6625 - val_loss: 364.7522
Epoch 6/100
 - 0s - loss: 334.6323 - val_loss: 242.7151
Epoch 7/100
 - 0s - loss: 246.8182 - val_loss: 206.8918
Epoch 8/100
 - 0s - loss: 226.8955 - val_loss: 188.8603
Epoch 9/100
 - 0s - loss: 213.3007 - val_loss: 180.5835
Epoch 10/100
 - 0s - loss: 203.5750 - val_loss: 174.4849
Epoch 11/100
 - 0s - loss: 195.2748 - val_loss: 173.6469
Epoch 12/100
 - 0s - loss: 188.2415 - val_loss: 167.4751
Epoch 13/100
 - 0s - loss: 182.3050 - val_loss: 164.7302
Epoch 14/100
 - 0s - loss: 177.5561 - val_loss: 163.2757
Epoch 15/100
 - 0s - loss: 172.8737 - val_loss: 159.6130
Epoch 16/100
 - 0s - loss: 168.5800 - val_loss: 159.7342
Epoch 17/100
 - 0s - loss: 165.8401 - val_loss: 156.9543
Epoch 18/100
 - 0s - loss: 162.9399 - val_loss: 156.3259
Epoch 19/100
 - 0s - loss: 161.0244 - val_loss: 153.2428
Epoch 20/100
 - 0s - loss: 158.8714 - val_loss: 155.6716
Epoch 21/100
 - 0s - loss: 155.9926 - val_loss: 153.8475
Epoch 22/100
 - 0s - loss: 154.4706 - val_loss: 152.8932
Epoch 23/100
 - 0s - loss: 152.7205 - val_loss: 152.7468
Epoch 24/100
 - 0s - loss: 150.7871 - val_loss: 152.0807
Epoch 25/100
 - 0s - loss: 149.0808 - val_loss: 153.8629
Epoch 26/100
 - 0s - loss: 147.4698 - val_loss: 151.2865
Epoch 27/100
 - 0s - loss: 146.5196 - val_loss: 152.7747
Epoch 28/100
 - 0s - loss: 145.2828 - val_loss: 152.6636
Epoch 29/100
 - 0s - loss: 143.9435 - val_loss: 151.1194
Epoch 30/100
 - 0s - loss: 142.7949 - val_loss: 152.2665
Epoch 31/100
 - 0s - loss: 141.5886 - val_loss: 151.8301
Epoch 32/100
 - 0s - loss: 140.3568 - val_loss: 153.0241
Epoch 33/100
 - 0s - loss: 138.7006 - val_loss: 152.6009
Epoch 34/100
 - 0s - loss: 137.3886 - val_loss: 151.3620
Epoch 35/100
 - 0s - loss: 136.5214 - val_loss: 151.2687
Epoch 36/100
 - 0s - loss: 135.6250 - val_loss: 150.5814
Epoch 37/100
 - 0s - loss: 134.5242 - val_loss: 152.0701
Epoch 38/100
 - 0s - loss: 133.3290 - val_loss: 151.5255
Epoch 39/100
 - 0s - loss: 132.5670 - val_loss: 150.3297
Epoch 40/100
 - 0s - loss: 131.1454 - val_loss: 150.6881
Epoch 41/100
 - 0s - loss: 130.4688 - val_loss: 150.1451
Epoch 42/100
 - 0s - loss: 129.0846 - val_loss: 150.5189
Epoch 43/100
 - 0s - loss: 127.9196 - val_loss: 148.4575
Epoch 44/100
 - 0s - loss: 127.4322 - val_loss: 149.2641
Epoch 45/100
 - 0s - loss: 125.4083 - val_loss: 147.9457
Epoch 46/100
 - 0s - loss: 124.0667 - val_loss: 149.8365
Epoch 47/100
 - 0s - loss: 122.9617 - val_loss: 147.2500
Epoch 48/100
 - 0s - loss: 121.6801 - val_loss: 150.8391
Epoch 49/100
 - 0s - loss: 120.1152 - val_loss: 146.8298
Epoch 50/100
 - 0s - loss: 118.5688 - val_loss: 145.5073
Epoch 51/100
 - 0s - loss: 117.4129 - val_loss: 145.3767
Epoch 52/100
 - 0s - loss: 115.8733 - val_loss: 143.4085
Epoch 53/100
 - 0s - loss: 113.8279 - val_loss: 141.8304
Epoch 54/100
 - 0s - loss: 112.9840 - val_loss: 142.4505
Epoch 55/100
 - 0s - loss: 111.3093 - val_loss: 139.5618
Epoch 56/100
 - 0s - loss: 109.8632 - val_loss: 138.9079
Epoch 57/100
 - 0s - loss: 107.9520 - val_loss: 140.7587
Epoch 58/100
 - 0s - loss: 106.7036 - val_loss: 135.6453
Epoch 59/100
 - 0s - loss: 105.0979 - val_loss: 134.1957
Epoch 60/100
 - 0s - loss: 103.2258 - val_loss: 137.6269
Epoch 61/100
 - 0s - loss: 101.7049 - val_loss: 131.4618
Epoch 62/100
 - 0s - loss: 100.2655 - val_loss: 133.8560
Epoch 63/100
 - 0s - loss: 98.2417 - val_loss: 127.7560
Epoch 64/100
 - 0s - loss: 96.2997 - val_loss: 129.6818
Epoch 65/100
 - 0s - loss: 94.2302 - val_loss: 126.5763
Epoch 66/100
 - 0s - loss: 92.2391 - val_loss: 123.4025
Epoch 67/100
 - 0s - loss: 90.4317 - val_loss: 125.9777
Epoch 68/100
 - 0s - loss: 87.7478 - val_loss: 119.0046
Epoch 69/100
 - 0s - loss: 84.9902 - val_loss: 118.6105
Epoch 70/100
 - 0s - loss: 82.8815 - val_loss: 117.9550
Epoch 71/100
 - 0s - loss: 80.6261 - val_loss: 113.2463
Epoch 72/100
 - 0s - loss: 78.4199 - val_loss: 115.0651
Epoch 73/100
 - 0s - loss: 76.7727 - val_loss: 113.7870
Epoch 74/100
 - 0s - loss: 74.6652 - val_loss: 109.6053
Epoch 75/100
 - 0s - loss: 72.1555 - val_loss: 109.4099
Epoch 76/100
 - 0s - loss: 70.5007 - val_loss: 106.5021
Epoch 77/100
 - 0s - loss: 68.8560 - val_loss: 104.6554
Epoch 78/100
 - 0s - loss: 67.5171 - val_loss: 102.2907
Epoch 79/100
 - 0s - loss: 65.6759 - val_loss: 102.0672
Epoch 80/100
 - 0s - loss: 65.1350 - val_loss: 96.7747
Epoch 81/100
 - 0s - loss: 63.5541 - val_loss: 96.2711
Epoch 82/100
 - 0s - loss: 62.4988 - val_loss: 96.5356
Epoch 83/100
 - 0s - loss: 61.3104 - val_loss: 93.7187
Epoch 84/100
 - 0s - loss: 59.8665 - val_loss: 89.6953
Epoch 85/100
 - 0s - loss: 58.6486 - val_loss: 92.6926
Epoch 86/100
 - 0s - loss: 57.7250 - val_loss: 87.1423
Epoch 87/100
 - 0s - loss: 56.6477 - val_loss: 85.3037
Epoch 88/100
 - 0s - loss: 55.4515 - val_loss: 84.4039
Epoch 89/100
 - 0s - loss: 54.8336 - val_loss: 82.6492
Epoch 90/100
 - 0s - loss: 53.4918 - val_loss: 84.1664
Epoch 91/100
 - 0s - loss: 52.9099 - val_loss: 78.3426
Epoch 92/100
 - 0s - loss: 52.3684 - val_loss: 78.6576
Epoch 93/100
 - 0s - loss: 51.6645 - val_loss: 76.6748
Epoch 94/100
 - 0s - loss: 50.9349 - val_loss: 80.4118
Epoch 95/100
 - 0s - loss: 49.7738 - val_loss: 75.5752
Epoch 96/100
 - 0s - loss: 48.9837 - val_loss: 78.1588
Epoch 97/100
 - 0s - loss: 48.8881 - val_loss: 72.5153
Epoch 98/100
 - 0s - loss: 48.5101 - val_loss: 76.3569
Epoch 99/100
 - 0s - loss: 46.9792 - val_loss: 74.4060
Epoch 100/100
 - 0s - loss: 47.0060 - val_loss: 72.4625
```