# Replace text
import os


def main():
    filename = input("Enter a filename:")
    old = input("Enter the old string to be replaced:")
    new = input("Enter the new string to replace the old string:")
    if os.path.isfile(filename):
        content = ""
        with open(filename, 'r') as f:
            content += f.read().replace(old, new)
            f.close()
        with open(filename, "w") as f:
            f.write(content)
            f.close()
            print("Done")
    else:
        print("The file doesn't exist!")


if __name__ == '__main__':
    main()
