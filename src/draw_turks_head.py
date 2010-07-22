import optparse
import math

import cairo

import turkshead

parser = optparse.OptionParser()
parser.add_option( "-w", "--width", type="int", default=800, help="Width" )
parser.add_option( "-h", "--height", type="int", default=600, help="Height" )
parser.add_option( "-b", "--bights", type="int", default=4, help="Bights" )
parser.add_option( "-l", "--leads", type="int", default=4, help="Leads" )
parser.add_option( "-r", "--radius-variation", type="int", default=4, help="Radius variation" )
( options, arguments ) = parser.parse_args( arguments )

width = 800
height = 600
outerRadius = min( width, height ) / 2 - 10
innerRadius = outerRadius - 200


img = cairo.ImageSurface( cairo.FORMAT_RGB24, width, height )
ctx = cairo.Context( img )
ctx.set_source_rgb( 1, 1, 0xBF / 255. );
ctx.paint();
ctx.set_source_rgb( 0, 0, 0 );
ctx.rectangle( 10, 10, width - 20, height - 20 );
ctx.translate( width / 2, height / 2 );
ctx.move_to( -width, 0 );
ctx.line_to( width, 0 );
ctx.move_to( 0, -height );
ctx.line_to( 0, height );
ctx.stroke(); ### @todo Find, if possible, how to delete the current point of the context, while continuing to draw
ctx.arc( 0, 0, outerRadius, 0, 2 * math.pi );
ctx.stroke();
ctx.arc( 0, 0, innerRadius, 0, 2 * math.pi );
ctx.stroke();

ctx.rotate( 0.000000001 ); ### @todo Understand why removing this rotate gives a strange sharp line for --leads=2 --bights=3

t = turkshead.TurksHead( 2, 3, innerRadius, outerRadius, 75 )
t.draw( ctx )

img.write_to_png( "turks_head.png" )