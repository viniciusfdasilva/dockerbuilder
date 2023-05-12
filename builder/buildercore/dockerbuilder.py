import argparse, os, sys, django
from templates import Languanges, WebFullStack

sys.dont_write_bytecode = True

# Django specific settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import Environment 


parser = argparse.ArgumentParser(prog="DockerBuilder", add_help=True)

usages = parser.add_argument_group("usages")

usages.add_argument("-l", "--list",  action="store_true" , help="List all environments avaliable", required=False)
usages.add_argument("-S", "--start", help="Start system environment",   required=False)
usages.add_argument("-s", "--stop",  help="Stop system environment",    required=False)
usages.add_argument("-r", "--rm",    help="Remove system environment", required=False)
usages.add_argument("-n", "--navigate", help="Navigate inside the environment", required=False)

createenv = parser.add_argument_group("createenv")

createenv.add_argument("-o", "--option", choices=["clike", "java", "python", "ruby"], required=False)
#fullstack_package = parser.add_argument_group("WebStack", "")

#fullstack_package.add_argument("-d","--db", type=str, required=False)
#fullstack_package.add_argument("-w", "--webserver", type=str, required=False)
#fullstack_package.add_argument("-f", "--framework", type=str, required=False)
#fullstack_package.add_argument("-e", "--env_name", type=str, required=False)

args = parser.parse_args()

languanges_and_softwares = {
                                "clike"  : Languanges.CLike(), 
                                "java"   : Languanges.Java(), 
                                "python" : Languanges.Python(),
                                "ruby"   : Languanges.Ruby()
                            }

webfullstack_databases  = {
                                "postgres" : WebFullStack.Postgres(), 
                                "mysql"    : WebFullStack.Mysql()
                          }

webfullstack_webservers = {
                                "apache" : WebFullStack.Apache(), 
                                "nginx"  : WebFullStack.Nginx()
                          }

webfullstack_frameworks = {"django" : WebFullStack.Django()}

if args.option:

    name = input("Please enter environment name: ")
    languanges_and_softwares.get(args.option).install(name, args.option)

if args.navigate:
    Environment.navigate(args.navigate)

if args.start:
    Environment.start_environment(args.start)

if args.list:
    Environment.list_environments()

if args.rm:
    Environment.rm_environment(args.rm)

if args.stop:
    Environment.stop_environment(args.stop)
#else:
#
#    webfullstack_databases.get(args.db).install(args.name)
#    
#    webfullstack_webservers.get(args.webserver).install(args.name)
#    webfullstack_frameworks.get(args.framework).install(args.name)
