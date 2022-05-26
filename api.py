from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from nltk.sentiment.vader import SentimentIntensityAnalyzer

app = FastAPI()



@app.get("/", response_class=HTMLResponse)
def root():
    return  f"""
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
        <h1> Predict sentiment with a sentence </h1>
         <form action="/vader-predict" method="get">
        <label for="fname">Texte a analyser</label>
        <input type="text" id="sentence" name="sentence"><br><br>

        <input type="submit" value="Submit">
        </form>

        </body>

    </html>
    """

@app.get("/vader-predict")
def predict_vader(sentence):

    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(sentence)
    ss["sentence"]= sentence
    return ss
