# Bounday_Fill_using_Python
This is an implementation of boundary fill algorithm using Python. It can generate any polygon or circle of custom user given specifications and will colour the figure starting from a user provided point  with a user defined colour.

It uses Bresenham's line drawing algorithm to draw the polygon sides.Each point plotted has a 8 unit size.For drawwing a polygon of 4 vertex input vertex as 5 and give the last vertex the same as the first one.

It uses Midpoint circle algorithm, to generate the circle.Each point plotted has a 8 unit size.

The colour is filled using r,g,b values from 0-255.

I used a 100*100 sized plot as i wanted the boundary fill to be over fastly. You can change this in the code to build figures with more definition but the boundary fill will take good time as the plot is shown after each unit is filled with colour.

I used Spyder IDE for building and running this code.The images generated are shown in the plot screen.
