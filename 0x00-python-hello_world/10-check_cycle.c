#include "lists.h"

/***
 * check_cycle - a fct that check if a singly list has a cycle in it
 * @list: The adress of first element of the list
 *
 * Return: 0 if there is no cycle and 1 if there is
 */

int check_cycle(listint_t *list)
{
	listint_t *ptr;

	if (list == NULL)
		return (0);
	ptr = list;
	while (ptr->next != NULL)
	{
		if (ptr->next == list)
			return (1);
		ptr = ptr->next;
	}
	return (0);
}
