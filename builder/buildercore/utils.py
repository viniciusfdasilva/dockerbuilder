from tqdm import tqdm
from time import sleep



class PythonAguments():

    arguments_list = []

    def __init__(self, arguments) -> None:
        
        argument_help = arguments.get("help")
        
        if argument_help:

            arguments.append({"args" : {"arg_words" : ["--help", "-h"], "required": False, "options": " "}})

        self.arguments_list = arguments

    def add_argument(self, arguments):
        self.argument = self.arguments_list + arguments

    def argument_help(self):
        
        line_command = "dockerbuilder "
        for argument in self.arguments_list:
            
            required    = argument.get("args").get("required")
            arg_words   = argument.get("args").get("arg_words")
            arg_options = argument.get("args").get("options")

            if required:

                for word in arg_words:
                    for arg_option in word:
                        line_command += f"({arg_option} "  
                    line_command += ")"
                line_command += arg_options
            else:

                for word in arg_words:
                    line_command = "[ "
                    for arg_option in word:
                        line_command += f"({arg_option} "  
                    line_command += ")"
                
                line_command = " ]"
                line_command += arg_options,
        
        return line_command

class Utils():

    @staticmethod
    def get_progress():
        for i in tqdm(range(100)):
            sleep(0.1)
        
