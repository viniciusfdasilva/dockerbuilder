import os, uuid
from tqdm import tqdm
from time import sleep

print("Opções:\n")
print("[1] C/C++")
print("[2] Java")


option_selected = int(input("Choose options:\n"))

if option_selected == 2:

    openjdk_versions = {1 : "openjdk8", 2: "openjdk11", 3: "openjdk17"}
    
    print("[1] openjdk8")
    print("[2] openjdk11")
    print("[3] openjdk17")

    openjdk_version_selected = int(input("Type openjdk version:"))

environment_name = input("Type environment name: \n")

def build_environment(dependences_list, environment_name):
    
    dependences_installed_error = []

    print(f"Building system environment : [{environment_name}]")

    container_name = str(uuid.uuid4())

    environment_response_created = os.system(f"docker create -t -i --name {container_name} alpine > /dev/null")
    environment_response_started = os.system(f"docker start {container_name} > /dev/null")

    if environment_response_created == 0 and environment_response_started == 0:

        print("\nPlease! Wait a moment!!")
        print("Building container:") 

        for i in tqdm(range(100)):    

            if i == 1:
                for dependence in dependences_list:

                    os.system(f"docker exec -it {container_name} apk add {dependence} > /dev/null") 
            
            sleep(0.1)
        
        num_dependences_to_install    = len(dependences_list)
        num_dependences_not_installed = len(dependences_installed_error)

        num_installed_dependences     = (num_dependences_to_install-num_dependences_not_installed)

        if num_installed_dependences == num_dependences_to_install:
            print(f"Environment {environment_name} builded succesfully!")
            print("0 erros reported!")


            print(f"Container name {container_name}")

            os.system(f"docker exec -it {container_name} sh")

        else:
            print(f"Enviroment {environment_name} builded with erros!\n")
            print(f"{num_installed_dependences} dependences installed")
            print(f"{len(dependences_installed_error)} dependences not installed\n")

            print("Dependences with erros:")
            for fail_dependence in dependences_installed_error:
                print(fail_dependence)

    else:
        print("Enviroment could not be started!")
        exit(0)

if option_selected == 1:
    build_environment(["c++", "g++"], environment_name)
else:
    build_environment([openjdk_versions.get(openjdk_version_selected)], environment_name)



