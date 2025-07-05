""" Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
"""

from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, render_template, request

app = Flask(__name__)
app.config["APP_NAME"] = "Emotion Detector"


@app.route("/emotionDetector")
def emotion_detect():
    """This code receives the text from the HTML interface and
    runs emotion detection over it using emotion_detector()
    function. The output returned shows the emotions and its confidence
    score for the provided text, along with the dominant emotion.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)

    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    """This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
