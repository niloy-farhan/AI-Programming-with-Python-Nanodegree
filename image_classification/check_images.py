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
from classifier import classifier



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

    end_time = time()
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time / 3600))) + ":" + str(int((tot_time % 3600) / 60)) + ":" + str(int((tot_time % 3600) % 60)))


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

    parser.add_argument('--dir', type=str, default='pet_images/',
                        help='path to the folder my_folder')

    parser.add_argument("--arch", type=str, default='vgg',
                        help='chosen model')

    parser.add_argument('--dogfile', type=str, default='dognames.txt',
                        help='text file that has dognames')
    in_args = parser.parse_args()

    return in_args


def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Creates list of files in directory
    in_files = listdir(image_dir)

    results_dic = dict()

    for idx in range(0, len(in_files), 1):

        if in_files[idx][0] != ".":
            pet_image = in_files[idx].lower().split("_")
            pet_label = ""

            for word in pet_image:
                if word.isalpha():
                    pet_label += word.lower() + " "
            pet_label = pet_label.strip()

            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_label]

            else:
                print("** Warning: Duplicate files exist in directory:",
                      in_files[idx])

    return results_dic


def classify_images(images_dir, pet_label_dic, model):
    """
       Creates classifier labels with classifier function, compares pet labels to
       the classifier labels, and adds the classifier label and the comparison of
       the labels to the results dictionary using the extend function. Be sure to
       format the classifier labels so that they will match your pet image labels.
       The format will include putting the classifier labels in all lower case
       letters and strip the leading and trailing whitespace characters from them.
       For example, the Classifier function returns = 'Maltese dog, Maltese terrier, Maltese'
       so the classifier label = 'maltese dog, maltese terrier, maltese'.
       Recall that dog names from the classifier function can be a string of dog
       names separated by commas when a particular breed of dog has multiple dog
       names associated with that breed. For example, you will find pet images of
       a 'dalmatian'(pet label) and it will match to the classifier label
       'dalmatian, coach dog, carriage dog' if the classifier function correctly
       classified the pet images of dalmatians.
        PLEASE NOTE: This function uses the classifier() function defined in
        classifier.py within this function. The proper use of this function is
        in test_classifier.py Please refer to this program prior to using the
        classifier() function to classify images within this function
        Parameters:
         images_dir - The (full) path to the folder of images that are to be
                      classified by the classifier function (string)
         results_dic - Results Dictionary with 'key' as image filename and 'value'
                       as a List. Where the list will contain the following items:
                     index 0 = pet image label (string)
                   --- where index 1 & index 2 are added by this function ---
                     NEW - index 1 = classifier label (string)
                     NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                       and classifer labels and 0 = no match between labels
         model - Indicates which CNN model architecture will be used by the
                 classifier function to classify the pet images,
                 values must be either: resnet alexnet vgg (string)
        Returns:
              None - results_dic is mutable data type so no return needed.
    """

    for key in pet_label_dic:
        model_label = classifier(images_dir+key, model)



if __name__ == "__main__":
    main()


