class GameStateManager:
    def __init__(self, state):
        self.state = state
        self.level = None

    def get_state(self) -> tuple:
        return self.state, self.level

    def set_state(self, new_state):
        self.state = new_state

    def set_level(self, new_level):
        if self.state != "level":
            self.set_state("level")
        self.level = new_level
