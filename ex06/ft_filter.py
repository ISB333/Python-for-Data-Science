import sys
import string

def main():
    """Main function to test the filter function."""
    try:
        # if len(sys.argv) == 1:
        #     raise TypeError("No aguments, please provide a string")
        # elif len(sys.argv) != 2:
        #     raise TypeError("Too much arguments, only 1 string")
    except TypeError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
