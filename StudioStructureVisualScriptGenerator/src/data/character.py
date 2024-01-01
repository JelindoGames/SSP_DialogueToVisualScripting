from enum import Enum


class Character:
    AKARI = 0
    AMELIA = 1
    BRITNEY = 2
    CHLOE = 3
    DANIEL = 4
    EMI = 5
    ETHAN = 6
    MC = 7
    STEVE = 8
    THEODORE = 9
    VIOLA = 10
    YONAKA = 11
    C1 = 12
    SCP = 13

    max_character_value = 13  # For iteration

    character_to_guid = {
        AKARI: "1ad1737fe07774751b25d03892f4ff2b",
        AMELIA: "89fac5143b3d348b9a445ef619bc3be2",
        BRITNEY: "5ca89f0313ad44ae5b2a9707d0702dff",
        C1: "c2ae1484ae4de45f099c5b3d35a7a065",
        CHLOE: "c59b44350ae0e4a339def1015b20fb5e",
        DANIEL: "13d5ed6df56b443c0a12f7f4b108c37c",
        EMI: "652110768cd0a4c7a9aeb6c6e703d589",
        ETHAN: "b0eac8812412b444988726f0482dca75",
        MC: "617588a0ea5a34d729372141c22656a6",
        SCP: "8dbf819b407dc482eab61ef88b6db806",
        STEVE: "17c04beccfdb94100a04a1a3d5b30db3",
        THEODORE: "adf95db3a761141ccaa783ddfd78e551",
        VIOLA: "708d61c8311a341fb8b15c437008c6c0",
        YONAKA: "4a9dfb61d3e3640fcb35b08aee8da1e7"
    }

    string_to_character = {
        "MCW": AKARI,
        "AKARI": AKARI,
        "AKARI HAYASHI": AKARI,
        "A": AMELIA,
        "AMELIA": AMELIA,
        "AMELIA LEE": AMELIA,
        "B": BRITNEY,
        "BRITNEY": BRITNEY,
        "BRITNEY SUMMERS": BRITNEY,
        "C1": C1,
        "FELIX": C1,
        "FELIX BEAUMONT": C1,
        "C": CHLOE,
        "CHLOE": CHLOE,
        "CHLOE SUZUKI": CHLOE,
        "D": DANIEL,
        "DANIEL": DANIEL,
        "DANIEL HARRINGTON": DANIEL,
        "MOM": DANIEL,
        "DAD": DANIEL,
        "HT": EMI,
        "EMI": EMI,
        "EMI SATO": EMI,
        "EGT": ETHAN,
        "ETHAN": ETHAN,
        "ETHAN REED": ETHAN,
        "MC": MC,
        "NEKU": MC,
        "NEKU IWAKURA": MC,
        "SCP": SCP,
        "ALEXIS": SCP,
        "ALEXIS AIZAKI": SCP,
        "AO": STEVE,
        "ARCADE OWNER": STEVE,
        "STEVE": STEVE,
        "CMG": THEODORE,
        "THEODORE": THEODORE,
        "THEODORE WILBURN": THEODORE,
        "J": VIOLA,
        "SJ": VIOLA,
        "JOURNALIST": VIOLA,
        "VIOLA": VIOLA,
        "VIOLA VOLKOV": VIOLA,
        "C3": YONAKA,
        "AMBER": YONAKA,
        "YONAKA": YONAKA,
        "AMBER KAGE": YONAKA,
        "YONAKA KAGE": YONAKA
    }

    character_to_real_name = {
        AKARI: "Akari",
        AMELIA: "Amelia",
        BRITNEY: "Britney",
        C1: "Felix",
        CHLOE: "Chloe",
        DANIEL: "Daniel",
        EMI: "Emi",
        ETHAN: "Ethan",
        MC: "Neku",
        SCP: "Alexis",
        STEVE: "Steve",
        THEODORE: "Theodore",
        VIOLA: "Viola",
        YONAKA: "Yonaka"
    }


def get_character_from_string(text: str):
    text_stripped = "".join([char for char in text if char.isalnum() or char.isspace()])
    text_stripped = text_stripped.strip()
    character = Character.string_to_character.get(text_stripped.upper())
    return character
