from django.db import models


class NonAggregateCount(models.Count):
    contains_aggregate = False
