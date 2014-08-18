#!/usr/bin/env python
"""
Copyright 2014 Taxamo, Ltd.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
class Transaction_lines:
    """NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually."""


    def __init__(self):
        self.swaggerTypes = {
            'custom_fields': 'list[custom_fields]',
            'additional_currencies': 'additional_currencies',
            'custom_id': 'str',
            'deducted_tax_amount': 'number',
            'product_type': 'str',
            'quantity': 'number',
            'tax_amount': 'number',
            'unit_price': 'number',
            'unit_of_measure': 'str',
            'total_amount': 'number',
            'tax_rate': 'number',
            'refunded_tax_amount': 'number',
            'line_key': 'str',
            'amount': 'number',
            'id': 'number',
            'refunded_total_amount': 'number',
            'description': 'str',
            'product_code': 'str',
            'supply_date': 'str'

        }


        #Custom fields, stored as key-value pairs. This property is not processed and used mostly with Taxamo-built helpers.
        self.custom_fields = None # list[custom_fields]
        #Additional currency information - can be used to receive additional information about invoice in another currency.
        self.additional_currencies = None # additional_currencies
        #Custom id, provided by ecommerce software.
        self.custom_id = None # str
        #Deducted tax amount, calculated by taxmo.
        self.deducted_tax_amount = None # number
        #Product type, according to dictionary /dictionaries/product_types
        self.product_type = None # str
        #Quantity Defaults to 1.
        self.quantity = None # number
        #Tax amount, calculated by taxamo.
        self.tax_amount = None # number
        #Unit price.
        self.unit_price = None # number
        #Unit of measure.
        self.unit_of_measure = None # str
        #Total amount. Required if amount is not provided.
        self.total_amount = None # number
        #Tax rate, calculated by taxamo.
        self.tax_rate = None # number
        #Refunded tax amount, calculated by taxmo.
        self.refunded_tax_amount = None # number
        #Generated line key.
        self.line_key = None # str
        #Amount. Required if total amount is not provided.
        self.amount = None # number
        #Generated id.
        self.id = None # number
        #Refunded total amount, calculated by taxmo.
        self.refunded_total_amount = None # number
        #Line contents description.
        self.description = None # str
        #Internal product code, used for invoicing for example.
        self.product_code = None # str
        #Date of supply in yyyy-MM-dd format.
        self.supply_date = None # str
        
