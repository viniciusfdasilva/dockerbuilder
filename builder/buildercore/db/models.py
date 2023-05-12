from django.db import models
from docker import Docker
from datetime import datetime
from django.core.exceptions import ValidationError
class Environment(models.Model):
    container_name = models.UUIDField()
    status         = models.BooleanField(default=True)
    name           = models.TextField()
    created        = models.DateField(default=datetime.now())
    template       = models.TextField(default="")

    @staticmethod
    def navigate(container_name):
    
        try:
            environment = Environment.objects.filter(container_name=container_name)

            if environment.count() == 0:
                print("Environment doenst exist!")
                exit(1)
            else:
                resp = Docker.navigate(container_name)

                if resp != 0:
                    print("Error!")
                    exit(1)
        except ValidationError as error:
            print("Environment doenst exist!")
            exit(1)

    @staticmethod
    def rm_environment(container_name):

        resp = Docker.stop(container_name)

        if resp == 0:
            environment = Environment.objects.filter(container_name=container_name)

            if environment.count() == 0:
                print("Environment doesnt exist!")
                exit(1)
            else:
                
                Docker.rm(container_name)

                env = environment.first()               
                env.delete()     

                print("Environment removed successfully!")
                exit(0)


    @staticmethod
    def start_environment(container_name):

        resp = Docker.start(container_name)

        if resp == 0:
            environment = Environment.objects.filter(container_name=container_name)

            if environment.count() == 0:
                print("Environment doesnt exist!")
                exit(1)
            else:
                env = environment.first()

                env.status = True
                env.save()     

                print("Environment started successfully!")
                exit(0)

    @staticmethod
    def stop_environment(container_name):

        resp = Docker.stop(container_name)
        
        if resp == 0:
            environment = Environment.objects.filter(container_name=container_name)

            if environment.count() == 0:
                print("Environment doesnt exist!")
                exit(1)
            else:
                env = environment.first()

                env.status = False
                env.save()     

                print("Environment stopped successfully!")
                exit(0)

    @staticmethod
    def list_environments():

        environments = Environment.objects.all()
        print("==================================================================================================================================")
        print("ENVIRONMENT NAME  |  TEMPLATE  |       CREATED         |            CONTAINER NAME            |     IMAGE     |      STATUS")
        print("==================================================================================================================================")

        if environments.count() > 0:
            for environment in environments:
                name = str(environment.name)
                status_icon = "🟢 Running" if environment.status else "🔴 Stopped"
                repeat = (11-len(name)) * '.'

                template = str(environment.template)

                repeat_template = (6-len(template)) * ' '

                print(f"{name[0:11]}{repeat}           {template}{repeat_template}          {environment.created}         {environment.container_name}       Alpine        {status_icon}")

        print("==================================================================================================================================")


    class Meta:
        db_table = "environment"
# Create your models here.
