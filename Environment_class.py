class Environment:

    def __init__(self, t_env, color_env, character_env  ):
        self.t_env = t_env
        self.color_env = color_env
        self.character_env = character_env

    def __str__(self):
        return f"{self.t_env}, {self.color_env} is a part of {self.character_env}"