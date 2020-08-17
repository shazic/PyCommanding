from CLI.main_command import run
from App.MainApp import Application
from ArgumentDetails.custom import CustomArgument

commandDescription = """This command prints Hello world on the screen
"""
argumentsClassList = [CustomArgument]

data = run(Application, argumentsClassList, commandDescription)