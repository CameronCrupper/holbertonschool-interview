#include "menger.h"
#include <stdio.h>

/**
 * menger - Draws 2D menger sponge
 * @level: depth of sponge to print
 * Return: none
 */

void menger(int level)
{
int axisX, axisY, d, dim = 1;

if (level >= 0)
{
for (axisX = 0; axisX < level; axisX++)
{
dim *= 3;
}
for (axisX = 0; axisX < dim; axisX++)
{
for (axisY = 0; axisY < dim; axisY++)
{
for (d = dim / 3; d > 0; d /= 3)
{
if ((axisX % (d * 3)) / d == 1 && (axisY % (d * 3)) / d == 1)
break;
}
if (d)
{
printf(" ");
}
else
{
printf("#");
}
}
printf("\n");
}
}
}
