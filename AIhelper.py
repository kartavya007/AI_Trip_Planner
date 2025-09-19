import google.generativeai as genai

genai.configure(api_key="AIzaSyAiBiJ13IeCAvXm5vo-RDamqUs8_utC8-M")
model = genai.GenerativeModel('gemini-2.5-flash')
response = model.generate_content(
            [
                """
                hi
                """
            ]
        )
print(response.text) 
