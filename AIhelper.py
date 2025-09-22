import google.generativeai as genai
from Currency import get_currency_by_country
from FileHandel import FileHandel

class AiHelper:
    def __init__(self):
        genai.configure(api_key="AIzaSyBHnvwf6EGYrQDXnd7nSB4Ea7A0d92AOCc")
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    def generate_suggestions(self, country, interest, budget, days):
        prompt = f"You are a Experience Curator with 40 years of experience in crafting personalized travel recommendations based on destination, interests, budget, and schedule. Suggest multiple travel options (at least 8 can be more) for someone interested in visiting {country}, with a focus on {interest} areas, a budget of {get_currency_by_country(country)}{budget} (each person), and a duration of {days} days. Include brief descriptions, estimated costs, and key highlights for each option so the traveler can choose."
        response = self.model.generate_content(
            prompt
        )
        print(response.text)
        # print(prompt)

    def generate_itinerary(self, destination, days, interests):
        prompt = f"Create a {days}-day travel itinerary for {destination} focusing on {interests}. Include activities, dining, and sightseeing."
        response = self.model.generate_content(prompt)
        return response.text
     