import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            #model_path=os.path.join("artifacts","model.pkl")
            #preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path = "artifacts\model.pkl"
            preprocessor_path = 'artifacts\proprocessor.pkl'
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(  self,
        Education: str,
        Marital_Status: str,
        Income:float,
        Kidhome: int,
        Teenhome: int,
        Recency: int,
        MntWines: int,
        MntFruits: float,
        MntMeatProducts: float,
        MntFishProducts: float,
        MntSweetProducts: float,
        MntGoldProds: float,
        NumDealsPurchases: float,
        NumWebPurchases: float,
        NumCatalogPurchases: float,
        NumStorePurchases: float,
        NumWebVisitsMonth:float,
        Complain:int,
        Present_Age_CST:int,
        Customer_Since_year:int,
        AcceptedCmp:int
        ):

        self.Education = Education

        self.Marital_Status = Marital_Status

        self.Income = Income

        self.Kidhome = Kidhome

        self.Teenhome = Teenhome
        
        self.Recency = Recency

        self.MntWines = MntWines

        self.MntFruits = MntFruits
        
        self.MntMeatProducts = MntMeatProducts

        self.MntFishProducts = MntFishProducts

        self.MntSweetProducts = MntSweetProducts

        self.MntGoldProds = MntGoldProds

        self.NumDealsPurchases = NumDealsPurchases

        self.NumWebPurchases = NumWebPurchases

        self.NumCatalogPurchases = NumCatalogPurchases
        
        self.NumStorePurchases = NumStorePurchases

        self.NumWebVisitsMonth = NumWebVisitsMonth

        self.Complain = Complain

        self.Present_Age_CST = Present_Age_CST
        
        self.Customer_Since_year = Customer_Since_year

        self.AcceptedCmp = AcceptedCmp

    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "Education": [self.Education],
                "Marital_Status": [self.Marital_Status],
                "Income": [self.Income],
                "Kidhome": [self.Kidhome],
                "Teenhome": [self.Teenhome],
                "Recency": [self.Recency],
                "MntWines": [self.MntWines],
                "MntFruits": [self.MntFruits],
                "MntMeatProducts": [self.MntMeatProducts],
                "MntFishProducts": [self.MntFishProducts],
                "MntSweetProducts": [self.MntSweetProducts],
                "MntGoldProds": [self.MntGoldProds],
                "NumDealsPurchases": [self.NumDealsPurchases],
                "NumWebPurchases": [self.NumWebPurchases],
                "NumCatalogPurchases": [self.NumCatalogPurchases],
                "NumStorePurchases": [self.NumStorePurchases],
                "NumWebVisitsMonth": [self.NumWebVisitsMonth],
                "Complain": [self.Complain],
                "Present_Age_CST": [self.Present_Age_CST],
                "Customer_Since_year": [self.Customer_Since_year],
                "AcceptedCmp": [self.AcceptedCmp],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)