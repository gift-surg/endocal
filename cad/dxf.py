from os.path import join, splitext
from pkg_resources import resource_filename


def __header():
    """Read header in from package data.

    :return:
    """
    header_filename = resource_filename(
        'cad', join('data/dxf', 'header.dxf'))
    with open(header_filename, 'r') as header_file:
        return header_file.read()


def __footer():
    """Read footer in from package data.

    :return:
    """
    footer_filename = resource_filename(
        'cad', join('data/dxf', 'footer.dxf'))
    with open(footer_filename, 'r') as footer_file:
        return footer_file.read()


def __format_float(value):
    """Format float in scientific notation, 6 decimal places.

    :param value:
    :return:
    """
    return '{:.6e}'.format(float(value))


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

    # now we shift paradigm: width becomes rows, height cols
    num_rows = 2 * width
    num_cols_even = height / 2
    num_cols_odd = num_cols_even + 1

    # first and last line coordinates
    x0 = laser_beam_width / 2.0
    y0 = 0.0
    xn = diameter / 2.0

    # number of laser application trajectories (i.e. lines)
    num_lines = int(round(diameter / (2.0 * laser_beam_width)) + 1)

    # step size for lines
    dx = (xn - x0) / (num_lines - 1)

    grid_str = ''
    for row in range(num_rows):
        if row % 2 == 0:  # even row
            num_cols = num_cols_even
            offset = diameter
        else:  # odd row
            num_cols = num_cols_odd
            offset = 0

        for col in range(num_cols):
            for line in range(num_lines):
                grid_str += 'CIRCLE' + '\n'
                for value in [8, 0, 62, 7, 10]:
                    grid_str += str(value) + '\n'
                grid_str += __format_float(
                    x0 + col * (2 * diameter) + offset) + '\n'
                grid_str += str(20) + '\n'
                grid_str += __format_float(
                    y0 + (row + 1) * (1.5 * diameter)) + '\n'
                for value in [30, 0, 40]:
                    grid_str += str(value) + '\n'
                grid_str += __format_float(x0 + dx * line) + '\n'
                grid_str += str(0) + '\n'

    return grid_str


def grid_footer():
    """Generate grid footer text for DXF file.

    :return:
    """
    return __footer()


def legend_filename(grid_filename):
    """Generate legend filename corresponding to `grid_filename`.

    :param grid_filename:
    :return:
    """
    split_buffer = splitext(grid_filename)
    return split_buffer[0] + '-legend' + split_buffer[1]


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


def legend_footer():
    """Generate legend footer text for DXF file.

    :return:
    """
    return __footer()
