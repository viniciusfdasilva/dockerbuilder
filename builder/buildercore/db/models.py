from django.db import models
from docker import Docker

class Environment(models.Model):
    container_name = models.UUIDField()
    status         = models.BooleanField(default=True)
    name           = models.TextField()

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
        print("==================================================================================")
        print("ENVIRONMENT NAME           |        CONTAINER NAME               |       STATUS")
        print("==================================================================================")

        for environment in environments:
            name = environment.name
            status_icon = "🟢 Active" if environment.status else "🔴 Stopped"
            repeat = (11-len(name)) * '.'
            print(f"{name[0:11]}{repeat}               {environment.container_name}      {status_icon}")

        print("==================================================================================")


    class Meta:
        db_table = "environment"
# Create your models here.
