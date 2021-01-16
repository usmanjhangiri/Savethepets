from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from keywords import main
# print('hello!')
app = Flask(__name__)

@app.route('/') 
def home():
        
    sheet = main()
    # Call the Sheets API
    data = [{'Keyword':i[0]} for i in sheet.values().get(spreadsheetId='1UYnqmwEaphPmBoQThryxSAVraSewcWogQ8AxSfjrqN4', 
    range='Keywords!A2:A').execute().get('values', [])]
    print(data,'\n\n\n\n\n')
    return render_template("index.html",data=data)


if __name__ == "__main__":
    # app.run(debug=True)
    app.run()
    