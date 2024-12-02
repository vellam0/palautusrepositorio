class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.player_points = {player1: 0, player2: 0}

    def won_point(self, player_name):
        self.player_points[player_name] += 1
        print(self.get_score())

    def tie(self):
        tie_calls = {0: "Love-All", 1: "Fifteen-All", 2: "Thirty-All"}
        if self.player_points[self.player1] in tie_calls:
            return tie_calls.get(self.player_points[self.player1])
        else:
            return "Deuce"

    def advantage_or_win(self):
        difference = self.player_points[self.player1] - self.player_points[self.player2]
        if difference == 1:
            return "Advantage player1"
        elif difference == -1:
            return "Advantage player2"
        elif difference >= 2:
            return "Win for player1"
        else:
            return "Win for player2"

    def call_score(self):
        score_calls = ["Love", "Fifteen", "Thirty", "Forty"]
        player1_score = score_calls[self.player_points[self.player1]]
        player2_score = score_calls[self.player_points[self.player2]]
        return f"{player1_score}-{player2_score}"
                
    def get_score(self):
        if self.player_points[self.player1] == self.player_points[self.player2]:
            return self.tie()

        elif self.player_points[self.player1] >= 4 or self.player_points[self.player2] >= 4:
            return self.advantage_or_win()
        
        else:
            return self.call_score()
