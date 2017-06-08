import configparser

class Configuration:

    def __init__(self, configFile, section):
        self.config = configparser.ConfigParser()
        self.config.read(configFile)
        self.section = section

    def get(self, attribut):
        
        return self.config[self.section][attribut]
