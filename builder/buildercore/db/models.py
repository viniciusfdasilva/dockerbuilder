from django.db import models
from docker import Docker

class Environment(models.Model):
    container_name = models.UUIDField()
    status         = models.BooleanField(default=True)
    name           = models.TextField()

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
        print("=================================================================")
        print("ENVIRONMENT NAME    |       CONTAINER NAME       |       STATUS")
        print("=================================================================")

        for environment in environments:
            
            status_icon = "🟢 Active" if environment.status else "🔴 Stopped"
            print(f"{environment.name}    {environment.container_name}    {status_icon}")

        print("=================================================================")


    class Meta:
        db_table = "environment"
# Create your models here.
