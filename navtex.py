from collections import defaultdict
ALPHABET_LTRS = defaultdict(lambda: '???')
ALPHABET_FIGS = defaultdict(lambda: '???')
ALPHABET_LTRS.update({
    0x0f: "[alpha]",
    0x17: "J",
    0x1b: "F",
    0x1d: "C",
    0x1e: "K",
    0x27: "W",
    0x2b: "Y",
    0x2d: "P",
    0x2e: "Q",
    0x33: "[beta]",
    0x35: "G",
    0x36: "[figs]",
    0x39: "M",
    0x3a: "X",
    0x3c: "V",
    0x47: "A",
    0x4b: "S",
    0x4d: "I",
    0x4e: "U",
    0x53: "D",
    0x55: "R",
    0x56: "E",
    0x59: "N",
    0x5a: "[ltrs]",
    0x5c: " ",
    0x63: "Z",
    0x65: "L",
    0x66: "[rep]",
    0x69: "H",
    0x6a: "[]",
    0x6c: "\n",
    0x71: "O",
    0x72: "B",
    0x74: "T",
    0x78: "[cr]"
})
ALPHABET_FIGS.update({
    0x0f: "[alpha]",
    0x17: "'",
    0x1b: "!",
    0x1d: ":",
    0x1e: "(",
    0x27: "2",
    0x2b: "6",
    0x2d: "0",
    0x2e: "1",
    0x33: "[beta]",
    0x35: "&",
    0x36: "[figs]",
    0x39: ".",
    0x3a: "/",
    0x3c: ";",
    0x47: "-",
    0x4b: "[bell]",
    0x4d: "8",
    0x4e: "7",
    0x53: "$",
    0x55: "4",
    0x56: "3",
    0x59: ",",
    0x5a: "[ltrs]",
    0x5c: " ",
    0x63: "\"",
    0x65: ")",
    0x66: "[rep]",
    0x69: "#",
    0x6a: "[]",
    0x6c: "\n",
    0x71: "9",
    0x72: "?",
    0x74: "5",
    0x78: "[cr]"
})
