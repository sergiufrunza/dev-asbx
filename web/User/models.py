# from django.db import models
# from Trusts.models import Disease, JobIndustry, State, Trust
#
#
# class Client(models.Model):
#     CHOICESSMOKER = [('yes', 'Yes'), ('no', 'No'), ('unknown', 'Unknown')]
#     CHOICES = [('yes', 'Yes'), ('no', 'No')]
#     CHOICESVICTIM = [('i was exposed', 'self'), ('family member', 'family member')]
#     token = models.CharField(max_length=60, unique=True)
#     disease = models.ForeignKey(Disease, on_delete=models.CASCADE)
#     victim = models.CharField(max_length=30, choices=CHOICESVICTIM, default='self')
#     lives = models.CharField(max_length=5, choices=CHOICES, default='yes')
#     industries = models.ManyToManyField(JobIndustry, blank=True, symmetrical=False)
#     additional_info = models.TextField(blank=True)
#     deceased = models.CharField(max_length=25, blank=True, null=True)
#     diagnosed = models.CharField(max_length=20, blank=True, null=True)
#     phone = models.CharField(max_length=20)
#     smoker = models.CharField(max_length=10, choices=CHOICESSMOKER, default='unknown')
#     work_state = models.ManyToManyField(State, symmetrical=False, blank=True, related_name="work_state")
#     resident_state = models.ForeignKey(State, on_delete=models.PROTECT,related_name="resident_state")
#     trusts = models.ManyToManyField(Trust, symmetrical=False, blank=True)
#     verdict_ir = models.BigIntegerField(default=0, editable=True)
#     verdict_avg = models.BigIntegerField(default=0, editable=True)
#     verdict_er = models.BigIntegerField(default=0, editable=True)
#
#     def __str__(self):
#         return self.phone
