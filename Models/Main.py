from services.database import create_tables
from views.menu import main_menu


def main():
    create_tables()
    main_menu()


if __name__ == "__main__":
    main()