#include "lists.h"
/**
 * print_listint - a fct that print each element of a node
 * @h: The list head
 *
 * Return: The number of elt in the list
 */

size_t print_listint(const listint_t *h)
{
	const listint_t *current;
	unsigned int n;

	current = h;
	n = 0;
	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		n++;
	}
	return (n);
}
/**
 * add_nodeint - adds a new node at the beg of listint_t list
 * @head: A pointer to address of first elt of list
 * @n: integer to include in the node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = *head;
	*head = new;
	return (NULL);
}
/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */

void free_listint(listint_t *head)
{
	listint_t *current;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
