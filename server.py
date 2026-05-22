"""Server module for emotion detection web application."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emo_detector():
    """Analyze the emotion of the submitted text."""
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(text_to_analyze)
    dominant_emotion = response['dominant_emotion']
    emotions = ", ".join(
        f"'{key}': {value}"
        for key, value in response.items()
        )

    if dominant_emotion is None:
        return "Invalid text! Please try again!."

    return (
        f"For the given statement, the system response is {emotions}." 
        f"The dominant emotion is {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """Render the home page."""
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
