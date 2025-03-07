import pandas as pd
import datetime


def profit_loss_menu():

    flag = True # flag set to true so it starts the while loop 
    
    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show profit/loss for specific products")
        print("2. Show profit/loss for all products")
        print("###############################################")# outputs this message

        profit_loss_choice = input("Please enter the number of your choice (1-2): ") # you input a valid input  

        try:
            int(profit_loss_choice) # validation to see if is a integer 
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True# flag set to true so it restarts the while loop when you input an invalid date
        else:
            if int(profit_loss_choice) < 1 or int(profit_loss_choice) > 2: # validation to see if it is within the range 
                print("Sorry, you did not neter a valid choice")
                flag = True# flag set to true so it restarts the while loop when you input an invalid date
            else:
                return int(profit_loss_choice) # returns the choice 




def get_product_choice():

    product_list = ["Potatoes", "Carrots", "Peas", "Lettuce", "Onions", 
"Apples", "Oranges", "Pears", "Lemons", "Limes","Melons", "Cabbages", 
"Asparagus", "Broccoli", "Cauliflower", "Celery"]

    flag = True

    while flag:
        print("######################################################")
        print("Please choose a product form the list:")
        print("Please enter the number of the product (1-16)")
        print(product_list)#just called the list instead of 16 prints
        print("######################################################")

        product_choice = input("Please enter the number of your choice (1-16): ")

        try:
            int(product_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(product_choice) < 1 or int(product_choice) > 16:
                print("Sorry, you did not neter a valid choice")
                flag = True
            else:
                product_name = product_list[int(product_choice)-1]
                return product_name



def get_start_date():
    
    flag = True # flag set to true so it starts the while loop 
    
    while flag:
        start_date = input('Plese enter start date for your time range (DD/MM/YYYY)')#input the date 
    
        try:
           pd.to_datetime(start_date) # this is validation for your date you have submitted
        except:
            print("Sorry, you did not enter a valid date") 
            flag = True # flag set to true so it restarts the while loop when you input an invalid date 
        else:
            return pd.to_datetime(start_date, dayfirst=True)


def get_end_date():
    
    flag = True # flag set to true so it starts the while loop
    
    while flag:
        end_date = input('Plese enter end date for your time range (DD/MM/YYYY)')#input the date 

        try:
           pd.to_datetime(end_date)# this is validation for your date you have submitted
        except:
            print("Sorry, you did not enter a valid date")
            flag = True# flag set to true so it restarts the while loop when you input an invalid date 
        else:
            return pd.to_datetime(end_date, dayfirst=True)

def get_date_range_all():
    df1 = pd.read_csv("esp/Task4a_data.csv") 

    df1["Date"] = pd.to_datetime(df1["Date"], dayfirst=True)

    results = df1.loc[(df1["Date"] >= start_date) & (df1["Date"] <= end_date), df1.columns != "Supplier"].copy()
    
    results["Cost Subtotal"] = results["KGs Purchased"] * results["Purchase Price"]
    results["Sales subtotal"] = results["KGs Sold"] * results["Selling Price"]
    results["Profit subtotal"] = results["Sales subtotal"] - results["Cost Subtotal"]
    
    total = round(results["Profit subtotal"].sum(),2)
    results_print = results.to_string(index=False)
    
    print(results_print)
    print("The overall profit/loss for the selected time frame was £{}".format(total))



def get_date_range_product():
    product_name = get_product_choice()
    df2 = pd.read_csv("Task4a_data.csv") 

    df2["Date"] = pd.to_datetime(df2["Date"], dayfirst=True)
   
    product_results = df2.loc[(df2["Date"] >= start_date) & (df2["Date"] <= end_date) & (df2["Product"] == product_name)].copy()

    product_results["Cost Subtotal"] = product_results["KGs Purchased"] * product_results["Purchase Price"]
    product_results["Sales subtotal"] = product_results["KGs Sold"] * product_results["Selling Price"]
    product_results["Profit subtotal"] = product_results["Sales subtotal"] - product_results["Cost Subtotal"]
    
    total = round(product_results["Profit subtotal"].sum(),2)
    results_print = product_results.to_string(index=False)
    
    print(results_print)
    print("The profit/loss for the {} for selected time frame was £{}".format(product_name, total))


def process_menu_choice():

    if profit_choice == 1:
        get_date_range_product()
    else:
        get_date_range_all()

start_date = get_start_date() # program starts here and goes to the get_start_date function and returns a start date 
end_date = get_end_date()# program starts here and goes to the get_end_date function and returns a end date
profit_choice = profit_loss_menu()# goes to profit loss menu 
process_menu_choice() # 