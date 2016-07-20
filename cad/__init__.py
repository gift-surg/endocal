#!/usr/bin/env python

from argparse import ArgumentParser
import dxf


def generate_dxf():
    """Entry point for generating DXF files.

    """
    parser = ArgumentParser()
    parser.add_argument('--laser-beam-width', type=float,
                        help='Laser beam width in microns',
                        required=True)
    parser.add_argument('--diameter', type=float,
                        help='Circular blob diameter in mm',
                        required=True)
    parser.add_argument('--width', type=int,
                        help='Circle grid width, i.e. nr. of columns',
                        required=True)
    parser.add_argument('--height', type=int,
                        help='Circle grid height, i.e. nr. or rows',
                        required=True)
    parser.add_argument('--horizontal-space', type=float,
                        help='Space between adjacent columns of grid in mm'
                             ' (measured center-to-center)',
                        required=True)
    parser.add_argument('--vertical-space', type=float,
                        help='Space between adjacent rows of grid in mm'
                             ' (measured center-to-center)',
                        required=True)
    parser.add_argument('--output-file', type=str,
                        help='DXF file for saving generated grid',
                        required=True)
    args = parser.parse_args()

    grid_header_str = dxf.grid_header()
    grid_str = dxf.grid(laser_beam_width=args.laser_beam_width,
                        diameter=args.diameter,
                        width=args.width, height=args.height,
                        horizontal_space=args.horizontal_space,
                        vertical_space=args.vertical_space)

    legend_header_str = dxf.legend_header()
    legend_str = dxf.legend()

    print 'Saving grid to file ' + args.output_file
    output_file = open(args.output_file, 'w')
    output_file.write(grid_header_str)
    output_file.write('\n')
    output_file.write(grid_str)
    output_file.write('\n')
    output_file.close()

    legend_file = dxf.legend_filename(args.output_file)
    print 'Saving legend to file ' + legend_file
    legend_file = open(legend_file, 'w')
    legend_file.write(legend_header_str)
    legend_file.write('\n')
    legend_file.write(legend_str)
    legend_file.write('\n')
    legend_file.close()
