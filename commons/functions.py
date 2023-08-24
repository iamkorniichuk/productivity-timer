from django.db import models
from django.db.models.functions import Concat, Cast
from django.db.models.lookups import Exact


class NonAggregateCount(models.Count):
    """Doesn't aggregate rows, unlike built-in Count function"""

    contains_aggregate = False


class TimeUnitToDuration(Cast):
    """Converts text fields to duration using Cast function.
    Expresses 'quarter' as '3 months.'"""

    def __init__(self, expression, output_field=models.DurationField()):
        expression = models.Case(
            models.When(Exact(expression, "quarter"), then=models.Value("3 months")),
            default=Concat(
                models.Value("1 "),
                expression,
            ),
        )
        super().__init__(expression, output_field)


class StartOf(models.Func):
    """Accepts 'kind' argument as field, unlike built-in Trunc function."""

    def as_postgresql(self, compiler, connection):
        return super().as_sql(compiler, connection, function="DATE_TRUNC")


class EndOf(StartOf):
    """Returns start of the next time unit's cycle."""

    def __init__(self, *expressions, output_field=None, **extra):
        expressions = list(expressions)
        expressions[1] += TimeUnitToDuration(expressions[0])
        super().__init__(*expressions, output_field=output_field, **extra)
