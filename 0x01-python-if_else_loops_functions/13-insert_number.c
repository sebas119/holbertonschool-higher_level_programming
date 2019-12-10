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

	if (*head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	if (h->n >= number)
	{
		new->n = number;
		new->next = *head;
		*head = new;
		return (new);
	}

	while (h != NULL)
	{
		if (h->next->n >= number)
		{
			new->n = number;
			new->next = h->next;
			h->next = new;
			return (new);
		}
		h = h->next;
	}
	free(new);
	return (NULL);
}
