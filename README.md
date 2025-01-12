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

| Argument            | Help                                                                                                                                                       | Defaults
| --------            | ----                                                                                                                                                       | --------
| `--character`, `-c` | Allows the user to insert a random special character into a random word in the passphrase. Only works with the `passphrase` option of the `kind` argument. | `False`
| `--kind`, `-k`      | Allows the user to choose which kind of password to generate. Options include `passphrase`, `password`, and `pin`.                                         | `passphrase`
| `--length`, `-l`    | Allows the user to choose the length of the password.                                                                                                      | `6` for `passphrase` <br> `12` for `password` <br> `4` for `pin`
| `--quiet`, `-q`     | Allows the user to not print the password to the terminal.                                                                                                 | `False`
| `--repeat`, `-r`    | Allows the user to generate multiple passwords at once.                                                                                                    | `1`
| `--separator`, `-s` | Allows the user to choose the separator character for the passphrase. Only works with the `passphrase` option of the `kind` argument.                      | `(space)`

# FAQ

* Why Python?

It comes pre-installed on the operating systems I commonly use and it had been a minute since I wrote something in Python.

* Is this cryptographically secure?

According to [Python's documentation](https://docs.python.org/3/library/secrets.html): The secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets.