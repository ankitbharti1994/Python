class DataIdentifier:
    def __init__(self):
        with open('file1.txt') as file:
            self.file_1_data = [int(value) for value in file.readlines()]
        with open('file2.txt') as file:
            self.file_2_data = [int(value) for value in file.readlines()]

    def find_common_value(self):
        print(self.file_1_data)
        print(self.file_2_data)
        new_list = [value for value in self.file_1_data if value in self.file_2_data]
        print('common values in both files: {0}'.format(new_list))


data_identifier = DataIdentifier()
data_identifier.find_common_value()
