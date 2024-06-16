import click, os
from dotenv import load_dotenv

from chefgpt.chefgpt import ChefGPT
from chefgpt.chef_personalities import chef_personality_factory, chefs_map

class ChefGPTContext:
    def __init__(self):
        self.current_chef: ChefGPT = None

pass_chef_context = click.make_pass_decorator(ChefGPTContext, ensure=True)

@click.group()
@click.option('--chef', type=click.Choice(list(chefs_map.keys())), prompt='Choose your chef',
              help='Select a chef to assist you.')
@pass_chef_context
def cli(chef_ctx: ChefGPTContext, chef):
    """ChefGPT CLI: Your personal chef assistant"""
    load_dotenv()

    if not os.environ.get("OPENAI_KEY"):
        click.echo("OPENAI_KEY environment variable not set. You can use a .env file for that.")
        exit(1)
    
    api_key = os.environ.get("OPENAI_KEY")
    chef_personality = chef_personality_factory(chef_name=chef)
    chef_gpt = ChefGPT(api_key=api_key, personality=chef_personality)
    chef_ctx.current_chef = chef_gpt
    
    click.echo(f'You have selected Chef {chef_personality.name}!')

@cli.command()
@pass_chef_context
def ask(chef_ctx: ChefGPTContext):
    """Ask your chef anything!"""
    dish = click.prompt('What would you like to ask your Chef?\n', type=str)
    chef = chef_ctx.current_chef
    response = chef.get_recipe_for_dish(dish)
    
    click.echo('==== ChefGPT ====')
    click.echo(response)
