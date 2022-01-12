# ProjetoIntegrado - API

- [User](#User)
- [Auth](#Auth)
- [Password_Recovery](#Password_Recovery)

---

## User

### Campos

| Campo           | Tipo                                 |
| --------------- | ------------------------------------ |
| **user_id**     | integer                              |
| **name**        | string                               |
| **last_name**   | string                               |
| **email**       | string                               |
| **password**    | Large-Binary                         |

### Endpoints
| Função                           | Método  | Endpoint          | Token Necessário       |
| -------------------------------- | ------- | ----------------- | ---------------------- |
| **Current**                      | GET     | `/user/current`   | token de admin logado  |
| **List All**                     | GET     | `/user/all`       | token de usuário logado|
| **Create**                       | POST    | `/user/create`    | nenhum 	              |
| **Details**                      | GET     | `/user/<user_id>` | token de admin logado  |
| **(Partial) Edit**               | PATCH   | `/user/<user_id>` | token de admin logado  |
| **Delete**                       | DELETE  | `/user/<user_id>` | token de admin logado  |

---
## Auth

### Campos

| Campo        | Tipo             |
| ------------ | ---------------- |
| **email**    | string(required) |
| **password** | string(required) |

### Endpoints

| Método | Endpoint         | Função                                                                                                                    |
| ------ | ---------------- | ------------------------------------------------------------------------------------------------------------------------- |
| POST   | `/login`         | **Retorna um fresh token para acesso e um refresh token para atualização** 	   				                                    |
| GET    | `/refresh`       | **Usado para atualizar o token recebendo um refresh token no header. Retorna um non-fresh token e um novo refresh token** |
---

## Password_Recovery

### Campos

| Campo        | Tipo             |
| ------------ | ---------------- |
| **email**    | string(required) |
| **password** | string(required) |
| **link**     | string(required) |

### Endpoints

| Método | Endpoint             | Função                                                                   |
| ------ | -------------------- | ------------------------------------------------------------------------ |
| POST   | `/pw/email`          | **Envia um email com o link para o reset da senha**                      |
| PATCH  | `/pw/reset/<token>`  | **Confirma a identidade do usuário pelo token e altera a senha       **  |
