#include "lists.h"

/**
* palin - palindrome functio
* @s: String to evaluate
* @i: an auxiliar
* @lenght: length of @s
* Return: 1 if string is a palindrome and 0 if not.
**/
int palin(int *s, int i, int lenght)
{
	if (i == lenght)
	{
		return (1);
	}
	if (s[i] != s[lenght])
	{
		return (0);
	}
	if (i < lenght)
	{
		return (palin(s, i + 1, lenght - 1));
	}
	return (1);
}

/**
* is_palindrome - checks if a list is palindrome
* @head: pointer to the list
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
**/
int is_palindrome(listint_t **head)
{
	listint_t *start = *head;
	int i = 0, t[1024];

	if (*head != NULL)
	{
		while (start != NULL)
		{
			t[i] = (*start).n;
			start = (*start).next;
			i++;
		}
		return (palin(t, 0, i -1));
	}
	return (1);
}
