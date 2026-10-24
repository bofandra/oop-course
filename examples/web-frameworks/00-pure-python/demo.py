"""Run after 'python -m pip install -r requirements.txt'."""

from book_domain import BookService, CompactWhitespaceTitlePolicy, InMemoryBookRepository


def main():
    repository = InMemoryBookRepository()
    service = BookService(repository, CompactWhitespaceTitlePolicy())

    created = service.create("  The    Pragmatic Python  ", "  Ana  ")
    print("CREATE:", created.to_dict())

    print("READ:", service.get(created.id).to_dict())
    service.update(created.id, "  New   Title  ", "Ana")
    print("UPDATE:", service.list()[0].to_dict())

    service.delete(created.id)
    print("DELETE:", service.list())


if __name__ == "__main__":
    main()
