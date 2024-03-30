# suv

suv (shared-uv) is cli tool based on [uv](https://github.com/astral-sh/uv) for managing python virtual environments

## Why?

I don't like Conda, Miniconda and other similar tools. I prefer to use virtualenv and venv. But I don't like to create virtual environments in every project. I prefer to use one virtual environment for all projects. So I created suv. I like uv and it's speed. So I used uv for creating suv.

## Configuration

suv uses a configuration file named `suv.json` in the user's home directory. The configuration file is a JSON file. The configuration file has the following fields:

- `venv_path`: The path of the virtual environment. Default is `~/suv-venvs`
- `shell`: The shell to use. Default is `git bash`

## Todo

- [ ] Add Python path to the config
- [ ] Add support for Windows
- [ ] Add support for Mac and Linux
- [ ] Add support for other shells
- [ ] Add support for `pip`
