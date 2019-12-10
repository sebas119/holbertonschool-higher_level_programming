#include "lists.h"

/**
 * insert_node - Insert node in a sorted linked list
 * @head: Head of the list
 * @number: Data of the new node
 *
 * Return: The head of the updated list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *h = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	/* Empty list */
	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (new);
	}
	/* Insert in the head */
	if (h->n >= number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	while (h != NULL)
	{
		if (h->next == NULL)
		{
			new->next = NULL;
			h->next = new;
			return (new);
		}
		if (h->next->n >= number)
		{
			new->next = h->next;
			h->next = new;
			return (new);
		}
		h = h->next;
	}
	free(new);
	return (NULL);
}
