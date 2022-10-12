# Setting Up Your Programming Environmen

1. Install [HombreBrew](https://brew.sh) for MacOS

    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"s
    ```

2. Install Pyenv:

    ```bash
    brew update
    brew install pyenv
    ```

    Set up your shell environment for Pyenv

    bash:

    ```bash
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
    echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
    ```

    zsh:

    ```bash
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
    echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
    echo 'eval "$(pyenv init -)"' >> ~/.zshrc
    ```

3. Install Python version

    ```bash
    pyenv install 3.10.7
    ```

4. Switch to Python version

    ```bash
    pyenv global 3.10.7
    ```

    Now you can run on your terminal `python --version` and it should print `3.10.7`.

5. Create virtual environment

    ```bash
    pyenv virtualenv 3.10.7 tutoring
    ```

6. Install [PyCharm](https://www.jetbrains.com/pycharm/)

7. Configure Python virtual environment on PyCharm. Go to PyCharm>Preferences>Python Interpreter>Add Interpreter>Pyenv Environment and search for something like /Users/<mac_user>/.pyenv/versions/tutoring/bin/python

8. Create and run `hello_world.py` file to check everything is working as expected. Create a new file `hello_world.py` with the following content:

    ```python
    print("Hello World")
    ```

    Go to your terminal and run `python hello_world.py` and it should print `Hello World`. You can also run it from PyCharm with the green arrow.

    >It's best to use lowercase letters and underscores for spaces in files and folder names, because Python uses there naming convections.
    