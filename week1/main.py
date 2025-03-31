from decorators import catches

@catches((RuntimeError,  ))
def main(arguments):
    if len(arguments)>1:
        print("We have some arguments")
        print(f"{arguments}")
    else: 
        raise RuntimeError("no arguments passed in!")

if __name__ == '__main__':
    import sys
    main(sys . argv)
