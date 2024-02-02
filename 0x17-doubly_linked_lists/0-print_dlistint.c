#include "lists.h"

/**
 * print_dlistint - a fct that prints all the elements of a dlistint_t list.
 * @h: The head of our list
 *
 * Return: Number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *ptr = h;
	size_t count = 0;

	while (ptr != NULL)
	{
		printf("%d\n", ptr->n);
		ptr = ptr->next;
		count++;
	}
	return (count);
}
