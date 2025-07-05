from ibm_cloud_sdk_core.api_exception import ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import NaturalLanguageUnderstandingV1


def emotion_detector(text_to_analyze):
    try:
        api_key = "API_KEY"
        url = (
            "https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/"
            "instances/INSTANCE"
        )

        authenticator = IAMAuthenticator(api_key)
        nlu = NaturalLanguageUnderstandingV1(
            version="2022-08-10", authenticator=authenticator
        )
        nlu.set_service_url(url)

        response = nlu.analyze(
            text=text_to_analyze, features={"emotion": {}}
        ).get_result()

        response = response["emotion"]["document"]["emotion"]
        dominant_emotion = max(response, key=response.get)
        response["dominant_emotion"] = dominant_emotion

        return response

    except ApiException:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }
