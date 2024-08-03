def parse_input(user_input):
    parts = user_input.strip().split(maxsplit=1)
    command = parts[0].lower()
    args = parts[1] if len(parts) > 1 else ""
    args = args.split()
    return command, args
