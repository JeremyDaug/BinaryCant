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

# masks for the class
# sentence masks
ZEROED                = uint(0b0)
SENT_META_MASK        = uint(0b1        << 63)
SENT_TYPE_MASK        = uint(0b01       << 62)
SENT_SUBTYPE_MASK     = uint(0b00111    << 59)
AFF_TYPE_MASK         = uint(0b000001111 << 55)
EVID_MASK             = uint(0b000000000111 << 52)
WORD_COUNT_MASK       = 2**52-1
if __name__ == '__main__':
    print_word_bin(ZEROED)
    print_word_bin(SENT_META_MASK)
    print_word_bin(SENT_TYPE_MASK)
    print_word_bin(SENT_SUBTYPE_MASK)
    print_word_bin(AFF_TYPE_MASK)
    print_word_bin(EVID_MASK)
    print_word_bin(WORD_COUNT_MASK)
# word meta masks
IN_LANGUAGE_MASK      = uint(0b1 << 62)
GRAMMAR_MASK          = uint(0b0111 << 59)
TEMPORAL_MASK         = uint(0b11 << 57)
PROGRESS_MASK         = uint(0b11 << 55)
RECURRENCE_MASK       = uint(0b11 << 53)
DEGREE_MASK           = uint(0b111 << 50)
EMPHASIS_MASK         = uint(0b1 << 49)
DETERMINATIVE_MASK    = uint(0b1 << 48)
PLURALITY_MASK        = uint(0b11 << 46)
# External masks (for things without abstract meanings).
EXTERNAL_TYPE_MASK    = uint(0b11111111111111 << 32)
EXTERNAL_WORD_MASK    = uint(0xFFFFFFFF)
# Internal word masks
INTERNAL_TYPE_MASK    = uint(0b11 << 44)
INTERNAL_WORD_MASK    = uint(0xFFFFFFFFFFF)
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
    print_word_bin(EXTERNAL_TYPE_MASK)
    print_word_bin(EXTERNAL_WORD_MASK)
    print_word_bin(INTERNAL_TYPE_MASK)
    print_word_bin(INTERNAL_WORD_MASK)

# Flags
SENT_META_TRUE_FLAG   = uint(0b1 << 63)
# Query flags
QUERY_FLAG            = uint(0b0 << 62)
Q_SUBJECT_FLAG        = uint(0b0000 << 59)
Q_OBJECT_FLAG         = uint(0b0001 << 59)
Q_VERB_FLAG        = uint(0b0010 << 59)
Q_TIME_FLAG           = uint(0b0011 << 59)
Q_LOCATION_FLAG       = uint(0b0100 << 59)
Q_REASONING_FLAG      = uint(0b0101 << 59)
Q_EXPLAIN_FLAG        = uint(0b0110 << 59)
Q_SPECIFY_FLAG        = uint(0b0111 << 59)
# Statement flags
STATEMENT_FLAG        = uint(0b1 << 62)
S_FACT_FLAG           = uint(0b1000 << 59)
S_FICTION_FLAG        = uint(0b1001 << 59)
S_UNCERTAIN_FLAG      = uint(0b1010 << 59)
S_CONDITION_FLAG      = uint(0b1011 << 59)
S_RESULT_FLAG         = uint(0b1100 << 59)
S_IMPERATIVE_FLAG     = uint(0b1101 << 59)
S_EXCLAMATORY_FLAG    = uint(0b1110 << 59)
S_UNDEFINED_FLAG      = uint(0b1111 << 59)
# Affections
A_HONEST_FLAG         = uint(0b0000 << 55)
A_DISHONEST_FLAG      = uint(0b0001 << 55)
A_HAPPY_FLAG          = uint(0b0010 << 55)
A_SAD_FLAG            = uint(0b0011 << 55)
A_FEAR_FLAG           = uint(0b0100 << 55)
A_ANGER_FLAG          = uint(0b0101 << 55)
A_ANTICIPATION_FLAG   = uint(0b0110 << 55)
A_SURPRISE_FLAG       = uint(0b0111 << 55)
A_BENEVOLENT_FLAG     = uint(0b1000 << 55)
A_MALICE_FLAG         = uint(0b1001 << 55)
A_PAIN_FLAG           = uint(0b1010 << 55)
A_PLEASURE_FLAG       = uint(0b1011 << 55)
A_UNDEF_FLAG_0        = uint(0b1100 << 55)
A_UNDEF_FLAG_1        = uint(0b1101 << 55)
A_UNDEF_FLAG_2        = uint(0b1110 << 55)
A_UNDEF_FLAG_3        = uint(0b1111 << 55)
# Evidentiality
E_OBSERVATION_FLAG    = uint(0b000 << 52)
E_QUOTATION_FLAG      = uint(0b001 << 52)
E_EXPECTATION_FLAG    = uint(0b010 << 52)
E_CONCLUSION_FLAG     = uint(0b011 << 52)
E_GENERALIZATION_FLAG = uint(0b100 << 52)
E_POSTULATE_FLAG      = uint(0b101 << 52)
E_OPINION_FLAG        = uint(0b110 << 52)
E_UNDEFINED_FLAG      = uint(0b111 << 52)
# Word Flags
SENT_META_FALSE_FLAG  = uint(0b0 << 63)
# In Language Flag
IN_LANGUAGE_FALSE     = uint(0b0 << 62)
IN_LANGUAGE_TRUE      = uint(0b1 << 62)
# Grammar Flags
G_SUBJECT_FLAG        = uint(0b000 << 59)
G_OBJECT_FLAG         = uint(0b001 << 59)
G_TOPIC_FLAG          = uint(0b010 << 59)
G_VERB_FLAG           = uint(0b011 << 59)
G_MODIFIER_FLAG       = uint(0b100 << 59)
G_RELATION_FLAG       = uint(0b101 << 59)
G_UNDEFINED_FLAG_1    = uint(0b110 << 59)
G_UNDEFINED_FLAG_2    = uint(0b111 << 59)
# Temporal Flags
T_TIMELESS_FLAG       = uint(0b00 << 57)
T_PAST_FLAG           = uint(0b01 << 57)
T_PRESENT_FLAG        = uint(0b10 << 57)
T_FUTURE_FLAG         = uint(0b11 << 57)
# Progress Flags
P_UNPROGRESSED_FLAG   = uint(0b00 << 55)
P_UNSTARTED_FLAG      = uint(0b01 << 55)
P_IN_PROGRESS_FLAG    = uint(0b10 << 55)
P_COMPLETE_FLAG       = uint(0b11 << 55)
# Recurrence Flags
R_NON_RECURRING_FLAG  = uint(0b00 << 53)
R_IRREGULAR_FLAG      = uint(0b01 << 53)
R_CONTINUOUS_FLAG     = uint(0b10 << 53)
R_HABITUAL_FLAG       = uint(0b11 << 53)
# Degree Flags
D_UNSPECIFIED_FLAG    = uint(0b000 << 50)
D_NONE_FLAG           = uint(0b001 << 50)
D_LEAST_FLAG          = uint(0b010 << 50)
D_LESSER_FLAG         = uint(0b011 << 50)
D_COMMON_FLAG         = uint(0b100 << 50)
D_GREATER_FLAG        = uint(0b101 << 50)
D_GREATEST_FLAG       = uint(0b110 << 50)
D_TOTAL_FLAG          = uint(0b111 << 50)
# Emphasis Flags
E_UNEMPHASIZED_FLAG   = uint(0b0 << 49)
E_EMPHASIZED_FLAG     = uint(0b1 << 49)
# Determinative Flags
DT_NON_SPECIFIC_FLAG  = uint(0b0 << 48)
DT_SPECIFIC_FLAG      = uint(0b1 << 48)
# Plurality Flags
PL_UNNUMBERED_FLAG    = uint(0b00 << 46)
PL_SINGULAR_FLAG      = uint(0b01 << 46)
PL_PLURAL_FLAG        = uint(0b10 << 46)
PL_SPECIFIC_VAL_FLAG  = uint(0b11 << 46)
# Word Catagory Flags
C_OBJECT_FLAG         = uint(0b00 << 44)
C_LOCATION_FLAG       = uint(0b01 << 44)
C_RELATION_FLAG       = uint(0b10 << 44)
C_ACTION_FLAG         = uint(0b11 << 44)