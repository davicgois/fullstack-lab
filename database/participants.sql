-- Nomes dos participantes do evento informado, em ordem alfabética.
-- Cada inscrição aponta para um usuário; o JOIN busca o nome desse usuário.
-- Não escreva o parâmetro com dois-pontos em comentários: o SQLAlchemy
-- também o trataria como parâmetro.
SELECT users.name
FROM registrations
JOIN users ON users.id = registrations.user_id
WHERE registrations.event_id = :event_id
ORDER BY users.name;
