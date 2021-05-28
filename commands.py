import requests
import base64
import random
import json
# from nudenet import NudeClassifier
import os
from datetime import datetime
from termcolor import colored

#nsfw_classifier = NudeClassifier()
animals = ["cat", "dog", "wolf", "otter", "panda"]
muted_people = []

cat_images_api = "https://api.thecatapi.com/v1/images/search"
dog_facts_api = "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1"
trivia_api = "https://opentdb.com/api.php?amount=1&category=9&difficulty=easy&type=boolean&encode=base64"
yoda_api = "http://yoda-api.appspot.com/api/v1/yodish?text="
joke_api = "https://official-joke-api.appspot.com/random_joke"
nasa_image_search_api = "https://images-api.nasa.gov/search?"


def get_json_data(url):
    result = requests.get(url)
    result_json = result.json()
    return result_json


def get_cat_image_url():
    json_object = get_json_data(cat_images_api)
    image_object = json_object[0]
    image_url = image_object["url"]
    return image_url


def decode_base64(string):
    new_string = base64.b64decode(string)
    new_string = new_string.decode("utf-8")
    return new_string


def get_fact():
    fact = ""

    trivia_object = get_json_data(trivia_api)
    results_object = trivia_object["results"]
    first_result_object = results_object[0]

    question_statement = first_result_object["question"]
    question_statement = decode_base64(question_statement)
    question_statement = question_statement[:-1]

    accuracy = first_result_object["correct_answer"]
    accuracy = decode_base64(accuracy)
    accuracy = accuracy.lower()

    if accuracy == "true":
        fact = f"Did you know that {question_statement}?"
    elif accuracy == "false":
        fact = f"Did you know that '{question_statement}' is not true?"

    return fact


def get_animal_command():
    command = f"a!{random.choice(animals)}"
    return command


def get_verification(name):
    result = is_senior(name)
    response = "There was an error"

    if result:
        response = f"{name} is a senior."
    elif not result:
        response = f"{name} is not a senior"

    return response


def is_senior(name):
    with open("Leland Class of 2021.json") as file:
        user_found = False
        name = name.lower()
        student_list = json.loads(file.read())

        for student in student_list:
            student_name = f"{student['First Name']} {student['Last Name']}"
            student_name = student_name.lower()

            if student_name == name:
                user_found = True

        return user_found


def get_batch_verification(list_of_names):
    responses = []
    names = list_of_names

    for name in names:
        response = get_verification(name)
        if response.__contains__("not"):
            responses.append(response)

    return responses


# def check_nsfw_image(url, channel_name):
#     file_path = "nsfw_video.gif"
#
#     get_content(url, file_path)
#
#     result = nsfw_classifier.classify(file_path)
#     is_nsfw = False
#     image_results = result[file_path]
#     unsafe_percent = image_results["unsafe"] * 100
#
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#
#     num = unsafe_percent
#     formatted_num = '{0:.3g}'.format(num)
#
#     print_message = f"The image scanned in {channel_name} channel is {formatted_num}% unsafe. Time: {current_time}"
#
#     if unsafe_percent > 30:
#         print(colored(print_message, 'red'))
#         is_nsfw = True
#     else:
#         print(print_message)
#         is_nsfw = False
#
#     os.remove(file_path)
#
#     return is_nsfw


# def check_nsfw_video(url, channel_name):
#     file_path = "nsfw_video.mp4"
#
#     get_content(url, file_path)
#
#     result = nsfw_classifier.classify_video(file_path)
#     is_nsfw = False
#     video_result = result["preds"]
#
#     total_score = 0
#
#     for frame in video_result:
#         scores = video_result[frame]
#         total_score += scores["unsafe"]
#
#     average_score = total_score / len(video_result)
#
#     num = average_score
#     formatted_num = '{0:.3g}'.format(num)
#
#     now = datetime.now()
#     current_time = now.strftime("%H:%M:%S")
#
#     print_message = f"The video scanned in channel: {channel_name} is {formatted_num}% unsafe. Time: {current_time}"
#
#     if average_score > 30:
#         print(colored(print_message, 'red'))
#         is_nsfw = True
#     else:
#         print(print_message)
#         is_nsfw = False
#
#     os.remove(file_path)
#
#     return is_nsfw


def get_content(url, file_path):
    response = requests.get(url)
    with open(file_path, "wb") as file:
        file.write(response.content)


def get_yoda_speak(sentence):
    url = yoda_api + sentence
    result = get_json_data(url)
    text = result["yodish"]
    text = "Yoda: " + text
    return text


class Joke:
    def __init__(self, setup, punchline):
        self.punchline = punchline
        self.setup = setup


def get_joke():
    joke_json = get_json_data(joke_api)
    joke = Joke(joke_json["setup"], joke_json["punchline"])
    return joke


def get_nasa_image_url(search):
    url = nasa_image_search_api + f"q={search}&media_type=image"
    json_object = get_json_data(url)
    collection = json_object["collection"]
    items = collection["items"]
    item = items[0]
    link = item["links"][0]
    url = link["href"]
    return url

