# ProjetoIntegrado - API

- [User](#User)
- [Auth](#Auth)
- [Password_Recovery](#Password_Recovery)
- [Data_Read](#Data_Read)
- [Graph](#Graph)
- [Daily_Tip](#Daily_Tip)
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
| Função                           | Método  | Endpoint          | Token Necessário         |
| -------------------------------- | ------- | ----------------- | ------------------------ |
| **Current**                      | GET     | `/user/current`   | token de usuário logado  |
| **List All**                     | GET     | `/user/all`       | token de usuário logado  |
| **Create**                       | POST    | `/user/create`    | nenhum 	            |
| **Details**                      | GET     | `/user/<user_id>` | token de usuário logado  |
| **(Partial) Edit**               | PATCH   | `/user/<user_id>` | token de usuário logado  |
| **Delete**                       | DELETE  | `/user/<user_id>` | token de usuário logado  |

### Exemplos
POST /user/create
```
```json
{
	"name":"Gabriel",
	"last_name":"Lima",
	"email":"gabriel.lima.moura@poli.ufrj.br",
	"password":"123456"
}
```
```json
201
{
  "user_id": 1,
  "name": "Gabriel",
  "last_name": "Lima",
  "email": "gabriel.lima.moura@poli.ufrj.br",
  "create_time": "2022-01-12T00:26:03.169427+00:00",
  "update_time": null
}
```
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
### Exemplos

```c
POST /login
```
```json
{
	"email" : "gabriel.lima.moura@poli.ufrj.br",
	"password": "abcd"
}
```
```json
200
{
  "name": "Gabriel",
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNjQxOTQ5NjAzLCJqdGkiOiIzNDc1Njc4OC0wYTg4LTQxMTctOTBmYy03MDcwNjZlNTkxYzIiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoyLCJuYmYiOjE2NDE5NDk2MDMsImV4cCI6MTY0MjU0OTYwM30.RbUdyCQtNqGOFDPtCchtseGyQ88dXsYfExn_E5me2HE",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0MTk0OTYwMywianRpIjoiMjZjMTUzZjItYTljNS00ZWY1LTllMjQtODMwNzE1MWVjMzRkIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOjIsIm5iZiI6MTY0MTk0OTYwMywiZXhwIjoxNjQyNTQ5NjAzfQ.MyZ2X2QxsuNsFf_yMvGg5WtDSpWQrlbB_wu_L6FR1EY"
}
```
---
```c
POST /login
```
```json
{
	"email" : "gabriel.lima.moura@poli.ufrj.br",
	"password": "abcd"
}
```
```json
200
{
  "name": "Gabriel",
  "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6dHJ1ZSwiaWF0IjoxNjQxOTQ5NjAzLCJqdGkiOiIzNDc1Njc4OC0wYTg4LTQxMTctOTBmYy03MDcwNjZlNTkxYzIiLCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoyLCJuYmYiOjE2NDE5NDk2MDMsImV4cCI6MTY0MjU0OTYwM30.RbUdyCQtNqGOFDPtCchtseGyQ88dXsYfExn_E5me2HE",
  "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0MTk0OTYwMywianRpIjoiMjZjMTUzZjItYTljNS00ZWY1LTllMjQtODMwNzE1MWVjMzRkIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOjIsIm5iZiI6MTY0MTk0OTYwMywiZXhwIjoxNjQyNTQ5NjAzfQ.MyZ2X2QxsuNsFf_yMvGg5WtDSpWQrlbB_wu_L6FR1EY"
}
```
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

### Exemplos

```c
POST /pw/email
```
```json
{ 
  "email" : "gabriel.lima.moura@poli.ufrj.br",
  "link" : "www.svuv.com/password/reset/"
}
```
```json
200
{}
```
---
```c
POST /pw/reset/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyNTAyNTk5MiwianRpIjoiNDI0MmEyOGUtYjVjYi00YWMyLWI5NzgtOTcwMDg5NjEzMTk2IiwidHlwZSI6ImNvbnN1bHRhbnQiLCJzdWIiOjEsIm5iZiI6MTYyNTAyNTk5MiwiZXhwIjoxNjI1MDI5NTkyfQ.NH6lukQ0q9TRcopno0igQ2s8Rbj5uAybL3HhgdsB7lQ
```
```json
{ "password" : "123"}
```
```json
204
{}
```
---
## Data_Read

### Campos

| Campo            | Tipo                                 |
| ---------------- | ------------------------------------ |
| **data_read_id** | integer                              |
| **risco**        | string                               |
| **uv**           | Float                                |
| **voltage**      | Float                                |
| **nivel_bateria**| Float                                |
| **sensor_id**    | Integer                              |

### Endpoints
| Função                           | Método  | Endpoint          | Token Necessário         |
| -------------------------------- | ------- | ----------------- | ------------------------ |
| **List All**                     | GET     | `/data_read/all`  | token de usuário logado  |
| **Load Read**                    | POST    | `/data_read/load` | token de usuário logado  |
| **Details**                      | GET     | `/data_read/<id>` | token de usuário logado  |
| **Delete**                       | DELETE  | `/data_read/<id>` | token de usuário logado  |
| **Get Last Read**                | LAST    | `/data_read/last` | token de usuário logado  |

### Exemplos

---
## Graph

### Endpoints
| Função                  | Método  | Endpoint                                      | Token Necessário         |
| ----------------------- | ------- | --------------------------------------------- | ------------------------ |
| **One Day Graph**       | GET     | `/graph/one_day/<int:number_of_days_before>`  | token de usuário logado  |
| **Many Days Graph**     | GET     | `/graph/many_days/<int:number_of_days_before>`| token de usuário logado  |
| **Max Uv By Day Graph** | GET     | `/graph/max_uv/<int:number_of_days_before>`   | token de usuário logado  |

### Exemplos

---
## Data_Read

### Campos

| Campo             | Tipo                |
| ----------------- | ------------------- |
| **data_tip_id**   | Integer             |
| **tip**           | String              |
| **already_shown** | String  (automatic) |

### Endpoints
| Função                           | Método  | Endpoint               | Token Necessário         |
| -------------------------------- | ------- | ---------------------- | ------------------------ |
| **List All**                     | GET     | `/daily_tip/all`       | token de usuário logado  |
| **Create**                       | POST    | `/daily_tip/create`    | token de usuário logado  |
| **Details**                      | GET     | `/daily_tip/<user_id>` | token de usuário logado  |
| **(Partial) Edit**               | PATCH   | `/daily_tip/<user_id>` | token de usuário logado  |
| **Delete**                       | DELETE  | `/daily_tip/<user_id>` | token de usuário logado  |
| **Get Random Tip**               | GET     | `/daily_tip/random`    | token de usuário logado  |

### Exemplos

---