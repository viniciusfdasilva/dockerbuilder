import os
import uuid
from time import sleep
from utils import Utils

class Docker():

    @staticmethod
    def stop(container_name):
        return os.system(f"docker stop {container_name}")

    @staticmethod
    def create_container():
        container_name = str(uuid.uuid4())

        environment_response_created = os.system(f"docker create -t -i --name {container_name} alpine > /dev/null")
        environment_response_started = os.system(f"docker start {container_name} > /dev/null") 

        return container_name if environment_response_created == 0 and environment_response_started == 0 else None

    @staticmethod
    def build_environment(packages, commands, container_name, environment_name):
        
        os.system(f"docker exec -it {container_name} apk add figlet > /dev/null")
        os.system(f"docker exec -it {container_name} apk add ruby > /dev/null")
        os.system(f"docker exec -it {container_name} gem install lolcat > /dev/null")

        print("\nPlease! Wait a moment!!")
        print("Building container:") 
        print(f"Installing {len(packages)} packages\n")

        list_packages_not_installed = []
        i = 1

        if packages:


            for package in packages:

                print(f"Installing {package} ({i}/{len(packages)})")
                Utils.get_progress()   
                response = os.system(f"docker exec -it {container_name} apk add {package} > /dev/null")

                i += 1

                if response != 0:

                    list_packages_not_installed.append(package)

        if commands:

            for command in commands:
                
                print(f'Executing "{package}" command')
                Utils.get_progress()   
                response = os.system(f"docker exec -it {container_name} apk add {command} > /dev/null")

                if response != 0:

                    list_packages_not_installed.append(package)

        packages_to_install    = len(packages)
        packages_not_installed = len(list_packages_not_installed)
        packages_installed     = (packages_to_install-packages_not_installed)
        
        if packages_installed == packages_to_install:
            
            print(f"Environment {environment_name} builded succesfully!")
            print("0 erros reported!")

            print(f"Container name {container_name}")

            os.system(f'docker exec -it {container_name} echo "Welcome to:" | lolcat -a -s 95')
            os.system(f'docker exec -it {container_name} figlet "Docker Builder!" | lolcat -a -s 95')
            os.system(f'docker exec -it {container_name} echo "Version: 0.1" | lolcat -a -s 95')
            os.system(f'docker exec -it {container_name} echo "Author: Vinicius F. da Silva" | lolcat -a -s 95')
            os.system(f"docker exec -it {container_name} fish")
        
        else:
            
            print(f"Enviroment {environment_name} builded with erros!\n")
            print(f"{packages_installed} dependences installed")
            print(f"{packages_not_installed} dependences not installed\n")
            print("Dependences with erros:")
            
            for fail_dependence in list_packages_not_installed:
                print(fail_dependence)