import json

class DVLAReg():

    def totalquantity_registration(self):

        with open('Vehicles_reg_details.json') as f:
            json_data = json.load(f)
            vehicledetails_list = json_data['Vehicle_details']
            quantity_registration = 0
            for index in range(len(vehicledetails_list)):
                vehicledetail = vehicledetails_list[index]
                if vehicledetail['Registration Number'] is not None:
                    quantity_registration = quantity_registration + 1
            #print(f'total quantity of Vehicle registration number: {quantity_registration}')
            return quantity_registration



    def returnvehicledetailsforgivenregnumbers(self, reg_number):
        with open('Vehicles_reg_details.json') as f:
            json_data = json.load(f)
            vehicledetails_list = json_data['Vehicle_details']
            #reg_number = input('Enter registration number: ')
            for index in range(len(vehicledetails_list)):
                if vehicledetails_list[index].get('Registration Number') == reg_number:
                    if vehicledetails_list[index].get('Vehicle ID') is not None:
                        return reg_number, vehicledetails_list[index].get('Year'), vehicledetails_list[index].get('Vehicle ID')

                    else:
                       return reg_number, vehicledetails_list[index].get('Year'), None

            return None, None, None
