import pandas as pd
from sklearn.linear_model import LinearRegression

a = pd.read_csv('data/realest.csv')
# c = a[a['Bathroom'] == 2 & a['Bathroom'] == 1]
# d = c[c['Bedroom'] == 4]
# print(d.count())
# print(d['Tax'].mean())
# print(d['Tax'].median())
# print(d['Tax'].std())
# print(d['Tax'].min())
# print(d['Tax'].max())

# data_frame = a[a['Space'] > 800].sort_values(by='Price', ascending=False)
# print(data_frame)



# print(len(a[a['Lot'] > a['Lot'].quantile(0.80)]))
# a[a['Bathroom'] == 2] & a['Bedroom'] == 4]].count()

a = a.dropna()
# print(a)
#
X = a[['Bedroom', 'Space', 'Room', 'Lot', 'Tax', 'Bathroom', 'Garage', 'Condition']]
y = a['Price']



b = LinearRegression()
b.fit(X, y)
# print(dict(zip(X.columns, b.coef_)))
# print(b.intercept_)

model_parameters = {
        'Intercept': b.intercept_,
        **dict(zip(X.columns, b.coef_))
        }

print()




import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


class AnalysisDataAndFitLinearRegression:

    def __init__(self):
        self.version = 1

    def analyse_and_fit_lrm(self, path):
        # a path to a dataset is "./data/realest.csv"
        # dataset can be loaded by uncommenting the line bellow
        data = pd.read_csv(path)
        a = data[data['Bathroom'] == 2]
        b = a[a['Bedroom'] == 4]
        statistics = [b['Tax'].mean(), b['Tax'].std(), b['Tax'].median(), b['Tax'].min(), b['Tax'].max()]

        data_frame = data[data['Space'] > 800].sort_values(by='Price', ascending=False)

        number_of_observations = len(data[data['Lot'] >= data['Lot'].quantile(0.80)])


        summary_dict = {'statistics': statistics, 'data_frame': data_frame, 'number_of_observations': number_of_observations}

        data = self.__listwise_deletion(data)
        X = data[['Bedroom', 'Space', 'Room', 'Lot', 'Tax', 'Bathroom', 'Garage', 'Condition']]
        y = data['Price']

        model = LinearRegression()
        model.fit(X, y)

        model_parameters = {
            'Intercept': model.intercept_,
            **dict(zip(X.columns, model.coef_))
            }

        price_prediction = model.predict([[3, 1500, 8, 40, 1000, 2, 1, 0]])[0]

        regression_dict = {'model_parameters': model_parameters, 'price_prediction': price_prediction}
        return {'summary_dict':summary_dict, 'regression_dict':regression_dict}

    def __listwise_deletion(self, data: pd.DataFrame):
        return data.dropna()


import pandas as pd
print(pd.read_csv('./data/realest.csv'))
