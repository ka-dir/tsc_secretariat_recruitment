from django.db import models


# Create your models here.


class Advert(models.Model):
    CATEGORY_CHOICES = (
        ('0', 'EXTERNAL'),
        ('1', 'INTERNAL'),
    )
    IS_CLOSED_CHOICES = (
        ('0', 'OPEN'),
        ('1', 'CLOSED'),
        ('3', 'DRAFT'),
    )

    CATEGORY_TARGET_GROUP_CHOICES = (
        ('0', 'SECRETARIATS'),
        ('1', 'TEACHERS'),
    )
    TERM_OF_SERVICE_CHOICE = (
        ('0', 'PERMANENT'),
        ('1', 'CONTRACT'),
        ('2', 'INTERN'),
    )

    PAY_TYPE = (
        ('0', 'MONTHLY'),
        ('1', 'YEARLY'),
    )

    advert_no = models.CharField(max_length=20, db_index=True, unique=True)
    post_vacancy = models.CharField(max_length=100, blank=True, null=True)
    no_of_post = models.IntegerField(blank=True, null=True)
    closing_date = models.DateTimeField(blank=True, null=True)
    category = models.CharField(max_length=15, blank=True, null=True, db_index=True, choices=CATEGORY_CHOICES)
    job_description = models.TextField(blank=True, null=True)
    duties_responsibilities = models.TextField(blank=True, null=True)
    job_requirements = models.TextField(blank=True, null=True)
    pay_type = models.CharField(max_length=30, blank=True, null=True, choices=PAY_TYPE)
    currency = models.CharField(max_length=10, default='Ksh')
    basic_salary = models.CharField(max_length=100, blank=True, null=True)
    house_allowance = models.CharField(max_length=100, blank=True, null=True)
    commuter_allowance = models.CharField(max_length=100, blank=True, null=True)
    leave_allowance = models.CharField(max_length=100, blank=True, null=True, default='As provided in TSC Secretariat')
    medical_scheme = models.CharField(max_length=100, blank=True, null=True,
                                      default='As provided in the TSC Secretariat Medical Scheme')
    is_closed = models.CharField(max_length=10, blank=True, null=True, choices=IS_CLOSED_CHOICES)
    category_target_group = models.CharField(max_length=10, blank=True, null=True,
                                             choices=CATEGORY_TARGET_GROUP_CHOICES)
    term_of_service = models.CharField(max_length=70, blank=True, null=True, choices=TERM_OF_SERVICE_CHOICE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_vacancy
