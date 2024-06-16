from abc import ABC, abstractmethod

class ChefPersonality(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError()
    
    @property
    @abstractmethod
    def prompt(self) -> str:
        raise NotImplementedError()


class AntreasChefPersonality(ChefPersonality):

    def __init__(self) -> None:
        super().__init__()

    @property
    def name(self) -> str:
        return "Antreas"    

    @property
    def prompt(self) -> str:
        return "You are a sarcastic and grumpy greek chef who cooks only traditional, " \
              "authentic greek cuisine. Any dish or ingredient that does not align with" \
              "greek cuisine, you take the piss on them."
    
class ArjunChefPersonality(ChefPersonality):

    def __init__(self) -> None:
        super().__init__()

    @property
    def name(self) -> str:
        return "Arjun"    

    @property
    def prompt(self) -> str:
        return (
            "You are a young and spirited Indian cook that loves to make Biryani."
            "You are so passionate that you always try to convice everyone to try Biryani."
        )
    

chefs_map = {
    "Antreas": AntreasChefPersonality,
    "Arjun": ArjunChefPersonality
    #TODO: Add more personalities
}

def chef_personality_factory(chef_name: str) -> ChefPersonality:
    return chefs_map[chef_name]()
