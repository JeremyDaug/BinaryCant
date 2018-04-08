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
EXTERNAL_POINTER_SHIFT   = 63  # Completely outside the language
SENT_META_SHIFT          = 62  # Language Meta Flag
SENT_TYPE_SHIFT          = 61  # Type of sentence
SENT_SUBTYPE_SHIFT       = 58  # sentence subtype
AFF_TYPE_SHIFT           = 54  # affection
EVID_SHIFT               = 51  # evidentiality
WORD_COUNT_SHIFT         = 0  # the word count of the sentence
# word meta masks
GRAMMAR_SHIFT            = 60  # grammar flag for a word
TEMPORAL_SHIFT           = 58
PROGRESS_SHIFT           = 56
RECURRENCE_SHIFT         = 54
DEGREE_SHIFT             = 51
EMPHASIS_SHIFT           = 50
DETERMINATIVE_SHIFT      = 49
PLURALITY_SHIFT          = 47
# External masks (for things without abstract meanings).
EXTERNAL_WORD_FLAG_SHIFT = 46
EXTERNAL_TYPE_SHIFT      = 32
EXTERNAL_WORD_SHIFT      = 0
# Internal word masks
INTERNAL_TYPE_SHIFT      = 43
INTERNAL_WORD_SHIFT      = 0

# masks for the class
# sentence masks
ZEROED                = uint(0b0)
EXTERNAL_POINTER_TRUE_FLAG = uint(0b1 << EXTERNAL_POINTER_SHIFT)
EXTERNAL_POINTER_FALSE_FLAG = uint(0b0 << EXTERNAL_POINTER_SHIFT)
SENT_META_MASK        = uint(0b1        << SENT_META_SHIFT)
SENT_TYPE_MASK        = uint(0b01       << SENT_TYPE_SHIFT)
SENT_SUBTYPE_MASK     = uint(0b00111    << SENT_SUBTYPE_SHIFT)
AFF_TYPE_MASK         = uint(0b000001111 << AFF_TYPE_SHIFT)
EVID_MASK             = uint(0b000000000111 << EVID_SHIFT)
WORD_COUNT_MASK       = uint(2**51-1)
if __name__ == '__main__':
    print_word_bin(ZEROED)
    print_word_bin(SENT_META_MASK)
    print_word_bin(SENT_TYPE_MASK)
    print_word_bin(SENT_SUBTYPE_MASK)
    print_word_bin(AFF_TYPE_MASK)
    print_word_bin(EVID_MASK)
    print_word_bin(WORD_COUNT_MASK)

# word meta masks
GRAMMAR_MASK          = uint(0b0111 << GRAMMAR_SHIFT)
TEMPORAL_MASK         = uint(0b11 << TEMPORAL_SHIFT)
PROGRESS_MASK         = uint(0b11 << PROGRESS_SHIFT)
RECURRENCE_MASK       = uint(0b11 << RECURRENCE_SHIFT)
DEGREE_MASK           = uint(0b111 << DEGREE_SHIFT)
EMPHASIS_MASK         = uint(0b1 << EMPHASIS_SHIFT)
DETERMINATIVE_MASK    = uint(0b1 << DETERMINATIVE_SHIFT)
PLURALITY_MASK        = uint(0b11 << PLURALITY_SHIFT)
WORD_FLAG_COUNT       = uint(8)
# External masks (for things without abstract meanings).
EXTERNAL_WORD_FLAG    = uint(0b1 << EXTERNAL_WORD_FLAG_SHIFT)
EXTERNAL_TYPE_MASK    = uint(0x1FFF << EXTERNAL_TYPE_SHIFT)
EXTERNAL_WORD_MASK    = uint(0xFFFFFFFF)
# Internal word masks
INTERNAL_TYPE_MASK    = uint(0b11 << INTERNAL_TYPE_SHIFT)
INTERNAL_WORD_MASK    = uint(0x7FFFFFFFFFF)
INT_EXT_MASK          = uint(0b1 << (EXTERNAL_WORD_FLAG_SHIFT+1) - 1)
if __name__ == '__main__':
    print('------WORD MASKS------')
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
S_ASSERTION_FLAG      = uint(0b1000 << SENT_SUBTYPE_SHIFT)
S_DELETION_FLAG       = uint(0b1001 << SENT_SUBTYPE_SHIFT)
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

# tokens
# Grammar Flags
G_SUBJECT_TOK        = "sub"
G_OBJECT_TOK         = "obj"
G_TOPIC_TOK          = "top"
G_VERB_TOK           = "ver"
G_MODIFIER_TOK       = "mod"
G_RELATION_TOK       = "rel"
G_UNDEFINED_TOK_1    = "und1"
G_UNDEFINED_TOK_2    = "und2"
GRAMMAR_TOKENS = [G_SUBJECT_TOK,
                  G_OBJECT_TOK,
                  G_TOPIC_TOK,
                  G_VERB_TOK,
                  G_MODIFIER_TOK,
                  G_RELATION_TOK,
                  G_UNDEFINED_TOK_1,
                  G_UNDEFINED_TOK_2]
# Temporal Flags
T_TIMELESS_TOK       = ""
T_PAST_TOK           = "pas"
T_PRESENT_TOK        = "pre"
T_FUTURE_TOK         = "fut"
TEMPORAL_TOKENS = [T_PAST_TOK,
                   T_PRESENT_TOK,
                   T_FUTURE_TOK]
# Progress Flags
P_UNPROGRESSED_TOK   = ""
P_UNSTARTED_TOK      = "uns"
P_IN_PROGRESS_TOK    = "pro"
P_COMPLETE_TOK       = "com"
PROGRESS_TOKENS = [P_UNSTARTED_TOK,
                   P_IN_PROGRESS_TOK,
                   P_COMPLETE_TOK]
# Recurrence Flags
R_NON_RECURRING_TOK  = ""
R_IRREGULAR_TOK      = "irr"
R_CONTINUOUS_TOK     = "con"
R_HABITUAL_TOK       = "hab"
RECURRENCE_TOKENS = [R_IRREGULAR_TOK,
                     R_CONTINUOUS_TOK,
                     R_HABITUAL_TOK]
# Degree Flags
D_UNSPECIFIED_TOK    = ""
D_NONE_TOK           = "0"
D_LEAST_TOK          = "1"
D_LESSER_TOK         = "2"
D_COMMON_TOK         = "3"
D_GREATER_TOK        = "4"
D_GREATEST_TOK       = "5"
D_TOTAL_TOK          = "6"
DEGREE_TOKENS = [D_NONE_TOK,
                 D_LEAST_TOK,
                 D_LESSER_TOK,
                 D_COMMON_TOK,
                 D_GREATER_TOK,
                 D_GREATEST_TOK,
                 D_TOTAL_TOK]
# Emphasis Flags
E_UNEMPHASIZED_TOK   = ""
E_EMPHASIZED_TOK     = "!"
# Determinative Flags
DT_NON_SPECIFIC_TOK  = ""
DT_SPECIFIC_TOK      = "?"
# Plurality Flags
PL_UNNUMBERED_TOK    = ""
PL_SINGULAR_TOK      = "sin"
PL_PLURAL_TOK        = "plu"
PL_SPECIFIC_VAL_TOK  = "num"
PLURALITY_TOKENS = [PL_SINGULAR_TOK,
                    PL_PLURAL_TOK,
                    PL_SPECIFIC_VAL_TOK]

TOKENDICT = {G_SUBJECT_TOK: G_SUBJECT_FLAG,
             G_OBJECT_TOK: G_OBJECT_FLAG,
             G_TOPIC_TOK: G_TOPIC_FLAG,
             G_VERB_TOK: G_VERB_FLAG,
             G_MODIFIER_TOK: G_MODIFIER_FLAG,
             G_RELATION_TOK: G_RELATION_FLAG,
             G_UNDEFINED_TOK_1: G_UNDEFINED_FLAG_1,
             G_UNDEFINED_TOK_2: G_UNDEFINED_FLAG_2,
             T_TIMELESS_TOK: T_TIMELESS_FLAG,
             T_PAST_TOK: T_PAST_FLAG,
             T_PRESENT_TOK: T_PRESENT_FLAG,
             T_FUTURE_TOK: T_FUTURE_FLAG,
             P_UNPROGRESSED_TOK: P_UNPROGRESSED_FLAG,
             P_UNSTARTED_TOK: P_UNSTARTED_FLAG,
             P_IN_PROGRESS_TOK: P_IN_PROGRESS_FLAG,
             P_COMPLETE_TOK: P_COMPLETE_FLAG,
             R_NON_RECURRING_TOK: R_NON_RECURRING_FLAG,
             R_IRREGULAR_TOK: R_IRREGULAR_FLAG,
             R_CONTINUOUS_TOK: R_CONTINUOUS_FLAG,
             R_HABITUAL_TOK: R_HABITUAL_FLAG,
             D_UNSPECIFIED_TOK: D_UNSPECIFIED_FLAG,
             D_NONE_TOK: D_NONE_FLAG,
             D_LEAST_TOK: D_LEAST_FLAG,
             D_LESSER_TOK: D_LESSER_FLAG,
             D_COMMON_TOK: D_COMMON_FLAG,
             D_GREATER_TOK: D_GREATER_FLAG,
             D_GREATEST_TOK: D_GREATEST_FLAG,
             D_TOTAL_TOK: D_TOTAL_FLAG,
             E_UNEMPHASIZED_TOK: E_UNEMPHASIZED_FLAG,
             E_EMPHASIZED_TOK: E_EMPHASIZED_FLAG,
             DT_NON_SPECIFIC_TOK: DT_NON_SPECIFIC_FLAG,
             DT_SPECIFIC_TOK: DT_SPECIFIC_FLAG,
             PL_UNNUMBERED_TOK: PL_UNNUMBERED_FLAG,
             PL_SINGULAR_TOK: PL_SINGULAR_FLAG,
             PL_PLURAL_TOK: PL_PLURAL_FLAG,
             PL_SPECIFIC_VAL_TOK: PL_SPECIFIC_VAL_FLAG
             }

def FIND_WORD_FLAG(val):
    for key, value in TOKENDICT.items():
        if val == value:
            return key
    raise ValueError("Key Not found")

WORD_TYPES = ["int", "float", "rbg"]
WORD_TYPE_DICT = {"int": uint(0 << EXTERNAL_TYPE_SHIFT),
                  "float": uint(1 << EXTERNAL_TYPE_SHIFT),
                  "rbg": uint(2 << EXTERNAL_TYPE_SHIFT)}

# sentence tokens
QUERY_TOK            = "Q"
Q_SUBJECT_TOK        = "QS"
Q_OBJECT_TOK         = "QO"
Q_VERB_TOK           = "QV"
Q_TIME_TOK           = "QT"
Q_LOCATION_TOK       = "QL"
Q_REASONING_TOK      = "QR"
Q_EXPLAIN_TOK        = "QE"
Q_SPECIFY_TOK        = "QC"  # clarify
# Statement flags
STATEMENT_TOK        = "S"
S_ASSERTION_TOK      = "SA"
S_DELETION_TOK       = "SD"
S_UNCERTAIN_TOK      = "SU"
S_CONDITION_TOK      = "SC"
S_RESULT_TOK         = "SR"
S_IMPERATIVE_TOK     = "SI"
S_EXCLAMATORY_TOK    = "S!"
S_UNDEFINED_TOK      = "S?"
# Affections
A_HONEST_TOK         = ""
A_DISHONEST_TOK      = "lie"
A_HAPPY_TOK          = "hap"
A_SAD_TOK            = "sad"
A_FEAR_TOK           = "fea"
A_ANGER_TOK          = "ang"
A_ANTICIPATION_TOK   = "ant"
A_SURPRISE_TOK       = "sur"
A_BENEVOLENT_TOK     = "ben"
A_MALICE_TOK         = "mal"
A_PAIN_TOK           = "pai"
A_PLEASURE_TOK       = "ple"
A_UNDEF_TOK_0        = "000"
A_UNDEF_TOK_1        = "111"
A_UNDEF_TOK_2        = "222"
A_UNDEF_TOK_3        = "333"
# Evidentiality
E_OBSERVATION_TOK    = ""
E_QUOTATION_TOK      = "quo"
E_EXPECTATION_TOK    = "exp"
E_CONCLUSION_TOK     = "con"
E_GENERALIZATION_TOK = "gen"
E_POSTULATE_TOK      = "pos"
E_OPINION_TOK        = "opi"
E_UNDEFINED_TOK      = "und"

SENT_FLAG_DICT = {
    Q_SUBJECT_TOK: Q_SUBJECT_FLAG,
    Q_OBJECT_TOK: Q_OBJECT_FLAG,
    Q_VERB_TOK: Q_VERB_FLAG,
    Q_TIME_TOK: Q_TIME_FLAG,
    Q_LOCATION_TOK: Q_LOCATION_FLAG,
    Q_REASONING_TOK: Q_REASONING_FLAG,
    Q_EXPLAIN_TOK: Q_EXPLAIN_FLAG,
    Q_SPECIFY_TOK: Q_SPECIFY_FLAG,
    S_ASSERTION_TOK: S_ASSERTION_FLAG,
    S_DELETION_TOK: S_DELETION_FLAG,
    S_UNCERTAIN_TOK: S_UNCERTAIN_FLAG,
    S_CONDITION_TOK: S_CONDITION_FLAG,
    S_RESULT_TOK: S_RESULT_FLAG,
    S_IMPERATIVE_TOK: S_IMPERATIVE_FLAG,
    S_EXCLAMATORY_TOK: S_EXCLAMATORY_FLAG,
    S_UNDEFINED_TOK: S_UNDEFINED_FLAG,
    A_DISHONEST_TOK: A_DISHONEST_FLAG,
    A_HAPPY_TOK: A_HAPPY_FLAG,
    A_SAD_TOK: A_SAD_FLAG,
    A_FEAR_TOK: A_FEAR_FLAG,
    A_ANGER_TOK: A_ANGER_FLAG,
    A_ANTICIPATION_TOK: A_ANTICIPATION_FLAG,
    A_SURPRISE_TOK: A_SURPRISE_FLAG,
    A_BENEVOLENT_TOK: A_BENEVOLENT_FLAG,
    A_MALICE_TOK: A_MALICE_FLAG,
    A_PAIN_TOK: A_PAIN_FLAG,
    A_PLEASURE_TOK: A_PLEASURE_FLAG,
    A_UNDEF_TOK_0: A_UNDEF_FLAG_0,
    A_UNDEF_TOK_1: A_UNDEF_FLAG_1,
    A_UNDEF_TOK_2: A_UNDEF_FLAG_2,
    A_UNDEF_TOK_3: A_UNDEF_FLAG_3,
    E_OBSERVATION_TOK: E_OBSERVATION_FLAG,
    E_QUOTATION_TOK: E_QUOTATION_FLAG,
    E_EXPECTATION_TOK: E_EXPECTATION_FLAG,
    E_CONCLUSION_TOK: E_CONCLUSION_FLAG,
    E_GENERALIZATION_TOK: E_GENERALIZATION_FLAG,
    E_POSTULATE_TOK: E_POSTULATE_FLAG,
    E_OPINION_TOK: E_OPINION_FLAG,
    E_UNDEFINED_TOK: E_UNDEFINED_FLAG
}


def FIND_SENT_FLAG(val):
    for key, value in TOKENDICT.items():
        if val == value:
            return key
    raise ValueError("Key Not found")


# External Value Types
ET_CONST = uint(0b10000000000000 << EXTERNAL_TYPE_SHIFT)
ET_INT   = uint(0b10000000000001 << EXTERNAL_TYPE_SHIFT)
ET_FLOAT = uint(0b10000000000010 << EXTERNAL_TYPE_SHIFT)
ET_RGB   = uint(0b10000000000011 << EXTERNAL_TYPE_SHIFT)

EX_VAL_TYPE_DICT = {
    'const': ET_CONST,
    'int': ET_INT,
    'float': ET_FLOAT,
    'rgb': ET_RGB
}

def FIND_EXT_WORD_TYPE(val):
    for key, value in EX_VAL_TYPE_DICT.items():
        if val == value:
            return key
