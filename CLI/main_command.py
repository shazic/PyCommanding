from argparse import ArgumentParser
from CLI.arguments import Arguments
from CLI.logging import Logger

__version__ = '0.1.1'

__all__ = [
    'MainCommand',
    'run'
]

class MainCommand():

    ARGPARSE_KEYWORD_PARAMETERS = {
        "action",
        "const",
        "type",
        "required",
        "nargs",
        "help",
        "default",
        "choices",
        "metavar",
        "dest"
    }

    def __init__(self, commandExecuterClass, argumentsClassList, description = None):
        self.commandExecuterClass = commandExecuterClass
        self.description          = description
        self.args                 = self.setArgs(argumentsClassList)

    def setArgs(self, argumentsClassList):
        try:
            options = Arguments(argumentsClassList).getArgDetails()
            parser  = ArgumentParser(description = self.description)
        except Exception as e:
            self.log("ERROR", f"{e}")
            return None

        for option in options:
            parser = self.setArgument(parser, option)
            if not parser:
                return None

        return parser.parse_args()

    def setArgument(self, parser, option):
        try:
            parser = self.addArgument(parser, option)
        except Exception as e:
            self.log("ERROR", f"{e}")
            return None
        return parser

    def addArgument(self, parser, option):

        positionalParameters = self.getPositionalParams(option)
        keywordParameters    = self.getKeywordParameters(option)

        parser.add_argument(*positionalParameters, **keywordParameters)
        return parser

    def getPositionalParams(self, option):
        positional = []
        for key, value in option.items():
            if key == None or key not in self.ARGPARSE_KEYWORD_PARAMETERS:
                positional.append(value)

        return positional

    def getKeywordParameters(self, option):
        keywordParams = {}
        for key in self.ARGPARSE_KEYWORD_PARAMETERS:
            keywordParams[key] = option[key] if key in option else None
        return keywordParams

    def execute(self):
        if not self.args:
            return None

        return self.commandExecuterClass(self.args).execute()

    def log(self, loglevel, loginfo, logfile=None):
        Logger(loglevel, loginfo, logfile).log()

def run(commandExecuterClass, argumentsClassList, commandDescription = None):
    return MainCommand(commandExecuterClass, argumentsClassList, commandDescription).execute()