#6 BEGINNER LEVELS - progressing in difficulty
BEGINNER_LEVELS = [
    {
        "maze": [ #level 1
            "#########",
            "#.o.o.o.#",
            "#.###.#.#",
            "#.o.#.o.#",
            "#.#.#.#.#",
            "#.o.o.o.#",
            "#########",
        ],
        "player_start": (1,1),
        "enemies": [
            {"start": (3,5), "moves_every_turn": False},
        ],

    },
    {
        "maze": [ #level 2
            "###########",
            "#o.o.#.o.o#",
            "#.#.....#.#",
            "#o.#.#.#o.#",
            "#.#.....#.#",
            "#o.o.#.o.o#",
            "###########",
        ],
        "player_start": (1,1),
        "enemies": [
            {"start": (3,9), "moves_every_turn": False},
        ],
    },
    {
        "maze": [ #level 3
            "#############",
            "#.o.o.o.o.o.#",
            "#.##.##.###.#",
            "#.#...#...#.#",
            "#.#.o.#.o.#.#",
            "#.#...#...#.#",
            "#.#########.#",
            "#.o.......o.#",
            "#############",
        ],
        "player_start": (1,1),
        "enemies": [
            {"start": (3,7), "moves_every_turn": False}, #chases the player now every turn
        ],
    },
    {
        "maze": [ #level 4
            "#############",
            "#.o...o...o.#",
            "###########.#",
            "#.o...o...o.#",
            "#.###########",
            "#.o...o...o.#",
            "###########.#",
            "#.o...o...o.#",
            "#############",
        ],
        "player_start": (1,1),
        "enemies": [
            {"start": (3,5), "moves_every_turn": False},
        ],
    },
    {
        "maze": [ #level 5
            "###############",
            "#.o...#...#.o #",
            "#.###.#.#.###.#",
            "#.#..o...o.#..#",
            "#.#.#####.#.#.#",
            "#o..#...#..o#.#",
            "#.###.#.###.#.#",
            "#.o...#.o...o.#",
            "###############",
        ],
        "player_start": (1,1),
        "enemies": [
            {"start": (5,11), "moves_every_turn":True},
        ],
    },
    {
        #level 6: now there comes a second enemy - one is a chaser the other is a stationary trap
        "maze": [
            "###############",
            "#.o...#.o...o.#",
            "#.###.#.#####.#",
            "#o..#.o...#..o#",
            "###.#.###.#.###",
            "#o..#...#..o..#",
            "#.#####.#####.#",
            "#.o...o.#.o...#",
            "###############",
        ],
        "player_start": (1,1),
        "enemies": [
            {"start": (5,7), "moves_every_turn":True}, #chaser
            {"start": (3,12), "moves_every_turn": False}, #stationary trap
        ],
    },
]

#ADVANCED LEVELS

ADVANCED_LEVELS = [
    {
        "maze": [
            "###################",
            "#.o.o.o.#.o.o.o.o.#",
            "#.#####.#.#######.#",
            "#.#...#...#.....#.#",
            "#.#.#.#####.###.#.#",
            "#o..#.o.o.o.#..o#.#"
            "#.#####.#.#####.#.#",
            "#o..o...#...o..o#.#",
            "###################",
        ],
        "player_start": (1,1),
        "enemies": [
            {"start": (5,9), "moves_every_turn": True},
            {"start": (1,17), "moves_every_turn": True},
            {"start": (7,1), "moves_every_turn": False},
        ],
    },
    {
        "maze": [
            "###################",
            "#o...o.o.o.o.o...o#",
            "#.#.##.##.##.##.#.#",
            "#.#.#...#.#...#.#.#",
            "#o..#.o.#.#.o.#..o#",
            "#.#.#...#.#...#.#.#",
            "#.#.#####.#####.#.#",
            "#o.#.o.o.o.o.o.#.o#",
            "###################",
        ],
        "player_start": (4,9),
        "enemies": [
            {"start": (1,1), "moves_every_turn": True},
            {"start": (1,17), "moves_every_turn": False},
            {"start": (7,1), "moves_every_turn": False},
            {"start": (7,17), "moves_every_turn": True},
        ],
    },
]
