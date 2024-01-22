#include "lists.h"

/***
 * check_cycle - a fct that check if a singly list has a cycle in it
 * @list: The adress of first element of the list
 *
 * Return: 0 if there is no cycle and 1 if there is
 */

int check_cycle(listint_t *list)
{
	listint_t *l;
	listint_t *t;

	if (list == NULL)
		return (0);
	l = list;
	t = list;
	while (t != NULL && t->next != NULL)
	{
		l = l->next;
		t = t->next->next;
		if (l == t)
			return (1);
	}
	return (0);
}
