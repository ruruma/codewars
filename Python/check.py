My solution:
SELECT name, greeting, SUBSTRING(SUBSTRING(greeting FROM '#[0-9]+') FROM '[0-9]+') AS user_id FROM greetings;

Better solution:

SELECT namae, greeting, SUBSTRING(greeting FROM '#(\d+)') AS user_id FROM greetings