class OktaKnowledgeHub:
    def sell(self):
        print("Welcome to Roy Cohen's Okta Knowledge Hub.")
        choice = input("Would you like to explore the various software options offered by Okta? (yes/no): ").lower()
        if choice in ["yes", "y"]:
            print("Great! We offer 2 major cloud services:")
            print("1. Workforce Identity Cloud")
            print("2. Customer Identity Cloud")
            choice2 = input("Which would you like to learn more about? (1/2): ")
            if choice2 == "1":
                print("Excellent choice! Here is a list of our Workforce Identity Cloud options, and remember we offer free trials:")
                print("- Actions")
                print("- Multifactor Authentication")
                print("- Passwordless")
                print("- Single Sign On")
                print("- Universal Login")
                print("Feel free to contact us if you'd like to learn more about our pricing plans.")
            elif choice2 == "2":
                print("Excellent choice! Here is a list of our Customer Identity Cloud options, and remember we offer free trials:")
                print("- Single Sign On")
                print("- Adaptive MFA")
                print("- Lifecycle Management")
                print("- Workflows")
                print("- Identity Governance")
                print("- Privileged Access")
                print("Feel free to contact us if you'd like to learn more about our pricing plans.")
            else:
                print("Invalid input. Please enter '1' or '2'.")
        elif choice in ["no", "n"]:
            print("No problem, have a great day!")
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
        print("\n\n---\n")
        print("Thank you for using Roy Cohen's Okta Knowledge Hub. Have a great day!")

if __name__ == "__main__":
    okh = OktaKnowledgeHub()
    okh.sell()
