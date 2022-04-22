import logging 
import speech_recognition as sr

r = sr.Recognizer()
mic = sr.Microphone()

def s2t():
    with mic as source:
        r.adjust_for_ambient_noise(source) #雑音対策
        audio = r.listen(source)

    try:
        return r.recognize_google(audio, language='ja-JP')

    # 以下は認識できなかったときに止まらないように。
    except sr.UnknownValueError:
        return "error: could not understand audio"
    except sr.RequestError as e:
        return "error: could not request results from Google Speech Recognition service; {0}".format(e)
