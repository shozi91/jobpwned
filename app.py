########################################################
# this file calls etl modules
########################################################
from flask import Flask, jsonify, request, render_template
from ETL import extract, transform, load
import os
#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    return render_template("index.html")

#################################################

@app.route("/etl", methods = ['GET', 'POST'])
def etl():
    try:
        #extract the data 
        app.config["IMAGE_UPLOADS"] = os.path.join(os.path.dirname(os.getcwd()), "Upload", "Saved", "normal")
        extract.extractor(request.method, app.config["IMAGE_UPLOADS"])

<<<<<<< HEAD:ETL/main.py
    #extract the data
    app.config["IMAGE_UPLOADS"] = os.path.join(os.path.dirname(os.getcwd()), "Upload", "saved", "normal")
    extractor(request.method, app.config["IMAGE_UPLOADS"])
=======
        #transform the data
        predictions, y_class = transform.transformer()
        #load the data
        load.loader(predictions, y_class)
    except Exception as e:
        print(e)
>>>>>>> b58782163f47253a8766cd6256ccf1d0968fa5fd:app.py


    return render_template("index.html")

#################################################

@app.route("/stats")
def stats():
    return render_template("stats.html")

#################################################

@app.route("/predictions")
def predictions():
    return 1

if __name__ == '__main__':
    app.run(debug=True)
    