#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: singly linked list to be checked
 * Return: integer
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;
	listint_t *slow = list;
	
	if (!list || !list->next)
		return (0);
	while (fast != NULL && slow != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (fast == slow)
			return (1);
	}
	return (0);
		
}

