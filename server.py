"""Flask app for detecting emotions from a text query."""

from flask import Flask, render_template, request
from EmotionDetection.get_response import emotion_detector, format_output

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_response():
    """Analyze the text query and return formatted emotion scores."""
    text_to_analyze = request.args.get("textToAnalyze")

    response = format_output(emotion_detector(text_to_analyze))

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return response

@app.route("/")
def render_index_page():
    """Render the index page."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
