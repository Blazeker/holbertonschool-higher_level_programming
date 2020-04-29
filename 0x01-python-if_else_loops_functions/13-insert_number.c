#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - adds a new node on a specific position
 * @head: a pointer
 * @number: an int
 * Return: The new node
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL;
	listint_t *aux1, *aux2;
	int cmp = 0;

	if (!head)
		return (NULL);

	aux1 = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	if (number < aux1->n)
	{
		new->next = aux1;
		*head = new;
		return (new);
	}
	while (aux1)
	{
		if (aux1->next)
		{
			aux2 = aux1->next;
			cmp = aux1->next->n;
		}
		else
		{
			aux2 = NULL;
			cmp = number + 1; }
		if (number >= aux1->n && number < cmp)
		{
			aux1->next = new;
			new->next = aux2; }
		aux1 = aux2; }
	return (new);
}
