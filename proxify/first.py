import pandas as pd
from sklearn.linear_model import LinearRegression


class AnalysisDataAndFitLinearRegression:
    def __init__(self):
        self.version = 1

    def analyse_and_fit_lrm(self, path):
        # a path to a dataset is "./data/realest.csv"
        data = pd.read_csv(path)
        two_bathroom = data[data["Bathroom"] == 2]
        two_bathroom_four_bedroom = two_bathroom[two_bathroom["Bedroom"] == 4]
        statistics = [
            two_bathroom_four_bedroom["Tax"].mean(),
            two_bathroom_four_bedroom["Tax"].std(),
            two_bathroom_four_bedroom["Tax"].median(),
            two_bathroom_four_bedroom["Tax"].min(),
            two_bathroom_four_bedroom["Tax"].max(),
        ]

        data_frame = data[data["Space"] > 800].sort_values(by="Price", ascending=False)

        number_of_observations = len(data[data["Lot"] >= data["Lot"].quantile(0.80)])

        summary_dict = {
            "statistics": statistics,
            "data_frame": data_frame,
            "number_of_observations": number_of_observations,
        }

        data = self.__listwise_deletion(data)
        X = data[["Bedroom", "Space", "Room", "Lot", "Tax", "Bathroom", "Garage", "Condition"]]
        y = data["Price"]

        model = LinearRegression()
        model.fit(X, y)

        model_parameters = {
            "Intercept": model.intercept_,
            **dict(zip(X.columns, model.coef_)),
        }

        price_prediction = model.predict([[3, 1500, 8, 40, 1000, 2, 1, 0]])[0]

        regression_dict = {
            "model_parameters": model_parameters,
            "price_prediction": price_prediction,
        }
        return {"summary_dict": summary_dict, "regression_dict": regression_dict}

    def __listwise_deletion(self, data: pd.DataFrame):
        return data.dropna()


if __name__ == "__main__":
    result = AnalysisDataAndFitLinearRegression().analyse_and_fit_lrm("data/realest.csv")
    print(result["summary_dict"])
    print(result["regression_dict"])
