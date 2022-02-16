<h1><strong>Machine_Learning_Model Api for real estate Website</strong></h1>

<p>This is a Rest Api created using Flask which was fatching data BAYUT API (which is used to post real estate dataset for real estate application) and predict real estate price of fatched model</p>

<h2><strong>In this model 2 data set were trained :-</strong></h2>

<h3><strong>first model </strong>which was done using pretained model which was commonly known as <strong>Supervised Learning </strong>based upon <strong>Regression based models.</strong></h3>

<p>in this test different test were performed (Linear Regression, Decision Tree, Random Forest Regressor) As per the result of test data ( <strong>Random Forest Regressor </strong>) had given best result and hend opted for creation of Machine Learning model of Real Estate Price Predictor</p>

<h3><strong>Second Model</strong> Created using <strong>Cloud Auto ML</strong> of Google (commonly used to created Custom Machine Learing Models for <strong>Unsupervised Learning</strong> based upon <strong>Association based model)</strong></h3>

<p>the costom Model which was created was giving output to Testing Model of Main model based on its previous classification.</p>

<h2><strong>By application of both models together real time price prediction of real estate based upon its parameter and their classification was happening</strong></h2>

<p>Model was than Jsonify and created into <strong>REST Api</strong> using <strong>flask</strong></p>

<p><strong>Rest Api</strong> is first <strong>Containerised </strong>using <strong>docker</strong> and <strong>orchestrated </strong>for <strong>scaling purposes</strong> using <strong>Google Kubernetes</strong></p>

<p>Created <strong>WebApi</strong> is atlast fired to <strong>Real Estate Website</strong></p>
