import google.generativeai as genai


class AiHelper:
    def __init__(self):
        genai.configure(api_key="AIzaSyBHnvwf6EGYrQDXnd7nSB4Ea7A0d92AOCc")
        self.model = genai.GenerativeModel('gemini-2.5-flash')
    
    def suggestions(self):
        response = self.model.generate_content(
            "Hi",
        )
        print(response.text)

    def generate_itinerary(self, destination, days, interests):
        prompt = f"Create a {days}-day travel itinerary for {destination} focusing on {interests}. Include activities, dining, and sightseeing."
        response = self.model.generate_content(prompt)
        return response.text
