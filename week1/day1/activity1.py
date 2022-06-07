message = "Welcome to Code Nation!"
message_length = len(message)


def is_length_even(message, length):
    if (length % 2 == 0):
        print(f"The message, '{message}', has an even length of {length}")
    else:
        print(f"The message, '{message}', has an odd length of {length}")


is_length_even(message, message_length)
