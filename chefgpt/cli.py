import click, os
from dotenv import load_dotenv

from chefgpt.chefgpt import ChefGPT
from chefgpt.chef_personalities import chef_personality_factory, chefs_map


class ChefGPTContext:
    def __init__(self):
        load_dotenv()

        self.api_key = os.environ.get("OPENAI_KEY")
        self.current_chef: ChefGPT = None


pass_chef_context = click.make_pass_decorator(ChefGPTContext, ensure=True)


@click.group()
@click.option(
    "--chef",
    type=click.Choice(list(chefs_map.keys())),
    prompt="Choose your chef",
    help="Select a chef to assist you.",
)
@pass_chef_context
def cli(chef_ctx: ChefGPTContext, chef):
    """ChefGPT CLI: Your personal chef assistant"""

    if not chef_ctx.api_key:
        click.echo("OPENAI_KEY environment variable not set.")
        api_key = click.prompt("OPENAI_KEY", type=str)
        chef_ctx.api_key = api_key

    chef_personality = chef_personality_factory(chef_name=chef)
    chef_gpt = ChefGPT(api_key=chef_ctx.api_key, personality=chef_personality)
    chef_ctx.current_chef = chef_gpt

    click.echo(f"[+] You have selected Chef {chef_personality.name}!")


@cli.command()
@pass_chef_context
def ask(chef_ctx: ChefGPTContext):
    """Ask your chef anything!"""
    click.echo(
        "[+] What would you like to ask your Chef? (double new line to finish)\n(you) >>> ", nl=False
    )
    question_lines = []
    while True:
        line = input().strip()
        if len(question_lines) > 0 and question_lines[-1] == '' and line == '' :
            break
        question_lines.append(line)
    question = "".join(question_lines)
    chef = chef_ctx.current_chef
    response = chef.ask_chef(question)

    click.echo(f"({chef.personality.name}) >>> ", nl=False)
    click.echo(response)
