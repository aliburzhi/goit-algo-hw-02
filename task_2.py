from collections import deque

def is_palindrome(s: str) -> bool:
    cleaned_str = s.lower().replace(" ", "")
    d = deque(cleaned_str)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

def main():
    while True:
        user_input = input("Введіть строку (порожня — вихід): ")
        if user_input == "":
            break
        if is_palindrome(user_input):
            print("Це паліндром!")
        else:
            print("Це не паліндром!")

if __name__ == "__main__":
    main()