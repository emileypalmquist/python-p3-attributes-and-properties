#!/usr/bin/env python3

class Dog:

    breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei",
              "Beagle", "French Bulldog", "Pug", "pointer"]

    def __init__(self, name="Todo", breed="Mutt"):
        self._name = name
        self._breed = breed

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        if type(new_name) is str and 1 <= len(new_name) <= 25:
            self._name = new_name
            return self.name
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_breed(self):
        return self._breed

    def set_breed(self, new_breed):
        if new_breed in self.breeds:
            self._breed = new_breed
            return self._breed
        else:
            print('Breed must be in list of approved breeds.')

    breed = property(get_breed, set_breed,)
    name = property(get_name, set_name,)
