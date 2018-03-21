"""
A const file for our word flags, just to organize things better.
"""
from numpy import uint64 as uint


def print_word_bin(word: uint) -> None:
    """
    Helper to print a value in binary.
    :param word: The word to print
    """
    print(format(word, '#066b'))


def print_word_hex(word: uint) -> None:
    """
    Helper to print a value in binary.
    :param word: The word to print
    """
    print(format(word, '#018x'))


# Bit shifts for our values.
EXTERNAL_POINTER_SHIFT   = 63
SENT_META_SHIFT          = 62
SENT_TYPE_SHIFT          = 61
SENT_SUBTYPE_SHIFT       = 58
AFF_TYPE_SHIFT           = 54
EVID_SHIFT               = 51
WORD_COUNT_SHIFT         = 0
# word meta masks
IN_LANGUAGE_SHIFT        = 62
GRAMMAR_SHIFT            = 59
TEMPORAL_SHIFT           = 57
PROGRESS_SHIFT           = 55
RECURRENCE_SHIFT         = 53
DEGREE_SHIFT             = 50
EMPHASIS_SHIFT           = 49
DETERMINATIVE_SHIFT      = 48
PLURALITY_SHIFT          = 46
# External masks (for things without abstract meanings).
EXTERNAL_WORD_FLAG_SHIFT = 45
EXTERNAL_TYPE_SHIFT      = 32
EXTERNAL_WORD_SHIFT      = 0
# Internal word masks
INTERNAL_TYPE_SHIFT      = 43
INTERNAL_WORD_SHIFT      = 0

# masks for the class
# sentence masks
ZEROED                = uint(0b0)
SENT_META_MASK        = uint(0b1        << SENT_META_SHIFT)
SENT_TYPE_MASK        = uint(0b01       << SENT_TYPE_SHIFT)
SENT_SUBTYPE_MASK     = uint(0b00111    << SENT_SUBTYPE_SHIFT)
AFF_TYPE_MASK         = uint(0b000001111 << AFF_TYPE_SHIFT)
EVID_MASK             = uint(0b000000000111 << EVID_SHIFT)
WORD_COUNT_MASK       = 2**51-1
if __name__ == '__main__':
    print_word_bin(ZEROED)
    print_word_bin(SENT_META_MASK)
    print_word_bin(SENT_TYPE_MASK)
    print_word_bin(SENT_SUBTYPE_MASK)
    print_word_bin(AFF_TYPE_MASK)
    print_word_bin(EVID_MASK)
    print_word_bin(WORD_COUNT_MASK)
# word meta masks
IN_LANGUAGE_MASK      = uint(0b1 << IN_LANGUAGE_SHIFT)
GRAMMAR_MASK          = uint(0b0111 << GRAMMAR_SHIFT)
TEMPORAL_MASK         = uint(0b11 << TEMPORAL_SHIFT)
PROGRESS_MASK         = uint(0b11 << PROGRESS_SHIFT)
RECURRENCE_MASK       = uint(0b11 << RECURRENCE_SHIFT)
DEGREE_MASK           = uint(0b111 << DEGREE_SHIFT)
EMPHASIS_MASK         = uint(0b1 << EMPHASIS_SHIFT)
DETERMINATIVE_MASK    = uint(0b1 << DETERMINATIVE_SHIFT)
PLURALITY_MASK        = uint(0b11 << PLURALITY_SHIFT)
# External masks (for things without abstract meanings).
EXTERNAL_WORD_FLAG    = uint(0b1 << EXTERNAL_WORD_FLAG_SHIFT)
EXTERNAL_TYPE_MASK    = uint(0x1FFF << EXTERNAL_TYPE_SHIFT)
EXTERNAL_WORD_MASK    = uint(0xFFFFFFFF)
# Internal word masks
INTERNAL_TYPE_MASK    = uint(0b11 << INTERNAL_TYPE_SHIFT)
INTERNAL_WORD_MASK    = uint(0x7FFFFFFFFFF)
if __name__ == '__main__':
    print('------WORD MASKS------')
    print_word_bin(IN_LANGUAGE_MASK)
    print_word_bin(GRAMMAR_MASK)
    print_word_bin(TEMPORAL_MASK)
    print_word_bin(PROGRESS_MASK)
    print_word_bin(RECURRENCE_MASK)
    print_word_bin(DEGREE_MASK)
    print_word_bin(EMPHASIS_MASK)
    print_word_bin(DETERMINATIVE_MASK)
    print_word_bin(PLURALITY_MASK)
    print_word_bin(EXTERNAL_WORD_FLAG)
    print_word_bin(EXTERNAL_TYPE_MASK)
    print_word_bin(EXTERNAL_WORD_MASK)
    print_word_bin(INTERNAL_TYPE_MASK)
    print_word_bin(INTERNAL_WORD_MASK)

# Flags

SENT_META_TRUE_FLAG   = uint(0b1 << SENT_META_SHIFT)
# Query flags
QUERY_FLAG            = uint(0b0 << SENT_TYPE_SHIFT)
Q_SUBJECT_FLAG        = uint(0b0000 << SENT_SUBTYPE_SHIFT)
Q_OBJECT_FLAG         = uint(0b0001 << SENT_SUBTYPE_SHIFT)
Q_VERB_FLAG           = uint(0b0010 << SENT_SUBTYPE_SHIFT)
Q_TIME_FLAG           = uint(0b0011 << SENT_SUBTYPE_SHIFT)
Q_LOCATION_FLAG       = uint(0b0100 << SENT_SUBTYPE_SHIFT)
Q_REASONING_FLAG      = uint(0b0101 << SENT_SUBTYPE_SHIFT)
Q_EXPLAIN_FLAG        = uint(0b0110 << SENT_SUBTYPE_SHIFT)
Q_SPECIFY_FLAG        = uint(0b0111 << SENT_SUBTYPE_SHIFT)
# Statement flags
STATEMENT_FLAG        = uint(0b1 << SENT_TYPE_SHIFT)
S_FACT_FLAG           = uint(0b1000 << SENT_SUBTYPE_SHIFT)
S_FICTION_FLAG        = uint(0b1001 << SENT_SUBTYPE_SHIFT)
S_UNCERTAIN_FLAG      = uint(0b1010 << SENT_SUBTYPE_SHIFT)
S_CONDITION_FLAG      = uint(0b1011 << SENT_SUBTYPE_SHIFT)
S_RESULT_FLAG         = uint(0b1100 << SENT_SUBTYPE_SHIFT)
S_IMPERATIVE_FLAG     = uint(0b1101 << SENT_SUBTYPE_SHIFT)
S_EXCLAMATORY_FLAG    = uint(0b1110 << SENT_SUBTYPE_SHIFT)
S_UNDEFINED_FLAG      = uint(0b1111 << SENT_SUBTYPE_SHIFT)
# Affections
A_HONEST_FLAG         = uint(0b0000 << AFF_TYPE_SHIFT)
A_DISHONEST_FLAG      = uint(0b0001 << AFF_TYPE_SHIFT)
A_HAPPY_FLAG          = uint(0b0010 << AFF_TYPE_SHIFT)
A_SAD_FLAG            = uint(0b0011 << AFF_TYPE_SHIFT)
A_FEAR_FLAG           = uint(0b0100 << AFF_TYPE_SHIFT)
A_ANGER_FLAG          = uint(0b0101 << AFF_TYPE_SHIFT)
A_ANTICIPATION_FLAG   = uint(0b0110 << AFF_TYPE_SHIFT)
A_SURPRISE_FLAG       = uint(0b0111 << AFF_TYPE_SHIFT)
A_BENEVOLENT_FLAG     = uint(0b1000 << AFF_TYPE_SHIFT)
A_MALICE_FLAG         = uint(0b1001 << AFF_TYPE_SHIFT)
A_PAIN_FLAG           = uint(0b1010 << AFF_TYPE_SHIFT)
A_PLEASURE_FLAG       = uint(0b1011 << AFF_TYPE_SHIFT)
A_UNDEF_FLAG_0        = uint(0b1100 << AFF_TYPE_SHIFT)
A_UNDEF_FLAG_1        = uint(0b1101 << AFF_TYPE_SHIFT)
A_UNDEF_FLAG_2        = uint(0b1110 << AFF_TYPE_SHIFT)
A_UNDEF_FLAG_3        = uint(0b1111 << AFF_TYPE_SHIFT)
# Evidentiality
E_OBSERVATION_FLAG    = uint(0b000 << EVID_SHIFT)
E_QUOTATION_FLAG      = uint(0b001 << EVID_SHIFT)
E_EXPECTATION_FLAG    = uint(0b010 << EVID_SHIFT)
E_CONCLUSION_FLAG     = uint(0b011 << EVID_SHIFT)
E_GENERALIZATION_FLAG = uint(0b100 << EVID_SHIFT)
E_POSTULATE_FLAG      = uint(0b101 << EVID_SHIFT)
E_OPINION_FLAG        = uint(0b110 << EVID_SHIFT)
E_UNDEFINED_FLAG      = uint(0b111 << EVID_SHIFT)
# Word Flags
SENT_META_FALSE_FLAG  = uint(0b0 << SENT_META_SHIFT)
# In Language Flag
IN_LANGUAGE_FALSE     = uint(0b0 << IN_LANGUAGE_SHIFT)
IN_LANGUAGE_TRUE      = uint(0b1 << IN_LANGUAGE_SHIFT)
# Grammar Flags
G_SUBJECT_FLAG        = uint(0b000 << GRAMMAR_SHIFT)
G_OBJECT_FLAG         = uint(0b001 << GRAMMAR_SHIFT)
G_TOPIC_FLAG          = uint(0b010 << GRAMMAR_SHIFT)
G_VERB_FLAG           = uint(0b011 << GRAMMAR_SHIFT)
G_MODIFIER_FLAG       = uint(0b100 << GRAMMAR_SHIFT)
G_RELATION_FLAG       = uint(0b101 << GRAMMAR_SHIFT)
G_UNDEFINED_FLAG_1    = uint(0b110 << GRAMMAR_SHIFT)
G_UNDEFINED_FLAG_2    = uint(0b111 << GRAMMAR_SHIFT)
# Temporal Flags
T_TIMELESS_FLAG       = uint(0b00 << TEMPORAL_SHIFT)
T_PAST_FLAG           = uint(0b01 << TEMPORAL_SHIFT)
T_PRESENT_FLAG        = uint(0b10 << TEMPORAL_SHIFT)
T_FUTURE_FLAG         = uint(0b11 << TEMPORAL_SHIFT)
# Progress Flags
P_UNPROGRESSED_FLAG   = uint(0b00 << PROGRESS_SHIFT)
P_UNSTARTED_FLAG      = uint(0b01 << PROGRESS_SHIFT)
P_IN_PROGRESS_FLAG    = uint(0b10 << PROGRESS_SHIFT)
P_COMPLETE_FLAG       = uint(0b11 << PROGRESS_SHIFT)
# Recurrence Flags
R_NON_RECURRING_FLAG  = uint(0b00 << RECURRENCE_SHIFT)
R_IRREGULAR_FLAG      = uint(0b01 << RECURRENCE_SHIFT)
R_CONTINUOUS_FLAG     = uint(0b10 << RECURRENCE_SHIFT)
R_HABITUAL_FLAG       = uint(0b11 << RECURRENCE_SHIFT)
# Degree Flags
D_UNSPECIFIED_FLAG    = uint(0b000 << DEGREE_SHIFT)
D_NONE_FLAG           = uint(0b001 << DEGREE_SHIFT)
D_LEAST_FLAG          = uint(0b010 << DEGREE_SHIFT)
D_LESSER_FLAG         = uint(0b011 << DEGREE_SHIFT)
D_COMMON_FLAG         = uint(0b100 << DEGREE_SHIFT)
D_GREATER_FLAG        = uint(0b101 << DEGREE_SHIFT)
D_GREATEST_FLAG       = uint(0b110 << DEGREE_SHIFT)
D_TOTAL_FLAG          = uint(0b111 << DEGREE_SHIFT)
# Emphasis Flags
E_UNEMPHASIZED_FLAG   = uint(0b0 << EMPHASIS_SHIFT)
E_EMPHASIZED_FLAG     = uint(0b1 << EMPHASIS_SHIFT)
# Determinative Flags
DT_NON_SPECIFIC_FLAG  = uint(0b0 << DETERMINATIVE_SHIFT)
DT_SPECIFIC_FLAG      = uint(0b1 << DETERMINATIVE_SHIFT)
# Plurality Flags
PL_UNNUMBERED_FLAG    = uint(0b00 << PLURALITY_SHIFT)
PL_SINGULAR_FLAG      = uint(0b01 << PLURALITY_SHIFT)
PL_PLURAL_FLAG        = uint(0b10 << PLURALITY_SHIFT)
PL_SPECIFIC_VAL_FLAG  = uint(0b11 << PLURALITY_SHIFT)
# Word Catagory Flags
C_OBJECT_FLAG         = uint(0b00 << INTERNAL_TYPE_SHIFT)
C_LOCATION_FLAG       = uint(0b01 << INTERNAL_TYPE_SHIFT)
C_RELATION_FLAG       = uint(0b10 << INTERNAL_TYPE_SHIFT)
C_ACTION_FLAG         = uint(0b11 << INTERNAL_TYPE_SHIFT)
