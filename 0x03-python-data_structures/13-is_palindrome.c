#include "lists.h"

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
* palin - check array
* @arr: array to check
* @n: size
* Return: 0 si, 1 no
**/
int palin(int arr[], int n)
{
	int i, j = n - 1, flag = 0;

	for (i = 0; i < n / 2; i++)
	{
		if (arr[i] != arr[j])
		{
			flag = 1;
			break;
		}
		j--;
	}
	free(arr);
	if (flag == 1)
		return (0);
	else
		return (1);
}

/**
* is_palindrome - checks if a list is palindrome
* @head: pointer to the list
* Return: 0 if it is not a palindrome, 1 if it is a palindrome
**/
int is_palindrome(listint_t **head)
{
	listint_t *start;
	int i = 0;
	int *t = NULL;

	start = *head;
	i = listint_len(*head);
	t = malloc(sizeof(int) * i);
	i = 0;
	while (start != NULL)
	{
		t[i] = (*start).n;
		start = (*start).next;
		i++;
	}
	return (palin(t, i));
}


