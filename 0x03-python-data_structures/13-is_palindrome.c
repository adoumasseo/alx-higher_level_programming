#include "lists.h"

/**
 * lenght - a fct that return length of as singly list
 * @head: A pointer to the address of first elt
 *
 * Return: 0 if list is NULL and his lenght else
 */

int lenght(listint_t *head)
{
	listint_t *ptr;
	int n = 0;

	if (head == NULL)
		return (0);
	ptr = head;
	while (ptr != NULL)
	{
		n++;
		ptr = ptr->next;
	}
	return (n);
}
/**
 * take_l - a fct that take a sub list in an big one and return it
 * @head: A pointer to first elt of big list
 * @lgt: lenght of big list
 * @st: the index where start to take the list
 *
 * Return: A pointer to the list take or NULL
 */

listint_t *take_l(listint_t *head, int lgt, int st)
{
	int count = st, t;
	listint_t *ptr = head, *new_list_head;

	new_list_head = NULL;
	if (st == 0)
	{
		t = (int)lgt / 2;
		while (count < t)
		{
			add_nodeint_end(&new_list_head, ptr->n);
			ptr = ptr->next;
			count++;
		}
		return (new_list_head);
	}
	else
	{
		t = 0;
		while (t < lgt)
		{
			if (t >= st)
				add_nodeint_end(&new_list_head, ptr->n);
			ptr = ptr->next;
			t++;
		}
		return (new_list_head);
	}
}

/**
 * reverse_list - a fct that reverse a slingly list
 * @head: A pointer to the adress of the first elt of list
 *
 * Return: Nothing is void tyoe function
 */

void reverse_list(listint_t **head)
{
	listint_t *ptr = (*head), *temp = NULL;

	while ((*head) != NULL)
	{
		ptr = ptr->next;
		(*head)->next = temp;
		temp = (*head);
		(*head) = ptr;
	}
	(*head) = temp;
}

/**
 * compare_list - a fct that check if two linked list are the same
 * @head_first: The first list
 * @head_sd: the second one
 *
 * Return: 0 if there are != and 1 else
 */

int compare_list(listint_t *head_first, listint_t *head_sd)
{
	int l1, l2;
	listint_t *ptr1 = head_first, *ptr2 = head_sd;

	l1 = lenght(head_first);
	l2 = lenght(head_sd);
	if (l1 != l2)
		return (0);
	while (ptr1 != NULL && ptr2 != NULL)
	{
		if (ptr1->n != ptr2->n)
			return (0);
		ptr1 = ptr1->next;
		ptr2 = ptr2->next;
	}
	return (1);
}

/**
 * is_palindrome - a fct that check if singly list is a palindrome
 * @head: A pointer to the first elt of the singly list
 *
 * Return: 0 if not a palindrome and 1 else
 */

int is_palindrome(listint_t **head)
{
	listint_t *ptr = (*head), *n1, *n2;
	int n, d;

	n = lenght(ptr);
	if (n % 2 != 0)
		d = (int)n / 2 + 1;
	else
		d = (int)n / 2;
	n1 = take_l(ptr, n, 0);
	n2 = take_l(ptr, n, d);
	reverse_list(&n1);
	n = compare_list(n1, n2);
	free_listint(n1);
	free_listint(n2);
	return (n);
}
