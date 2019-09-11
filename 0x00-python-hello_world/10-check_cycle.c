#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list:
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp1 = list;
	listint_t *tmp2 = list;

	if (list == NULL)
		return (0);

	while (tmp1->next != NULL && tmp2->next != NULL && tmp2->next->next != NULL)
	{
		tmp1 = tmp1->next;
		tmp2 = tmp2->next->next;

		if (tmp1 == tmp2)
			return (1);
	}
	return (0);
}
