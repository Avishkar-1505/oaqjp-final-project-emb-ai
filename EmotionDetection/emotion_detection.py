import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers=header)


    formatted_response = json.loads(response.text)

    if response.status_code == 400 or response.status_code == 500:
        emotionsError = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion' : None
        }

        return emotionsError
    

    anger_score = formatted_response["emotionPredictions"][0]["emotion"]["anger"]
    disgust_score = formatted_response["emotionPredictions"][0]["emotion"]["disgust"]
    fear_score = formatted_response["emotionPredictions"][0]["emotion"]["fear"]
    joy_score = formatted_response["emotionPredictions"][0]["emotion"]["joy"]
    sadness_score = formatted_response["emotionPredictions"][0]["emotion"]["sadness"]
    dominant_emotion = max(anger_score, disgust_score, fear_score, joy_score, sadness_score)
    
    if dominant_emotion == anger_score:
        dominant_emotion = 'anger'
    elif dominant_emotion == disgust_score:
        dominant_emotion = 'disgust'
    elif dominant_emotion == fear_score:
        dominant_emotion = 'fear'
    elif dominant_emotion == joy_score:
        dominant_emotion = 'joy'
    elif dominant_emotion == sadness_score:
        dominant_emotion = 'sadness'


    return {'anger': anger_score, 'disgust': disgust_score, 'fear': fear_score, 'joy': joy_score, 'sadness': sadness_score, 'dominant_emotion': dominant_emotion}