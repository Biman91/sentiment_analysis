Run application in local environment

1. create an conda environment: "conda create -n sentiment_analysis"
2. activate conda environment: "conda activate sentiment_analysis"
3. install requirements.txt file: "pip install -r requirements.txt"
4. run app.py file
5. open a link: "http://127.0.0.1:5000/"
6. write a comment on the box
7. click on "predict"


File Description:
1. templates:
	home.html	: home page of web app
	output.html	: prediction page
2. app.py		: Flask framework. to run the web application and server. 
3. bow.pkl		: binary file, dump of bag of words/couter vectorization file
4. dataset.csv		: Dataset to training and test model
5. model.pkl		: binary file, dump model , use for predict output
6. preprocessing.py	: used to clean user input
7. Prockfile		: in deployment server to identify which file to run and which language
8. requirements.txt	: all libraries which are required to run web app
9. Sentiment analysis.ipynb	:train and test a model 