def parse_input(user_input):
    parts = user_input.split()
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args


def add_contact(args, contacts):
    if len(args) < 2:
        return "Insufficient input. Use: add Name phone"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) < 2:
        return "Insufficient input. Use: change Name new_phone"
    name, phone = args
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    if len(args) < 1:
        return "Input the name. Use: phone Name"
    name = args[0]
    return contacts.get(name, "Contact not found.")


def show_all(contacts):
    if not contacts:
        return "No contacts found."

    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
