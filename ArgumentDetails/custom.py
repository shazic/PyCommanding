class CustomArgument():

    DESCRIBE_CUSTOM_ATTR = "a task"
    DEFAULT_VALUE        = "ship"
    OPTIONS              = ["aeroplane", "truck", "ship"]

    options = [
        {
            # Positional parameters
            "name"      : "--custom",
            "shortname" : "-z",
            # Keyword Parameters
            "required"  : False,
            "nargs"     : "?",
            "help"      : f"Optional custom argument to accomplish {DESCRIBE_CUSTOM_ATTR}",
            "default"   : DEFAULT_VALUE,
            "choices"   : OPTIONS
        }
    ]
