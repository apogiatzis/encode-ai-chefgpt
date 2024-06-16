# Encode - AI Bootcamp - Week 1 Project

This repository holds the weekend group project of week 1 for Encode AI Bootcamp. This is a python package which implements uses OPENAI API and prompt engineering to expose Chef GPT with some configurable personality  traits.

## Group Members' IDs
- **76tsNrC**
- **ipJZCWC**
- **s0qmoqC**
- **3nmWtwC**
- **XLiUjNC**

## Chef Personalities (WIP)

- **Antreas**: A grumpy greek chef who cooks only traditional, authentic greek cuisine. 
- === MORE TO BE ADDED HERE ===

## Get Started

Before runnning the script you need to set your OPENAI API key by setting the `OPENAI_KEY` environment variable.

Instead of a explicitly setting the env var in your terminal e.g. using `export OPENAI_KEY=...` you can also do it using a .env file. See the [.env.example](./.env.example) file for reference.

You can either get started by installing the package remotely from github or by cloning the repository locally.

### Run script by cloning:

Clone the repo
```
git clone https://github.com/apogiatzis/encode-ai-chefgpt && cd encode-ai-chefgpt
```

Make sure that you have poetry installed:
```
pip install -U poetry
```

Install dependencies:
```
poetry install
```

Run ChefGPT
```
poetry run chefgpt --chef <chef_name> ask
```



### Run script by installing package from github remote:

Install package from github
```
pip install git+https://github.com/apogiatzis/encode-ai-chefgpt.git
```

> Note that if you have installed the package using pip from the github remote then you will need to explicitly set OPENAI_KEY in your environment variables

Run ChefGPT
```
OPENAI_KEY="sk-..." chefgpt --chef <chef_name> makerecipe
```

### Uninstall

To uninstall the package run:
```
pip uninstall chefgpt    
```

### How to add more Chef personalities:

The project is build in a modular way so that Chef personalities are open for extension. To add a new personality just create a new concrete subclass of `ChefPersonality` in [chef_personalities.py](./chefgpt/chef_personalities.py) and define the name and prompt properties. 

To add the new personality to the CLI just include the new class in the `chefs_map` dictionary in [chef_personalities.py](./chefgpt/chef_personalities.py)
