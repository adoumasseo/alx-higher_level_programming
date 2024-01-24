#include "lists.h"

/**
 * insert_node - a fct that insert a node in a sorted list
 * @head: A pointer to the address of first elt of our list
 * @number: number to insert in our list
 *
 * Return: the adress of new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
