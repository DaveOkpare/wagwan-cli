## Wagwan CLI

A CLI tool that explains code snippets, converts them to other languages, and fixes bugs, built in Python using [OpenAI's Codex.](https://openai.com/blog/openai-codex/)


### Installation

You can install `wagwan` by running the following command in your terminal.

```commandline
pip install "git+https://github.com/DaveOkpare/wagwan-cli"
```

### Usage 

`wagwan` uses [OpenAI's Codex API.](https://openai.com/blog/openai-codex/) To use it, you'll first need to request access from [OpenAI](http://beta.openai.com/codex-waitlist). Once granted access, obtain an API key from your dashboard, and run the following command.

```commandline
wagwan login
```

Once you have configured your environment, run `wagwan --help` to find the various options available.

```commandline
wagwan --help


 Usage: wagwan [OPTIONS] COMMAND [ARGS]...                                                                                                              
                                                                                                                                                        
╭─ Options ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ --install-completion          Install completion for the current shell.                                                                              │
│ --show-completion             Show completion for the current shell, to copy it or customize the installation.                                       │
│ --help                        Show this message and exit.                                                                                            │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Commands ───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╮
│ convert                Converts script from one language to another.                                                                                 │
│ explain                Explains a Python script.                                                                                                     │
│ login                  Initializes OpenAI                                                                                                            │
╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯

```

### License

This project is open-sourced under the MIT license. See the [License](LICENSE) file for more information.