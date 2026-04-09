import json
import requests


def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json=myobj, headers=headers)

    formatted_response = json.loads(response.text)
    emotion_predictions = formatted_response["emotionPredictions"][0]["emotion"]
    highest_emotion = max(emotion_predictions, key=emotion_predictions.get)
    emotion_predictions['dominant_emotion'] = highest_emotion

    return emotion_predictions
