from os.path import join
from pkg_resources import resource_filename


def __header():
    """Read header in from package data

    :return:
    """
    header_filename = resource_filename(
        'cad', join('data/dxf', 'header.dxf'))
    with open(header_filename, 'r') as header_file:
        return header_file.read()


def grid_header():
    """Generate grid header text for DXF file.

    :return:
    """
    return __header()


def grid(laser_beam_width, diameter):
    """Generate DXF text describing asymmetrical circles grid.

    :param laser_beam_width:
    :param diameter:
    :return:
    """
    width = 3
    height = 11
    horizontal_space = diameter,
    vertical_space = 1.5 * diameter
    # TODO
    return 'grid string'


def legend_filename(grid_filename):
    """Generate legend filename corresponding to `grid_filename`.

    :param grid_filename:
    :return:
    """
    # TODO
    return 'legend.dxf'


def legend_header():
    """Generate legend text for DXF file.

    :return:
    """
    return __header()


def legend(laser_beam_width, total_line_width):
    """Generate DXF text describing legend.

    :param laser_beam_width:
    :param total_line_width:
    :return:
    """
    # TODO
    return 'legend'
