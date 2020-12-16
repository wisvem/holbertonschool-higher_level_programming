#include "lists.h"
/**
 * palindrome_check - check
 * @palindrome: list
 * @counter: size
 * Return: 1 and 0
 */
int palindrome_check(listint_t *palindrome, int counter)
{
	int i = 0, j;
	listint_t *front, *rear;

	while (i != counter / 2)
	{
		front = rear = palindrome;
		for (j = 0; j < i; j++)
		{
			front = front->next;
		}
		for (j = 0; j < counter - (i + 1); j++)
		{
			rear = rear->next;
		}
		if (front->n != rear->n)
		{
			return (0);
		}
		else
		{
			i++;
		}
	}
	return (1);
}

/**
* listint_len - Entry point
* @h: head of the list
* Return: the number of elements in a linked list
**/
int listint_len(const listint_t *h)
{
	int elements;

	if (h == NULL)
	{
		return (0);
	}
	for (elements = 0; h != NULL; elements++)
	{
		if ((*h).n == 0)
			elements--;
		h = (*h).next;
	}
	return (elements);
}


/**
* is_palindrome - checks if a list is palindrome
* @head: pointer to the list
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
**/
int is_palindrome(listint_t **head)
{
	listint_t *temp = *head;
	int i = listint_len(temp);
/*
*	listint_t *start;
*	int i = 0;
*	int *t = NULL;
*
*	start = *head;
*	i = listint_len(*head);
*	t = malloc(sizeof(int) * i);
*	i = 0;
*	while (start != NULL)
*	{
*		t[i] = (*start).n;
*		start = (*start).next;
*		i++;
*	}
*	return (palin(t, i));
*/
	return (palindrome_check(*head, i));
}
