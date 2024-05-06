class Player:
    def __init__(self, name: str, rating: int):
        self.name = name
        self.rating = rating
        self.score = 0

    def __str__(self) -> str:
        return f"{self.name} ({self.rating}) - {self.score} points"

class Tournament:
    def __init__(self):
        self.players = []

    def add_player(self, name: str, rating: int) -> None:
        self.players.append(Player(name, rating))

    def sort_players(self) -> None:
        self.players.sort(key=lambda x: (-x.score, -x.rating, x.name))

    def pair_round(self) -> list[tuple[Player, Player]]:
        self.sort_players()
        pairs = []
        for i in range(0, len(self.players), 2):
            pairs.append((self.players[i], self.players[i+1]))
        return pairs

def print_table(players: list[Player]) -> None:
    print("Final Table:")
    for i, player in enumerate(sorted(players, key=lambda x: (-x.score, -x.rating, x.name)), 1):
        print(f"{i}. {player}")

def main() -> None:
    tournament = Tournament()
    num_players = int(input("Enter the number of players: "))
    for i in range(num_players):
        name = input(f"Enter player {i+1} name: ")
        rating = int(input(f"Enter player {i+1} rating: "))
        tournament.add_player(name, rating)

    print("Tournament pairings:")
    for round_num in range(num_players - 1):
        pairs = tournament.pair_round()
        for pair in pairs:
            print(f"Round {round_num+1}: {pair[0].name} vs {pair[1].name}")
        # Update scores based on user input
        for pair in pairs:
            winner = input(f"Enter winner of {pair[0].name} vs {pair[1].name} (0 for draw, 1 for {pair[0].name}, 2 for {pair[1].name}): ")
            if winner == "1":
                pair[0].score += 1
            elif winner == "2":
                pair[1].score += 1
            else:
                pair[0].score += 0.5
                pair[1].score += 0.5

    print_table(tournament.players)
    print("Made in Python by blackbox.ai")

if __name__ == "__main__":
    main()
