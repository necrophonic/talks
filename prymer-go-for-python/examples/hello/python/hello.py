from datetime import datetime


def greet():
    """Returns a nice greeting including the current date and time"""
    return "Hello! The time is " + datetime.now().isoformat("T") + " (python)"


def _now():
    return datetime.now().isoformat("T")


def main():
    print(greet())


if __name__ == "__main__":
    main()
