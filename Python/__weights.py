# given a matrix of binary values, properly weight
from __future__ import division
import __set
import math
import numpy as np




def tf_idf(term, term_sets, document_sets):

    term_freq = 1.0 / len(term_sets[term])
    tf = 0.5 + 0.5 * term_freq # max term freq is assumed to be 1

    num_documents = len(term_sets)
    document_freq = len(document_sets[term]) / num_documents
    idf = math.log(document_freq)

    tf_idf = tf * idf

    return tf_idf


# calculates the tf-idf scores for all values in a matrix where rows are docs
# and cols are terms. also needs a list of documents that each term appears in
def tf_idf_matrix(np_matrix, document_sets, term_list):

    num_rows = len(np_matrix) # num docs
    num_cols = len(np_matrix[0]) # num terms

    new_matrix = np.copy(np_matrix)

    for i in range(0, num_rows):
        row = np_matrix[i]

        row_total = __set.get_size(row)
        # print row_total

        for j in range(0, num_cols):
            # print row[j]

            tf = float(0.5 * (row[j] / row_total))
            idf = math.log(num_rows / len(document_sets[term_list[j]]))

            new_matrix[i][j] = tf * idf

    return new_matrix
