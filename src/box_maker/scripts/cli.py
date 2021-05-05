import click
import box_maker

@click.command()
def entry():
    """box-maker command line."""
    bm = box_maker.BoxMaker()
    bm.hello()
