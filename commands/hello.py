def hello(args):
    print(f"Hello, {args}!")

def register(register_command):
    register_command(
        name="hello",
        func=hello,
        description="Say hello with an optional name.",
        devmode=False
    )
