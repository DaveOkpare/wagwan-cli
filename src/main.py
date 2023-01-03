import typer

from config import explanation_response

app = typer.Typer()


@app.command("explain", help="Explains a Python script")
def explain_script(
    path: str, start_at: int = typer.Option(None), end_at: int = typer.Option(None)
):
    response = explanation_response(path, start_at, end_at)
    print(response)


@app.command("convert", help="Explains a bug")
def explain_bug(item: str):
    print(f"Creating item: {item}")


if __name__ == "__main__":
    app()
