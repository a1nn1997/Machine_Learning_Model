from flask import Flask, jsonify
from joblib import dump, load
import numpy as np
# flask app creation

app = Flask(__name__)


@app.route("/")
def no():
    model=load('housing_data.joblib')
    input=np.array([[-0.40833261, -0.48421961,  1.5469924 ,0,  0.58892748,
       -0.82654395,  0.96975828, -0.94918894, -0.65131258,  0.15645733,
        1.29672341,  0.40481527,  0.61691861]])
    k=100*10000*model.predict(input)
    k[0]=int(k[0])
    result={ 
        ' CRIM      per capita crime rate by town' : input[0][0],
        ' ZN        proportion of residential land zoned for lots over 25,000 sq.ft.' : input[0][1], 
        ' INDUS     proportion of non-retail business acres per town.' :input[0][2],
        ' CHAS      Charles River dummy variable (= 1 if tract bounds, river; 0 otherwise)' :input[0][3],
        ' NOX       nitric oxides concentration (parts per 10 million)' :input[0][4],
        ' RM        average number of rooms per dwelling' : input[0][5],
        ' AGE       proportion of owner-occupied units built prior to 1940' : input[0][6],
        ' DIS       weighted distances to five Boston employment centres' : input[0][7],
        ' RAD       index of accessibility to radial highways' : input[0][8],
        ' TAX      full-value property-tax rate per $10,000' : input[0][9],
        ' PTRATIO  pupil-teacher ratio by town' : input[0][10],
        ' B        1000(Bk - 0.63)^2 where Bk is the proportion of blacks by town' : input[0][11],
        '13. LSTAT     lower status of the population': input[0][12],
        '14. MEDV     Median value of owner-occupied homes in $1000s' : 20*input[0][12], 
        'result   : predicted price of the house based upon above features in inr' : k[0]
    }
    return jsonify(result)



if __name__=="__main__":
    #app.run(debug=True)
    app.run(host = '0.0.0.0', port = 8080)

