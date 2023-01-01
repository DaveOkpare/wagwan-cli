import os
import re

import openai
import typer
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.getcwd()
ENV_PATH = os.path.join(BASE_DIR, ".env")
KEY = "OPEN_AI_KEY"


class OpenAI:
    def __init__(self, file_path=None, starts_at=None, ends_at=None):
        self.file_path = file_path
        self.starts_at = starts_at
        self.ends_at = ends_at

    @staticmethod
    def read_file(path: str, start_line: int = None, end_line: int = None):
        with open(path, "r") as f:
            data = f.readlines()

            if start_line is None:
                start_at = 0
            if end_line is None:
                end_at = len(data)
            else:
                start_at = start_line - 1
                end_at = end_line

            line_number = range(start_at, end_at)
            lines = []

            for i, line in enumerate(data):
                if i in line_number:
                    lines.append(line)
                elif i > line_number[-1]:
                    break
        output = "".join(lines)
        return output

    def generate_prompt(self, file_path, start_at, end_at):
        file_input = self.read_file(file_path, start_at, end_at)
        prompt = "# Python 3 \n"
        prompt += file_input
        prompt += "\n\n# Explanation of what the code does\n\n#"
        return prompt

    def explain_prompt(self, file_path, start_at, end_at):
        file_input = self.read_file(file_path, start_at, end_at)
        prompt = file_input
        prompt += '\n\n"""\nHere\'s what the above code is doing:\n1. '
        return prompt

    def get_response(self):
        response = openai.Completion.create(
            model="code-davinci-002",
            prompt=self.generate_prompt(self.file_path, self.starts_at, self.ends_at),
            temperature=0,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["\n\n#"],
        )
        output = response["choices"][0]["text"]
        clean_output = re.sub(r"#", "", output)
        return clean_output


def get_key():
    key = typer.prompt("Enter your OpenAI API Key")
    if key is None:
        get_key()
    else:
        # openai.api_key = key
        with open(ENV_PATH, "w+") as f:
            f.write(f"OPENAI_API_KEY={key}")
    return key


def path_exists():
    return os.path.isfile(ENV_PATH)


def initialize_openai():
    if not path_exists():
        key = get_key()
        openai.api_key = key
    else:
        openai.api_key = os.getenv("OPENAI_API_KEY")


def get_response(file_path, start_at, end_at):
    initialize_openai()
    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=OpenAI().generate_prompt(file_path, start_at, end_at),
        temperature=0,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stop=["\n\n#"],
    )
    output = response["choices"][0]["text"]
    clean_output = re.sub(r"#", "", output)
    return clean_output


def explanation_response(file_path, start_at, end_at):
    initialize_openai()
    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=OpenAI().explain_prompt(file_path, start_at, end_at),
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=['"""'],
    )
    output = response["choices"][0]["text"]
    return output
