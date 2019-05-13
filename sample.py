def pigify(text):
    def pigify_word(word):
        end = len(word)
        word = word[1:end] + word[0] + "ay"
        return word

    return " ".join([pigify_word(word) for word in text.split(" ")])


def englify(text):
    def englify_word(word):
        end = len(word)
        word = word[end - 3] + word[0:end - 3]
        return word

    return " ".join([englify_word(word) for word in text.split(" ")])


def main():
    while (True):
        choose = input("Choose or press Enter to exit: \n 1. English -> Pig Latin \n 2. Pig Latin -> Enlish \n")

        if (len(choose) == 0):
            print("Exit")
            break
        else:
            try:
                choose = int(choose)
                if (choose == 1):
                    text = input("Enter text: \n")
                    print(pigify(text))
                    break
                elif (choose == 2):
                    text = input("Enter text: \n")
                    print(englify(text))
                    break
                else:
                    print("Choose from available")
            except ValueError:
                print("Write a number")


main()