import argparse, os, sys, django
from templates import Languanges, WebFullStack

sys.dont_write_bytecode = True

# Django specific settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import Environment 


parser = argparse.ArgumentParser(prog="DockerBuilder", add_help=True)

langs_softwares = parser.add_argument_group("Languanges and Softwares", "")

langs_softwares.add_argument("-l", "--list")
#langs_softwares.add_argument("-s", "--stop")
#langs_softwares.add_argument("-o", "--option", type=str, required=True, choices=["clike","java", "python", "ruby"])
#langs_softwares.add_argument("-n", "--name",   type=str, required=True)

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

#if args.option:

#    languanges_and_softwares.get(args.option).install(args.name)

if args.list:
    Environment.list_environments()

#if args.stop:
#    Environment.stop_environment(args.stop)
#else:
#
#    webfullstack_databases.get(args.db).install(args.name)
#    
#    webfullstack_webservers.get(args.webserver).install(args.name)
#    webfullstack_frameworks.get(args.framework).install(args.name)
