from fastapi import FastAPI, HTTPException
from schemas import User
app = FastAPI()

employees = [
    {
        'id': 1,
        'first_name': 'John',
        'last_name': 'Doe',
        'date_joined': '2022-01-18',
        'age': 30,
        'city': 'Berlin',
        'library_id': '1345',
        'is_active': True,
        'salary': 50000.00
    },
    {
        'id': 2,
        'first_name': 'Swift',
        'last_name': 'Crick',
        'date_joined': '2022-02-09',
        'age': 25,
        'city': 'New Jercy',
        'library_id': '12345',
        'is_active': False,
        'salary': 150000.00
    },
    {
        'id': 3,
        'first_name': 'Victas',
        'last_name': 'Got',
        'date_joined': '2022-09-01',
        'age': 28,
        'city': 'Kyiv',
        'library_id': '1234',
        'is_active': True,
        'salary': 10000.00
    },
    {
        'id': 4,
        'first_name': 'Komerc',
        'last_name': 'Blatata',
        'date_joined': '2022-06-15',
        'age': 60,
        'city': 'New York',
        'library_id': '12345',
        'is_active': False,
        'salary': 9000.00
    },
    {
        'id': 5,
        'first_name': 'Watson',
        'last_name': 'Brick',
        'date_joined': '2022-04-20',
        'age': 15,
        'city': 'New',
        'library_id': '12',
        'is_active': True,
        'salary': 100000.00
    },
    {
        'id': 6,
        'first_name': 'Codis',
        'last_name': 'Codis',
        'date_joined': '2022-10-29',
        'age': 26,
        'city': 'Lviv',
        'library_id': '123',
        'is_active': False,
        'salary': 1000.00
    }
]


@app.get("/")
async def get_user_info(age: int | None = None, salary: int | None = None, is_active: bool | None = None):
    filter_emp = employees

    if age is not None:
        filter_emp = list(filter(lambda x: x['age'] == age, employees))
    if salary is not None:
        filter_emp = list(filter(lambda x: x['salary'] == salary, employees))
    if is_active is not None:
        filter_emp = list(filter(lambda x: x['is_active'] == is_active, employees))

    return {'filter_emp': filter_emp}


@app.get("/users/{employees_id}")
async def search_user(employees_id: int):
    # Пошук користувача за id
    employee = list(filter(lambda x: x['id'] == employees_id, employees))

    if employee is None:
        # Якщо користувач не знайдений, підняти HTTPException з кодом 404
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return {"user_index": employee}


@app.post("/users/create")
async def create_employees(user: User):
    return User.model_dump(user)


@app.put("/users/{user_id}")
async def update_user(user_id: int, updated_user: User):
    # Пошук користувача за id
    user_index = next((index for index, emp in enumerate(employees) if emp['id'] == user_id), None)

    if user_index is not None:
        # Оновлення користувача за індексом
        employees[user_index].update(updated_user)
        return {"message": "User updated successfully"}
    else:
        # Якщо користувач не знайдений, підняти HTTPException з кодом 404
        raise HTTPException(status_code=404, detail="User not found")