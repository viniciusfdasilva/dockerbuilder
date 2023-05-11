from docker import Docker

import os, sys, django
sys.dont_write_bytecode = True

# Django specific settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import Environment 

class Essentials():

    packages = ["fish", "vim", "nano", "micro"]
       
class Languanges():

    class Python():

        packages = ["python3", "py3-pip"]

        def install(self, environment_name):
            container_name = Docker.create_container()

            

            if container_name:
                
                Environment.objects.get_or_create(container_name=container_name, name=environment_name)

                joined_packages = self.packages + Essentials().packages
                Docker.build_environment(joined_packages, None, container_name, environment_name)
            
    class CLike():

        packages = ["gcc", "g++", "clang", "rust cargo"]

        def install(self, environment_name):
            container_name = Docker.create_container()

            if container_name:
                
                Environment.objects.get_or_create(container_name=container_name,name=environment_name)

                joined_packages = self.packages + Essentials().packages
                Docker.build_environment(joined_packages, None, container_name, environment_name)

    class Java():

        packages = ["openjdk8", "openjdk11", "openjdk17"]

        def install(self, environment_name):
            container_name = Docker.create_container()

            if container_name:
                
                Environment.objects.get_or_create(container_name=container_name,name=environment_name)

                joined_packages = self.packages + Essentials().packages
                Docker.build_environment(joined_packages, None, container_name, environment_name)

    class Ruby():

        packages = ["ruby"]

        def install(self, environment_name):
            container_name = Docker.create_container()

            if container_name:
                
                joined_packages = self.packages + Essentials().packages
                Docker.build_environment(joined_packages, None, container_name, environment_name)
                
class WebFullStack():

    class Postgres():

        packages = ["postgresql", "postgresql-client"]

        def install(self, environment_name):
            container_name = Docker.create_container()

            if container_name:
                
                Environment.objects.get_or_create(container_name=container_name,name=environment_name)

                joined_packages = self.packages + Essentials().packages
                Docker.build_environment(joined_packages, None, container_name, environment_name)

    class Mysql():

        packages = ["mysql", "mysql-client"]

        def install(self, environment_name):
            container_name = Docker.create_container()

            if container_name:

                Environment.objects.get_or_create(container_name=container_name,name=environment_name)

                joined_packages = self.packages + Essentials().packages
                Docker.build_environment(joined_packages, None, container_name, environment_name)

    class Nginx():

        packages = ["nginx"]

        def install(self, environment_name):
            container_name = Docker.create_container()

            if container_name:
                
                Environment.objects.get_or_create(container_name=container_name,name=environment_name)

                joined_packages = self.packages + Essentials().packages
                Docker.build_environment(joined_packages, None, container_name, environment_name)

    class Apache():

        packages = ["apache2"]

        def install(self, environment_name):
            container_name = Docker.create_container()

            if container_name:
                
                Environment.objects.get_or_create(container_name=container_name,name=environment_name)

                joined_packages = self.packages + Essentials().packages
                Docker.build_environment(joined_packages, None, container_name, environment_name)

    class Django():

        packages = ["python3", "py3-pip"]
        commands = ["pip3 install django", "pip3 install env"]

        def install(self, environment_name):
            container_name = Docker.create_container()

            if container_name:

                joined_packages = self.packages + Essentials().packages
                Docker.build_environment(joined_packages, None, container_name, environment_name)
