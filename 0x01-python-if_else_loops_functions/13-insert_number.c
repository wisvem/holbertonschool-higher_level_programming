#include "lists.h"

/**
* add_nodeint - adds a new node at the beginning of a list
* Return: the address of the new element, or NULL if it failed
* @head: pointer to list
* @n: int to put into the new node
**/
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *newnode;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
	{
		return (NULL);
	}
	(*newnode).n = n;
	(*newnode).next = *head;
	*head = newnode;
	return (newnode);
}

/**
* insert_node - inserts a number into a sorted singly linked list
* @head: pointer to head of the list
* @number: number to be inserted
* Return: the address of the new node, or NULL if it failed
**/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current, *prox;

	if (*head != NULL)
		current = *head, prox = (*current).next;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	(*new).n = number, (*new).next = NULL;
	if (*head == NULL)
		*head = new;
	else if (number < (*current).n)
		add_nodeint(head, number);
	else
	{
		while (current != NULL)
		{
			if ((*current).next == NULL)
			{
				add_nodeint_end(head, number);
				break;
			}
			if (number == (*current).n)
			{
				(*new).next = prox;
				(*current).next = new;
				break;
			}
			if (number < (*prox).n && prox != NULL)
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
