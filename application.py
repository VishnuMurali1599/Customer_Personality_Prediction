from flask import Flask,request,render_template
from src.pipeline.predict_pipeline import CustomData,PredictPipeline

application=Flask(__name__)

app=application

## Route for a home page

@app.route('/')
def index():
    return render_template('index.html') 

@app.route('/predictdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(
            Education=request.form.get('Education'),
            Marital_Status=request.form.get('Marital_Status'),
            Income=request.form.get('Income'),
            Kidhome=request.form.get('Kidhome'),
            Teenhome=request.form.get('Teenhome'),
            Recency=float(request.form.get('Recency')),
            MntWines=float(request.form.get('MntWines')),
            MntFruits=request.form.get('MntFruits'),
            MntMeatProducts=request.form.get('MntMeatProducts'),
            MntFishProducts=request.form.get('MntFishProducts'),
            MntSweetProducts=request.form.get('MntSweetProducts'),
            MntGoldProds=request.form.get('MntGoldProds'),
            NumDealsPurchases=float(request.form.get('NumDealsPurchases')),
            NumWebPurchases=float(request.form.get('NumWebPurchases')),
            NumCatalogPurchases=request.form.get('NumCatalogPurchases'),
            NumStorePurchases=request.form.get('NumStorePurchases'),
            NumWebVisitsMonth=request.form.get('NumWebVisitsMonth'),
            Complain=request.form.get('Complain'),
            Present_Age_CST=request.form.get('Present_Age_CST'),
            Customer_Since_year=float(request.form.get('Customer_Since_year')),
            AcceptedCmp=float(request.form.get('AcceptedCmp'))

        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results=predict_pipeline.predict(pred_df)
        print("after Prediction")
        return render_template('home.html',results=results[0])
    

if __name__=="__main__":
    app.run(host="0.0.0.0")        