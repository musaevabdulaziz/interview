# class MyCustomContextManager:
#     def __enter__(self):
#         print("Started")
#         return "Hello world!"

#     def __exit__(self, exp_type, exp_value, exp_tb):
#         print("Leaving the context")

#         if isinstance(exp_value, IndexError):
#             print(f"Exception type: {exp_type}")
#             print(f"Exception value: {exp_value}")
#             return True



# with MyCustomContextManager() as context:
#     print(context)
#     context[100]

# print("After with statement")



from contextlib import contextmanager

# @contextmanager
# def hello_context_manager():
#     print("Entering the context")
#     yield "Hello world"
#     print("Exiting the context")


# with hello_context_manager() as hello:
#     print("hello")


@contextmanager
def writable_file(file_path):
    f = open(file_path, "w")
    try:
        yield f
    finally:
        f.close()

with writable_file("hello.txt") as file:
    file.write("Hello world!") 
