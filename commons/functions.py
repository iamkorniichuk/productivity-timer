from django.db import models
from django.db.models.functions import Concat, Cast
from django.db.models.lookups import Exact


class NonAggregateCount(models.Count):
    contains_aggregate = False


class TimeUnitToDuration(Cast):
    def __init__(self, expression, output_field=models.DurationField()):
        # TODO: Accept a number of time units
        expression = models.Case(
            models.When(Exact(expression, "quarter"), then=models.Value("3 months")),
            default=Concat(
                models.Value("1 "),
                expression,
            ),
        )
        super().__init__(expression, output_field)


# Accepts kind argument of models.F type unlike built-in function Trunc
class StartOf(models.Func):
    def as_postgresql(self, compiler, connection):
        return super().as_sql(compiler, connection, function="DATE_TRUNC")


class EndOf(StartOf):
    def __init__(self, *expressions, output_field=None, **extra):
        expressions = list(expressions)
        expressions[1] += TimeUnitToDuration(expressions[0])
        super().__init__(*expressions, output_field=output_field, **extra)
