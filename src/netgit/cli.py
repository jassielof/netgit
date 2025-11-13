import cyclopts

app = cyclopts.App(
    name="netgit",
    usage="NET-Git is a Git-based .NET tool manager CLI.",

)
app.register_install_completion_command()

