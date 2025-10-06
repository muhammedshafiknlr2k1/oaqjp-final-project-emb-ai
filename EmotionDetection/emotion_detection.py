import requests
import json
def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = input_json, headers=header)
    formatted_response = json.loads(response.text)
    
    if response.status_code == 200:
        return formatted_response
    elif response.status_code == 400:
        formatted_response = {
                            'anger': None, 'disgust': None, 
                            'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}
        return formatted_response
