#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# TODO 0: Add your information below for Programmer & Date Created.                                                                             
# PROGRAMMER: Niloy Farhan
# DATE CREATED: Thu 14 Dec 2023
# REVISED DATE: 
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
import argparse
from time import time, sleep
from os import listdir


# Main program function defined below
def main():
    start_time = time()

    in_arg = get_input_args()

    answers_dic = get_pet_labels(in_arg.dir)

    print("\nanswers_dic has", len(answers_dic), "key-value pairs.\nBelow are 10 of them:")
    prnt = 0
    for key in answers_dic:
        if prnt < 10:
            print("%2d key: %-30s label: %-26s" % (prnt+1, key, answers_dic[key]))
        prnt += 1

    print("Command Line Arguments:\n    dir=", in_arg.dir, "\n arch=", in_arg.arch, "\n dogfile=", in_arg.dogfile)

    end_time = time()
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time / 3600))) + ":" + str(int((tot_time % 3600) / 60)) + str(int((tot_time % 3600) % 60)))

def get_input_args():
    """
    Retrieves and parses the command line arguments created and defined using
    the argparse module. This function returns these arguments as an
    ArgumentParser object.
     3 command line arguments are created:
       dir - Path to the pet image files(default- 'pet_images/')
       arch - CNN model architecture to use for image classification(default-
              pick any of the following vgg, alexnet, resnet)
       dogfile - Text file that contains all labels associated to dogs(default-
                'dognames.txt'
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object
    """

    parser = argparse.ArgumentParser()

    parser.add_argument('--dir', type=str, default='my_folder/',
                        help='path to the folder my_folder')

    parser.add_argument("--arch", type=str, default='vgg',
                        help='chosen model')

    parser.add_argument('--dogfile', type=str, default='dognames.txt',
                        help='text file that has dognames')
    in_args = parser.parse_args()

    return in_args

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based upon the filenames of the image
    files. This is used to check the accuracy of the image classifier model.
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by pretrained CNN models (string)
    Returns:
     petlabels_dic - Dictionary storing image filename (as key) and Pet Image
                     Labels (as value)
    """
    in_files = listdir(image_dir)

    pet_labels_dic = dict()

    for idx in range(0, len(in_files), 1):
        if in_files[idx][0] != ".":

            image_name = in_files[idx].split("_")

            pet_label = ""

            for word in image_name:
                if word.isalpha():
                    pet_label += word.lower() + " "
            pet_label = pet_label.strip()

            if in_files[idx] not in pet_labels_dic:
                pet_labels_dic[in_files[idx]] = pet_label
            else:
                print("Warning: Duplicate files exist in directory", in_files[idx])

    return(pet_labels_dic)




if __name__ == "__main__":
    main()


