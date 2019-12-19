import xmlrpc.client


def main():
    with xmlrpc.client.ServerProxy("http://localhost:8000/") as proxy:
        print("3 is even: %s" % str(proxy.is_even(3)))
        print("100 is even: %s" % str(proxy.is_even(100)))


if __name__ == "__main__":
    main()
