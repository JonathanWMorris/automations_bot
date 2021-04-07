import requests
import base64
import random
import json
from nudenet import NudeClassifier
import os

nsfw_classifier = NudeClassifier()

cat_images_url = "https://api.thecatapi.com/v1/images/search"
dog_facts_url = "https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1"
trivia_url = "https://opentdb.com/api.php?amount=1&category=9&difficulty=easy&type=boolean&encode=base64"
animals = ["cat", "dog", "wolf", "otter", "panda"]


def get_json_data(url):
    result = requests.get(url)
    result_json = result.json()
    return result_json


def get_cat_image_url():
    json = get_json_data(cat_images_url)
    image_object = json[0]
    image_url = image_object["url"]
    return image_url


def decode_base64(string):
    new_string = base64.b64decode(string)
    new_string = new_string.decode("urf-8")
    return new_string


def get_fact():
    fact = ""

    trivia_object = get_json_data(trivia_url)
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


def check_nsfw_image(image_path):
    result = nsfw_classifier.classify(image_path)
    is_nsfw = False
    image_results = result[image_path]
    unsafe_percent = image_results["unsafe"] * 100

    print(f"The image scanned is {unsafe_percent}% unsafe.")

    if unsafe_percent > 50:
        is_nsfw = True

    os.remove(image_path)

    return is_nsfw


def get_image(url, file_name):
    response = requests.get(url)
    with open(file_name, "wb") as file:
        file.write(response.content)
