import typer

from .test_utils import OpenAI

app = typer.Typer()


@app.command("login", help="Initializes OpenAI")
def login():
    OpenAI().initialize_openai()


@app.command("explain", help="Explains a Python script.")
def explain_script(
    path: str, start_at: int = typer.Option(None), end_at: int = typer.Option(None)
):
    response = OpenAI(path, start_at, end_at).explain()
    print(response)


@app.command("convert", help="Converts script from one language to another.")
def convert_script(
    path: str,
    initial: str,
    final: str,
    start_at: int = typer.Option(None),
    end_at: int = typer.Option(None),
):
    response = OpenAI(path, start_at, end_at).convert(initial, final)
    print(response)
