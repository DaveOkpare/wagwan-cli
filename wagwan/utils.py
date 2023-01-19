import configparser
import os
import re

import openai
import typer

BASE_DIR = os.getcwd()
ENV_PATH = os.path.join(BASE_DIR, ".wagwan")
config = configparser.ConfigParser()
config.read(ENV_PATH)


def path_exists():
    return os.path.isfile(ENV_PATH)


def get_key():
    key = typer.prompt("Enter your OpenAI API Key")
    if key is None:
        get_key()
    else:
        with open(ENV_PATH, "w+") as f:
            f.write("[openai]\n")
            f.write(f"API_KEY={key}")
    return key


class OpenAI:
    def __init__(
        self, file_path: str = None, starts_at: int = None, ends_at: int = None
    ):
        self.file_path = file_path
        self.starts_at = starts_at
        self.ends_at = ends_at

    @staticmethod
    def initialize_openai():
        if not path_exists():
            key = get_key()
            openai.api_key = key
        else:
            openai.api_key = config.get("openai", "API_KEY")

    def read_file(self):
        with open(self.file_path, "r") as f:
            data = f.readlines()

            if self.starts_at is None:
                start_line = 0
            if self.ends_at is None:
                end_line = len(data)
            else:
                start_line = self.starts_at - 1
                end_line = self.ends_at

            line_number = range(start_line, end_line)
            lines = []

            for i, line in enumerate(data):
                if i in line_number:
                    lines.append(line)
                elif i > line_number[-1]:
                    break
        output = "".join(lines)
        return output

    def explain_prompt(self):
        file_input = self.read_file()
        prompt = (
            f"# Python 3 \n{file_input}\n\n# Explanation of what the code does\n\n#"
        )
        return prompt

    def convert_prompt(self, initial, output):
        initial = initial.lower()
        output = output.lower()
        file_input = self.read_file()
        prompt = f"##### Translate this function  from {initial} into {output}\n### {initial}\n    \n    {file_input}\n    \n### {output} "
        return prompt

    def explain(self):
        self.initialize_openai()
        response = openai.Completion.create(
            model="code-davinci-002",
            prompt=self.explain_prompt(),
            temperature=0,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["\n\n#"],
        )
        output = response["choices"][0]["text"]
        response_text = re.sub(r"#", "", output)
        return response_text

    def convert(self, initial, final):
        self.initialize_openai()
        response = openai.Completion.create(
            model="code-davinci-002",
            prompt=self.convert_prompt(initial, final),
            temperature=0,
            max_tokens=1000,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            stop=["###"],
        )
        response_text = response["choices"][0]["text"]
        return response_text.strip()
