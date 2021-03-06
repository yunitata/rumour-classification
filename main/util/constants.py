'''
Copyright (c) 2014-2015, The University of Sheffield. 
This file is part of the SDQ rumour classification software 
(see https://github.com/mlukasik/rumour-classification), 
and is free software, licenced under the GNU Library General Public License,
Version 2, June 1991 (in the distribution as file LICENSE).

Created on 16 May 2015

@author: michal

Constants specific for the experiment.
'''

LABELS=[11, 12, 13]
BOW_FEATURENAMES_PREFIX="BOW_"
BROWN_FEATURENAMES_PREFIX="BROWN_"
TASK_FEATURENAME="event"
IS_SIMPLE_RETWEET_FEATURENAME="is_simple_retweet"
TIME_FEATURENAME='time'

def extract_feature_indices(header):
    features_bow=[ind for ind, name in enumerate(header) if name.startswith(BOW_FEATURENAMES_PREFIX)]
    features_brown=[ind for ind, name in enumerate(header) if name.startswith(BROWN_FEATURENAMES_PREFIX)]
    index_task=header.index(TASK_FEATURENAME)
    rttypecol_processed=header.index(IS_SIMPLE_RETWEET_FEATURENAME)
    return features_bow, features_brown, index_task, rttypecol_processed