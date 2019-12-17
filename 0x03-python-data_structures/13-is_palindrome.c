#include "lists.h"

void reverse_list(listint_t **head);
int compareEqual(listint_t *head, listint_t *toCompare);

/**
 * is_palindrome - Check if the linked list given is palindrome
 * @head: Address of the head of the linked list
 *
 * Return: Boolean values
 */
int is_palindrome(listint_t **head)
{
	listint_t *h1 = *head, *h2 = *head;
	listint_t *secHalf, *prev_h1 = *head, *midNode = NULL;
	int ans = 1;

	if (*head == NULL)
		return (ans);

	if (*head != NULL && (*head)->next != NULL)
	{
		while (h2 != NULL && h2->next != NULL)
		{
			h2 = h2->next->next;

			prev_h1 = h1;
			h1 = h1->next;
		}

		if (h2 != NULL)
		{
			midNode = h1;
			h1 = h1->next;
		}

		secHalf = h1;
		prev_h1->next = NULL;
		reverse_list(head);
		ans = compareEqual(*head, secHalf);

		reverse_list(head);

		if (midNode != NULL)
		{
			prev_h1->next = midNode;
			midNode->next = secHalf;
		}
		else
		{
			prev_h1->next = secHalf;
		}
	}
	return (ans);
}

/**
 * compareEqual - Compare if two given list are equal
 * @head: Head of a linked list
 * @toCompare: Head of a linked list
 *
 * Return: 1 on sucess, 0 on failure
 */
int compareEqual(listint_t *head, listint_t *toCompare)
{
	listint_t *h1 = head, *h2 = toCompare;

	while (h1 != NULL && h2 != NULL)
	{
		if (h1->n == h2->n)
		{
			h1 = h1->next;
			h2 = h2->next;
		}
		else
		{
			return (0);
		}
	}
	if (h1 == NULL && h2 == NULL)
		return (1);

	return (0);
}

/**
 * reverse_list - Reverse the linked list
 * @head: Address of the head of the list
 *
 */
void reverse_list(listint_t **head)
{
	listint_t *prev = NULL, *current = *head;
	listint_t *next = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
}
