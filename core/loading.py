from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn
import time

def loading(text="Initializing MrScan..."):

    with Progress(
        SpinnerColumn(),
        TextColumn("[cyan]{task.description}"),
        BarColumn(),
        transient=True
    ) as progress:

        task = progress.add_task(text, total=100)

        while not progress.finished:
            progress.update(task, advance=2)
            time.sleep(0.02)
