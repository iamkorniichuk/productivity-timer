from itertools import chain


def format_timedelta(timedelta, template="{d} days {H}:{M}:{S}"):
    units = {"d": timedelta.days}
    units["h"], remainings = divmod(timedelta.seconds, 3600)
    units["m"], units["s"] = divmod(remainings, 60)
    justified_units = {}
    for key, value in units.items():
        justified_units[key.upper()] = str(value).rjust(2, "0")
    units |= justified_units
    return template.format_map(units)


def model_to_data(instance, exclude=None):
    opts = instance._meta
    data = {}
    for f in chain(opts.concrete_fields, opts.private_fields, opts.many_to_many):
        if not getattr(f, "editable", False):
            continue
        if exclude and f.name in exclude:
            continue
        data[f.name] = getattr(instance, f.name)
    return data
