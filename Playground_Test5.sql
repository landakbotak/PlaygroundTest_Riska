users(
    user_id PK,
    phone
)

transactions(
    tx_id PK,
    user_id FK → users.user_id,
    amount DECIMAL,
    status ENUM('PENDING','SUCCESS','FAILED','REVERSED'),
    created_at
)

-- Answer
select  trx.tx_id, usr.phone, usr.amount, usr.created_at
from    transactions trx, users usr
where   usr.user_id = trx.user_id
