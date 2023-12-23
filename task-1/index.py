import csv

def calculate_and_write_average_age(input_csv_file_path, output_csv_file_path):
    try:
        ages = []
        with open(input_csv_file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                age = int(row['Age'])
                ages.append(age)

        if len(ages) > 0:
            average_age = round(sum(ages) / len(ages))
            with open(output_csv_file_path, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['Average Age'])
                csv_writer.writerow([average_age])
            print(f"Average age is written to {output_csv_file_path}")
        else:
            print("No data to calculate average age.")

    except FileNotFoundError:
        print(f"Error: File not found. Please check the file path.")
    except ValueError:
        print("Error: Unable to convert age to an integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
#end of calculate_and_write_average_age

input_csv_file_path = './data.csv'
output_csv_file_path = './output.csv'

calculate_and_write_average_age(input_csv_file_path, output_csv_file_path)
