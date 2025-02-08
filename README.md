# fastapi

What is FastAPI?
- FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.
- FastAPI is a modern Python web framework that leverage the latest Python features to provide you with a simple way to build APIs.


Why FastAPI?
- Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.
- Fast to code: Increase the speed to develop features by about 200% to 300%. *
- Fewer bugs: Reduce about 40% of human (developer) induced errors. *
- Intuitive: Great editor support. Completion everywhere. Less time debugging.
- Easy: Designed to be easy to use and learn. Less time reading docs.

Why We Need Schema?
- It's a pain to get all the values from the request body and validate them manually.
- the client can send the wrong data type, or forget to send a required field, etc.
- FastAPI will do all the validation for us.
- FastAPI will also convert the data to the correct data type.
- FastAPI will provide us with clear error messages.

