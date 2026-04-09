''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app : TODO
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This function is responsible for receiving the text to be analyzed from the 
    front end, passing it to the emotion_detector function and returning 
    the response back to the front end
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    text = (
        "For the given statement, the system response is "
        "'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        "'joy': {joy} and 'sadness': {sadness}. "
        "The dominant emotion is {dominant_emotion}."
    )

    return text.format(**response)

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
