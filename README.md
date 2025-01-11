# pypass

A script to generate passwords locally with Python's `secrets` module.

# Instructions

1. Clone this repository and go inside.

```bash
git clone https://github.com/davidherszenhaut/pypass.git
cd pypass
```

2. Run the script. Refer to the [Arguments](#arguments) section for more options.

```bash
python pypass.py
```

# Arguments

| Argument            | Effect                                                             |
| --------            | ------                                                             |
| `--length`, `-l`    | Allows the user to choose the length of the password.              |
| `--times`, `-t`     | Allows the user to generate multiple passwords at once.            |
| `--separator`, `-s` | Allows the user to choose the separator character for passphrases. |

# FAQ

* Why Python?

It comes pre-installed on the operating systems I commonly use and it had been a minute since I wrote something in Python.

* Is this cryptographically secure?

According to [Python's documentation](https://docs.python.org/3/library/secrets.html): The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.