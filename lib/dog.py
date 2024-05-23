#!/usr/bin/env python3

class Dog:
    # Class body goes here

    #Instance method definition
    def bark(self):
        '''prints a barking dog'''
        print("Woof!")

    def sit(self):
        '''make dog to sit'''
        print( "The dog is sitting.")


my_dog = Dog()
snoopy = Dog()

my_dog.bark()
snoopy.bark()
snoopy.sit()
    
