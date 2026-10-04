# Password Generator

A Python and Tkinter exercise in building a small desktop application.
It generates a password and saves the website, email, and password in a local text file.

## Run locally

Use Python 3 with Tkinter installed.
Run this command from the repository directory:

```sh
python main.py
```

Enter a website and an email address.
Select **Generate Password**, then select **Add**.
The application appends the entry to `data.txt`.

## Current limits

This is a learning project, not a credential manager for real accounts.
It uses Python's `random` module and stores passwords without encryption.
Use invented account details only.

The application does not use `secrets` or create Word documents.
