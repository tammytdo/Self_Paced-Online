#!/usr/bin/env python3

import pathlib
pth = pathlib.Path('./')


class Donor:

    def __init__(self, name):
        self._name = name
        self._donations = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        if not val:
            raise ValueError("A Donor must have a name.")
        self._name = val

    @property
    def donations(self):
        return self._donations

    def add_donation(self, val):
        if val < 1:
            raise ValueError("A positive donation value is required.")
        self.donations.append(val)


class DonorList:

    def __init__(self):
        self._donors = {}

    @property
    def donors(self):
        return self._donors

    def add_donor(self, name):
        donor = Donor(name)
        self.donors[donor.name] = donor

    def get_donor(self, name):
        if not name:
            raise ValueError("Please provide a donor name.")

        if name in self.donors:
            return self.donors[name]
        else:
            return "Donor not found."

    def get_donor_donations(self, name):
        if not name:
            raise ValueError("Please provide a donor name.")

        if name in self.donors:
            return self.donors[name].donations
        else:
            return "Donor not found."

    def compose_donor_thank_you(self, donor):
        if not donor:
            raise ValueError("Please provide a donor.")

        message_obj = {
            'donor_name': donor.name,
            'donation': donor.donations[-1]
        }
        message = 'Dear {donor_name}, thanks so much '\
                  'for your generous donation in the amount of: '\
                  '${donation}.'.format(**message_obj)
        return message

    def get_donor_names(self):
        return "\n".join([donor for donor in self.donors])
