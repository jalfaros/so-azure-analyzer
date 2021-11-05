import json, os, requests

subscription_key = "245f37d21cbc451c9bfc6e01f4f8e6bf"

face_api_url = "https://face-api-python-so.cognitiveservices.azure.com/" + 'face/v1.0/detect'

image_url = 'https://thumbs.dreamstime.com/z/retrato-el-suyo-%C3%A9l-ella-persona-confusa-descontenta-hosca-decepcionada-preciosa-atractiva-dos-aislada-personas-confusas-hoscas-155490519.jpg'

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    #'detectionModel': 'detection_03',
    #'returnFaceId': 'true',
    'returnFaceAttributes': 'age,gender,emotion'
}

response = requests.post(face_api_url, params=params,
    headers=headers, json={"url": image_url})
print(json.dumps(response.json(), indent=4, sort_keys=True))