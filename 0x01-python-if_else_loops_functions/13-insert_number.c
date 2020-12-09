#include "lists.h"

/**
* insert_node - inserts a number into a sorted singly linked list
* @head: pointer to head of the list
* @number: number to be inserted
* Return: the address of the new node, or NULL if it failed
**/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *current, *prox;

	current = *head;
	prox = (*current).next;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	(*new).n = number;
	(*new).next = NULL;

	if (*head == NULL)
		*head = new;
	else
	{
		while (current != NULL)
		{
			if (number < (*prox).n)
			{
				(*new).next = prox;
				(*current).next = new;
				break;
			}
			current = (*current).next;
			prox = (*current).next;
		}
	}
	return (new);
}
