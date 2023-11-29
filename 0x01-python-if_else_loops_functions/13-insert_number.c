#include"lists.h"
#include<stdio.h>
#include<stddef.h>
#include<stdlib.h>
#include<unistd.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: pointer to the first node
 * @number: number to be inserted
 * Return: pointer to the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_head = *head;
	listint_t *new_node = NULL;
	listint_t *temp = NULL;

	if (head == NULL)
		return (NULL);
	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new_node->next = *head;
		return (*head = new_node);
	}
	else
	{
		while (new_node && new_node->n < number)
		{
			temp = new_head;
			new_head = new_head->next;
		}
		temp->next = new_node;
		new_node->next = new_head;
	}
	return (new_node);
}
