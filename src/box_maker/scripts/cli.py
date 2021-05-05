import click
import box_maker


@click.command()
@click.option('--width', '-w', default=640, type=int, show_default=True,
              help='The width of generated image.')
@click.option('--height', '-h', default=640, type=int, show_default=True,
              help='The height of generated image.')
@click.option('--num-of-images', '-n', default=100, type=int, show_default=True,
              help='The number of images will be generated.')
@click.option('--num-of-categories', '-c', default=10, type=int,
              help='The number of categories.')
@click.option('--num-of-instances-per-category', default='[100]', show_default=True,
              help='Repeated number for each category. e.g. if num-of-categories is 8, '
                   'and this option is [1, 3 ,2], then the number of '
                   'instance for each category will be [1, 3, 2, 1, 3, 2, 1, 3]')
@click.option('--type', '-t', default='PASCAL', show_default=True,
              type=click.Choice(['PASCAL'], case_sensitive=False))
@click.option('--seed', default=0, show_default=True, type=int, help='Random seed.')
@click.option('--output-path', '-o', default='./', type=str, show_default=True)
@click.option('--verbose', '-v', is_flag=True, help='Increase output verbosity')
def entry(**kwargs):
    """box-maker command line."""
    bm = box_maker.BoxMaker(
        **kwargs,
    )
    bm.hello()
    print('kwargs', kwargs, kwargs['height'])


@click.command()
def test():
    """box-maker command line."""
    bm = box_maker.BoxMaker()
    bm.test()
