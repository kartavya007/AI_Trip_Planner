import google.generativeai as genai


class AiHelper:
    def __init__(self):
        genai.configure(api_key="AIzaSyAiBiJ13IeCAvXm5vo-RDamqUs8_utC8-M")
        self.model = genai.GenerativeModel('gemini-2.5-flash')
    
    
