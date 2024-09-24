'''That application runs an emotion detector.'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route('/emotionDetector')
def sent_detector():
    '''Return the result of the emotions of the text in string format.'''

    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    retstring = "For the given statement, the system response is "
    retstring += f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
    retstring += f"'fear': {result['fear']}, 'joy':{result['joy']} and "
    retstring += f"'sadness': {result['sadness']}. "
    retstring += f"The dominant emotion is {result['dominant_emotion']}."

    return retstring

@app.route('/')
def render_index_page():
    '''Return the index page.'''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
