def main():
 number = int(input("Enter a number "))
 create_number_dict = dict()
 for i in range(1, number+1):
    create_number_dict[i] = i * i
 print("The generated dictionary of the form (i: i*i) is")
 print(create_number_dict)
if __name__ == "__main__":
  main()
