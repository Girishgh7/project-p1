import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 
import pandas_datareader as web 
import datetime as dt 

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Dropout,LSTM

#Load data 
company='APPL'
start=dt.datetime(2010,1,1)
end=dt.datetime(2020,1,1)

data=web.DataReader(company,'yahoo',start,end)

scaler=MinMaxScaler(feature_range=(0,1))
scaled_data=scaler.fit_transform(data['Close'].values.reshape(-1,1))
prediction_days=30

X_train=[]
Y_train=[]

for x in range(prediction_days,len(scaled_data)):
    X_train.append(scaled_data[x-prediction_days:x,0])
    Y_train.append(scaled_data[x,0])
X_train,Y_train=np.array(X_train),np.array(Y_train)
X_train=np.reshape(X_train,(X_train.shape[0],X_train.shape[1],1))

#model 
model=Sequential()
model.add(LSTM(units=50,return_sequences=True,input_shape=(X_train.shape[1],1)))
model.add(Dropout(0.2))
model.add(LSTM(units=50,return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1))

model.complie(optimizer='adam',loss='mean_saqured_error')
model.fit(X_train,Y_train,epochs=25,batch=32)

'''Model accuaracy test '''

test_start=dt.datetime(2020,1,1)
test_end=dt.datetime.now()

test_data=web.DataReader(company,'yahoo',test_start,test_end)
actual_price=test_data['Close'].values

total_dataset=pd.concat((data['Close']))

model_inputs=total_dataset[len(total_dataset)-len(test_data)-prediction_days:].values
model_input=model_inputs.reshape(-1,1)
model_input=scaler.transform(model_inputs)

#predictions on tests 

x_test=[]

for x in range(prediction_days,len(model_input)):
    x_test.append(model_inputs[x-prediction_days:x,0])
x_test=np.array(x_test)
x_test=np.reshape(x_test,(x_test.shape[0],x_test.hape[1],1))

predicted_prices=model.predict(x_test)
predicted_prices=scaler.inverse_transform(predicted_prices)

#ploting 
plt.plot(actual_price,color="black",label=f"Actual {company} Price")
plt.plot(predicted_prices,color='green',label=f"Predicted {company} Price")
plt.title(f"{company}Share Price")
plt.xlabel('Time')
plt.ylabel(f"{company} Share Price")
plt.legend()
plt.show()