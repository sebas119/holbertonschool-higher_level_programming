#include "lists.h"

/**
 * check_cycle - Checks if the singly linked list has a cycle
 * @list: The linked list
 *
 * Return: Boolean values
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *twoHead = list;

	while (twoHead != NULL && twoHead->next != NULL)
	{
		head = head->next; /* One time */
		twoHead = twoHead->next->next; /* Two times */
		if (head == twoHead)
			return (1);
	}

	return (0);
}
