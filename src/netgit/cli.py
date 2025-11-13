import typer

app = typer.Typer(
    name="netgit",
)


@app.command()
def install(
    git_url: str,
    csproj: str,
    branc: str,
    alias: str,
    dir_path: str,
):
    """
    Install a tool from a git repository
    """
    print("git url:", git_url)


@app.command()
def update():
    pass


@app.command()
def remove():
    pass


@app.command()
def list():
    """
    Docstring for list
    """
    pass
