
# Ad = Ace of Diamonds
# Ah = Ace of Hearts
# As = Ace of Spades
# Ac = Ace of Clubs

PROMPT_INITIAL = "a"
PROMPT_SUFFIX = " of BlackJack"
PROMPT_ANOTHER = "another"
PROMPT_SUFFIX_EMPTY = ""
HIT_KEY = "H"
STAND_KEY = "S"
DOUBLE_KEY = "D"
SPLIT_KEY = "t"
QUIT_KEY = "Q"
PROMPT_CHOICE = (f"({HIT_KEY})it, ({STAND_KEY})tand, ({DOUBLE_KEY})ouble Down, Spli({SPLIT_KEY})-Requires doubles, "
                 f"({QUIT_KEY})uit (*note* not case sens): ")
WINNING_SCORE = 21
DECK = ["Ad", "Ah", "As", "Ac",
        "2d", "2h", "2s", "2c",
        "3d", "3h", "3s", "3c",
        "4d", "4h", "4s", "4c",
        "5d", "5h", "5s", "5c",
        "6d", "6h", "6s", "6c",
        "7d", "7h", "7s", "7c",
        "8d", "8h", "8s", "8c",
        "9d", "9h", "9s", "9c",
        "1d", "1h", "1s", "1c",
        "Jd", "Jh", "Js", "Jc",
        "Qd", "Qh", "Qs", "Qc",
        "Kd", "Kh", "Ks", "Kc",
        ]

CARD_VALUES = {"A": 11,
               "2": 2, "3": 3, "4": 4,
               "5": 5, "6": 6, "7": 7,
               "8": 8, "9": 9, "1": 10,
               "J": 10, "Q": 10, "K": 10}

CARD_COUNT_VALUES = {"A": -1,
                     "1": -1, "J": -1, "Q": -1, "K": -1,
                     "7": 0, "8": 0, "9": 0,
                     "2": 1, "3": 1, "4": 1, "5": 1, "6": 1}