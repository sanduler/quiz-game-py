# Ruben Sanduleac
# Description: The data file uses the question bank found from OpenTrivia API.
#              The questions are loaded and passed into the respective classes from
import requests
NUMBER_OF_QUESTIONS = 10

# parameters for the api requested
parameters = {
    "amount": NUMBER_OF_QUESTIONS,
    "type": "boolean",
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = (data["results"])