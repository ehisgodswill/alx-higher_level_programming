#include "lists.h"

/**
 * check_cycle - checks if a cycle is contained in a linked list
 * @list: linked list
 *
 * Return: 1 if the list has a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *f = list;
	listint_t *sl = list;

	if (!list)
		return (0);

	while (sl && f && f->next)
	{
		f = f->next->next;
		sl = sl->next;
		if (f == sl)
			return (1);
	}

	return (0);
}
