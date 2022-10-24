#include "palindrome.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * is_palindrome - checks whether or not a given unsigned integer is a palindrome
 * @n: nummber to be checked
 * Return: 1 if n is a palindrome otherwise returns 0
 */

int is_palindrome(unsigned long n)
{
  unsigned long int x;
  unsigned long int y;

  if (n == 0)
    return (1);

  x = n % 10;
  y = n;

  while (y / 10 != 0)
  {
    y = y / 10;
    x = x * 10;
  }

  if (y != n % 10)
    return (0);

  n = (n - x) / 10;
    return(is_palindrome(n));

}
