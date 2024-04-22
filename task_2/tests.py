import asyncio

from prostopay.task_2.main import UserService
from prostopay.task_2.models import UserDTO


async def test_user_service():
    # Initialize the service
    user_service = UserService()

    # Create a new user
    new_user = UserDTO(name="John Doe", email="john@example.com")
    await user_service.add(new_user)

    # Retrieve the user and check if the information matches
    retrieved_user = await user_service.get(1)
    assert retrieved_user.name == "John Doe"
    assert retrieved_user.email == "john@example.com"

# Run the test
asyncio.run(test_user_service())