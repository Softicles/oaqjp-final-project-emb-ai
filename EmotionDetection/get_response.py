import requests, json

def emotion_detector(text_to_analyze) :
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    response = requests.post(url, json = myobj, headers = header)

    if response.status_code == 200:
        return response.text

    return None

def format_output(output_text):

    if output_text != None:
        emotion_prediction = json.loads(output_text)
        emotion_prediction = emotion_prediction["emotionPredictions"][0]["emotion"]
        emotion_prediction["dominant_emotion"] = max(emotion_prediction, key=emotion_prediction.get)
        return emotion_prediction

    return {"anger": None, 
                "disgust": None, 
                "fear": None, 
                "joy": None, 
                "sadness": None, 
                "dominant_emotion": None
            }