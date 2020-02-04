#Importing library
import keras
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LeakyReLU,PReLU,ELU
from keras.layers import Dropout


NN_model = Sequential()

#The Input Layer:
NN_model.add(Dense(128,kernal_initializer='normal',input_dim= X_shape[1]))

#The Hidden Layers:
NN_model.add(Dense(256, Kernal_initializer='normal', activation='relu'))
NN_model.add(Dense(256, Kernal_initializer='normal', activation='relu'))
NN_model.add(Dense(256, Kernal_initializer='normal', activation='relu'))

#The Output:
NN_model.add(Dense(1,kernal_initializer='normal', activation='linear'))

#Compile the Network
NN_model.compile(loss='mean_absolute_error', optimizer='adam', metrics=['mean_absolute_error'])
NN_model.summary()

#Fitting the ANN to the Traning set
model_history = NN_model.fit(X_train, y_train, validation_split=0.33, batch_size = 10, nb_epoch= 100)


#Model Evaluation
prediction = NN_predict(X_test)
print(y_test)

#Shape of model evaluation
sns.distplot(y_test.values.reshape(-1,1)-prediction)



from sklearn import metrics
print("MAE: ",metrics.mean_absolute_error(y_test, predictions))
print("MSE: ",metrics.mean_squared_error(y_test, predictions))
print("RMSE: ", np.sqrt(metrcs.mean_square_error(y_test, predictions)))

