import pandas as pd
df= pd.read_excel("coke.xlsx")
df_dummies=pd.get_dummies(df['Quarter'])
import numpy as np

df = pd.concat([df,df_dummies],axis = 1)
df["t"] = np.arange(1,43)
df["t_squared"] = df["t"]*df["t"]
df.columns
df["log_Sales"] = np.log(df["Sales"])
df.drop(['Quarter'],inplace=True,axis=1)

Train = df.head(30)
Test = df.tail(12)
####################### L I N E A R ##########################
import statsmodels.formula.api as smf 
linear_model = smf.ols('Sales~t',data=Train).fit()
pred_linear =  pd.Series(linear_model.predict(pd.DataFrame(Test['t'])))
rmse_linear = np.sqrt(np.mean((np.array(Test['Sales'])-np.array(pred_linear))**2))
rmse_linear

##################### Exponential ##############################

Exp = smf.ols('log_Sales~t',data=Train).fit()
pred_Exp = pd.Series(Exp.predict(pd.DataFrame(Test['t'])))
rmse_Exp = np.sqrt(np.mean((np.array(Test['Sales'])-np.array(np.exp(pred_Exp)))**2))
rmse_Exp

#################### Quadratic ###############################

Quad = smf.ols('Sales~t+t_squared',data=Train).fit()
pred_Quad = pd.Series(Quad.predict(Test[["t","t_squared"]]))
rmse_Quad = np.sqrt(np.mean((np.array(Test['Sales'])-np.array(pred_Quad))**2))
rmse_Quad



################## Testing #######################################

data = {"MODEL":pd.Series(["rmse_linear","rmse_Exp","rmse_Quad"]),"RMSE_Values":pd.Series([rmse_linear,rmse_Exp,rmse_Quad])}
table_rmse=pd.DataFrame(data)
table_rmse
# so rmse Exp has the least value among the models prepared so far 
