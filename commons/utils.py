# TODO: Fix (doesn't work in admin)
def format_timedelta(timedelta, template="{d} days {H}:{M}:{S}"):
    units = {"d": timedelta.days}
    units["h"], remainings = divmod(timedelta.seconds, 3600)
    units["m"], units["s"] = divmod(remainings, 60)
    justified_units = {}
    for key, value in units.items():
        justified_units[key.upper()] = str(value).rjust(2, "0")
    units |= justified_units
    return template.format_map(units)
