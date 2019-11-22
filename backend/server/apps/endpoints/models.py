from django.db import models

# Create your models here.

class Endpoint(models.Model):
    '''
    The Endpoint object represents ML API endpoint.
    '''
    name = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)


class MLAlgorithm(models.Model):
    '''
    The MLAlgorithm represents the ML algorithm object.
    '''
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=1000)
    code = models.CharField(max_length=100000)
    version = models.CharField(max_length=128)
    owner = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)


class MLAlgorithmStatus(models.Model):
    '''
    The MLAlgorithmStatus represents the status of the MLAlgorithm which can change over time.
    '''
    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE, related_name= 'status')


class MLRequest(models.Model):
    '''
    The MLRequest will keep information about all requests to ML algorithms.
    '''
    input_data = models.CharField(max_length=100000)
    full_response = models.CharField(max_length=100000)
    response = models.CharField(max_length=100000)
    feedback = models.CharField(max_length=100000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MLAlgorithm, on_delete=models.CASCADE)
    

