#include "lists.h"

/**
 * check_cycle - check if there are a cycle on the list
 * @list: The list
 * Return: 1 if the cycle exist and 0 if not
 */

int check_cycle(listint_t *list)
{
	listint_t *Point1, *Point2;

	if (!list)
		return (0);
	Point1 = list;
	Point2 = list->next;
	while (1)
	{
		if (!Point2 || !Point2->next)
			return (0);
		else if (Point2 == Point1 || Point2->next == Point1)
			return (1);
		Point1 = Point1->next;
		Point2 = Point2->next->next;
	}
}
