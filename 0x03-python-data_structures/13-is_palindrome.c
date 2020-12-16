#include "lists.h"

/**
* is_palindrome - checks if a list is palindrome
* @head: pointer to the list
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
**/
int is_palindrome(listint_t **head)
{
	listint_t *start;
	int i = 0, j;
	int t[1024];

	if (head != NULL)
	{
		start = *head;
		i = 0;
		while (start != NULL)
		{
			t[i] = (*start).n;
			start = (*start).next;
			i++;
		}
		for (j = 0; j < (i / 2); j++)
		{
			if (t[i - j - 1] != t[j])
			{
				return (0);
			}
		}
	}
	return (1);
}
