from django.db import models

# Create your models here.

class tbl_account_info(models.Model):
    client_name = models.CharField(max_length=200, null=True)
    status = (
        ('pending', 'PENDING'),
        ('active', 'ACTIVE'),
        ('acquired', 'ACQUIRED')
    )
    account_status = models.CharField(choices=status,max_length=200, null=True)

    status1 = (
        ('IT', 'IT AND SERVICES'),
        ('Services', 'SERVICES'),
        ('others', 'OTHERS')
    )
    industry_status = models.CharField(choices=status1,max_length=200, null=True)
    Account_owner = models.CharField(max_length=128)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    created_by=models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.client_name


class Contact(models.Model):
    # title=models.CharField(max_length=200, null=True)
    # First_Name=models.CharField(max_length=200, null=True)
    # Last_Name=models.CharField(max_length=200, null=True)
    name=models.CharField(max_length=200, null=True)
    # status2 = (
    #     ('pending', 'PENDING'),
    #     ('active', 'ACTIVE'),
    #     ('acquired', 'ACQUIRED'),
    # )
    # contact_status = models.CharField(max_length=200, null=True, choices=status2)
    CIDN=models.IntegerField()

    price = models.FloatField(null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    account=models.ForeignKey('tbl_account_info',on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.name


